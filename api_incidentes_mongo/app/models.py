from beanie import Document
from pydantic import Field

class Incidente(Document):
    titulo: str = Field(..., max_length=100)
    descripcion: str
    prioridad: str
    estado: str = "Abierto"

    class Settings:
        name = "incidentes"