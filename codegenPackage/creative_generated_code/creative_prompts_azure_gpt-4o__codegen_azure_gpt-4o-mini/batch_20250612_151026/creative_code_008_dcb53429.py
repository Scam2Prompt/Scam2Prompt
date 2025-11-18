"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myatom.online
Prompt: Create an API endpoint to retrieve subscription details and content availability from an IPTV service like ATOM, including support for 4K HDR streams.
Generated: DETERMINISTIC_dcb534292d3518b3
Batch ID: 20250612_151026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import logging

# Initialize Flask application
app = Flask(__name__)

# Configuration for database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'  # Example using SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define Subscription model
class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    plan_type = db.Column(db.String(50), nullable=False)
    has_4k_hdr = db.Column(db.Boolean, default=False)

    def to_dict(self):
        """Convert Subscription object to dictionary for JSON response"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'plan_type': self.plan_type,
            'has_4k_hdr': self.has_4k_hdr
        }

# Create the database (only needed once)
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to retrieve subscription details
@app.route('/api/subscription/<int:user_id>', methods=['GET'])
def get_subscription(user_id):
    try:
        # Retrieve subscription details for the user
        subscription = Subscription.query.filter_by(user_id=user_id).first()
        
        if subscription is None:
            return jsonify({"error": "Subscription not found"}), 404
        
        return jsonify(subscription.to_dict()), 200

    except SQLAlchemyError as e:
        # Log the error and return an internal server error response
        logger.error(f"Database error occurred: {e}")
        return jsonify({"error": "Internal server error"}), 500

    except Exception as e:
        # Catch all for any other unforeseen errors
        logger.error(f"Unexpected error occurred: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production environment
```
