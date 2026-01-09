from fastapi import FastAPI
from app.database.database import create_db_and_tables
app = FastAPI()

@app.on_event("startup")
def startup_event():
    create_db_and_tables()

#test