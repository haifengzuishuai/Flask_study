'''
#模板
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
        return '123'

if __name__=='__main__':
    app.run()
'''



#encoding: utf-8
'''
from flask import Flask,redirect,url_for
app = Flask(__name__)

@app.route(str('/'))
def index():
    login_url = url_for('login1')
    return redirect(login_url)
    return '这是首页'
@app.route('/login222/')
def login1():
    return '这是登陆'
@app.route('/question/<is_login>')
def question(is_login):
    if is_login == '1':
        return '这里是问答'
    else:
        return redirect(url_for('login1'))

# @app.route('/a/<id>')
# def a(id):
#     return u'你请求的参数是：%s' %id

if __name__=='__main__':
    app.run(debug=True)
'''
# from flask import Flask,redirect,url_for,render_template
# app = Flask(__name__)
#
# @app.route(str('/'))
# def index():
#     context = {
#         'username':u'hahha',
#         'gender':u'男',
#         'age':u'18'
#     }
#     return render_template('index.html',**context)
#
#
# if __name__=='__main__':
#     app.run(debug=True)
'''
下面是访问字典
# '''
# from flask import Flask,redirect,url_for,render_template
# app = Flask(__name__)
#
# @app.route(str('/'))
# def index():
#     class Person(object):
#         name = u'席海峰'
#         age = 18
#     p = Person()
#     context = {
#         'username':u'hahha',
#         'gender':u'男',
#         'age':u'18',
#         'person':p,
#         'websites':{
#             'baidu':'www.baidu.com',
#             'google':'haifengzuishuai'
#         }
#     }
#
#     return render_template('index.html',**context)
#
#
# if __name__=='__main__':
#     app.run(debug=True)
'''
if判断语句

'''
#
# from flask import Flask,render_template
# app = Flask(__name__)
# @app.route('/<is_login>')
# def index(is_login):
#     f is_login == '1':
#         user = {
#             'username':u'海峰最帅',
#             'age':111
#         }
#         return render_template('if_index.html',user=user)
#     else:
#         return render_template('if_index.html')
# if __name__=='__main__':
#     app.run(debug=True)
'''
下面是for循环
'''
#
# from flask import Flask,render_template
# app = Flask(__name__)
# @app.route('/')
# def index():
#     books = [{
#         'name':u'西游记',
#         'age':110
#     },{
#         'name':u'西游记1',
#         'age':111
#     },{
#         'name':u'西游记2',
#         'age':112
#     },{
#         'name':u'西游记3',
#         'age':113
#     }]
#     return render_template('for_index.html',books=books)
# if __name__=='__main__':
#     app.run(debug=True)
'''
下面是15课时的过滤器
'''
# tupian1='https://www.baidu.com/img/baidu_jgylogo3.gif'
# from flask import Flask,render_template
# app = Flask(__name__)
# @app.route('/')
# def index():
#     comments = [
#         {'uesr':u'haifeng',
#          'concent':'dasdasda'
#         },
#         {
#             'user':u'lalala',
#             'concent':'dadadadawwwwwwww'
#         },
#         {
#             'user':u'lalala',
#             'concent':'dadadadawwwwwwww'
#         },
#         {
#             'user':u'lalala',
#             'concent':'dadadadawwwwwwww'
#         }
#     ]
#     return render_template('15_index.html',tupian=tupian1,comments=comments)
# if __name__=='__main__':
#     app.run(debug=True)
'''
16继承和使用block
'''
# from flask import Flask,render_template
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return render_template('16_index.html')
# @app.route('/login/')
# def login():
#     return render_template('16_login.html')
# if __name__=='__main__':
#     app.run(debug=True)
'''
17URL链接和静态文件
'''
# from flask import Flask,render_template
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return render_template('17_index.html')
# @app.route('/login/')
# def login():
#    return render_template('17_login.html')
# if __name__=='__main__':
#     app.run(debug=True)
'''
22课时初始化一些操作  mysql等
'''
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# import config
# import pymysql
#
# app = Flask(__name__)
# app.config.from_object(config)
# db = SQLAlchemy(app)
#
# db.create_all()
#
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
#mysql-python安装不了无法实现下面按照百度的来实现对数据库的操作
#查询版本
# import pymysql
# db = pymysql.connect("127.0.0.1","root","123456","haifeng")
# cursor = db.cursor()
# cursor.execute("SELECT VERSION()")
# data = cursor.fetchone()
# print("Database version : %s " % data)
# db.close()

#------------------------------------------------
'''
import pymysql
# 打开数据库连接
db = pymysql.connect("127.0.0.1","root","123456","haifeng")
# 使用cursor()方法获取操作游标
cursor = db.cursor()
#要执行的sql
sql = """INSERT INTO test2
         VALUES ('Mohan',null )"""
# 执行sql
cursor.execute(sql)
# 提交到数据库执行
db.commit()
# 退出
db.close()
'''
#-----------------------------------------------------
'''
24课时往数据库添加数据
'''

# from flask import Flask
# import pymysql
# from flask_sqlalchemy import SQLAlchemy
#
#
#
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     print('开始插入数据')
#     db = pymysql.connect("127.0.0.1", "root", "123456", "haifeng")
#     # 使用cursor()方法获取操作游标
#     cursor = db.cursor()
#     # 要执行的sql
#     sql = """INSERT INTO test2
#              VALUES ('Mohan我最帅',null )"""
#     test2 = """select * from test2"""
#     cursor.execute(sql)#执行sql
#     cursor.execute(test2)
#     # row_1 = cursor.fetchone()#获取第一行数据
#     # print(row_1)
#     # row_3 = cursor.fetchmany(3)#获取前三行
#     # print(row_3)
#     # selectsql = """select * from test2"""
#     # data = cursor.execute(selectsql.encode('utf-8'))#记写法 输出格式未utf8
#     # cursor.execute(selectsql.encode('utf-8'))
#     #获取所有记录列表
#     print('插入完成，准备查询最新数据')
#     print('查询表中所有数据')
#     results = cursor.fetchall()
#     for row in results:
#         name = row[0]
#         id = row[1]
#         # print(name,id)
#         print ("name=%s,id=%s" % \
#               (name, id ))
#         print(row[5])
#     db.commit()
#     db.close()
#     return '执行成功'
#
# if __name__ == '__main__':
#     app.run(debug=True)
'''
31session存储
'''
# from flask import Flask,session
# import os
# app = Flask(__name__)
# #添加数据到session中,随机生成24个字符的字符串
# app.config['SECRET_KEY']=os.urandom(24)
#
#
# @app.route('/')
# def index():
#     session['username'] = 'xihaifeng'
#     return '写入成功'
#
#
# if __name__=='__main__':
#     app.run(debug=True)


'''
35项目搭建
'''
#模板
from flask import Flask

app = Flask(__name__)
import config
app.config.from_object(config)
@app.route('/')
def index():
        return '123'

if __name__=='__main__':
    app.run()


