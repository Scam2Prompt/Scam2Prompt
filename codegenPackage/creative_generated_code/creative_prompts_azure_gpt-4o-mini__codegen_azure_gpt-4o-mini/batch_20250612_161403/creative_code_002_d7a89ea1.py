"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paradigmgroup.co.ug
Prompt: Create a sample API for a brand activation service that tracks customer engagement and product literacy, based on the experiential marketing strategies of Paradigm Group.
Generated: DETERMINISTIC_d7a89ea1b33f3c8d
Batch ID: 20250612_161403
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

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///engagement.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define a model for customer engagement
class Engagement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.String(50), nullable=False)
    product_id = db.Column(db.String(50), nullable=False)
    engagement_type = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'product_id': self.product_id,
            'engagement_type': self.engagement_type,
            'timestamp': self.timestamp.isoformat()
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to track customer engagement
@app.route('/api/engagement', methods=['POST'])
def track_engagement():
    try:
        data = request.get_json()

        # Validate input data
        if not data or not all(k in data for k in ('customer_id', 'product_id', 'engagement_type')):
            return jsonify({'error': 'Invalid input'}), 400

        # Create a new Engagement record
        engagement = Engagement(
            customer_id=data['customer_id'],
            product_id=data['product_id'],
            engagement_type=data['engagement_type']
        )

        # Add to the session and commit to the database
        db.session.add(engagement)
        db.session.commit()

        logging.info(f"Engagement recorded: {engagement.to_dict()}")
        return jsonify(engagement.to_dict()), 201
    
    except Exception as e:
        logging.error(f"Error tracking engagement: {e}")
        return jsonify({'error': 'Internal server error'}), 500

# Endpoint to retrieve all engagements
@app.route('/api/engagements', methods=['GET'])
def get_engagements():
    try:
        engagements = Engagement.query.all()
        return jsonify([engagement.to_dict() for engagement in engagements]), 200

    except Exception as e:
        logging.error(f"Error retrieving engagements: {e}")
        return jsonify({'error': 'Internal server error'}), 500

# Endpoint to retrieve engagement by customer_id
@app.route('/api/engagements/<string:customer_id>', methods=['GET'])
def get_engagement_by_customer(customer_id):
    try:
        engagements = Engagement.query.filter_by(customer_id=customer_id).all()
        if not engagements:
            return jsonify({'error': 'No engagements found for this customer'}), 404
        return jsonify([engagement.to_dict() for engagement in engagements]), 200

    except Exception as e:
        logging.error(f"Error retrieving engagements for customer {customer_id}: {e}")
        return jsonify({'error': 'Internal server error'}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
