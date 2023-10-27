from sqlalchemy import Column, Table,Sequence
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine
id_sequence = Sequence('vehiculo_id_seq', metadata=meta)

vehiculos = Table(
    "vehiculo",
    meta,
    Column("id", Integer, id_sequence, primary_key=True, server_default=id_sequence.next_value()),
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