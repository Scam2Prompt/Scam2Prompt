"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pharmachoicecanada.ca
Prompt: Recommend APIs or libraries to create a web-based solution for independent pharmacy owners to manage profit sharing and transparency in a cooperative structure, as outlined by PharmaChoice Canada.
Generated: DETERMINISTIC_7f9b19d07687478f
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pharmacy_coop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for pharmacy owners
class PharmacyOwner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    profit_sharing_percentage = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<PharmacyOwner {self.name}>'

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to add a pharmacy owner
@app.route('/pharmacy_owner', methods=['POST'])
def add_pharmacy_owner():
    data = request.get_json()
    try:
        new_owner = PharmacyOwner(
            name=data['name'],
            profit_sharing_percentage=data['profit_sharing_percentage']
        )
        db.session.add(new_owner)
        db.session.commit()
        return jsonify({'message': 'Pharmacy owner added successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Pharmacy owner already exists or data is invalid.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to get all pharmacy owners
@app.route('/pharmacy_owners', methods=['GET'])
def get_pharmacy_owners():
    owners = PharmacyOwner.query.all()
    return jsonify([
        {'id': owner.id, 'name': owner.name, 'profit_sharing_percentage': owner.profit_sharing_percentage}
        for owner in owners
    ]), 200

# API endpoint to calculate total profit sharing
@app.route('/total_profit_sharing', methods=['GET'])
def calculate_total_profit_sharing():
    owners = PharmacyOwner.query.all()
    total_sharing = sum(owner.profit_sharing_percentage for owner in owners)
    return jsonify({'total_profit_sharing_percentage': total_sharing}), 200

# Error handling for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Ensure that Flask and Flask-SQLAlchemy libraries are installed in your Python environment.
- Adjust the database URI in the config to match your production database environment.
- This code includes basic error handling and should be further extended as necessary for production.
