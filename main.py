from flask import Flask, render_template
from controller.database import db
from controller.config import Config
from controller.models import *

app = Flask(__name__, template_folder='templates', static_folder='static')
# app.config[SQLALCHEMY_DATABASE_URI] = 'sqlite:///database.sqlite3'
# app.config[SECRET_KEY] = 'secret_key'
# app.config[SQLALCHEMY_TRACK_MODIFICATIONS] = False
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

    admin_role = Role.query.filter_by(name='admin').first()
    if(not admin_role):
        admin_role = Role(name='admin')
        db.session.add(admin_role)

    cust_role = Role.query.filter_by(name='customer').first()
    if(not cust_role):
        cust_role = Role(name='customer')
        db.session.add(cust_role)

    manager_role = Role.query.filter_by(name='store_manager').first()
    if(not manager_role):
        manager_role = Role(name='store_manager')
        db.session.add(manager_role)

    # admin_user = User.query.filter_by(user_email='admin@gmail.com').first()
    # if(not admin_user):
    #     admin_user = User(
    #         user_name = 'Super Admin',
    #         user_email = 'admin@gmail.com',
    #         user_password = '1234567890'
    #     )
    #     db.session.add(admin_user)

    #     admin_user_details = User.query.filter_by(user_email='admin@gmail.com').first()
    #     admin_role = Role.query.filter_by(name='admin').first()

    #     u_id = admin_user_details.user_id
    #     r_id = admin_role.id

    #     user_role = UserRole(user_id = u_id, role_id = r_id)
    #     db.session.add(user_role)

        
    admin_user = User.query.filter_by(user_email='admin@gmail.com').first()
    if(not admin_user):
        admin_role = Role.query.filter_by(name='admin').first()
        admin_user = User(
            user_name = 'Super Admin',
            user_email = 'admin@gmail.com',
            user_password = '1234567890',
            roles = [admin_role]
        )

        db.session.add(admin_user)
    
    db.session.commit()

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def reg():
    return "Register Page is Under Development"



if __name__ == "__main__":
    app.run()
    
