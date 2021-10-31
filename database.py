from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *
from textblob import TextBlob

engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# TODO: Add your database functions below this line!
def create_user(email, username,password,full_name):
	user = User(email=email, username=username, password=password, full_name=full_name)
	session.add(user)
	session.commit()
def get_user_by_username(username):
	user = session.query(User).filter_by(username=username).first()
	return user
	session.commit()
def get_movie_by_name(movie):
	movie = session.query(Movies).filter_by(movie=movie).first()
	return movie
	session.commit()

def query_all():
	movies= session.query(Movies).all()
	return movies
	session.commit()
def query_all():
	movies= session.query(Movies).all()
	return movies
	session.commit()
def print_all():
	shows= session.query(Series).all()
	return shows
	session.commit()
def add_movie(movie, image, link,rating):
	movie= Movies(movie=movie, image=image, link=link,rating=rating)
	session.add(movie)
	session.commit()
def rating_post():
	rating_post= session.query(Post).all()
	return rating_post
	session.commit()
def Rating(movie, rating):
	movie1= get_movie_by_name(movie)
	blob= TextBlob(rating)
	if blob.polarity >=0.5:
		movie1.rating+=5
	elif blob.polarity>0 and blob.polarity<0.5:
		movie1.rating+=2
	elif blob.polarity > -0.5 and blob.polarity<0:
		movie1.rating-=2
	elif blob.polarity<= -0.5:
		movie1.rating-=5
	session.commit()

	
# add_movie("Harry Potter and the philosopher's stone", 'static''/potter.jpg',"harrypotter1", 80)
# add_movie("The lord of the rings: the fellowship of the ring", 'static''/lotr1.jpg',"lotr1", 80)
