"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://samaalnaser.co
Prompt: What are the best practices for developing a remote medical consultation application like the Tadawy Application from Sama Al-Naser Group, and can you provide a sample API structure?
Generated: DETERMINISTIC_9bc863adfd2b79d6
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consultation_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Model for Consultation
class Consultation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    doctor_name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default='pending')

    user = db.relationship('User', backref='consultations')


# Endpoint to create a new user
@app.route('/api/users', methods=['POST'])
def create_user():
    """Create a new user in the system"""
    data = request.json
    if not data or not 'name' in data or not 'email' in data:
        raise BadRequest("Name and email are required")

    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"id": new_user.id, "name": new_user.name, "email": new_user.email}), 201

# Endpoint to create a new consultation
@app.route('/api/consultations', methods=['POST'])
def create_consultation():
    """Schedule a new consultation"""
    data = request.json
    if not data or not 'user_id' in data or not 'doctor_name' in data:
        raise BadRequest("User ID and doctor name are required")

    new_consultation = Consultation(user_id=data['user_id'], doctor_name=data['doctor_name'])
    db.session.add(new_consultation)
    db.session.commit()
    
    return jsonify({"id": new_consultation.id, "status": new_consultation.status}), 201

# Endpoint to get consultations for a user
@app.route('/api/users/<int:user_id>/consultations', methods=['GET'])
def get_user_consultations(user_id):
    """Retrieve all consultations for a specific user"""
    consultations = Consultation.query.filter_by(user_id=user_id).all()
    if not consultations:
        raise NotFound("No consultations found for this user")

    return jsonify([{"id": c.id, "doctor_name": c.doctor_name, "timestamp": c.timestamp, "status": c.status} for c in consultations]), 200

# Error handling for NotFound errors
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": str(error)}), 404

# Error handling for BadRequest errors
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": str(error)}), 400

# Main method to run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Set debug to False in production
```

**Sample API Structure:**
- **POST /api/users**: Create a new user
- **POST /api/consultations**: Schedule a new consultation
- **GET /api/users/<user_id>/consultations**: Retrieve consultations for a specific user

**Note**: Don't forget to add appropriate security measures such as authentication and authorization when deploying this application in a production environment.
