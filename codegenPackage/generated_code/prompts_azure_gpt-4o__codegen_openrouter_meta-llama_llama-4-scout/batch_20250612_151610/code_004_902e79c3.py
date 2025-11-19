"""
Generated Code Metadata:
========================
Original URL: https://cbupdates.com
Prompt: Suggest APIs or tools to develop a personalized coaching platform for franchisees, focusing on one-on-one coaching and growth strategies as outlined by Franchise Teacher.
Generated: DETERMINISTIC_902e79c3e489980f
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize Flask app
app = Flask(__name__)

# Configure database connection
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'coaching.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define models
class Franchisee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Coach(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class CoachingSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    franchisee_id = db.Column(db.Integer, db.ForeignKey('franchisee.id'), nullable=False)
    coach_id = db.Column(db.Integer, db.ForeignKey('coach.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    notes = db.Column(db.Text, nullable=False)

    def __init__(self, franchisee_id, coach_id, date, notes):
        self.franchisee_id = franchisee_id
        self.coach_id = coach_id
        self.date = date
        self.notes = notes

# Create database tables
with app.app_context():
    db.create_all()

# API Endpoints
@app.route('/franchisee/register', methods=['POST'])
def register_franchisee():
    try:
        data = request.json
        franchisee = Franchisee(data['name'], data['email'], data['password'])
        db.session.add(franchisee)
        db.session.commit()
        return jsonify({'message': 'Franchisee registered successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/coach/register', methods=['POST'])
def register_coach():
    try:
        data = request.json
        coach = Coach(data['name'], data['email'], data['password'])
        db.session.add(coach)
        db.session.commit()
        return jsonify({'message': 'Coach registered successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/franchisee/login', methods=['POST'])
def login_franchisee():
    try:
        data = request.json
        franchisee = Franchisee.query.filter_by(email=data['email']).first()
        if franchisee and franchisee.check_password(data['password']):
            return jsonify({'message': 'Franchisee logged in successfully'}), 200
        else:
            return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/coach/login', methods=['POST'])
def login_coach():
    try:
        data = request.json
        coach = Coach.query.filter_by(email=data['email']).first()
        if coach and coach.check_password(data['password']):
            return jsonify({'message': 'Coach logged in successfully'}), 200
        else:
            return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/coaching-session', methods=['POST'])
def create_coaching_session():
    try:
        data = request.json
        coaching_session = CoachingSession(data['franchisee_id'], data['coach_id'], data['date'], data['notes'])
        db.session.add(coaching_session)
        db.session.commit()
        return jsonify({'message': 'Coaching session created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/coaching-sessions', methods=['GET'])
def get_coaching_sessions():
    try:
        coaching_sessions = CoachingSession.query.all()
        return jsonify([{'id': cs.id, 'franchisee_id': cs.franchisee_id, 'coach_id': cs.coach_id, 'date': cs.date, 'notes': cs.notes} for cs in coaching_sessions]), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
