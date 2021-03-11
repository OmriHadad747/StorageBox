import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    
    SECRET_KEY = "omri"
    

class DevelopmentConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = "sqlite:///storageBox.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # DEBUG = False


env_config = {
    "development": DevelopmentConfig
}