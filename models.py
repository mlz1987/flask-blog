from flask_sqlalchemy import SQLAlchemy
from main import app

# INIT the sqlalchemy object
# will be load the SQLALCHEMY_DATABASE_URL from config.py
# SLQAlchemy will be auto loaded from DevConfig in app
db = SQLAlchemy(app)

class User(db.Model):
    """Represents Protected users."""

    # Set the name from table
    __tablename__ = 'users'
    id = db.Column(db.String(45),primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self,username):
        self.username = username

    def __repr__(self):
        """Define the string format for instance of User."""
        return "<Model User `{}`>".format(self.username)

    #mysql - uroot - p123123 - e
    #"CREATE DATABASE blog default charset utf8 COLLATE utf8_general_ci;"
    #mysql - uroot - p123123 - e
    #"GRANT ALL ON blog.* TO 'root'@'127.0.0.1' IDENTIFIED BY '123123';"
    #mysql - uroot - p123123 - e
    #"GRANT ALL ON blog.* TO 'root'@'localhost' IDENTIFIED BY '123123';"
    #mysql - uroot - p123123 - e
    #"GRANT ALL ON blog.* TO 'root'@'%' IDENTIFIED BY '123123';"