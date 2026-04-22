from passlib.context import CryptContext
from datetime import datetime,timedelta
from jose import jwt
import os

ACCESS_TOKEN_EXPIRE_MINUTES = 60
pwd_context=CryptContext(schemes=['bcrypt'],deprceated='auto')

def hash_password(password:str):
    return pwd_context.hash(password)

def verify_password(plain_password:str, hashed_password:str):
    return pwd_context.verify(plain_password,hashed_password)

def create_access_token(data:dict,expires_delta:timedelta):
    to_encode=data.copy()
    expire=datetime.utcnow() +( expires_delta or timedelta.)
    