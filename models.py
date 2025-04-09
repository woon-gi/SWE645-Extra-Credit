from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Survey(db.Model):
    __tablename__ = 'surveys'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    street_address = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    zip = db.Column(db.String(10))
    phone_number = db.Column(db.String(20))
    email = db.Column(db.String(255))
    date_of_survey = db.Column(db.DateTime)
    liked_most = db.Column(db.Text)
    interested_in = db.Column(db.Text)
    likelihood = db.Column(db.String(100))

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "street_address": self.street_address,
            "city": self.city,
            "state": self.state,
            "zip": self.zip,
            "phone_number": self.phone_number,
            "email": self.email,
            "date_of_survey": self.date_of_survey.isoformat() if self.date_of_survey else None,
            "liked_most": self.liked_most,
            "interested_in": self.interested_in,
            "likelihood": self.likelihood
        }

