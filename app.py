from flask import Flask, request, render_template, redirect, url_for, flash, session
import os
from exts import db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import config1
from models import User, Question
from decorators import login_required

SECRET_KEY = os.urandom(24)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:123456@127.0.0.1:3306/haifeng'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config.from_object(config1)
db.init_app(app)


@app.route('/')
def index():
    context = {
        'questions': Question.query.all()
    }
    return render_template('index.html', **context)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter(User.username == username, User.password == password).first()
        if user:
            session['user_id'] = user.id
            session.permanent = True
            # return redirect(url_for('templates/login.html'))
            return render_template('index.html')
        else:
            return '账户名或密码错误'


@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')

        user = User.query.filter(User.telephone == telephone).first()
        if user:
            return '该手机号码已被注册，请换号码'
        else:
            if password != repassword:
                return '两次密码不相同'
            else:
                user = User(telephone=telephone, username=username, password=repassword, repassword=password)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))


@app.route('/logout/')
def logout():
    # session.pop('user_id')
    # del session['user_id']
    session.clear()
    return redirect(url_for('login'))


@app.route('/question/', methods=['GET', 'POST'])
@login_required
def question():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        question = Question(title=title, content=content)
        user_id = session.get('user_id')
        user = User.query.filter(User.id == user_id).first()
        question.author = user
        db.session.add(question)
        db.session.commit()
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
