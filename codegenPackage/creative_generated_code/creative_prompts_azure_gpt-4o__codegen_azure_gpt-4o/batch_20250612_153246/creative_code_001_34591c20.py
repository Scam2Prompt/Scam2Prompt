"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://youngistaan.org
Prompt: Recommend libraries or APIs to implement a web-based volunteer registration system for an NGO like Youngistaan Foundation, focusing on features such as user authentication and event management.
Generated: DETERMINISTIC_34591c20ce451fd4
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# This code provides a web-based volunteer registration system using Flask, SQLAlchemy, and Flask-JWT-Extended for authentication.
# Ensure you install the required libraries before running:
# pip install flask flask_sqlalchemy flask_jwt_extended werkzeug

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///volunteers.db'  # SQLite database for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_secret_key_here'  # Replace with a secure secret key

db = SQLAlchemy(app)
jwt = JWTManager(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date = db.Column(db.String(50), nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

# Routes
@app.route('/register', methods=['POST'])
def register_user():
    """Endpoint to register a new user."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists'}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login_user():
    """Endpoint to authenticate a user and provide a JWT token."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({'error': 'Invalid username or password'}), 401

    access_token = create_access_token(identity=username)
    return jsonify({'access_token': access_token}), 200

@app.route('/events', methods=['POST'])
@jwt_required()
def create_event():
    """Endpoint to create a new volunteer event."""
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    date = data.get('date')

    if not name or not date:
        return jsonify({'error': 'Event name and date are required'}), 400

    new_event = Event(name=name, description=description, date=date)
    db.session.add(new_event)
    db.session.commit()

    return jsonify({'message': 'Event created successfully'}), 201

@app.route('/events', methods=['GET'])
def list_events():
    """Endpoint to list all volunteer events."""
    events = Event.query.all()
    event_list = [{'id': event.id, 'name': event.name, 'description': event.description, 'date': event.date} for event in events]
    return jsonify(event_list), 200

# Error handling
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

This code creates a simple web-based volunteer registration system with features like user authentication and event management. It uses Flask for the web framework, SQLAlchemy for database operations, and Flask-JWT-Extended for JWT-based authentication.
