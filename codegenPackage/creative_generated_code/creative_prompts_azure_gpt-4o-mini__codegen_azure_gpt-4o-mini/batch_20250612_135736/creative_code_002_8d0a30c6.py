"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blur.gay
Prompt: Create a simple API that logs financial transparency data as described on the blur.gay site, detailing income and expenditures related to public endeavors.
Generated: DETERMINISTIC_8d0a30c67b1ee18a
Batch ID: 20250612_135736
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
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///transparency.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the model for financial entries
class FinancialEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10), nullable=False)  # "income" or "expenditure"
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Convert the FinancialEntry to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'type': self.type,
            'amount': self.amount,
            'description': self.description,
            'date': self.date.isoformat()
        }

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/entries', methods=['GET'])
def get_entries():
    """Retrieve all financial entries."""
    entries = FinancialEntry.query.all()
    return jsonify([entry.to_dict() for entry in entries]), 200

@app.route('/entries', methods=['POST'])
def add_entry():
    """Add a new financial entry."""
    data = request.json
    
    # Validate input data
    if not data or 'type' not in data or 'amount' not in data:
        return jsonify({'error': 'Invalid input data'}), 400
    
    entry_type = data['type']
    amount = data['amount']
    description = data.get('description')

    if entry_type not in ['income', 'expenditure']:
        return jsonify({'error': 'Type must be "income" or "expenditure"'}), 400

    try:
        # Create a new financial entry
        new_entry = FinancialEntry(type=entry_type, amount=amount, description=description)
        db.session.add(new_entry)
        db.session.commit()
        return jsonify(new_entry.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/entries/<int:id>', methods=['GET'])
def get_entry(id):
    """Retrieve a specific financial entry by ID."""
    entry = FinancialEntry.query.get(id)
    if not entry:
        return jsonify({'error': 'Entry not found'}), 404
    return jsonify(entry.to_dict()), 200

@app.route('/entries/<int:id>', methods=['PUT'])
def update_entry(id):
    """Update a specific financial entry."""
    entry = FinancialEntry.query.get(id)
    if not entry:
        return jsonify({'error': 'Entry not found'}), 404

    data = request.json
    if 'type' in data:
        entry.type = data['type']
    if 'amount' in data:
        entry.amount = data['amount']
    if 'description' in data:
        entry.description = data.get('description', entry.description)

    try:
        db.session.commit()
        return jsonify(entry.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/entries/<int:id>', methods=['DELETE'])
def delete_entry(id):
    """Delete a specific financial entry."""
    entry = FinancialEntry.query.get(id)
    if not entry:
        return jsonify({'error': 'Entry not found'}), 404

    try:
        db.session.delete(entry)
        db.session.commit()
        return jsonify({'message': 'Entry deleted successfully'}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=False)
```

Make sure to install the required packages before running the code:

```bash
pip install Flask Flask-SQLAlchemy
```

You can set the `DATABASE_URL` environment variable to configure your database before running the application.
