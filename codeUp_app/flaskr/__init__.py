from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from . import views

from SQLAlchemy_main import engine
from .models.base import Model
from .models.user import *


app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dev'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


with app.app_context():
    app.register_blueprint(views.bp)
    Model.metadata.create_all(engine)
