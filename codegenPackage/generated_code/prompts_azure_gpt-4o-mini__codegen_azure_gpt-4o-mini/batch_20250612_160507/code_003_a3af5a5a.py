"""
Generated Code Metadata:
========================
Original URL: https://nicerfoundation.org.ng
Prompt: Develop a mobile app feature that allows users to track their volunteer hours, reflecting the NICER Foundation's mission of community involvement and support.
Generated: DETERMINISTIC_a3af5a5a6bdf88c0
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///volunteer_hours.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the VolunteerHour model
class VolunteerHour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    hours = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<VolunteerHour {self.user_id} - {self.hours} hours on {self.date}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Route to log volunteer hours
@app.route('/log_hours', methods=['POST'])
def log_hours():
    try:
        # Get data from the request
        data = request.get_json()
        user_id = data.get('user_id')
        hours = data.get('hours')

        # Validate input
        if not user_id or not isinstance(hours, (int, float)):
            return jsonify({'error': 'Invalid input'}), 400

        # Create a new VolunteerHour entry
        new_entry = VolunteerHour(user_id=user_id, hours=hours)
        db.session.add(new_entry)
        db.session.commit()

        return jsonify({'message': 'Volunteer hours logged successfully'}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

# Route to retrieve volunteer hours for a user
@app.route('/get_hours/<user_id>', methods=['GET'])
def get_hours(user_id):
    try:
        # Query the database for the user's volunteer hours
        hours_entries = VolunteerHour.query.filter_by(user_id=user_id).all()
        total_hours = sum(entry.hours for entry in hours_entries)

        return jsonify({
            'user_id': user_id,
            'total_hours': total_hours,
            'entries': [{'date': entry.date, 'hours': entry.hours} for entry in hours_entries]
        }), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    # Run the app in debug mode for development
    app.run(debug=os.getenv('FLASK_DEBUG', '0') == '1')
```
