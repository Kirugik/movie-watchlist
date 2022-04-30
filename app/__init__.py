from flask import Flask
# from .config import DevConfig 
from flask_bootstrap import Bootstrap 
from config import config_options 


# creating bootstrap instance 
bootstrap = Bootstrap()

def create_app(config_name):
    
    # creating Flask app instance 
    app = Flask(__name__)
    
    # Initializing flask extensions
    bootstrap.init_app(app)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .request import configure_request
    configure_request(app)

    return app