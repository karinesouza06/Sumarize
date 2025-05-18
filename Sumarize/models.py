from pydantic import BaseModel

class Resumo(BaseModel):
    texto: str
    
    class Config:
        schema_extra = {
            "example": {
                "texto": "## Exemplo de Resumo\n* Primeiro ponto\n* Segundo ponto\n[Saiba mais](https://exemplo.com)"
            }
        }

class TextoEntrada(BaseModel):
    texto: str
    
    class Config:
        schema_extra = {
            "example": {
                "texto": "## Título Principal\n- Item da lista\n* Texto em itálico\n**Texto em negrito**"
            }
        }