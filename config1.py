import os
DEBUG = True
SECRET_KEY = os.urandom(24)

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/haifeng?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False