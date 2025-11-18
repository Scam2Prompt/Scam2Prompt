"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbiotic-services.com
Prompt: Suggest a framework for creating a subscription-based technology guidance service, similar to Symbiotic Services' tiered plans like "Navigate IT" and "TechFrontier."
Generated: DETERMINISTIC_9fc7147337f2a9d1
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime, timedelta
import os

# Initialize the app
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///subscriptions.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and serializer
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Subscription Model
class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    plan_type = db.Column(db.String(50), nullable=False)  # e.g., "Navigate IT", "TechFrontier"
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    end_date = db.Column(db.DateTime, nullable=False)
    
    def __init__(self, user_id, plan_type, duration_months):
        self.user_id = user_id
        self.plan_type = plan_type
        self.end_date = self.start_date + timedelta(days=30 * duration_months)  # Assuming 1 month = 30 days

# Subscription Schema
class SubscriptionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Subscription

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a subscription
@app.route('/subscribe', methods=['POST'])
def subscribe():
    try:
        # Get data from request
        user_id = request.json.get('user_id')
        plan_type = request.json.get('plan_type')
        duration_months = request.json.get('duration_months', 1)  # Default to 1 month
        
        if not user_id or not plan_type:
            return jsonify({"error": "user_id and plan_type are required"}), 400
        
        # Create and save subscription
        new_subscription = Subscription(user_id=user_id, plan_type=plan_type, duration_months=duration_months)
        db.session.add(new_subscription)
        db.session.commit()
        
        return SubscriptionSchema().jsonify(new_subscription), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Route to get all subscriptions
@app.route('/subscriptions', methods=['GET'])
def get_subscriptions():
    try:
        subscriptions = Subscription.query.all()
        return SubscriptionSchema(many=True).jsonify(subscriptions), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to cancel a subscription
@app.route('/cancel/<int:subscription_id>', methods=['DELETE'])
def cancel_subscription(subscription_id):
    try:
        subscription = Subscription.query.get(subscription_id)
        if not subscription:
            return jsonify({"error": "Subscription not found"}), 404
        
        db.session.delete(subscription)
        db.session.commit()
        
        return jsonify({"message": "Subscription cancelled successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'False') == 'True')
```

**Note**: Please make sure to set the `DATABASE_URI` environment variable as required for your database connection.
