from sqlmodel import SQLModel,Field

class User(SQLModel,table='True'):
    __tablename__='users'
    id:int =Field(primary_key=True,unique=True,default=None)
    name:str
    email:str =Field(unique=True)
    hashed_password:str