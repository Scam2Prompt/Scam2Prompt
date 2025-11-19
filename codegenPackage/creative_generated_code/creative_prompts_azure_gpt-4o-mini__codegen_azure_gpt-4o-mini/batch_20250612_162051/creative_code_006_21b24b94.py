"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webservicesindia.info
Prompt: Develop a mobile app that incorporates digital marketing strategies mentioned by WebServicesIndia, focusing on user experience and engagement.
Generated: DETERMINISTIC_21b24b948eb72890
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import the necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketing_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for storing user engagement data
class UserEngagement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), nullable=False)
    engagement_type = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<UserEngagement {self.user_id} - {self.engagement_type}>'

# Initialize the database
with app.app_context():
    db.create_all()

# Endpoint to log user engagement
@app.route('/log_engagement', methods=['POST'])
def log_engagement():
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        engagement_type = data.get('engagement_type')

        # Validate input data
        if not user_id or not engagement_type:
            return jsonify({'error': 'user_id and engagement_type are required'}), 400

        # Create a new UserEngagement instance
        new_engagement = UserEngagement(user_id=user_id, engagement_type=engagement_type, timestamp=datetime.utcnow())
        db.session.add(new_engagement)
        db.session.commit()

        return jsonify({'message': 'Engagement logged successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to retrieve engagement data for a user
@app.route('/user_engagement/<user_id>', methods=['GET'])
def get_user_engagement(user_id):
    try:
        # Query the database for the user's engagement data
        engagements = UserEngagement.query.filter_by(user_id=user_id).all()
        if not engagements:
            return jsonify({'message': 'No engagement data found for this user'}), 404

        # Format the data for response
        engagement_data = [{
            'engagement_type': engagement.engagement_type,
            'timestamp': engagement.timestamp
        } for engagement in engagements]

        return jsonify({'engagements': engagement_data}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=False)  # Run the app in production mode
```
