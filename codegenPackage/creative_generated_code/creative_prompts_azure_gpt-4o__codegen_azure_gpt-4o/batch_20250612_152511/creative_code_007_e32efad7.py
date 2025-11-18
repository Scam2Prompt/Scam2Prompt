"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld-app.pages.dev
Prompt: Suggest tools or frameworks for implementing a Web3 socialfi platform like Everyworld, focusing on incentivized user engagement and environmental charity contributions.
Generated: DETERMINISTIC_e32efad774160630
Batch ID: 20250612_152511
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries and frameworks for the Web3 SocialFi platform
from web3 import Web3, HTTPProvider
from flask import Flask, request, jsonify
from eth_account import Account
from sqlalchemy import create_engine, Column, String, Float, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize Flask application
app = Flask(__name__)

# Connect to Ethereum blockchain
infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
web3 = Web3(HTTPProvider(infura_url))

# Check connection status
if web3.isConnected():
    print("Connected to Ethereum Blockchain")
else:
    raise ConnectionError("Failed to connect to Ethereum Blockchain")

# Define database setup
Base = declarative_base()
DATABASE_URL = "sqlite:///socialfi.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Define User model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    wallet_address = Column(String, unique=True, nullable=False)
    contribution_amount = Column(Float, default=0.0)

# Define Charity model
class Charity(Base):
    __tablename__ = 'charities'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    total_donations = Column(Float, default=0.0)

# Create tables
Base.metadata.create_all(engine)

# Helper function: Validate wallet address
def validate_wallet_address(address):
    """Validate Ethereum wallet address."""
    return web3.isAddress(address)

# Route: Register a new user
@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint to register a new user.
    JSON Request Body: { "username": "string", "wallet_address": "valid Ethereum address" }
    """
    data = request.json
    username = data.get("username")
    wallet_address = data.get("wallet_address")

    if not username or not wallet_address:
        return jsonify({"error": "Missing required fields"}), 400

    if not validate_wallet_address(wallet_address):
        return jsonify({"error": "Invalid wallet address"}), 400

    # Check for unique wallet address and username
    if session.query(User).filter_by(wallet_address=wallet_address).first() or session.query(User).filter_by(username=username).first():
        return jsonify({"error": "User already exists"}), 409

    # Create and save new user
    new_user = User(username=username, wallet_address=wallet_address)
    session.add(new_user)
    session.commit()

    return jsonify({"message": "User registered successfully"}), 201

# Route: Donate to an environmental charity
@app.route('/donate', methods=['POST'])
def donate_to_charity():
    """
    Endpoint to donate to a charity.
    JSON Request Body: { "username": "string", "charity_name": "string", "amount": float }
    """
    data = request.json
    username = data.get("username")
    charity_name = data.get("charity_name")
    amount = data.get("amount")

    if not username or not charity_name or not amount:
        return jsonify({"error": "Missing required fields"}), 400

    if amount <= 0:
        return jsonify({"error": "Donation amount must be greater than zero"}), 400

    user = session.query(User).filter_by(username=username).first()
    charity = session.query(Charity).filter_by(name=charity_name).first()

    if not user:
        return jsonify({"error": "User not found"}), 404

    if not charity:
        # If the charity doesn't exist, create a new charity record
        charity = Charity(name=charity_name)
        session.add(charity)

    # Update donation records
    user.contribution_amount += amount
    charity.total_donations += amount

    session.commit()

    return jsonify({"message": "Donation successful"}), 200

# Route: Get user details
@app.route('/user/<username>', methods=['GET'])
def get_user_details(username):
    """
    Endpoint to fetch user details by username.
    Path Parameter: username
    """
    user = session.query(User).filter_by(username=username).first()

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "username": user.username,
        "wallet_address": user.wallet_address,
        "contribution_amount": user.contribution_amount
    }), 200

# Route: Get charity details
@app.route('/charity/<name>', methods=['GET'])
def get_charity_details(name):
    """
    Endpoint to fetch charity details by name.
    Path Parameter: name
    """
    charity = session.query(Charity).filter_by(name=name).first()

    if not charity:
        return jsonify({"error": "Charity not found"}), 404

    return jsonify({
        "name": charity.name,
        "total_donations": charity.total_donations
    }), 200

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

This code provides the basic backend functionality to register users, donate to charities, and retrieve user and charity details, leveraging Web3, Ethereum, and Flask for the Web3 SocialFi platform.
