from exts import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    telephone = db.Column(db.String(80))
    password = db.Column(db.String(120), unique=True)
    repassword = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return '<User %r>' % self.username












