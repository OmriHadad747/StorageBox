from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from api.config import env_config


api = Api()
db = SQLAlchemy()


def createApp(configName):

    app = Flask(__name__, )
    app.config.from_object(env_config[configName])
    
    import resources
    api.add_resource(resources.user.User, "/api/user/<string:email>")
    api.add_resource(resources.user.UserRegistration, "/api/user")
    api.init_app(app)
    
    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app