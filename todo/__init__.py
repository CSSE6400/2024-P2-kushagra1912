from flask import Flask


def create_app():
    app = Flask(__name__)

    app.json.sort_keys = False  # Don't modify JSON order
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"

    # Load Models
    from todo.models import db
    from todo.models.todo import Todo

    db.init_app(app)

    # Create the database tables
    with app.app_context():
        db.create_all()
        db.session.commit()

    # Register Blueprints
    from .views.routes import api

    app.register_blueprint(api)

    return app
