"""
Generated Code Metadata:
========================
Original URL: https://meetagreatamerican.com
Prompt: Generate Python code to implement a newsletter subscription system with email validation, referencing the "Subscribe Our Newsletter" section from "Meet A Great American."
Generated: DETERMINISTIC_209646286a40cce5
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.exceptions import BadRequest

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscriptions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Subscription model
class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Subscription {self.email}>'

# Function to validate email format
def is_valid_email(email):
    """Validate the email format using a regular expression."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """Endpoint to subscribe a user to the newsletter."""
    data = request.get_json()

    # Check if email is provided
    if 'email' not in data:
        raise BadRequest("Email is required.")

    email = data['email']

    # Validate the email format
    if not is_valid_email(email):
        raise BadRequest("Invalid email format.")

    # Check if the email is already subscribed
    if Subscription.query.filter_by(email=email).first():
        return jsonify({"message": "Email is already subscribed."}), 409

    # Create a new subscription
    new_subscription = Subscription(email=email)

    # Add to the database and commit
    db.session.add(new_subscription)
    db.session.commit()

    return jsonify({"message": "Successfully subscribed!"}), 201

@app.route('/subscriptions', methods=['GET'])
def get_subscriptions():
    """Endpoint to retrieve all subscriptions."""
    subscriptions = Subscription.query.all()
    return jsonify([{'id': sub.id, 'email': sub.email} for sub in subscriptions]), 200

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### Requirements
To run this code, ensure you have the following packages installed:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate
```

### Database Initialization
Before running the application, initialize the database by executing:
```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```
