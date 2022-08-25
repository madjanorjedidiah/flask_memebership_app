from app import apps
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app.debug = True
app.port = 5000
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres1234@localhost/members'
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)