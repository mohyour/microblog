from flask import Flask

app = Flask(__name__)

# import at the bottom to prevent circular import
from app import routes  # noqa: E402
