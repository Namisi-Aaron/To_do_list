from app import db

class Task(db.Model):
    task = db.Column(db.String(20), primary_key=True, nullable=False, unique=True)

    def __repr__(self):
        return f'{self.task}'