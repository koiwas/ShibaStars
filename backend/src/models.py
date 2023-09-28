from datetime import datetime
from src import db

class Base(db.Model):
    __abstract__ = True

    def soft_delete(self, user: str):
        self.deleted_by = user
        self.deleted_at = datetime.now()

    def restore(self):
        self.deleted_by = None
        self.deleted_at = None

class User(Base):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    created_by = db.Column(db.String(30), default='sysadmin')
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_by = db.Column(db.String(30), default='sysadmin')
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_by = db.Column(db.String(30))
    deleted_at = db.Column(db.DateTime)

    def __repr__(self):
        return f"<User '{self.username}'>"

class Task(Base):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    is_closed = db.Column(db.Boolean, default=False)
    created_by = db.Column(db.String(30), default='sysadmin')
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_by = db.Column(db.String(30), default='sysadmin')
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_by = db.Column(db.String(30))
    deleted_at = db.Column(db.DateTime)

    contents = db.relationship('Content', backref='task', lazy='dynamic')

    def __repr__(self):
        return f"<Task ID: {self.id}, Closed: {self.is_closed}>"

class Content(Base):
    __tablename__ = 'contents'

    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False, index=True)
    content = db.Column(db.String(255))
    is_checked = db.Column(db.Boolean, default=False)
    created_by = db.Column(db.String(30), default='sysadmin')
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_by = db.Column(db.String(30), default='sysadmin')
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_by = db.Column(db.String(30))
    deleted_at = db.Column(db.DateTime)

    def __repr__(self):
        return f"<Task ID: {self.task_id}, Content: {self.content}, Checked: {self.is_checked}>"
