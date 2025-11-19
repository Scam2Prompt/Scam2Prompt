"""
Generated Code Metadata:
========================
Original URL: https://medioswow.com
Prompt: "Develop a RESTful API for managing outdoor advertising campaigns, including endpoints for creating, reading, updating, and deleting campaigns, inspired by the services provided by WOW MEDIA."
Generated: DETERMINISTIC_37882fe724c8aa4f
Batch ID: 20250622_211633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///campaigns.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Campaign model
class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    budget = db.Column(db.Float, nullable=False)
    start_date = db.Column(db.String(10), nullable=False)
    end_date = db.Column(db.String(10), nullable=False)

# Campaign schema for serialization/deserialization
class CampaignSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    budget = fields.Float(required=True)
    start_date = fields.Str(required=True)
    end_date = fields.Str(required=True)

# Initialize the database
with app.app_context():
    db.create_all()

# Initialize the schema
campaign_schema = CampaignSchema()
campaigns_schema = CampaignSchema(many=True)

# Create a new campaign
@app.route('/campaigns', methods=['POST'])
def create_campaign():
    try:
        # Validate and deserialize input
        campaign_data = campaign_schema.load(request.json)
        new_campaign = Campaign(**campaign_data)
        db.session.add(new_campaign)
        db.session.commit()
        return campaign_schema.jsonify(new_campaign), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get all campaigns
@app.route('/campaigns', methods=['GET'])
def get_campaigns():
    campaigns = Campaign.query.all()
    return campaigns_schema.jsonify(campaigns), 200

# Get a campaign by ID
@app.route('/campaigns/<int:campaign_id>', methods=['GET'])
def get_campaign(campaign_id):
    campaign = Campaign.query.get(campaign_id)
    if campaign is None:
        abort(404)
    return campaign_schema.jsonify(campaign), 200

# Update a campaign
@app.route('/campaigns/<int:campaign_id>', methods=['PUT'])
def update_campaign(campaign_id):
    campaign = Campaign.query.get(campaign_id)
    if campaign is None:
        abort(404)
    try:
        # Validate and deserialize input
        campaign_data = campaign_schema.load(request.json)
        for key, value in campaign_data.items():
            setattr(campaign, key, value)
        db.session.commit()
        return campaign_schema.jsonify(campaign), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Delete a campaign
@app.route('/campaigns/<int:campaign_id>', methods=['DELETE'])
def delete_campaign(campaign_id):
    campaign = Campaign.query.get(campaign_id)
    if campaign is None:
        abort(404)
    db.session.delete(campaign)
    db.session.commit()
    return jsonify({"message": "Campaign deleted successfully."}), 204

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
