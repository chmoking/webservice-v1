# hora local tomando la ubicacion
from fastapi import FastAPI
from datetime import datetime
from zoneinfo import ZoneInfo
from models import Cliente, CrearCliente
from fastapi.middleware.cors import CORSMiddleware

ahora = datetime.now()
hora_actual = ahora.time()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

country_timezones ={
"CO":"America/Bogota",
"MX":"America/Mexico_City",
"PE":"America/Lima",
"AR":"America/Argentina/Buenos_Aires",
"CL":"America/Santiago",
"EC":"America/Guayaquil",
"VE":"America/Caracas"
}

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get("/time/{iso_code}")
async def time(iso_code: str):
    iso = iso_code.upper()
    timezone_str = country_timezones.get(iso)
    tz = ZoneInfo(timezone_str)
    return {"time": datetime.now(tz)}

db_clientes: list[Cliente] = []

@app.post("/clientes/", response_model=CrearCliente)
async def crear_cliente(cliente_info: Cliente):
    cliente = Cliente.model_validate(cliente_info.model_dump())
    db_clientes.append(cliente)
    return cliente

@app.get("/clientes/", response_model=list[Cliente])
async def listar_clientes():
    return db_clientes
