# server/app.py

from flask import Flask
from flask_migrate import Migrate

from models import db

# create a Flask application instance 
app = Flask(__name__)