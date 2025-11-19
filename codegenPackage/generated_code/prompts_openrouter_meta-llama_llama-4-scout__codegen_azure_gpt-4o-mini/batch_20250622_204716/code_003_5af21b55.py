"""
Generated Code Metadata:
========================
Original URL: https://passive-income.online
Prompt: Design an API for a platform that helps users create and manage multiple income streams through affiliate marketing, including endpoints for tracking commissions and managing campaigns.
Generated: DETERMINISTIC_5af21b550207e57d
Batch ID: 20250622_204716
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
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///income_streams.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    campaigns = db.relationship('Campaign', backref='owner', lazy=True)

# Model for Campaign
class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    commissions = db.relationship('Commission', backref='campaign', lazy=True)

# Model for Commission
class Commission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'), nullable=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'])
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'id': new_user.id, 'username': new_user.username}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Username already exists'}), 400

# Endpoint to create a new campaign
@app.route('/campaigns', methods=['POST'])
def create_campaign():
    data = request.get_json()
    new_campaign = Campaign(name=data['name'], user_id=data['user_id'])
    db.session.add(new_campaign)
    db.session.commit()
    return jsonify({'id': new_campaign.id, 'name': new_campaign.name}), 201

# Endpoint to track a commission
@app.route('/commissions', methods=['POST'])
def track_commission():
    data = request.get_json()
    new_commission = Commission(amount=data['amount'], campaign_id=data['campaign_id'])
    db.session.add(new_commission)
    db.session.commit()
    return jsonify({'id': new_commission.id, 'amount': new_commission.amount}), 201

# Endpoint to get all campaigns for a user
@app.route('/users/<int:user_id>/campaigns', methods=['GET'])
def get_user_campaigns(user_id):
    campaigns = Campaign.query.filter_by(user_id=user_id).all()
    return jsonify([{'id': campaign.id, 'name': campaign.name} for campaign in campaigns]), 200

# Endpoint to get all commissions for a campaign
@app.route('/campaigns/<int:campaign_id>/commissions', methods=['GET'])
def get_campaign_commissions(campaign_id):
    commissions = Commission.query.filter_by(campaign_id=campaign_id).all()
    return jsonify([{'id': commission.id, 'amount': commission.amount} for commission in commissions]), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
