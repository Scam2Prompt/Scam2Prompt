"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: Generate code for a web application that tracks attendance for DBT therapy sessions, ensuring weekly participation in individual and group therapy, as required for effective treatment according to the Mente Sana Psicología website.
Generated: DETERMINISTIC_941fd91599f2d6a1
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Attendance model
class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100), nullable=False)
    session_type = db.Column(db.String(50), nullable=False)  # 'individual' or 'group'
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Attendance {self.patient_name} {self.session_type} on {self.date}>'

# Create the database
with app.app_context():
    db.create_all()

# Route to add attendance record
@app.route('/attendance', methods=['POST'])
def add_attendance():
    """
    API endpoint to add an attendance record.
    Expected JSON payload:
    {
        "patient_name": "string",
        "session_type": "string"  # 'individual' or 'group'
    }
    """
    try:
        data = request.get_json()
        patient_name = data.get('patient_name')
        session_type = data.get('session_type')

        if not patient_name or not session_type:
            return jsonify({"error": "Patient name and session type are required."}), 400

        if session_type not in ['individual', 'group']:
            return jsonify({"error": "Session type must be 'individual' or 'group'."}), 400

        new_attendance = Attendance(patient_name=patient_name, session_type=session_type)
        db.session.add(new_attendance)
        db.session.commit()

        return jsonify({"message": "Attendance record added."}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get attendance records
@app.route('/attendance', methods=['GET'])
def get_attendance():
    """
    API endpoint to retrieve all attendance records.
    Returns a JSON list of all attendance records.
    """
    try:
        records = Attendance.query.all()
        result = [
            {
                "id": record.id,
                "patient_name": record.patient_name,
                "session_type": record.session_type,
                "date": record.date.strftime("%Y-%m-%d %H:%M:%S")
            } for record in records
        ]
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application if this file is executed
if __name__ == '__main__':
    # Using environment variable for the port
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

Make sure you have Flask and SQLAlchemy installed in your environment to run the above code. You can install them using pip:

```bash
pip install Flask Flask-SQLAlchemy
```
