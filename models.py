from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from werkzeug.utils import secure_filename
class User(db.Model):
    # id name pw  info
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),unique=True)
    pw = db.Column(db.String(50))
    info = db.Column(db.String(100),default="")
    is_active = db.Column(db.Boolean,default=True)

    #指定关系属性字段
    articles = db.relationship('Article',backref = 'user')

    __tablename__ = 'user'

class Article(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50),unique=True)
    addtime = db.Column(db.DateTime)
    body = db.Column(db.String(50),unique=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))


    # user 想直接获取他下面的文章  指定db.relationship() 关系属性
    # 文章 直接拿到user对象


user_user_address = \
    db.Table('user_user_address',db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
		    		db.Column('user_address_id', db.Integer, db.ForeignKey('user_address.id')))

class UserAddress(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    address = db.Column(db.String(10),primary_key=True)
    users = db.relationship('User',secondary=user_user_address,backref='useraddress')