from sqlalchemy import create_engine, MetaData



engine = create_engine("mysql+pymysql://root:2862@localhost:3306/vehiculos",echo=True)


meta = MetaData()

conn = engine.connect()