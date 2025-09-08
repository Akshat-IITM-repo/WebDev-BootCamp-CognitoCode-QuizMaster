# user -- user_id,  _name, _email, _pwd, relationship ------ 1. customer_details 2. store_manager_details
# role -- id, name
# user_role -- id, user_id, role_id
# customer -- id, user_id, address, preferred_mode_of_payment, phone_number
# store_manager -- id, user_id, qualification 

from controller.database import db

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_name = db.Column(db.String(50),nullable=False)
    user_email = db.Column(db.String(50),unique=True,nullable=False)
    user_password = db.Column(db.String(250),nullable=False)

    customer_details = db.relationship('Customer', backref='user', lazy=True, uselist=False)
    store_manager_details = db.relationship('StoreManager', backref='user', lazy=True, uselist=False)

class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

class UserRole(db.Model):
    __tablename__ = 'user_role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    address = db.Column(db.String(50), nullable=False)
    preferred_mode_of_payment = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)

class StoreManager(db.Model):
    __tablename__ = 'store_manager'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    qualifications = db.Column(db.String(50), nullable=False)