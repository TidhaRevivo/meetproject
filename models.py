from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'
	id = Column(Integer, primary_key=True)
	username = Column(String)
	password = Column(String)
	full_name = Column(String)
	email = Column(String)
class Movies(Base):
	__tablename__='movies'
	id= Column(Integer, primary_key=True)
	movie=Column(String)
	image=Column(String)
	rating=Column(Integer)
	link=Column(String)
class Series(Base):
	__tablename__='series'
	id= Column(Integer, primary_key=True)
	show=Column(String)
	image=Column(String)
	rating=Column(Integer)
	link=Column(String)
class Post(Base):
	__tablename__= 'post'
	id = Column(Integer, primary_key=True)
	username= Column(String)
	rating= Column(String)
# TODO: Add your models below this line!