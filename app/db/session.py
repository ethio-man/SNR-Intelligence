from sqlmodel import Session,create_engine
import os

DB_URL=os.getenv('DB_URL')

engine=create_engine(DB_URL,echo=True)

def get_session():
    with Session(engine) as session:
        yield session