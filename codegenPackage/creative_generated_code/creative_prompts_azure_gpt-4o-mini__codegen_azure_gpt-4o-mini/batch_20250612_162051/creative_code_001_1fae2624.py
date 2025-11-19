"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azagros.com
Prompt: Write a code snippet that integrates mobile and web functionalities for agricultural activity monitoring, similar to Azagros.
Generated: DETERMINISTIC_1fae262499c6ff23
Batch ID: 20250612_162051
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

# Initialize Flask application
app = Flask(__name__)

# Configure database for SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agriculture_monitoring.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Database Model for Agricultural Activities
class AgriculturalActivity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity_type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    location = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Activity {self.activity_type} at {self.location}>'

# Create the database
with app.app_context():
    db.create_all()

# API endpoint to create a new agricultural activity
@app.route('/activities', methods=['POST'])
def create_activity():
    try:
        data = request.get_json()
        new_activity = AgriculturalActivity(
            activity_type=data['activity_type'],
            description=data.get('description'),
            location=data['location']
        )
        db.session.add(new_activity)
        db.session.commit()
        return jsonify({'message': 'Activity created successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# API endpoint to get all agricultural activities
@app.route('/activities', methods=['GET'])
def get_activities():
    try:
        activities = AgriculturalActivity.query.all()
        result = [
            {
                'id': activity.id,
                'activity_type': activity.activity_type,
                'description': activity.description,
                'date': activity.date,
                'location': activity.location
            } for activity in activities
        ]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to get activity by ID
@app.route('/activities/<int:activity_id>', methods=['GET'])
def get_activity(activity_id):
    try:
        activity = AgriculturalActivity.query.get_or_404(activity_id)
        return jsonify({
            'id': activity.id,
            'activity_type': activity.activity_type,
            'description': activity.description,
            'date': activity.date,
            'location': activity.location
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 404

# API endpoint to update an agricultural activity
@app.route('/activities/<int:activity_id>', methods=['PUT'])
def update_activity(activity_id):
    try:
        activity = AgriculturalActivity.query.get_or_404(activity_id)
        data = request.get_json()
        activity.activity_type = data.get('activity_type', activity.activity_type)
        activity.description = data.get('description', activity.description)
        activity.location = data.get('location', activity.location)
        db.session.commit()
        return jsonify({'message': 'Activity updated successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# API endpoint to delete an agricultural activity
@app.route('/activities/<int:activity_id>', methods=['DELETE'])
def delete_activity(activity_id):
    try:
        activity = AgriculturalActivity.query.get_or_404(activity_id)
        db.session.delete(activity)
        db.session.commit()
        return jsonify({'message': 'Activity deleted successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=os.environ.get('FLASK_DEBUG', True), host='0.0.0.0', port=5000)
```
