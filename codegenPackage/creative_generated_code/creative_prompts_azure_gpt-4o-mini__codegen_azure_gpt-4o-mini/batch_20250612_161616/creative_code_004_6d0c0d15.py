"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://outlaws.wtf
Prompt: Generate code for a blockchain-based game that allows users to participate in a narrative-driven treasure hunt like the one described on Outlaws.WTF.
Generated: DETERMINISTIC_6d0c0d15fd583ba1
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from web3 import Web3
import os

app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///treasure_hunt.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Web3 configuration (replace with your Ethereum node provider)
web3 = Web3(Web3.HTTPProvider(os.getenv('ETH_NODE_URL')))

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(42), unique=True, nullable=False)
    score = db.Column(db.Integer, default=0)

# Define the Treasure model
class Treasure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), unique=True, nullable=False)
    reward = db.Column(db.Integer, default=0)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to register a user
@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    address = data.get('address')

    # Error handling for missing address
    if not address:
        return jsonify({"error": "Address is required"}), 400

    # Check if user already exists
    existing_user = User.query.filter_by(address=address).first()
    if existing_user:
        return jsonify({"error": "User already exists"}), 400

    # Create and save the new user
    new_user = User(address=address)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully"}), 201

# Endpoint to list all treasures
@app.route('/treasures', methods=['GET'])
def get_treasures():
    treasures = Treasure.query.all()
    return jsonify([{"id": t.id, "location": t.location, "reward": t.reward} for t in treasures]), 200

# Endpoint to claim a treasure
@app.route('/claim_treasure', methods=['POST'])
def claim_treasure():
    data = request.json
    address = data.get('address')
    treasure_id = data.get('treasure_id')

    # Error handling for missing data
    if not address or not treasure_id:
        return jsonify({"error": "Address and Treasure ID are required"}), 400

    user = User.query.filter_by(address=address).first()
    treasure = Treasure.query.filter_by(id=treasure_id).first()

    # Check if user and treasure exist
    if not user:
        return jsonify({"error": "User not found"}), 404
    if not treasure:
        return jsonify({"error": "Treasure not found"}), 404

    # Update user's score and delete the treasure
    user.score += treasure.reward
    db.session.delete(treasure)
    db.session.commit()

    return jsonify({"message": "Treasure claimed successfully", "new_score": user.score}), 200

# Start the application
if __name__ == '__main__':
    # Ensure the required environment variable is set
    if not os.getenv('ETH_NODE_URL'):
        raise EnvironmentError("ETH_NODE_URL environment variable must be set")
    
    app.run(debug=True)
```

Make sure to install the required packages using:
```bash
pip install Flask Flask-SQLAlchemy web3
```

This code provides a basic server for a blockchain-based treasure hunt game where users can register, view treasures, and claim them for rewards. The database is set up using SQLite for simplicity, while Web3 is included for potential integration with an Ethereum smart contract.
