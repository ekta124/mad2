from extensions import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String,nullable=False,unique=True)
    password = db.Column(db.String,nullable=False)
    active = db.Column(db.Boolean,nullable=False)
    fs_uniquifier = db.Column(db.String(64),unique=True,nullable=False)
    roles = db.relationship('Role',secondary='user_roles')

class Role(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),nullable=False,unique=True)
    description = db.Column(db.String)
    
class UserRoles(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer,db.ForeignKey('role.id'))


 