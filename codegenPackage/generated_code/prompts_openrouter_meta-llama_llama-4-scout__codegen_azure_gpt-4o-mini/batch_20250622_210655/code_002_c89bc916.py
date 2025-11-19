"""
Generated Code Metadata:
========================
Original URL: https://azagros.com
Prompt: Generate code for a web-based platform that allows for real-time monitoring of agricultural activities, including scheduling, registration, and reporting, like Azagros.
Generated: DETERMINISTIC_c89bc91684221ed9
Batch ID: 20250622_210655
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
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agriculture.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the database model for agricultural activities
class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    scheduled_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), default='Pending')

    def __repr__(self):
        return f'<Activity {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to register a new agricultural activity
@app.route('/activities', methods=['POST'])
def register_activity():
    try:
        data = request.get_json()
        new_activity = Activity(
            name=data['name'],
            scheduled_time=datetime.fromisoformat(data['scheduled_time'])
        )
        db.session.add(new_activity)
        db.session.commit()
        return jsonify({'message': 'Activity registered successfully!'}), 201
    except Exception as e:
        logging.error(f"Error registering activity: {e}")
        return jsonify({'error': 'Failed to register activity'}), 400

# Route to get all activities
@app.route('/activities', methods=['GET'])
def get_activities():
    try:
        activities = Activity.query.all()
        return jsonify([{'id': a.id, 'name': a.name, 'scheduled_time': a.scheduled_time.isoformat(), 'status': a.status} for a in activities]), 200
    except Exception as e:
        logging.error(f"Error fetching activities: {e}")
        return jsonify({'error': 'Failed to fetch activities'}), 500

# Route to update the status of an activity
@app.route('/activities/<int:activity_id>', methods=['PUT'])
def update_activity(activity_id):
    try:
        data = request.get_json()
        activity = Activity.query.get_or_404(activity_id)
        activity.status = data['status']
        db.session.commit()
        return jsonify({'message': 'Activity updated successfully!'}), 200
    except Exception as e:
        logging.error(f"Error updating activity: {e}")
        return jsonify({'error': 'Failed to update activity'}), 400

# Route to delete an activity
@app.route('/activities/<int:activity_id>', methods=['DELETE'])
def delete_activity(activity_id):
    try:
        activity = Activity.query.get_or_404(activity_id)
        db.session.delete(activity)
        db.session.commit()
        return jsonify({'message': 'Activity deleted successfully!'}), 200
    except Exception as e:
        logging.error(f"Error deleting activity: {e}")
        return jsonify({'error': 'Failed to delete activity'}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements
- Install Flask and Flask-SQLAlchemy:
```bash
pip install Flask Flask-SQLAlchemy
```

### Note
- This code uses SQLite for simplicity. For production, consider using a more robust database system.
- Ensure to handle sensitive data and implement authentication for a production environment.
