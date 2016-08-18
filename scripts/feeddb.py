from sqlalchemy.engine import create_engine
from sqlalchemy import schema, types, Table, column, String
metadata = schema.MetaData()

users=Table('users', metadata,
	schema.Column('username', String(100)),
	schema.Column('password',String(100)),
	)
engine= create_engine("postgresql://root:master12!@localhost:5432/desktopsoftware")
metadata.bind= engine
metadata.create_all(checkfirst=True)
