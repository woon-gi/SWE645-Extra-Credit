from flask import Blueprint, request, jsonify
from services import SurveyService
from sqlalchemy.exc import NoResultFound

bp = Blueprint('survey_routes', __name__)

@bp.route('/api/surveys', methods=['GET'])
def get_surveys():
    surveys = SurveyService.get_all_surveys()
    return jsonify({"surveys": [s.to_dict() for s in surveys]})

@bp.route('/api/surveys/create', methods=['POST'])
def create_survey():
    survey = SurveyService.save_survey(request.json)
    return jsonify(survey.to_dict()), 201
