from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_debugtoolbar import DebugToolbarExtension

app = Flask('guestbook')
# app = Flask(__name__.split('.')[0])
app.config.from_pyfile('config.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
toolbar = DebugToolbarExtension(app)

from guestbook import views, errors, commands
