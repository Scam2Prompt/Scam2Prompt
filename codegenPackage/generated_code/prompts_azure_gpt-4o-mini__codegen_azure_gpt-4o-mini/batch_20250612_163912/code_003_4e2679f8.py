"""
Generated Code Metadata:
========================
Original URL: https://firstbaptistnj.org
Prompt: Create an API that allows users to subscribe to a church newsletter, inspired by the subscription feature on the First Baptist Church website.
Generated: DETERMINISTIC_4e2679f8cc5e3e01
Batch ID: 20250612_163912
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

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscribers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Subscriber model
class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, email):
        self.email = email

# Subscriber schema for serialization
class SubscriberSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Subscriber

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to subscribe to the newsletter
@app.route('/subscribe', methods=['POST'])
def subscribe():
    try:
        # Get the email from the request
        email = request.json.get('email')

        # Validate the email
        if not email:
            raise BadRequest("Email is required.")

        # Check if the email is already subscribed
        existing_subscriber = Subscriber.query.filter_by(email=email).first()
        if existing_subscriber:
            return jsonify({"message": "Email already subscribed."}), 400

        # Create a new subscriber
        new_subscriber = Subscriber(email)
        db.session.add(new_subscriber)
        db.session.commit()

        # Return a success response
        return jsonify({"message": "Successfully subscribed!"}), 201

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while subscribing."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
