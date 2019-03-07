#encoding: utf-8
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
import app
from exts import db
from models import User
from flask_session import Session

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db',MigrateCommand)
def init_ext(app):
    migrate.init_app(app)
    db.init_app(app)


if __name__ == '__main__':
    app.run()




