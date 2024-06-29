from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
from flask_restful import Api, Resource
from classes import *
import os

load_dotenv()

app = Flask(__name__)
app.config["SECKRET_KEY"] = os.getenv("SECKRET_KEY")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
CORS(app, resources={r'/*': {"origins": os.getenv("ORIGINS") }})

api=Api(app)

api.add_resource(NewPost, '/')

SWAGGER_URL = os.getenv('/swagger')
API_URL = os.getenv("API_URL")
swagger_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        "app_name": "SAMPLE API"
    }
)
app.register_blueprint(swagger_blueprint, url_prefix=SWAGGER_URL)

from . import routes