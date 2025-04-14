from flask import Flask
from config import Config
from models import db
from routes import bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Register the blueprint with a URL prefix
app.register_blueprint(bp, url_prefix='/api')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=8080, debug=True)
