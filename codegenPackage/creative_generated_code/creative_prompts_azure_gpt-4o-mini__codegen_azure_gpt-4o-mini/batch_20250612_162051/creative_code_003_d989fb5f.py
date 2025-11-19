"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metaforce360.com
Prompt: Provide an example of a campaign design API that could be used to track engagement metrics, reflecting the campaign design services of Meta Force 360.
Generated: DETERMINISTIC_d989fb5f9fe1833a
Batch ID: 20250612_162051
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (SQLite for this example)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///campaigns.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Campaign model
class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    engagement_metrics = db.relationship('EngagementMetric', backref='campaign', lazy=True)

# Define the EngagementMetric model
class EngagementMetric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'), nullable=False)
    metric_type = db.Column(db.String(50), nullable=False)
    value = db.Column(db.Float, nullable=False)
    recorded_at = db.Column(db.DateTime, default=datetime.utcnow)

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new campaign
@app.route('/campaigns', methods=['POST'])
def create_campaign():
    # Parse request data
    data = request.get_json()
    try:
        new_campaign = Campaign(
            name=data['name'],
            start_date=datetime.fromisoformat(data['start_date']),
            end_date=datetime.fromisoformat(data['end_date'])
        )
        db.session.add(new_campaign)
        db.session.commit()
        return jsonify({"message": "Campaign created successfully", "id": new_campaign.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Route to track engagement metrics
@app.route('/campaigns/<int:campaign_id>/metrics', methods=['POST'])
def track_engagement(campaign_id):
    # Parse request data
    data = request.get_json()
    try:
        # Check if the campaign exists
        campaign = Campaign.query.get_or_404(campaign_id)

        new_metric = EngagementMetric(
            campaign_id=campaign.id,
            metric_type=data['metric_type'],
            value=data['value']
        )
        db.session.add(new_metric)
        db.session.commit()
        return jsonify({"message": "Engagement metric recorded successfully", "id": new_metric.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Route to retrieve engagement metrics for a specific campaign
@app.route('/campaigns/<int:campaign_id>/metrics', methods=['GET'])
def get_engagement_metrics(campaign_id):
    try:
        # Check if the campaign exists
        campaign = Campaign.query.get_or_404(campaign_id)
        metrics = EngagementMetric.query.filter_by(campaign_id=campaign.id).all()
        return jsonify([{"id": m.id, "metric_type": m.metric_type, "value": m.value, "recorded_at": m.recorded_at} for m in metrics]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
