from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '7c15b3ce3513739816ab122bd95f13a1'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI = 'sqlite:///tasks.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes