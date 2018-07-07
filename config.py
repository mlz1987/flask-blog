
class Config(object):
    """Base config class"""
    pass

class ProdConfig(Config):
    """Production config class."""
    pass

class Devconfig(Config):
    """Development config class."""
    # Open the DEBUG
    DEBUG = True
    # MySQL connection
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123123@127.0.0.1:3306/blog'