from datetime import datetime, timedelta, timezone
import jwt
from dotenv import load_dotenv
import os

load_dotenv()

secret_key = os.getenv('SECRET_KEY')

def decode_token(auth_header):
    if auth_header and auth_header.startswith('Bearer '):
        token = auth_header.split(' ')[1]
    else:
        return False, "Authorization header missing or invalid"
    try:
        decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])
        return True, decoded_token
    except jwt.ExpiredSignatureError:
        return False, "Token has expired"
    except jwt.InvalidTokenError:
        return False, "Invalid token"


def encode_user(user):
    payload = {
        'sub': user["id"],
        'email': user["email"],
        'exp': datetime.now(timezone.utc) + timedelta(hours=12)
    }
    token = jwt.encode(payload, secret_key, algorithm='HS256')

    return token