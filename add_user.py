from venv.app import create_app
from logs.models import db, User

app = create_app()

with app.app_context():
    user = User(username='admin')
    user.set_password('password')
    db.session.add(user)
    db.session.commit()
