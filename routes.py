from flask import Blueprint, request, jsonify
from services import SurveyService
from sqlalchemy.exc import NoResultFound

bp = Blueprint('survey_routes', __name__)

@bp.route('/surveys', methods=['GET'])
def get_surveys():
    surveys = SurveyService.get_all_surveys()
    return jsonify({"surveys": [s.to_dict() for s in surveys]})

@bp.route('/surveys/create', methods=['POST'])
def create_survey():
    survey = SurveyService.save_survey(request.json)
    return jsonify(survey.to_dict()), 201

@bp.route('/surveys/<int:survey_id>/update', methods=['PUT'])
def update_survey(survey_id):
    try:
        updated_survey = SurveyService.update_survey(survey_id, request.json)
        return jsonify(updated_survey.to_dict())
    except NoResultFound:
        return jsonify({"error": "Survey not found"}), 404
    
@bp.route('/surveys/<int:survey_id>', methods=['DELETE'])
def delete_survey(survey_id):
    try:
        SurveyService.delete_survey(survey_id)
        return jsonify({"message": f"Survey {survey_id} deleted successfully."}), 200
    except NoResultFound:
        return jsonify({"error": "Survey not found"}), 404

@bp.route('/surveys/<int:survey_id>', methods=['GET'])
def get_survey_by_id(survey_id):
    try:
        survey = SurveyService.get_survey_by_id(survey_id)
        return jsonify(survey.to_dict())
    except NoResultFound:
        return jsonify({"error": "Survey not found"}), 404

