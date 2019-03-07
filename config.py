#encoding: utf-8
import os

DEBUG = True
SECRET_KEY = os.urandom(24)
DB_URI = 'mysql+mysqldb://root:123456@127.0.0.1:3306/haifeng?charset=utf8'
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False



