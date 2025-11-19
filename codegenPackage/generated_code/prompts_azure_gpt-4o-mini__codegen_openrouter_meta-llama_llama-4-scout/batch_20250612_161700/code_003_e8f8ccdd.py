"""
Generated Code Metadata:
========================
Original URL: https://ammaparivaar.org
Prompt: What are some best practices for creating a fundraising campaign API for an NGO, taking cues from the initiatives of Amma Parivaar Orphanage?
Generated: DETERMINISTIC_e8f8ccddb0574b94
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fundraising_campaign_api.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fundraising_campaign.db'
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class User(db.Model):
    """Represents a user in the database."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Check if the provided password matches the stored hash."""
        return check_password_hash(self.password, password)

class Donation(db.Model):
    """Represents a donation in the database."""
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('donations', lazy=True))

    def __init__(self, amount, user_id):
        self.amount = amount
        self.user_id = user_id

class Campaign(db.Model):
    """Represents a fundraising campaign in the database."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    goal = db.Column(db.Float, nullable=False)
    donations = db.relationship('Donation', backref='campaign', lazy=True)

    def __init__(self, title, description, goal):
        self.title = title
        self.description = description
        self.goal = goal

@app.route('/register', methods=['POST'])
def register_user():
    """Register a new user."""
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Missing request data'}), 400
        user = User(data['name'], data['email'], data['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        logger.error(f"Error registering user: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/login', methods=['POST'])
def login_user():
    """Login an existing user."""
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Missing request data'}), 400
        user = User.query.filter_by(email=data['email']).first()
        if not user or not user.check_password(data['password']):
            return jsonify({'error': 'Invalid credentials'}), 401
        return jsonify({'message': 'User logged in successfully'}), 200
    except Exception as e:
        logger.error(f"Error logging in user: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/campaigns', methods=['GET', 'POST'])
def manage_campaigns():
    """Get all campaigns or create a new campaign."""
    try:
        if request.method == 'GET':
            campaigns = Campaign.query.all()
            return jsonify([{'id': c.id, 'title': c.title, 'description': c.description, 'goal': c.goal} for c in campaigns]), 200
        elif request.method == 'POST':
            data = request.json
            if not data:
                return jsonify({'error': 'Missing request data'}), 400
            campaign = Campaign(data['title'], data['description'], data['goal'])
            db.session.add(campaign)
            db.session.commit()
            return jsonify({'message': 'Campaign created successfully'}), 201
    except Exception as e:
        logger.error(f"Error managing campaigns: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/donate', methods=['POST'])
def make_donation():
    """Make a donation to a campaign."""
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Missing request data'}), 400
        campaign_id = data['campaign_id']
        amount = data['amount']
        user_id = data['user_id']
        campaign = Campaign.query.get(campaign_id)
        if not campaign:
            return jsonify({'error': 'Campaign not found'}), 404
        donation = Donation(amount, user_id)
        campaign.donations.append(donation)
        db.session.commit()
        return jsonify({'message': 'Donation made successfully'}), 201
    except Exception as e:
        logger.error(f"Error making donation: {e}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
