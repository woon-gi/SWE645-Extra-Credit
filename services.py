from models import db, Survey
from sqlalchemy.exc import NoResultFound
from datetime import datetime

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

    @staticmethod
    def update_survey(survey_id, data):
        survey = Survey.query.get(survey_id)
        if not survey:
            raise NoResultFound("Survey not found")

        # Update all relevant fields if they exist in input data
        for field in [
            'first_name', 'last_name', 'street_address', 'city', 'state', 'zip',
            'phone_number', 'email', 'liked_most', 'interested_in', 'likelihood'
        ]:
            if field in data:
                setattr(survey, field, data[field])

        # Handle date_of_survey separately
        if 'date_of_survey' in data:
            try:
                survey.date_of_survey = datetime.fromisoformat(data['date_of_survey'])
            except ValueError:
                raise ValueError("Invalid date format. Use ISO format.")

        db.session.commit()
        return survey

    @staticmethod
    def delete_survey(survey_id):
        survey = Survey.query.get(survey_id)
        if not survey:
            raise NoResultFound("Survey not found")
        
        db.session.delete(survey)
        db.session.commit()

    @staticmethod
    def get_survey_by_id(survey_id):
        survey = Survey.query.get(survey_id)
        if not survey:
            raise NoResultFound("Survey not found")
        return survey

