import io
import uuid
from anyio import Path
from fastapi import APIRouter, HTTPException, Response, UploadFile
from fastapi.responses import FileResponse
from config.db import conn
from models.vehiculo import vehiculos
from schemas.vehiculo import Vehiculo, VehiculoCount
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select


from cryptography.fernet import Fernet

vehiculo_api = APIRouter()
key = Fernet.generate_key()
f = Fernet(key)

@vehiculo_api.get(
    "/vehiculo",
    tags=["vehiculos"],
    response_model=List[Vehiculo],
    description="Listado de vehiculos",
)
def get_vehiculo():   
    return conn.execute(vehiculos.select()).fetchall()

@vehiculo_api.get(
    "/vehiculo/{id}",
    tags=["vehiculos"],
    response_model=Vehiculo,
    description="obtener vehiculo por id",
)
def get_vehiculo(id: str):
    return conn.execute(vehiculos.select().where(vehiculos.c.id == id)).first()


@vehiculo_api.post("/vehiculo", tags=["vehiculos"], response_model=Vehiculo, description="Crear un nuevo ticket")
def create_vehiculo(v: Vehiculo):
    new_vehiculo = { "fecha": v.fecha, "hora": v.hora,  "nombre": v.nombre, "email": v.email,"celular":v.celular,"tipoVehiculo": v.tipoVehiculo,  "matricula": v.matricula, "totalPagar": v.totalPagar}
    result = conn.execute(vehiculos.insert().values(new_vehiculo))
    conn.commit()
    print(new_vehiculo)
    return conn.execute(vehiculos.select().where(vehiculos.c.id == result.lastrowid)).first()