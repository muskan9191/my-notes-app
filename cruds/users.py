from datetime import datetime
import json
from bson.json_util import dumps
from uuid import uuid4
from bcrypt import checkpw, gensalt, hashpw

from utils.helper import encode_user
from database.mongodb import db


def register_user_method(body):
    try:
        name = body.get('name')
        email = body.get('email')
        password = body.get('password')
        user_exist = db.users.find_one({"email": body.get("email")})
        if user_exist:
            return {
                "status": False,
                "data": None,
                "message":"User already exists",
                "status_code": 200
            }
        
        hashed_password = hashpw(password.encode('utf-8'), gensalt(12))

        # Insert user into the database
        user_data = {
            "id": str(uuid4()),
            'name': name,
            'email': email,
            'password': hashed_password,
            "createdDate": datetime.now(),
        }
        db.users.insert_one(user_data)
        token = encode_user(user_data)
        return {
            "status": True,
            "data": {
                "token": token
            },
            "message":"User registered successfully",
            "status_code": 201
        }
    except Exception as e:
        return {
            "status": False,
            "data": None,
            "message": str(e),
            "status_code": 500
        }


def login_user_method(body):
    try:
        email = body.get('email')
        password = body.get('password')
        user_exist = db.users.find_one({"email": email})
        if not user_exist:
            return {
                "status": False,
                "data": None,
                "message":"User does not exist",
                "status_code": 404
            }
        if checkpw(password.encode('utf-8'), user_exist['password']):
            token = encode_user(user_exist)
            return {
                "status": True,
                "data": {
                    "token": token
                },
                "message":"User logged in successfully",
                "status_code": 200
            }
        else:
            return {
                "status": False,
                "data": None,
                'message': 'Invalid email or password',
                "status_code": 401
            }
    except Exception as e:
        return {
            "status": False,
            "data": None,
            "message": str(e),
            "status_code": 500
        }


def fetch_users_method():
    try:
        users_list = list(db.users.find({}, {'_id': 0, "password": 0}))
        return {
            "status": True,
            "data": json.loads(dumps(users_list)),
            "message":"Users fetched successfully",
            "status_code": 200
        }
    except Exception as e:
        return {
            "status": False,
            "data": None,
            "message": str(e),
            "status_code": 500
        }