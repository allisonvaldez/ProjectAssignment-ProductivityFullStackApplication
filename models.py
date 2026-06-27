"""
This file is in charge of defining the User, AvailablityBlock, and Meeting database tables and their respective relationships. This is the data layer and the AvailablityBlock and Meeting each will have a user_id foreign key which makes them a relational resource and allows relational resources for per-user ownership.
"""

# Create a class for the User table and its columns, and define the relationship to the AvailablityBlock and Meeting tables.

class User(db.Model):

    # Create the tablename for the User table
    __tablename__ = "users"

    # Create the columns necessary for the User table
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False, index = True)
    password_hash = db.Column(db.String(255), nullable = False)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)

    """
    Code the necessary components needed to establish the relationship between the User table and the AvailablityBlock and Meeting tables. This helps us to access and declare the necessary AvailablityBlocks and Meetings for each user. This declares the one to many relationships.
    """

    availability_blocks = db.relationship(
        "AvailablityBlock",
        backref = "user", 
        cascade = "all, delete-orphan",
        lazy = "True"
    )

    meetings = db.relationship(
        "Meeting",
        backref = "user",
        cascade = "all, delete-orphan",
        lazy = "True"
    )

    """
    This block of code is in charge of hashing the password for the user and storing it in the database. The set_password function will utilize werkzeug.security to hash the password. It will save the hashed password in the password_hash column in User table. 
    
    The check_password function will be used to verify the password when the user tries to log in. It will utilize werkzeug.security to check the password against the hashed password stored in the database and return a boolean value indicating whether the password is correct or not.
    """

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    # This function converts the SQLAlchemy object into a plain Python dictionary that jsonify() will turn into JSON. password_hash is purposely left out for security reasons.
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "created_at": self.created_at.isoformat(),
        }

# Create a class for the AvailablityBlock table and its columns, and define the relationship to the User table.

class AvailablityBlock(db.Model):

    # Create the tablename for the AvailablityBlock table
    __tablename__ = "availability_blocks"

    # Create the columns necessary for the AvailablityBlock table
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    day_of_week = db.Column(db.String(10), nullable = False)
    start_time = db.Column(db.Time, nullable = False)
    end_time = db.Column(db.Time, nullable = False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)



# Create a class for the Meeting table and its columns, and define the relationship to the User table.

class Meeting(db.Model):

    # Create the tablename for the AvailablityBlock table
    __tablename__ = "meeting_blocks"

    # Create the columns necessary for the AvailablityBlock table
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    day_of_week = db.Column(db.String(10), nullable = False)
    start_time = db.Column(db.DateTime, nullable = False)
    end_time = db.Column(db.DateTime, nullable = False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    