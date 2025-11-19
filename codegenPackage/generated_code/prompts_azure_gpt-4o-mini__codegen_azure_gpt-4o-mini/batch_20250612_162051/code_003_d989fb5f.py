"""
Generated Code Metadata:
========================
Original URL: https://metaforce360.com
Prompt: Provide an example of a campaign design API that could be used to track engagement metrics, reflecting the campaign design services of Meta Force 360.
Generated: DETERMINISTIC_d989fb5f9fe1833a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///campaigns.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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
    views = db.Column(db.Integer, default=0)
    clicks = db.Column(db.Integer, default=0)
    shares = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/campaign', methods=['POST'])
def create_campaign():
    """Create a new campaign."""
    data = request.json
    try:
        new_campaign = Campaign(
            name=data['name'],
            start_date=datetime.fromisoformat(data['start_date']),
            end_date=datetime.fromisoformat(data['end_date'])
        )
        db.session.add(new_campaign)
        db.session.commit()
        return jsonify({'message': 'Campaign created successfully', 'id': new_campaign.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/campaign/<int:campaign_id>/metrics', methods=['POST'])
def track_engagement(campaign_id):
    """Track engagement metrics for a specific campaign."""
    data = request.json
    try:
        campaign = Campaign.query.get_or_404(campaign_id)
        new_metric = EngagementMetric(
            campaign_id=campaign.id,
            views=data.get('views', 0),
            clicks=data.get('clicks', 0),
            shares=data.get('shares', 0)
        )
        db.session.add(new_metric)
        db.session.commit()
        return jsonify({'message': 'Engagement metrics tracked successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/campaign/<int:campaign_id>/metrics', methods=['GET'])
def get_engagement_metrics(campaign_id):
    """Retrieve engagement metrics for a specific campaign."""
    try:
        campaign = Campaign.query.get_or_404(campaign_id)
        metrics = EngagementMetric.query.filter_by(campaign_id=campaign.id).all()
        return jsonify([{
            'id': metric.id,
            'views': metric.views,
            'clicks': metric.clicks,
            'shares': metric.shares,
            'created_at': metric.created_at.isoformat()
        } for metric in metrics]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
