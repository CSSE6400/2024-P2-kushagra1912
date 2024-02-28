from datetime import datetime
from . import db


class Todo(db.Model):
    __tablename__ = "todos"

    id: int = db.Column(db.Integer, primary_key=True)
    title: str = db.Column(db.String(80), nullable=False)
    description: str = db.Column(db.String(120), nullable=True)
    completed: bool = db.Column(db.Boolean, nullable=False, default=False)
    deadline_at: datetime = db.Column(db.DateTime, nullable=True)
    created_at: datetime = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow
    )
    updated_at: datetime = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "deadlint_at": self.deadline_at.isoformat() if self.deadline_at else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    def __rep__(self):
        return f"<Todo {self.id} {self.title}>"
