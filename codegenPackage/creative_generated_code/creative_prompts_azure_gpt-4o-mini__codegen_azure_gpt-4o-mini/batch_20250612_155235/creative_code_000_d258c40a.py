"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abve.xyz
Prompt: Generate a sample code snippet for a subscription feature that collects user emails for updates, similar to the one mentioned on abve.xyz.
Generated: DETERMINISTIC_d258c40ae33a8904
Batch ID: 20250612_155235
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
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///subscribers.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Subscriber model
class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Define the schema for validation
class SubscriberSchema(Schema):
    email = fields.Email(required=True)

# Initialize the database
with app.app_context():
    db.create_all()

# Route to handle email subscriptions
@app.route('/subscribe', methods=['POST'])
def subscribe():
    # Parse and validate incoming JSON data
    schema = SubscriberSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Check for existing subscriber
    existing_subscriber = Subscriber.query.filter_by(email=data['email']).first()
    if existing_subscriber:
        return jsonify({"message": "Email already subscribed."}), 409

    # Create a new subscriber
    new_subscriber = Subscriber(email=data['email'])
    
    # Add the subscriber to the database
    try:
        db.session.add(new_subscriber)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "An error occurred while subscribing.", "error": str(e)}), 500

    return jsonify({"message": "Successfully subscribed!"}), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
