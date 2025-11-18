"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rickster.pages.dev
Prompt: Write code to integrate Relai's Bitcoin news subscription feature into a web application, allowing users to opt-in and manage their subscription preferences.
Generated: DETERMINISTIC_69435bd3758cc12d
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'
db = SQLAlchemy(app)

# Database model for User Subscription
class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    opt_in = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Subscription {self.email}>'

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Endpoint to allow users to opt-in for Bitcoin news subscription.

    Request JSON Body:
    {
        "email": "user@example.com",
        "opt_in": true
    }

    Returns:
    JSON response with success or error message.
    """
    data = request.get_json()

    # Validate request data
    if not data or 'email' not in data or 'opt_in' not in data:
        raise BadRequest("Invalid request data. Email and opt_in fields are required.")

    email = data['email']
    opt_in = data['opt_in']

    # Check if the user is already subscribed
    subscription = Subscription.query.filter_by(email=email).first()
    
    if subscription:
        # Update the existing subscription preference
        subscription.opt_in = opt_in
    else:
        # Create a new subscription
        subscription = Subscription(email=email, opt_in=opt_in)
        db.session.add(subscription)

    # Commit changes to the database
    db.session.commit()

    return jsonify({"message": "Subscription updated successfully."}), 200

@app.route('/subscriptions', methods=['GET'])
def get_subscriptions():
    """
    Endpoint to retrieve all subscriptions.

    Returns:
    JSON list of all subscriptions with their preferences.
    """
    subscriptions = Subscription.query.all()
    subscription_list = [{'email': sub.email, 'opt_in': sub.opt_in} for sub in subscriptions]

    return jsonify(subscription_list), 200

@app.errorhandler(BadRequest)
def handle_bad_request(e):
    """
    Custom error handler for BadRequest.
    """
    return jsonify({"error": str(e.description)}), 400

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=False)
```

### Notes:
- Ensure that you have Flask and Flask-SQLAlchemy installed in your Python environment.
- This code uses SQLite for simplicity; you can change the database URI to connect to a different database as needed.
- The application includes basic error handling and data validation for robust operation.
