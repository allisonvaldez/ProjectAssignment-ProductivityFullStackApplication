"""
This file is in charge of creating unbound instances of the db, migrate, jwt, and cors. It will help prevent unnecessary imports between app.py, models.py, and the route files. All the file imports will come from one shared place.
"""

# import necessary libraries, utilities, and modules
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# Instanitate the db, migrate, jwt, and cors variables
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
cors = CORS()

# Configure the necessary extensions for the app to work and be able to be used accross the app without unnecessary imports.
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
cors = CORS()
