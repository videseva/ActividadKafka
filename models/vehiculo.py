from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

vehiculos = Table(
    "vehiculo",
    meta,
    Column("id", Integer, primary_key=True),
    Column("fecha",String(50)),    
    Column("hora",String(50)),
    Column("nombre", String(50)),
    Column("email", String(50)),
    Column("celular", String(50)),
    Column("tipoVehiculo", String(50)),
    Column("matricula", String(50)),
    Column("totalPagar", String(50)),
)

meta.create_all(engine)