"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trx-bank.cc
Prompt: Create an API that allows users to manage and track their savings using devices and accessories mentioned on trx-bank.cc.
Generated: DETERMINISTIC_d0a0c61d81f429aa
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///savings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Setup logging for error tracking
logging.basicConfig(level=logging.INFO)

# Savings model representing the user's savings record
class Savings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_name = db.Column(db.String(100), nullable=False)
    amount_saved = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'device_name': self.device_name,
            'amount_saved': self.amount_saved
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Route to add a savings record
@app.route('/savings', methods=['POST'])
def add_savings():
    data = request.get_json()
    if not all(k in data for k in ('device_name', 'amount_saved')):
        return jsonify({'error': 'Missing data'}), 400
    
    new_savings = Savings(device_name=data['device_name'], amount_saved=data['amount_saved'])
    
    try:
        db.session.add(new_savings)
        db.session.commit()
        return jsonify(new_savings.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Failed to add savings record'}), 500

# Route to retrieve all savings records
@app.route('/savings', methods=['GET'])
def get_savings():
    savings_list = Savings.query.all()
    return jsonify([savings.to_dict() for savings in savings_list]), 200

# Route to update a savings record
@app.route('/savings/<int:savings_id>', methods=['PUT'])
def update_savings(savings_id):
    data = request.get_json()
    savings_record = Savings.query.get(savings_id)

    if savings_record is None:
        return jsonify({'error': 'Savings record not found'}), 404

    if 'device_name' in data:
        savings_record.device_name = data['device_name']
    if 'amount_saved' in data:
        savings_record.amount_saved = data['amount_saved']

    try:
        db.session.commit()
        return jsonify(savings_record.to_dict()), 200
    except Exception as e:
        logging.error(f"Error updating savings record: {e}")
        db.session.rollback()
        return jsonify({'error': 'Failed to update savings record'}), 500

# Route to delete a savings record
@app.route('/savings/<int:savings_id>', methods=['DELETE'])
def delete_savings(savings_id):
    savings_record = Savings.query.get(savings_id)

    if savings_record is None:
        return jsonify({'error': 'Savings record not found'}), 404

    try:
        db.session.delete(savings_record)
        db.session.commit()
        return jsonify({'message': 'Savings record deleted successfully'}), 200
    except Exception as e:
        logging.error(f"Error deleting savings record: {e}")
        db.session.rollback()
        return jsonify({'error': 'Failed to delete savings record'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
