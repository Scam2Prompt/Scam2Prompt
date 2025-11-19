"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://firstbaptistnj.org
Prompt: Create an API that allows users to subscribe to a church newsletter, inspired by the subscription feature on the First Baptist Church website.
Generated: DETERMINISTIC_4e2679f8cc5e3e01
Batch ID: 20250612_163912
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
from werkzeug.exceptions import BadRequest
from functools import wraps
import os

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newsletter_subscribers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Subscriber model
class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Subscriber {self.email}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Error handler for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return jsonify({"error": str(e)}), 400

# Decorator to validate the email format
def validate_email(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        email = request.json.get('email')
        if not email or '@' not in email:
            raise BadRequest("Invalid email address.")
        return f(*args, **kwargs)
    return decorated_function

# Endpoint to subscribe to the newsletter
@app.route('/subscribe', methods=['POST'])
@validate_email
def subscribe():
    """
    Subscribe a user to the church newsletter by adding their email
    to the database.
    """
    email = request.json['email']
    
    # Check if the email already exists
    existing_subscriber = Subscriber.query.filter_by(email=email).first()
    if existing_subscriber:
        return jsonify({"message": "This email is already subscribed."}), 409
    
    # Create a new subscriber
    new_subscriber = Subscriber(email=email)
    db.session.add(new_subscriber)
    db.session.commit()
    
    return jsonify({"message": "Successfully subscribed to the newsletter!"}), 201

# Run the application
if __name__ == '__main__':
    # Ensure the app runs on the correct host and port
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```
