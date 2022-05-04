import os

from flask import Flask
from sqlalchemy import create_engine

def init_app():
    app = Flask(__name__)
    engine = create_engine(os.getenv('POSTGRES_URL'), echo=True, future=True)
    with engine.connect() as conn:

    return app
