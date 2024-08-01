from flask import Flask
from dotenv import load_dotenv
from services.middleware import register_error_handlers, register_middleware
from routes.items import items_bp
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Import and register the items blueprint

app.register_blueprint(items_bp)
register_error_handlers(app)
register_middleware(app)

if __name__ == '__main__':
    port = int(os.getenv("FLASK_PORT", 5000))  # Default to 5000 if FLASK_PORT is not set
    app.run(debug=True, port=port)
