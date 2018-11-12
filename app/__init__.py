from flask import Flask
from app.config import Config


app = Flask(__name__)
app.config.from_object(Config)

# import at the bottom to prevent circular import
from app import routes  # noqa: E402
