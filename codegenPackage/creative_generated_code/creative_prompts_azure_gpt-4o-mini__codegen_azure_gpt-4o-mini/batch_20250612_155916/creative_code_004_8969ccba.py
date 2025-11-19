"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harda-ke.org
Prompt: Illustrate how to implement a microfinance tracking system for HARDA's small business support programs using a specific library or framework.
Generated: DETERMINISTIC_8969ccba0ac228d8
Batch ID: 20250612_155916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Microfinance Tracking System for HARDA's Small Business Support Programs

# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///microfinance.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Microfinance model
class Microfinance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    interest_rate = db.Column(db.Float, nullable=False)
    duration_months = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Microfinance {self.business_name}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Route to create a new microfinance entry
@app.route('/microfinance', methods=['POST'])
def create_microfinance():
    try:
        data = request.get_json()
        
        # Validate input data
        if not all(k in data for k in ("business_name", "amount", "interest_rate", "duration_months")):
            return jsonify({"error": "Missing required fields"}), 400
        
        # Create a new microfinance entry
        new_entry = Microfinance(
            business_name=data['business_name'],
            amount=data['amount'],
            interest_rate=data['interest_rate'],
            duration_months=data['duration_months']
        )
        
        db.session.add(new_entry)
        db.session.commit()
        
        return jsonify({"message": "Microfinance entry created", "id": new_entry.id}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Entry already exists"}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all microfinance entries
@app.route('/microfinance', methods=['GET'])
def get_microfinances():
    try:
        microfinances = Microfinance.query.all()
        return jsonify([{
            "id": mf.id,
            "business_name": mf.business_name,
            "amount": mf.amount,
            "interest_rate": mf.interest_rate,
            "duration_months": mf.duration_months
        } for mf in microfinances]), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get a single microfinance entry by ID
@app.route('/microfinance/<int:id>', methods=['GET'])
def get_microfinance(id):
    try:
        mf = Microfinance.query.get_or_404(id)
        return jsonify({
            "id": mf.id,
            "business_name": mf.business_name,
            "amount": mf.amount,
            "interest_rate": mf.interest_rate,
            "duration_months": mf.duration_months
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update a microfinance entry
@app.route('/microfinance/<int:id>', methods=['PUT'])
def update_microfinance(id):
    try:
        data = request.get_json()
        mf = Microfinance.query.get_or_404(id)

        # Update fields if provided
        mf.business_name = data.get('business_name', mf.business_name)
        mf.amount = data.get('amount', mf.amount)
        mf.interest_rate = data.get('interest_rate', mf.interest_rate)
        mf.duration_months = data.get('duration_months', mf.duration_months)

        db.session.commit()

        return jsonify({"message": "Microfinance entry updated"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a microfinance entry
@app.route('/microfinance/<int:id>', methods=['DELETE'])
def delete_microfinance(id):
    try:
        mf = Microfinance.query.get_or_404(id)
        db.session.delete(mf)
        db.session.commit()

        return jsonify({"message": "Microfinance entry deleted"}), 204

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
