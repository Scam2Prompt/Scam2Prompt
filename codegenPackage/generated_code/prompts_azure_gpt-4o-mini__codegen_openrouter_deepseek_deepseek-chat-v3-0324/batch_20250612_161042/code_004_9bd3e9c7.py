"""
Generated Code Metadata:
========================
Original URL: https://mandosecurity.com
Prompt: Create a sample code for a web application that provides 24/7 monitoring and access control features, reflecting the services offered by Mando Security.
Generated: DETERMINISTIC_9bd3e9c723fa3d1f
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import logging
import os

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///security.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')

# Initialize database
db = SQLAlchemy(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # admin, operator, viewer
    last_login = db.Column(db.DateTime)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class AccessLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    action = db.Column(db.String(50), nullable=False)  # login, logout, access_granted, access_denied
    location = db.Column(db.String(100))
    details = db.Column(db.Text)

class SecurityCamera(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default='active')  # active, inactive, maintenance
    last_checked = db.Column(db.DateTime)
    feed_url = db.Column(db.String(200))

# Helper functions
def log_access(user_id, action, location=None, details=None):
    try:
        log = AccessLog(
            user_id=user_id,
            action=action,
            location=location,
            details=details
        )
        db.session.add(log)
        db.session.commit()
    except Exception as e:
        logger.error(f"Failed to log access: {str(e)}")
        db.session.rollback()

# Authentication decorator
def role_required(role):
    def decorator(f):
        def wrapped(*args, **kwargs):
            auth_header = request.headers.get('Authorization')
            if not auth_header:
                return jsonify({'error': 'Authorization header missing'}), 401
                
            try:
                token = auth_header.split()[1]
                user = User.query.filter_by(username=token).first()
                if not user or user.role != role:
                    return jsonify({'error': 'Unauthorized'}), 403
                
                return f(*args, **kwargs)
            except Exception as e:
                logger.error(f"Authentication error: {str(e)}")
                return jsonify({'error': 'Invalid token'}), 401
        return wrapped
    return decorator

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({'error': 'Username and password required'}), 400
            
        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            return jsonify({'error': 'Invalid credentials'}), 401
            
        user.last_login = datetime.utcnow()
        db.session.commit()
        
        log_access(user.id, 'login')
        
        return jsonify({
            'message': 'Login successful',
            'username': user.username,
            'role': user.role
        })
    except Exception as e:
        logger.error(f"Login error: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/cameras', methods=['GET'])
@role_required('operator')
def get_cameras():
    try:
        cameras = SecurityCamera.query.all()
        return jsonify([{
            'id': cam.id,
            'name': cam.name,
            'location': cam.location,
            'status': cam.status,
            'feed_url': cam.feed_url
        } for cam in cameras])
    except Exception as e:
        logger.error(f"Failed to fetch cameras: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/cameras/<int:camera_id>', methods=['GET'])
@role_required('operator')
def get_camera(camera_id):
    try:
        camera = SecurityCamera.query.get(camera_id)
        if not camera:
            return jsonify({'error': 'Camera not found'}), 404
            
        return jsonify({
            'id': camera.id,
            'name': camera.name,
            'location': camera.location,
            'status': camera.status,
            'feed_url': camera.feed_url
        })
    except Exception as e:
        logger.error(f"Failed to fetch camera: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/access/logs', methods=['GET'])
@role_required('admin')
def get_access_logs():
    try:
        logs = AccessLog.query.order_by(AccessLog.timestamp.desc()).limit(100).all()
        return jsonify([{
            'id': log.id,
            'user_id': log.user_id,
            'timestamp': log.timestamp.isoformat(),
            'action': log.action,
            'location': log.location,
            'details': log.details
        } for log in logs])
    except Exception as e:
        logger.error(f"Failed to fetch access logs: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"Server error: {str(error)}")
    return jsonify({'error': 'Internal server error'}), 500

# Initialize database tables
@app.before_first_request
def initialize_database():
    db.create_all()
    # Create admin user if not exists
    if not User.query.filter_by(username='admin').first():
        admin = User(username='admin', role='admin')
        admin.set_password('securepassword')
        db.session.add(admin)
        db.session.commit()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
```
