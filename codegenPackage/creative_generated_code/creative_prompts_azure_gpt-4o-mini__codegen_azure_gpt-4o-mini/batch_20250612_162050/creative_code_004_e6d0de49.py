"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: What are the key components to consider when developing a web application for DBT therapy that includes both individual and group sessions?
Generated: DETERMINISTIC_e6d0de49aed95194
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web development
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (example using SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbt_therapy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tool
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the session model for both individual and group sessions
class Session(db.Model):
    __tablename__ = 'sessions'
    
    id = db.Column(db.Integer, primary_key=True)
    session_type = db.Column(db.String, nullable=False)  # 'individual' or 'group'
    date_time = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # duration in minutes
    therapist_id = db.Column(db.Integer, db.ForeignKey('therapists.id'), nullable=False)
    
    # Relationship to therapists
    therapist = db.relationship('Therapist', backref='sessions')

# Define the therapist model
class Therapist(db.Model):
    __tablename__ = 'therapists'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    specialty = db.Column(db.String)

# API route to create a new session
@app.route('/sessions', methods=['POST'])
def create_session():
    try:
        data = request.json
        new_session = Session(
            session_type=data['session_type'],
            date_time=data['date_time'],
            duration=data['duration'],
            therapist_id=data['therapist_id']
        )
        
        db.session.add(new_session)
        db.session.commit()
        return jsonify({'message': 'Session created successfully!'}), 201
    
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Therapist ID is invalid or session data is incomplete.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API route to get all sessions
@app.route('/sessions', methods=['GET'])
def get_sessions():
    try:
        sessions = Session.query.all()
        return jsonify([{
            'id': session.id,
            'session_type': session.session_type,
            'date_time': session.date_time.strftime("%Y-%m-%d %H:%M:%S"),
            'duration': session.duration,
            'therapist_id': session.therapist_id
        } for session in sessions]), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API route to get all therapists
@app.route('/therapists', methods=['GET'])
def get_therapists():
    try:
        therapists = Therapist.query.all()
        return jsonify([{
            'id': therapist.id,
            'name': therapist.name,
            'specialty': therapist.specialty
        } for therapist in therapists]), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application only if this script is executed
if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to install Flask and Flask-SQLAlchemy using pip:

```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate
```

This code sets up a simple web application using Flask, creates models for DBT therapy sessions, provides routes for creating and retrieving sessions and therapists, and includes error handling and comments for clarity.
