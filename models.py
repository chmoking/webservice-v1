from pydantic import BaseModel, EmailStr

class Cliente(BaseModel):
    nombre: str
    cedula: str
    email: EmailStr
    direcion: str | None = "Ibarra"

class CrearCliente(Cliente):
    pass