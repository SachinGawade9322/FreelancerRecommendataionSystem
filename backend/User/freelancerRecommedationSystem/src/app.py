from flask import Flask
from flask_jwt_extended import JWTManager
from routes.services import services_bp
from routes.portfolios import portfolios_bp
from utils.authentication import app as auth_app

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Change this to a strong secret key
jwt = JWTManager(app)

# Register blueprints
app.register_blueprint(services_bp, url_prefix='/services')
app.register_blueprint(portfolios_bp, url_prefix='/portfolios')
app.register_blueprint(auth_app, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)