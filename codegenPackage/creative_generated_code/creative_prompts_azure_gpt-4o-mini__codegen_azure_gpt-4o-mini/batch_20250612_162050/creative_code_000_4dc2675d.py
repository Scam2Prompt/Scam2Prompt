"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getupenergy.co.uk
Prompt: Generate a code snippet for a web application that integrates Tibi's massage therapy services, focusing on user appointment scheduling and stress management features.
Generated: DETERMINISTIC_4dc2675d55701d78
Batch ID: 20250612_162050
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
import os

# Initialize Flask application
app = Flask(__name__)

# Configure database URI (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    message = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f'<Appointment {self.id} - {self.user_name}>'

# Create the database and tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route for scheduling an appointment
@app.route('/schedule_appointment', methods=['POST'])
def schedule_appointment():
    try:
        # Get data from request
        data = request.get_json()
        user_name = data.get('user_name')
        email = data.get('email')
        date_time_str = data.get('date_time')
        
        # Validate input
        if not user_name or not email or not date_time_str:
            return jsonify({'error': 'Missing required fields'}), 400

        # Convert date_time_str to datetime object
        date_time = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
        
        # Create new appointment
        new_appointment = Appointment(user_name=user_name, email=email, date_time=date_time)
        db.session.add(new_appointment)
        db.session.commit()

        return jsonify({'message': 'Appointment scheduled successfully', 'appointment_id': new_appointment.id}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for stress management tips
@app.route('/stress_management', methods=['GET'])
def stress_management():
    tips = [
        "Practice deep breathing exercises.",
        "Engage in regular physical activity.",
        "Maintain a balanced diet.",
        "Ensure adequate sleep.",
        "Consider mindfulness or meditation practices."
    ]
    return jsonify({'tips': tips}), 200

# Run the application
if __name__ == '__main__':
    # Set the environment variable for production
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
```
