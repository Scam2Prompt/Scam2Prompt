"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thedaybrightener.com
Prompt: How can I set up a backend system to manage sweepstakes entries and ensure compliance with eligibility requirements like those on The Day Brightener?
Generated: DETERMINISTIC_26773f545d838981
Batch ID: 20250612_155150
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
import re

# Initialize Flask application and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sweepstakes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for sweepstakes entries
class SweepstakesEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)
    entry_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Entry {self.name}, {self.email}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Helper function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

# Endpoint to submit a sweepstakes entry
@app.route('/enter', methods=['POST'])
def enter_sweepstakes():
    data = request.json

    # Input validation
    name = data.get('name')
    email = data.get('email')
    age = data.get('age')

    if not name or not email or not age:
        return jsonify({"error": "Name, email, and age are required."}), 400
    if not is_valid_email(email):
        return jsonify({"error": "Invalid email format."}), 400
    if age < 18:
        return jsonify({"error": "You must be at least 18 years old to enter."}), 400

    try:
        # Create a new sweepstakes entry
        new_entry = SweepstakesEntry(name=name, email=email, age=age)
        db.session.add(new_entry)
        db.session.commit()
        return jsonify({"message": "Entry submitted successfully!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all entries (for administrative purposes)
@app.route('/entries', methods=['GET'])
def get_entries():
    try:
        entries = SweepstakesEntry.query.all()
        return jsonify([{'name': entry.name, 'email': entry.email, 'age': entry.age, 'entry_date': entry.entry_date} for entry in entries]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
