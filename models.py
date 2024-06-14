from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class LogEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(15), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    request_method = db.Column(db.String(10), nullable=False)
    request_path = db.Column(db.String(200), nullable=False)
    status_code = db.Column(db.Integer, nullable=False)
    user_agent = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            'ip_address': self.ip_address,
            'timestamp': self.timestamp.isoformat(),
            'request_method': self.request_method,
            'request_path': self.request_path,
            'status_code': self.status_code,
            'user_agent': self.user_agent,
        }

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)