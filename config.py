"""
The purpose of this file is to manage the configuration settings for the application, including secret keys and database connection details. It uses environment variables to securely store sensitive information and allows for easy configuration across different environments (development, testing, production).
"""

# import necessary libraries, utilities, and modules
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create a class for configuration settings
class Config:

    # Instantiate the secret key and JWT key
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'dev-jwt-secret-key')

    # Create both the private and public database url
    _database_url = os.environ.get('DATABASE_URL', 'postgresql://localhost:5432/hr_productivity')

    # Control flow for database url handling
    if _database_url.startswith('postgres://'):
        _database_url = _database_url.replace('postgres://', 'postgresql://', 1)
    
    # Set the database url do not track modifications to save resources
    SQLALCHEMY_DATABASE_URI = _database_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False

