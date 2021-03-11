from datetime import datetime
from run import db
class Audio(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(80),  nullable=False)
    upload_time = db.Column(db.DateTime, nullable=True)
    duration = db.Column(db.Integer,nullable=True)
    type_id = db.Column(db.String(80), db.ForeignKey(AudioType.id), nullable=False)
    type_=category = db.relationship('AudioBook',
        backref=db.backref('audio', lazy=True))
    created_at = db.Column(db.DateTime, nullable=True,)
    updated_at = db.Column(db.DateTime, nullable=True,onupdate=datetime.now())

    def __repr__(self):
        return '<User %r>' % self.name

class AudioType(db.Model):
    type_ = db.Column(db.String(80), unique=True, nullable=False)
