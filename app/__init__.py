from flask import Flask
from app.config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
# passin the view that handles login to flask_login
login.login_view = 'login'


# import at the bottom to prevent circular import
from app import routes, models  # noqa: E402
