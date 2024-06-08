from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Notes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    data = db.Column(db.String(100000))
    # Flask will handle the data and time on its own through the below code line
    date = db.Column(db.DateTime(timezone=True),default=func.now())

    # Setting relationship between notes and the respective user (Foreign Key)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model,UserMixin):
    id = db.Column(db.Integer , primary_key=True)
    email = db.Column(db.String(150),unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Notes')
    is_active = db.Column(db.Boolean, default=True)

    # @property
    # def is_active(self):
    #     return self.is_active