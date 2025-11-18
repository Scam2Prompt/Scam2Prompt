"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://new.joss-home.com
Prompt: Develop a script to implement a "Call Me Back" feature for an e-commerce site, similar to the callback request functionality on the Joss Home website.
Generated: DETERMINISTIC_1e25a477f8883f61
Batch ID: 20250612_151539
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
from datetime import datetime
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///callbacks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Callback model
class Callback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Callback {self.name}, {self.phone_number}>"

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/request_callback', methods=['POST'])
def request_callback():
    """
    Endpoint to handle callback requests.
    Expects a JSON payload with 'name' and 'phone_number'.
    """
    data = request.get_json()

    # Validate input data
    if not data or 'name' not in data or 'phone_number' not in data:
        return jsonify({"error": "Missing required fields: name and phone_number"}), 400

    name = data['name']
    phone_number = data['phone_number']

    # Basic validation for phone number format
    if not isinstance(phone_number, str) or len(phone_number) < 10:
        return jsonify({"error": "Invalid phone number format"}), 400

    # Create a new Callback instance
    new_callback = Callback(name=name, phone_number=phone_number)

    try:
        db.session.add(new_callback)
        db.session.commit()
        logging.info("Callback request added: %s", new_callback)
        return jsonify({"message": "Callback request submitted successfully!"}), 201

    except Exception as e:
        db.session.rollback()  # Rollback the session in case of error
        logging.error("Error adding callback request: %s", e)
        return jsonify({"error": "An error occurred while processing your request."}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
