from flask import Flask
from models import db
from controllers.v1.user_controller import user_blueprint_v1
from controllers.v2.user_controller import user_blueprint_v2
from config import Config
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Register versioned blueprints for routing
app.register_blueprint(user_blueprint_v1, url_prefix='/api/v1')
app.register_blueprint(user_blueprint_v2, url_prefix='/api/v2')

# Flask-Migrate will handle creating tables via migrations
# You don't need `before_first_request` if you're using migrations.

if __name__ == "__main__":
    app.run(debug=True)
