# web_app/routes/home_routes.py

from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    x = 2 + 2
    return f"Hello World, this the library on {x} th avenue"

@home_routes.route("/about")
def about():
    return "The book library"