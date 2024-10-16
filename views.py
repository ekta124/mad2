from flask import render_template_string, render_template, request, jsonify
from flask_security import auth_required, current_user, roles_required,SQLAlchemyUserDatastore, roles_accepted
from flask_security.utils import hash_password, verify_password 

from extentions import db
from models import StudyResource

def create_view(app,user_datastore:SQLAlchemyUserDatastore):
    # homepage
    
    @app.route("/")
    def home():
        return render_template('index.html')
    
    @app.route("/register",methods=['POST'])
    def register():
        data = request.get_json()
        
        email = data["email"]
        password = data["password"]
        role = data["role"]

        if not email or not password or role not in ['instructor','student']:
            return jsonify({"message":"Invalid Input"})
        
        if user_datastore.find_user(email=email):
            return jsonify({"message":"user already exissts"})
        if role =='instructor':
            active=False
        elif role == 'student':
            active = True
        try:
            user_datastore.create_user(email=email,password=hash_password(password),roles=[role],active=active)
            db.session.commit()
        except:
            print("error while creating")
            db.session.rollback()
            return jsonify({"message":"error while creating user"}),400
        return jsonify({"message":"user created"}),200
    
    @app.route('/user-login',methods=['POST'])
    def user_login():
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        print(data)
        # userModel = user_datastore.user_model()
        
        if not email or not password:
            return jsonify({"message":"not valid email or password"}),404
        
        user = user_datastore.find_user(email=email)
        
        if not user:
            return jsonify({"message" : "invalid user"}),404
        
        if verify_password(password,user.password):
            return jsonify({'token': user.get_auth_token(),'role' : user.roles[0].name, 'id': user.id, 'email':user.email}),200
        else:
            return jsonify({"message":"wrong password"})  
    
        
    @app.route('/activate-inst/<id>', methods=['GET'])
    @roles_required("admin")
    def activate_inst():
        user = user_datastore.find_user(id=id)
        if not user:
            return jsonify({"message":"user not present"}),404
        
        # check if inst already activated
        if(user.active == True):
            return jsonify({"message":"user already active"}),400
        
        user.active = True
        db.session.commit()
        return jsonify({"message":"user is activated"}),200
         
        
    # activate study resource
    @app.route('/verify-resource/<id>',methods=['GET'])
    @roles_required('instructor')
    def verify_resources(id):
        resource = StudyResource.query.get(id)
        if not resource:
            return jsonify({"message":"invalid id"}),404
        resource.is_approved = True
        db.session.commit()
        return jsonify({"message":"resource is now approved"}),200
    
    
    @app.route('/inactive-instructors')
    @roles_accepted("admin")
    def inactive_instructors():
        all_users = user_datastore.user_model().query.all()
        
        inactive_instructors = [
            user for user in all_users
            if not user.active and any(role.name == 'instructor' for role in user.roles)
        ]
        
        results = [
            {
                'id': user.id,
                'email': user.email,
            }
            for user in inactive_instructors
        ]
        return jsonify(results),200
    
    