import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_cors import CORS

DATABASE = create_engine(os.getenv["DATABASE_URL"])

Base = declarative_base()

Session = sessionmaker(DATABASE)
session = Session

def create_db():
    Base.metadata.create_all(DATABASE)