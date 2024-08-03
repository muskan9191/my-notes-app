from flask import Flask
from routes.notes import notes_router
from routes.users import user_router
from routes.health_check import test_router


def create_app():
    app = Flask(__name__)
    app.register_blueprint(notes_router, url_prefix='/api/v1/notes')
    app.register_blueprint(user_router, url_prefix='/api/v1/users')
    app.register_blueprint(test_router)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)

