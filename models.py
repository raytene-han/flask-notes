from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class User(db.Model):
    """User model."""

    __tablename__ = "users"
    user = db.Column(db.String(20),
                   primary_key=True)
    password = db.Column(db.String(100),
                         nullable=False)
    email = db.Column(db.String(50),
                         nullable=False,
                         unique=True)
    first_name = db.Column(db.String(30),
                         nullable=False)
    last_name = db.Column(db.String(30),
                         nullable=False)

    @classmethod
    def register(cls, username, pwd, email, first_name, last_name):
        """Register user w/hashed password & return user."""

        hashed_pwd = bcrypt.generate_password_hash(pwd).decode('utf8')
        # hashed_email = bcrypt.generate_password_hash(email).decode('utf8')


        # return instance of user w/username and hashed pwd
        return cls(username=username,
                   password=hashed_pwd,
                   email=email,
                   first_name=first_name,
                   last_name=last_name)
