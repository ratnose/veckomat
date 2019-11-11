from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = "dont-make-me"
app.config["MONGO_URI"] = "mongodb://10.20.1.50:27017/flaskmongo"
mongo = PyMongo(app)
