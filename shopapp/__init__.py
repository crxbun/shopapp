from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import os

static_folder = "static"
flask_obj = Flask(__name__)

base_path = os.path.abspath(os.path.dirname(__file__))
flask_obj.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(base_path, "app.db")
flask_obj.secret_key = "henrybrandonkathy"

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(flask_obj, model_class=Base)

from shopapp.models import User

with flask_obj.app_context():
    db.create_all()