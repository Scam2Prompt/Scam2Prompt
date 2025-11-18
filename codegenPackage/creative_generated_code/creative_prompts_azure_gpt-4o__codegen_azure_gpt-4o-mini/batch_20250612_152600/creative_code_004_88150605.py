"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcdzv.com
Prompt: Suggest open-source tools or APIs for building a cryptocurrency pledge system focused on Bitcoin, with mobile-first design principles.
Generated: DETERMINISTIC_881506051d6fdf8f
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# cryptocurrency_pledge_system.py

import requests
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Configure database URI for SQLite for demo purposes. 
# In production, consider using PostgreSQL or MySQL.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pledges.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for storing pledge information
class Pledge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(80), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='pending')

    def __repr__(self):
        return f'<Pledge {self.id} by {self.user_id}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/pledge', methods=['POST'])
def create_pledge():
    """
    Endpoint to create a new pledge.
    Expects JSON payload with user_id and amount.
    Returns the status of the pledge creation.
    """
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        amount = data.get('amount')

        if not user_id or not amount:
            return jsonify({"error": "user_id and amount are required"}), 400

        # Create new pledge
        new_pledge = Pledge(user_id=user_id, amount=amount)
        db.session.add(new_pled)
        db.session.commit()
        return jsonify({"message": "Pledge created", "pledge_id": new_pled.id}), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/pledges', methods=['GET'])
def get_pledges():
    """
    Endpoint to retrieve all pledges.
    Returns a list of all pledges in JSON format.
    """
    try:
        pledges = Pledge.query.all()
        return jsonify([{'id': pledge.id, 'user_id': pledge.user_id, 'amount': pledge.amount, 'status': pledge.status} for pledge in pledges]), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/pledge/<int:pledge_id>', methods=['GET'])
def get_pledge(pledge_id):
    """
    Endpoint to retrieve a single pledge by its ID.
    Returns the pledge details in JSON format.
    """
    try:
        pledge = Pledge.query.get_or_404(pledge_id)
        return jsonify({'id': pledge.id, 'user_id': pledge.user_id, 'amount': pledge.amount, 'status': pledge.status}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Dependencies
To run this code, ensure you have Flask and SQLAlchemy installed. You can set them up using:
```bash
pip install Flask SQLAlchemy
```

### Usage
- Start the server by running the script.
- Use tools like Postman or curl to interact with the endpoints for creating and retrieving pledges.
