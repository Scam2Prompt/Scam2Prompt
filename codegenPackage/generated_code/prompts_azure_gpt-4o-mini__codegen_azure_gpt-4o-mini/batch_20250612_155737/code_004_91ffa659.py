"""
Generated Code Metadata:
========================
Original URL: https://wholygood.com
Prompt: Create an API call that allows users to subscribe for updates, similar to the functionality suggested by wholygood.com.
Generated: DETERMINISTIC_91ffa659afa34cf8
Batch ID: 20250612_155737
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
from flask_marshmallow import Marshmallow
from werkzeug.exceptions import BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Subscription model
class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, email):
        self.email = email

# Subscription schema for serialization
class SubscriptionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Subscription

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Subscribe a user to updates by email.
    Expects a JSON payload with an 'email' field.
    Returns the created subscription or an error message.
    """
    try:
        # Get JSON data from the request
        data = request.get_json()
        
        # Validate input
        if not data or 'email' not in data:
            raise BadRequest("Email is required.")

        email = data['email']

        # Check if the email is already subscribed
        existing_subscription = Subscription.query.filter_by(email=email).first()
        if existing_subscription:
            return jsonify({"message": "Email is already subscribed."}), 400

        # Create a new subscription
        new_subscription = Subscription(email)
        db.session.add(new_subscription)
        db.session.commit()

        # Serialize the new subscription
        subscription_schema = SubscriptionSchema()
        return jsonify(subscription_schema.dump(new_subscription)), 201

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Log the error (in production, use a logging framework)
        print(f"Error: {str(e)}")
        return jsonify({"error": "An error occurred while processing your request."}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
