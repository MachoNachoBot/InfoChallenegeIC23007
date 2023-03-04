from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import routes
#from flaskblog.models import User, Post
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cda2564d2b56a1f70d6714c017ce32d5'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///PTechBlog.db'
db = SQLAlchemy(app)
app.app_context().push()
bcrypt = Bcrypt(flaskblog)
#db.create_all()


