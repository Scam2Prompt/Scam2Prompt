"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thatcounselingplace.com
Prompt: How can I implement a telehealth session feature for a counseling service similar to That Counseling Place?
Generated: DETERMINISTIC_a1838d5b141cb7e5
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# telehealth_service.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
import logging

# Initialize Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///telehealth.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Database model for Telehealth Sessions
class TelehealthSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100), nullable=False)
    counselor_name = db.Column(db.String(100), nullable=False)
    session_time = db.Column(db.DateTime, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/schedule', methods=['POST'])
def schedule_session():
    """Schedule a new telehealth session."""
    try:
        data = request.json
        patient_name = data.get('patient_name')
        counselor_name = data.get('counselor_name')
        session_time = datetime.fromisoformat(data.get('session_time'))
        duration_minutes = data.get('duration_minutes')

        # Validate input
        if not patient_name or not counselor_name or not session_time or not duration_minutes:
            return jsonify({"error": "Missing required fields"}), 400

        # Create a new session
        new_session = TelehealthSession(
            patient_name=patient_name,
            counselor_name=counselor_name,
            session_time=session_time,
            duration_minutes=duration_minutes
        )

        db.session.add(new_session)
        db.session.commit()

        return jsonify({"message": "Telehealth session scheduled successfully", "session_id": new_session.id}), 201

    except Exception as e:
        logging.error(f"Error scheduling session: {str(e)}")
        return jsonify({"error": "Failed to schedule session"}), 500

@app.route('/sessions', methods=['GET'])
def list_sessions():
    """Retrieve all scheduled telehealth sessions."""
    try:
        sessions = TelehealthSession.query.all()
        session_list = [
            {
                "id": session.id,
                "patient_name": session.patient_name,
                "counselor_name": session.counselor_name,
                "session_time": session.session_time.isoformat(),
                "duration_minutes": session.duration_minutes
            } for session in sessions
        ]
        return jsonify(session_list), 200

    except Exception as e:
        logging.error(f"Error fetching sessions: {str(e)}")
        return jsonify({"error": "Failed to retrieve sessions"}), 500

if __name__ == '__main__':
    # Run the application in debug mode
    app.run(debug=True)
```

### Instructions to Run the Code:
1. Ensure you have Python installed.
2. Install the required packages using pip:
   ```bash
   pip install Flask Flask-SQLAlchemy Flask-CORS
   ```
3. Save the code in a file named `telehealth_service.py`.
4. Run the application:
   ```bash
   python telehealth_service.py
   ```
5. Use an API client (like Postman) to send POST requests to `/schedule` to schedule sessions and GET requests to `/sessions` to list all sessions.
