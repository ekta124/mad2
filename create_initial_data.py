from flask_security import SQLAlchemySessionUserDatastore
from flask_security.utils import hash_password
from extentions import db

def create_data(user_datastore : SQLAlchemySessionUserDatastore):
    
    print("### creating Data ###")

    user_datastore.find_or_create_role(name='admin',description='Administrator')
    user_datastore.find_or_create_role(name='instructor',description='Instructor')
    user_datastore.find_or_create_role(name='student',description='Student')

    if not user_datastore.find_user(email="admin@iitm.ac.in"):
        user_datastore.create_user(email="admin@iitm.ac.in", password=hash_password('pass'),active=True,roles=['admin'])
    if not user_datastore.find_user(email="stud@iitm.ac.in"):
        user_datastore.create_user(email="stud@iitm.ac.in", password=hash_password('pass'),active=True,roles=['student'])
    if not user_datastore.find_user(email="inst@iitm.ac.in"):
        user_datastore.create_user(email="inst@iitm.ac.in", password=hash_password('pass'),active=True,roles=['instructor'])

    db.session.commit()