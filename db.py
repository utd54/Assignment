from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///expenses.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()