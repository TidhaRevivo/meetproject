from flask import Flask, render_template, request
from flask import session as userdata
from database import *
from textblob import TextBlob

app = Flask(__name__)
app.config['SECRET_KEY'] = 'changeme'

global current_user
current_user = ''
global current_movie
current_movie=''
# TODO: Add all of the routes you want below this line!


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	global current_user
	if request.method== "GET":

		return render_template('signup.html')
	else:
		if get_user_by_username(request.form["username"]) == None:

			name= request.form["name"]
			username= request.form["username"]
			current_user= username
			password= request.form["pwd"]
			email= request.form["email"]
			create_user(email,username, password, name)
			return render_template('home.html')
		else:
			return ("UserName already exists")

@app.route('/login', methods=['GET', 'POST'])
def login():
	global current_user
	if request.method== "GET":
		return render_template('login.html')
	else:
		username= request.form["username"]
		password= request.form["pwd"]
		x=get_user_by_username(request.form['username'])
		if x != None:
		
			if get_user_by_username(username).password== request.form['pwd']:
				current_user= username
				return render_template('home.html')
			else:
				return render_template('login.html')
		else:
			return render_template('login.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
	return render_template('home.html')
@app.route('/about', methods=['GET', 'POST'])
def about():
	return render_template('about.html')
@app.route('/movies',  methods=['GET', 'POST'])
def movies():
	global current_user
	if request.method=="GET":
		return render_template('movies.html', movies=query_all(), series=print_all(), u= current_user)
	# else:
	# 	art_id= request.form["art_id"]
	# 	add_like(art_id)
	# 	return render_template('movies.html', posts=query_all(), users=print_all(), u= current_user)

@app.route('/series',  methods=['GET', 'POST'])
def series():
	global current_user
	if request.method=="GET":
		return render_template('series.html', u= current_user)
	# else:
	# 	username= request.form['username']
	# 	image= request.form["image"]
	# 	likes= 0
	# 	add_img(current_user,image,likes)
	# 	return render_template('series', posts=query_all(), users=print_all())
@app.route('/harrypotter1',  methods=['GET', 'POST'])	
def harrypotter1():
	global current_user
	current_movie="Harry Potter and the philosopher's stone"
	m= get_movie_by_name(current_movie)
	if request.method=="GET":
		return render_template('harrypotter1.html', u= current_user, m=m , posts= rating_post())
	else:
		rating= request.form["rating"]
		Rating(current_movie, rating)
		return render_template('harrypotter1.html', u= current_user, m=m , posts= rating_post())
@app.route('/lotr1',  methods=['GET', 'POST'])	
def lotr1():
	global current_user
	current_movie="The lord of the rings: the fellowship of the ring"
	m= get_movie_by_name(current_movie)
	if request.method=="GET":
		return render_template('lotr1.html', u= current_user, m=m , posts= rating_post())
	else:
		rating= request.form["rating"]
		Rating(current_movie, rating)
		return render_template('lotr1.html', u= current_user, m=m , posts= rating_post())



if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
