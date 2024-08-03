from flask import Blueprint, request, jsonify
from cruds.users import fetch_users_method, login_user_method, register_user_method

user_router = Blueprint('user_router', __name__)

@user_router.route("/", methods=["POST"])
def register_user():
    try:
        body = request.get_json()
        response = register_user_method(body)
        return jsonify({
            "status": response["status"],
            "data": response["data"],
            "message": response["message"],
        }), response["status_code"]   
    except Exception as e:
        return jsonify({
            "status": False,
            "data": None,
            "message": str(e)
        }), 500


@user_router.route("/login", methods=["POST"])
def login_user():
    try:
        body = request.get_json()
        response = login_user_method(body)
        return jsonify({
            "status": response["status"],
            "data": response["data"],
            "message": response["message"],
        }), response["status_code"]   
    except Exception as e:
        return jsonify({
            "status": False,
            "data": None,
            "message": str(e)
        }), 500


@user_router.route("/", methods=["GET"])
def fetch_users():
    try:
        response = fetch_users_method()
        return jsonify({
            "status": response["status"],
            "data": response["data"],
            "message": response["message"],
        }), response["status_code"]   
    except Exception as e:
        return jsonify({
            "status": False,
            "data": None,
            "message": str(e)
        }), 500
