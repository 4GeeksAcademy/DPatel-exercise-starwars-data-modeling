import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    gender = Column(String(250))
    height = Column(String(250))
    homeworld = Column(String(250))

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    Cost = Column(String(250), nullable=False)
    Manufacturer = Column(String(250), nullable=False)
    Model = Column(String(250))
    length = Column(String(250))
    Created = Column(String(250))

class Species(Base):
    __tablename__ = 'Species'
    id = Column(Integer, primary_key=True)
    Name = Column(String(250), nullable=False)
    Homeworld = Column(String(250), nullable=False)
    Language = Column(String(250),)
    Average_Lifespan = Column(String(250))
    Classification = Column(String(250))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
