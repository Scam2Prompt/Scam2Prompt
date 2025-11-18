"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foodandwine.one
Prompt: Design a REST API for managing promotional campaigns on an online gambling site like Hi88, including endpoints for creating, updating, and tracking user participation.
Generated: DETERMINISTIC_051e00bbcd843d4e
Batch ID: 20250612_151345
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
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///campaigns.db'
db = SQLAlchemy(app)

# Define the Campaign model
class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    participants = db.relationship('Participant', backref='campaign', lazy=True)

# Define the Participant model
class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), nullable=False)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'), nullable=False)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new promotional campaign
@app.route('/api/campaigns', methods=['POST'])
def create_campaign():
    data = request.json
    if not all(k in data for k in ("name", "start_date", "end_date")):
        raise BadRequest("Missing required fields: name, start_date, end_date")
    
    new_campaign = Campaign(
        name=data["name"],
        start_date=datetime.fromisoformat(data["start_date"]),
        end_date=datetime.fromisoformat(data["end_date"])
    )
    db.session.add(new_campaign)
    db.session.commit()
    
    return jsonify({"id": new_campaign.id}), 201

# Endpoint to update an existing campaign
@app.route('/api/campaigns/<int:campaign_id>', methods=['PUT'])
def update_campaign(campaign_id):
    campaign = Campaign.query.get(campaign_id)
    if not campaign:
        raise NotFound("Campaign not found")

    data = request.json
    if "name" in data:
        campaign.name = data["name"]
    if "start_date" in data:
        campaign.start_date = datetime.fromisoformat(data["start_date"])
    if "end_date" in data:
        campaign.end_date = datetime.fromisoformat(data["end_date"])

    db.session.commit()
    return jsonify({"message": "Campaign updated successfully"}), 200

# Endpoint to track user participation in a campaign
@app.route('/api/campaigns/<int:campaign_id>/participants', methods=['POST'])
def participate_in_campaign(campaign_id):
    campaign = Campaign.query.get(campaign_id)
    if not campaign:
        raise NotFound("Campaign not found")

    user_id = request.json.get('user_id')
    if not user_id:
        raise BadRequest("Missing required field: user_id")

    new_participant = Participant(user_id=user_id, campaign_id=campaign_id)
    db.session.add(new_participant)
    db.session.commit()
    
    return jsonify({"message": "Participation recorded successfully"}), 201

# Endpoint to get all participants for a specific campaign
@app.route('/api/campaigns/<int:campaign_id>/participants', methods=['GET'])
def get_participants(campaign_id):
    campaign = Campaign.query.get(campaign_id)
    if not campaign:
        raise NotFound("Campaign not found")

    participants = Participant.query.filter_by(campaign_id=campaign_id).all()
    return jsonify({"participants": [p.user_id for p in participants]}), 200

# Error handling
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": str(error)}), 404

@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": str(error)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
