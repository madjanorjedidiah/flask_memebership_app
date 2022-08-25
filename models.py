from datetime import datetime
from . config import db
from flask_login import UserMixin, AnonymousUserMixin


class UserIdentity(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50), unique=True, nullable=False)
	password = db.Column(db.String(500), nullable=False)
	date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	member = db.relationship('Members', backref='user')


	def __init__(self, username, email, image_file, password, date_created, member):
		self.username = username
		self.email = email
		self.image_file = image_file
		self.password = password
		self.date_created = date_created
		self.member = member


	def __repr__(self):
		return str(self.username, self.email)


class Members(db.Model):
	name = db.Column(db.String(100), nullable=True)
	department = db.Column(db.String(100), nullable=True)
	role = db.Column(db.String(100), nullable=True)
	title = db.Column(db.String(5), nullable=True)
	gender = db.Column(db.String(7), nullable=True)
	phone_number = db.Column(db.String(13), nullable=True)
	last_cert_date = db.Column(db.DateTime, nullable=True)
	email = db.Column(db.String(100), nullable=True)
	image_file = db.Column(db.String(100), nullable=True, default='default.jpg')
	user_fk = db.Column(db.Integer, db.ForeignKey('useridentity.id'), nullable=False)


	def __init__(self, name, department, role, title, gender, phone_number, last_cert_date, email, image_file, user_fk):
		self.name = name 
		self.department = department
		self.gender = gender
		self.role = role
		self.phone_number = phone_number
		self.title = title
		self.last_cert_date = last_cert_date
		self.email = email
		self.image_file = image_file
		self.user_fk = user_fk


	def __repr__(self):
		return self.name

