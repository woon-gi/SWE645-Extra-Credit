from models import db, Survey
from sqlalchemy.exc import NoResultFound

class SurveyService:

    @staticmethod
    def get_all_surveys():
        return Survey.query.all()

    @staticmethod
    def save_survey(data):
        survey = Survey(**data)
        db.session.add(survey)
        db.session.commit()
        return survey