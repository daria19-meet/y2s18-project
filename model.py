from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Place your database schema code here

# Example code:
class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    year = Column(Integer)


    def __repr__(self):
        return ("Student name: {}\nStudent Year:{}".format(self.name, self.year))