"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iconfoundation.online
Prompt: Generate a code snippet for a web application that tracks the number of neurological cases registered, inspired by the ICON Foundation's data collection from December 2022 to January 2024.
Generated: DETERMINISTIC_e36b8f7f0d6c92d5
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///neurological_cases.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging for the application
logging.basicConfig(level=logging.INFO)

# Define the database model for Neurological Cases
class NeurologicalCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    case_date = db.Column(db.Date, nullable=False)
    case_count = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<NeurologicalCase {self.case_date}: {self.case_count}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to add a new neurological case
@app.route('/add_case', methods=['POST'])
def add_case():
    try:
        # Retrieve JSON data from the request
        data = request.get_json()
        case_date = datetime.strptime(data['case_date'], '%Y-%m-%d').date()
        case_count = data['case_count']

        # Validate input data
        if case_count < 0:
            return jsonify({'error': 'Case count must be a non-negative integer.'}), 400

        # Create a new NeurologicalCase instance
        new_case = NeurologicalCase(case_date=case_date, case_count=case_count)

        # Add the instance to the session and commit
        db.session.add(new_case)
        db.session.commit()

        logging.info(f'Added case: {new_case}')
        return jsonify({'message': 'Case added successfully.'}), 201

    except Exception as e:
        logging.error(f'Error adding case: {e}')
        return jsonify({'error': 'Failed to add case.'}), 500

# Endpoint to retrieve the total number of registered cases
@app.route('/total_cases', methods=['GET'])
def total_cases():
    try:
        # Query the total number of cases
        total = db.session.query(db.func.sum(NeurologicalCase.case_count)).scalar() or 0
        return jsonify({'total_cases': total}), 200

    except Exception as e:
        logging.error(f'Error retrieving total cases: {e}')
        return jsonify({'error': 'Failed to retrieve total cases.'}), 500

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
