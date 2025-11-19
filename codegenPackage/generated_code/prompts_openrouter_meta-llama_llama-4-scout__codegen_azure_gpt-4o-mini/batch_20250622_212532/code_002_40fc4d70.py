"""
Generated Code Metadata:
========================
Original URL: https://aimining6.cc
Prompt: Generate code for an AI-driven mining pool management system.
Generated: DETERMINISTIC_40fc4d7032ba0b80
Batch ID: 20250622_212532
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Configure database URI (SQLite for simplicity, can be changed to any other DB)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mining_pool.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Miner model
class Miner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(100), unique=True, nullable=False)
    hash_rate = db.Column(db.Float, nullable=False)
    last_seen = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'address': self.address,
            'hash_rate': self.hash_rate,
            'last_seen': self.last_seen.isoformat()
        }

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to register a new miner
@app.route('/api/miners', methods=['POST'])
def register_miner():
    try:
        data = request.json
        new_miner = Miner(
            address=data['address'],
            hash_rate=data['hash_rate'],
            last_seen=data['last_seen']
        )
        db.session.add(new_miner)
        db.session.commit()
        return jsonify(new_miner.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        logging.error(f"Error registering miner: {e}")
        return jsonify({"error": "Could not register miner"}), 500
    except KeyError as e:
        return jsonify({"error": f"Missing field: {str(e)}"}), 400

# API endpoint to get all miners
@app.route('/api/miners', methods=['GET'])
def get_miners():
    try:
        miners = Miner.query.all()
        return jsonify([miner.to_dict() for miner in miners]), 200
    except SQLAlchemyError as e:
        logging.error(f"Error fetching miners: {e}")
        return jsonify({"error": "Could not fetch miners"}), 500

# API endpoint to update miner's hash rate
@app.route('/api/miners/<int:miner_id>', methods=['PUT'])
def update_miner(miner_id):
    try:
        data = request.json
        miner = Miner.query.get_or_404(miner_id)
        miner.hash_rate = data['hash_rate']
        miner.last_seen = data['last_seen']
        db.session.commit()
        return jsonify(miner.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        logging.error(f"Error updating miner: {e}")
        return jsonify({"error": "Could not update miner"}), 500
    except KeyError as e:
        return jsonify({"error": f"Missing field: {str(e)}"}), 400

# API endpoint to delete a miner
@app.route('/api/miners/<int:miner_id>', methods=['DELETE'])
def delete_miner(miner_id):
    try:
        miner = Miner.query.get_or_404(miner_id)
        db.session.delete(miner)
        db.session.commit()
        return jsonify({"message": "Miner deleted successfully"}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        logging.error(f"Error deleting miner: {e}")
        return jsonify({"error": "Could not delete miner"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
