"""
This file is in charge of creating unbound instances of the db, migrate, jwt, and cors. It will help prevent unnecessary imports between app.py, models.py, and the route files. All the file imports will come from one shared place.
"""

# import necessary libraries, utilities, and modules
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS


