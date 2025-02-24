import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# people_vehicles = Table(
#    "people_vehicles",
#    Base.metadata,
#    Column("people_id", Integer, ForeignKey("people.id"), primary_key=True),
#    Column("vehicles_id", Integer, ForeignKey("vehicles.id"), primary_key=True)
# )

# vehicle_planets = Table(
#    "vehicle_planets",
#    Base.metadata,
#    Column("planet_id", Integer, ForeignKey("planets.id"), primary_key=True),
#    Column("vehicle_id", Integer, ForeignKey("vehicles.id"), primary_key=True),
   
# )

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    
    favoritePeople= relationship("FavoritePeople", backref="user")
   
class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    # description = Column(String(250))
    # gender = Column(String(250))
    # height = Column(String(250))
    homeworld = Column(String(250))

    # vehicles = relationship("Vehicles", secondary=people_vehicles, backref="pilots")
    favoritePeople = relationship("FavoritePeople", backref="people")



class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    homeworld_of = Column(String(250))
    # gravity = Column(String(250))
    # diameter = Column(String(250))

    favoritePlanet = relationship("FavoritePlanet", backref="planets")
    
# class Vehicles(Base):
#     __tablename__ = 'vehicles'
#     id = Column(Integer, primary_key=True)
#     cost = Column(String(250), nullable=False)
#     manufacturer = Column(String(250), nullable=False)
#     model = Column(String(250))
#     length = Column(String(250))
#     created = Column(String(250))

#     favorites = relationship("Favorite", backref="vehicles")

# class Species(Base):
#     __tablename__ = 'species'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)
#     homeworld = Column(String(250), nullable=False)
#     language = Column(String(250),)
#     average_Lifespan = Column(String(250))
#     classification = Column(String(250))
class FavoritePeople(Base):   
   __tablename__ = 'favoritePeople'
   id = Column(Integer, primary_key=True)
   user_id_favorites = Column(Integer, ForeignKey("users.id"))
   favorite_people_id = Column(Integer, ForeignKey("people.id"))
   

#    def to_dict(self):
#         return {}

class FavoritePlanets(Base):   
   __tablename__ = 'favoritePlanets'
   id = Column(Integer, primary_key=True)
   user_id_favorites = Column(Integer, ForeignKey("users.id"))
   favorite_planets_id = Column(Integer, ForeignKey("planets.id"))
  
   
   
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
