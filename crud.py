"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def get_user_by_email(email):
    """ Get user with email."""

    user = User.query.filter_by(email=email).first()

    return user


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(
        title=title, 
        overview=overview,
        release_date=release_date,
        poster_path=poster_path
        )

    db.session.add(movie)
    db.session.commit()

    return movie

def get_all_movies():
    """Return list of all movies(Movie objects)"""
    
    movies = Movie.query.all()

    return movies

def get_movie_by_id(movie_id):
    """Return a movie(Movie objects) with a specific id."""
    
    movie = Movie.query.get(movie_id)

    return movie

def get_all_users():
    """Return list of all users(User objects)"""
    
    users = User.query.all()

    return users

def get_user_by_id(user_id):
    """Return a movie(Movie objects) with a specific id."""
    
    user = User.query.get(user_id)

    return user


def create_rating(user, movie, score):
    """Create and return a new rating."""

    rating = Rating(
        user=user, 
        movie=movie,
        score=score
        )

    db.session.add(rating)
    db.session.commit()

    return rating





if __name__ == '__main__':
    from server import app
    connect_to_db(app)