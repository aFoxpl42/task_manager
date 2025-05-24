from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    print("DEBUG: Loaded config: ", app.config.get("SQLALCHEMY_DATABASE_URI"))
    
    db.init_app(app)
    
    from .routes import main
    app.register_blueprint(main)
    
    return app