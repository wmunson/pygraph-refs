from flask import Flask
# from app.start import app
from app.views import views
# from .models

app = Flask(__name__)

app.register_blueprint(views, url_prefix='/')