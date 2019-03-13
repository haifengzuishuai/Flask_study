from flask import Flask, request, render_template, redirect, url_for, flash, session
import os
from exts import db
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
import config1



SECRET_KEY = os.urandom(24)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:123456@127.0.0.1:3306/haifeng'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config.from_object(config1)

@app.route('/')
def hello_world():
    return render_template('index.html')
    # return redirect(url_for('index'))

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        pass

@app.route('/regist/',methods=['GET','POST'])
def regist():
    error = None
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        error = '注册错误'



if __name__ == '__main__':
    app.run()
