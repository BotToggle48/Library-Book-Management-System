"""Library Book Management System - Flask Application

Main application entry point for the Library Management System.
Features:
- Book catalog management
- Book issuance and returns tracking
- Overdue and fine calculations
- User authentication with roles
- Reports and notifications
"""

from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import timedelta

# Initialize Flask App
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'library-management-secret-key')

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL',
    'mysql+pymysql://root:password@localhost/library_management'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# JWT Configuration
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'jwt-secret-key')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)

# Initialize Extensions
db = SQLAlchemy(app)
jwt = JWTManager(app)
CORS(app)

# Error Handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Resource not found', 'error': str(error)}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'message': 'Internal server error', 'error': str(error)}), 500

@app.errorhandler(401)
def unauthorized(error):
    return jsonify({'message': 'Unauthorized access', 'error': str(error)}), 401

@app.errorhandler(403)
def forbidden(error):
    return jsonify({'message': 'Forbidden access', 'error': str(error)}), 403

# Health Check Endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'message': 'Library Management System is running',
        'version': '1.0.0'
    }), 200

# Import Routes after app initialization
try:
    from routes import auth_routes, book_routes, issuance_routes, reports_routes
    app.register_blueprint(auth_routes.auth_bp)
    app.register_blueprint(book_routes.book_bp)
    app.register_blueprint(issuance_routes.issuance_bp)
    app.register_blueprint(reports_routes.reports_bp)
except ImportError as e:
    print(f"Warning: Could not import all routes: {e}")

if __name__ == '__main__':
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()
        print("Database tables created successfully")
    
    # Run the application
    app.run(
        debug=os.getenv('FLASK_DEBUG', 'False') == 'True',
        host=os.getenv('FLASK_HOST', '0.0.0.0'),
        port=int(os.getenv('FLASK_PORT', 5000))
    )
