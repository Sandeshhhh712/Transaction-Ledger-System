from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql.annotation import Annotated
from sqlmodel import SQLModel , create_engine

database_url = "sqlite:///database.db"
engine = create_engine(database_url)
engine = create_engine(database_url,
                       connect_args={"check_same_thread": False},
                       echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session,Depends(get_session)]
