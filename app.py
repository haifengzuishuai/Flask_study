#encoding:utf-8
from flask import Flask,render_template,request
import config
from manage import init_ext


app = Flask(__name__)
app.config.from_object(config)
init_ext(app)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        pass

@app.route('/regist/',methods=['GET','POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        pass

if __name__ == '__main__':
    app.run()
