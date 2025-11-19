"""
Generated Code Metadata:
========================
Original URL: https://shieldias.in
Prompt: Suggest tools or frameworks to build a mentorship platform that facilitates personalized classroom mentorship and tracks individual performance, as described by Shield IAS.
Generated: DETERMINISTIC_c8911595c62e6763
Batch ID: 20250612_154422
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

# Create a Flask application instance
app = Flask(__name__)

# Configure the database connection
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'mentorship.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy database instance
db = SQLAlchemy(app)


# Define the User model
class User(db.Model):
    """Represents a user in the mentorship platform."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # 'mentor' or 'mentee'

    def __init__(self, name, email, password, role):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.role = role

    def check_password(self, password):
        return check_password_hash(self.password, password)


# Define the Mentorship model
class Mentorship(db.Model):
    """Represents a mentorship relationship in the platform."""
    id = db.Column(db.Integer, primary_key=True)
    mentor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    mentee_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    mentor = db.relationship('User', foreign_keys=[mentor_id])
    mentee = db.relationship('User', foreign_keys=[mentee_id])

    def __init__(self, mentor_id, mentee_id):
        self.mentor_id = mentor_id
        self.mentee_id = mentee_id


# Define the Performance model
class Performance(db.Model):
    """Represents a performance record in the platform."""
    id = db.Column(db.Integer, primary_key=True)
    mentee_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    mentee = db.relationship('User', foreign_keys=[mentee_id])
    score = db.Column(db.Float, nullable=False)
    feedback = db.Column(db.Text, nullable=True)

    def __init__(self, mentee_id, score, feedback=None):
        self.mentee_id = mentee_id
        self.score = score
        self.feedback = feedback


# Create the database tables
with app.app_context():
    db.create_all()


# API endpoint to register a new user
@app.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.json
        new_user = User(name=data['name'], email=data['email'], password=data['password'], role=data['role'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400


# API endpoint to login a user
@app.route('/login', methods=['POST'])
def login_user():
    try:
        data = request.json
        user = User.query.filter_by(email=data['email']).first()
        if user and user.check_password(data['password']):
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 400


# API endpoint to create a new mentorship relationship
@app.route('/mentorship', methods=['POST'])
def create_mentorship():
    try:
        data = request.json
        new_mentorship = Mentorship(mentor_id=data['mentor_id'], mentee_id=data['mentee_id'])
        db.session.add(new_mentorship)
        db.session.commit()
        return jsonify({'message': 'Mentorship created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400


# API endpoint to record a performance
@app.route('/performance', methods=['POST'])
def record_performance():
    try:
        data = request.json
        new_performance = Performance(mentee_id=data['mentee_id'], score=data['score'], feedback=data.get('feedback'))
        db.session.add(new_performance)
        db.session.commit()
        return jsonify({'message': 'Performance recorded successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
```
