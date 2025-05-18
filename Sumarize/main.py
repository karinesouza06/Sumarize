from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel, validator
from models import Resumo, TextoEntrada

app = FastAPI(title="API de Resumos Markdown",
             description="API para processamento de textos em Markdown",
             version="1.0.0")

resumos: List[Resumo] = []

@validator("texto")
def validar_markdown(cls, value):
    if not value.strip():
        raise ValueError("O texto não pode estar vazio.")
    if not any(md in value for md in ["#", "*", "-", "[", "]", "(", ")"]):
        raise ValueError("O texto deve conter pelo menos um elemento de Markdown.")
    return value

@app.post("/resumir/",
         response_model=Resumo,
         responses={
             200: {
                 "description": "Resumo criado com sucesso",
                 "content": {
                     "application/json": {
                         "example": {"texto": "## Resumo\\n- Ponto principal\\n- Outro ponto"}
                     }
                 }
             },
             400: {
                 "description": "Erro de validação",
                 "content": {
                     "application/json": {
                         "example": {"detail": "Texto muito longo"}
                     }
                 }
             }
         })
async def create_resumo(resumo: TextoEntrada):
    
    if len(resumo.texto) > 3000:
        raise HTTPException(status_code=400, detail="Texto muito longo, reduza a quantidade de caracteres para 3000")

    novo_resumo = Resumo(texto=resumo.texto)
    resumos.append(novo_resumo)
    return novo_resumo

@app.get("/resumos/", response_model=List[Resumo])
async def listar_resumos():
    return resumos


