from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.secret_key = 'your secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/lddsdb2023'
db = SQLAlchemy(app)


def create_app():
    from .view import views
    app.register_blueprint(views, url_prefix='/')
    from .model import Role, Administrator, Desease, Recommendation

    return app



