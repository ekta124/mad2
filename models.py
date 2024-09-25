from extentions import db
from flask_security import UserMixin, RoleMixin
from flask_security.models import fsqla_v3 as fsqla

fsqla.FsModels.set_db_info(db)
class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String,nullable=False,unique=True)
    password = db.Column(db.String,nullable=False)
    active = db.Column(db.Boolean,nullable=False)
    fs_uniquifier = db.Column(db.String(65),unique=True,nullable=False)
    roles = db.relationship('Role',secondary='user_roles')

class Role(db.Model,RoleMixin):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),nullable=False,unique=True)
    description = db.Column(db.String(255))
    
class UserRoles(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer,db.ForeignKey('role.id'))


# class StudyResource(db.Model):
#     pass