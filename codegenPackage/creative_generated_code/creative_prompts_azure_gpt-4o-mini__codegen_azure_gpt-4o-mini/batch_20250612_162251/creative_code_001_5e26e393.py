"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.icyd.org
Prompt: Write a code snippet for an API that tracks youth participation in community service activities as suggested by ICYD.
Generated: DETERMINISTIC_5e26e39367e0ec53
Batch ID: 20250612_162251
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
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure database URI and initialize SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///community_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Database model for tracking community service activities
class CommunityServiceActivity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    participant_name = db.Column(db.String(100), nullable=False)
    activity_name = db.Column(db.String(100), nullable=False)
    date_of_activity = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'participant_name': self.participant_name,
            'activity_name': self.activity_name,
            'date_of_activity': self.date_of_activity.isoformat()
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to track new community service activity
@app.route('/api/activities', methods=['POST'])
def track_activity():
    try:
        data = request.get_json()
        if not data or 'participant_name' not in data or 'activity_name' not in data:
            return jsonify({'error': 'Bad Request: Missing required fields'}), 400
        
        # Create a new activity instance
        new_activity = CommunityServiceActivity(
            participant_name=data['participant_name'],
            activity_name=data['activity_name']
        )
        
        # Add and commit the new activity to the database
        db.session.add(new_activity)
        db.session.commit()

        return jsonify(new_activity.to_dict()), 201

    except Exception as e:
        logging.error(f"Error tracking activity: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

# API endpoint to retrieve all activities
@app.route('/api/activities', methods=['GET'])
def get_activities():
    try:
        activities = CommunityServiceActivity.query.all()
        return jsonify([activity.to_dict() for activity in activities]), 200
    except Exception as e:
        logging.error(f"Error retrieving activities: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
