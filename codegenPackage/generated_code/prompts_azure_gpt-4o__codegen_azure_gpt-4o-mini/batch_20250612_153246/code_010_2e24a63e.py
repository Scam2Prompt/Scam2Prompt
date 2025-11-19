"""
Generated Code Metadata:
========================
Original URL: https://www.rankraze.fr
Prompt: Create a mobile app prototype for managing digital marketing campaigns, inspired by Rankraze's mobile app development services.
Generated: DETERMINISTIC_2e24a63eacbb4046
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///campaigns.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Campaign model
class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    budget = db.Column(db.Float, nullable=False)
    start_date = db.Column(db.String(10), nullable=False)
    end_date = db.Column(db.String(10), nullable=False)

# Create the Campaign schema for serialization
class CampaignSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    budget = fields.Float(required=True)
    start_date = fields.Str(required=True)
    end_date = fields.Str(required=True)

# Initialize the schema
campaign_schema = CampaignSchema()
campaigns_schema = CampaignSchema(many=True)

# Error handling for invalid data
@app.errorhandler(ValidationError)
def handle_validation_error(err):
    return jsonify(err.messages), 400

# Route to create a new campaign
@app.route('/campaigns', methods=['POST'])
def create_campaign():
    try:
        # Validate and deserialize input data
        campaign_data = campaign_schema.load(request.json)
        new_campaign = Campaign(**campaign_data)
        db.session.add(new_campaign)
        db.session.commit()
        return campaign_schema.jsonify(new_campaign), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all campaigns
@app.route('/campaigns', methods=['GET'])
def get_campaigns():
    campaigns = Campaign.query.all()
    return campaigns_schema.jsonify(campaigns), 200

# Route to get a specific campaign by ID
@app.route('/campaigns/<int:id>', methods=['GET'])
def get_campaign(id):
    campaign = Campaign.query.get_or_404(id)
    return campaign_schema.jsonify(campaign), 200

# Route to update a campaign
@app.route('/campaigns/<int:id>', methods=['PUT'])
def update_campaign(id):
    campaign = Campaign.query.get_or_404(id)
    try:
        # Validate and deserialize input data
        campaign_data = campaign_schema.load(request.json)
        for key, value in campaign_data.items():
            setattr(campaign, key, value)
        db.session.commit()
        return campaign_schema.jsonify(campaign), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a campaign
@app.route('/campaigns/<int:id>', methods=['DELETE'])
def delete_campaign(id):
    campaign = Campaign.query.get_or_404(id)
    db.session.delete(campaign)
    db.session.commit()
    return jsonify({"message": "Campaign deleted successfully."}), 204

# Main entry point to run the application
if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    # Run the Flask application
    app.run(debug=True)
```
