from flask import Blueprint, request, jsonify
from cruds.notes import add_notes_method, delete_notes_method, get_all_notes_method, get_notes_method, update_notes_method
from utils.helper import decode_token

notes_router = Blueprint('notes_router', __name__)


@notes_router.route("/", methods=["POST"])
def add_note():
    try:
        status, decode_response = decode_token(request.headers.get("Authorization"))
        if not status:
            return jsonify({
                "status": False,
                "data": None,
                "message": decode_response
            }), 401
        body = request.get_json()
        response = add_notes_method(body, decode_response)
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


@notes_router.route("/<id>",  methods=["GET"])
def get_notes(id):
    try:
        status, decode_response = decode_token(request.headers.get("Authorization"))
        if not status:
            return jsonify({
                "status": False,
                "data": None,
                "message": decode_response
            }), 401
        response = get_notes_method(id, decode_response)
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
    


@notes_router.route("/",  methods=["GET"])
def get_all_notes():
    try:
        status, decode_response = decode_token(request.headers.get("Authorization"))
        if not status:
            return jsonify({
                "status": False,
                "data": None,
                "message": decode_response
            }), 401
        response = get_all_notes_method(decode_response)
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



@notes_router.route("/<id>",  methods=["PATCH"])
def update_notes(id):
    try:
        status, decode_response = decode_token(request.headers.get("Authorization"))
        if not status:
            return jsonify({
                "status": False,
                "data": None,
                "message": decode_response
            }), 401
        body = request.get_json()
        response = update_notes_method(id, body, decode_response)
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
    

@notes_router.route("/<id>",  methods=["DELETE"])
def delete_notes(id):
    try:
        status, decode_response = decode_token(request.headers.get("Authorization"))
        if not status:
            return jsonify({
                "status": False,
                "data": None,
                "message": decode_response
            }), 401
        response = delete_notes_method(id, decode_response)
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
