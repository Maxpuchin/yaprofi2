from flask import Flask
from src import bp, db

import json

def create_app(config):
    app = Flask(__name__)
    app.config.update(config)

    db.init_app(app)
    app.register_blueprint(bp)

    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    config_path = "./config.json"
    config = json.load(open(config_path, "r", encoding="utf-8"))

    app = create_app(config)
    app.run("0.0.0.0", 8080)