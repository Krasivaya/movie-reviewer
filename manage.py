from app import create_app, db
from flask_script import Manager, Server
from app.models import User, Role

# Create app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

# Create app shell
@manager.shell
def shell_context():
    return dict(
        app = app,
        db = db,
        User = User,
        Role = Role
    )

if __name__ == '__main__':
    manager.run()
