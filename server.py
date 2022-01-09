"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined



app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# Replace this with routes and view functions!
@app.route("/")
def render_homepage():
    """Render homepage."""

    return render_template("homepage.html")

@app.route("/movies")
def show_all_movies():
    movies = crud.get_all_movies()

    return render_template("all_movies.html", movies=movies)


@app.route("/movies/<movie_id>")
def show_movie_details(movie_id):
   
    movie = crud.get_movie_by_id(movie_id)
   
    return render_template("movie_details.html", movie=movie)

@app.route("/users")
def show_all_users():
    users = crud.get_all_users()

    return render_template("all_users.html", users=users)


@app.route("/users/<user_id>")
def show_user_details(user_id):
   
    user = crud.get_user_by_id(user_id)
   
    return render_template("user_details.html", user=user)

@app.route("/users", methods=['POST'])
def create_user():
    """ Create User."""

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if not user:
        crud.create_user(email, password)
        message = "User created"      
    else:
        message = "An account for this email alrady exists"

    flash(message)

    return redirect("/")

    
@app.route("/login", methods=['POST'])
def login_user():
    """ Login User."""

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    
    if not user:
        message = "User doen't exist"      
    else:
        if password == user.password:
            message = "Logged in!"
            session["user"] = user.user_id

    flash(message)

    return redirect("/")

@app.route("/ratings", methods=['POST'])
def create_rating():
    """ Create User rating."""

    movie = request.form.get('movie')
    score = request.form.get('score')
    user = crud.get_user_by_id(session["user"])

    crud.create_rating(user, movie, score)

    return redirect(f"/movies/<{movie.movie_id}>")


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
