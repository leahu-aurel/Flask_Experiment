from flask import Flask
from flask_blog.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    bcrypt.init_app(app)

    from flask_blog.users.routes import bp as usersbp
    app.register_blueprint(usersbp)
    from flask_blog.main.routes import bp as mainbp
    app.register_blueprint(mainbp)

    return app