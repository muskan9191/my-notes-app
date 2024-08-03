from flask import Blueprint

test_router = Blueprint('test', __name__)

@test_router.route('/')
def health_check():
    return "Success!"
