"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meetagreatamerican.com
Prompt: Generate Python code to implement a newsletter subscription system with email validation, referencing the "Subscribe Our Newsletter" section from "Meet A Great American."
Generated: DETERMINISTIC_209646286a40cce5
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)
# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newsletter.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Database model for newsletter subscriptions
class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Subscription {self.email}>'

# Create the database and table if it doesn't exist
with app.app_context():
    db.create_all()

# Email validation function
def is_valid_email(email):
    """Validate the email format using a regex pattern."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """Endpoint to handle newsletter subscription requests."""
    data = request.get_json()
    
    # Validate input data
    if not data or 'email' not in data:
        return jsonify({"error": "Email is required."}), 400

    email = data['email']
    
    # Check if the email is valid
    if not is_valid_email(email):
        return jsonify({"error": "Invalid email format."}), 400

    # Create a new subscription
    new_subscription = Subscription(email=email)
    
    try:
        db.session.add(new_subscription)
        db.session.commit()
        return jsonify({"message": "Successfully subscribed!"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Email already subscribed."}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
