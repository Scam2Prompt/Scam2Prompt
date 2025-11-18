"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eyemagazine.gr
Prompt: Create a REST API that allows users to subscribe to newsletters like the one offered by Eye Magazine, ensuring compliance with privacy regulations.
Generated: DETERMINISTIC_b50d6722c3d06fae
Batch ID: 20250612_153246
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
import re
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscribers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy ORM
db = SQLAlchemy(app)

# Define the Subscriber model
class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Subscriber {self.email}>'

# Create the database
with app.app_context():
    db.create_all()

# Validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

# Endpoint to subscribe a user to the newsletter
@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.get_json()

    # Validate incoming request data
    if not data or 'email' not in data:
        raise BadRequest("Request must contain an 'email' field.")

    email = data['email']

    if not is_valid_email(email):
        raise BadRequest("Invalid email format.")

    # Check if the email is already subscribed
    existing_subscriber = Subscriber.query.filter_by(email=email).first()
    if existing_subscriber:
        return jsonify({"message": "You are already subscribed."}), 200

    # Subscribe the user
    new_subscriber = Subscriber(email=email)
    db.session.add(new_subscriber)

    try:
        db.session.commit()
        return jsonify({"message": "Successfully subscribed."}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Failed to subscribe.", "error": str(e)}), 500

# Error handler for BadRequest
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": str(error)}), 400

# Start the Flask application
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
```
