from sqlmodel import SQLModel,Field


class User(SQLModel,table='True'):
    id:int =Field(primary_key=True,unique=True,default=None)
    name:str
    hashed_password:str