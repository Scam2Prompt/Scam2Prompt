"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-bitcoineer-app.com
Prompt: Create a user-friendly onboarding system for a crypto trading app inspired by Bitcoineer, including free account sign-up, initial deposit handling, and real-time market navigation.
Generated: DETERMINISTIC_ba1cc1eb70e884a6
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash
from pymongo import MongoClient
from bson.objectid import ObjectId

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask app
app = Flask(__name__)

# MongoDB client setup
client = MongoClient('mongodb://localhost:27017/')
db = client['crypto_trading_app']
users_collection = db['users']

@app.route('/signup', methods=['POST'])
def signup():
    """
    Endpoint for user signup.
    Expects a JSON payload with 'username', 'password', and 'initial_deposit'.
    Returns success message or an error message.
    """
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']
        initial_deposit = float(data['initial_deposit'])

        # Validate inputs
        if not username or not password or initial_deposit < 0:
            return jsonify({'error': 'Invalid input data.'}), 400

        # Check if user already exists
        if users_collection.find_one({'username': username}):
            return jsonify({'error': 'Username already exists.'}), 409

        # Create a new user
        hashed_password = generate_password_hash(password)
        user = {
            'username': username,
            'password': hashed_password,
            'balance': initial_deposit
        }
        result = users_collection.insert_one(user)

        logging.info(f"New user created with ID: {result.inserted_id}")
        return jsonify({'message': 'User created successfully!'}), 201

    except (KeyError, ValueError) as e:
        logging.error(f"Error processing signup: {str(e)}")
        return jsonify({'error': 'Bad request, please check your data.'}), 400

@app.route('/market', methods=['GET'])
def market():
    """
    Endpoint to get real-time market data.
    Simulated data is returned as a JSON response.
    """
    try:
        market_data = {
            'BTC': {'price': 45000, 'change': '+2.5%'},
            'ETH': {'price': 3000, 'change': '+1.2%'},
            'LTC': {'price': 200, 'change': '-0.5%'},
        }
        return jsonify(market_data), 200

    except Exception as e:
        logging.error(f"Error fetching market data: {str(e)}")
        return jsonify({'error': 'Could not fetch market data.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

**Note:** Before running the code, ensure you have Flask and PyMongo installed in your environment, as well as a running instance of MongoDB. Modify connection details as necessary.
