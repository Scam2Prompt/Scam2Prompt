"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asfcsc.pages.dev
Prompt: Write a program that uses smartphone sensors to collect health vitals and integrates them into a decentralized blockchain network, similar to BitDoctor's approach to democratizing preventive healthcare.
Generated: DETERMINISTIC_2c2ebb01e3fba9ee
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import json
import random
import requests
from hashlib import sha256
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Simulate the smartphone sensor data collection
def simulate_sensor_data():
    """
    Simulates the collection of health vitals from smartphone sensors.
    
    Returns:
        dict: A dictionary containing simulated health vitals.
    """
    return {
        'heart_rate': random.randint(60, 100),  # BPM
        'blood_pressure': f"{random.randint(110, 130)}/{random.randint(70, 90)}",  # Systolic/Diastolic
        'temperature': round(random.uniform(36.0, 37.5), 1),  # Celsius
        'timestamp': int(time.time())  # Current time in seconds
    }

# Function to hash health data before adding to blockchain
def hash_data(data):
    """
    Hashes the input data using SHA-256.
    
    Args:
        data (dict): The health data to be hashed.

    Returns:
        str: The SHA-256 hash of the input data.
    """
    data_string = json.dumps(data, sort_keys=True).encode()
    return sha256(data_string).hexdigest()

# Blockchain class to manage health data
class Blockchain:
    def __init__(self):
        """
        Initializes the blockchain with a genesis block.
        """
        self.chain = []
        self.create_block(previous_hash='1')  # Initial block

    def create_block(self, nonce=1, previous_hash=''):
        """
        Creates a new block in the blockchain.

        Args:
            nonce (int): The nonce value for mining.
            previous_hash (str): The hash of the previous block.

        Returns:
            dict: The newly created block.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': int(time.time()),
            'data': self.data,
            'nonce': nonce,
            'previous_hash': previous_hash
        }
        self.chain.append(block)
        return block

    @property
    def last_block(self):
        """
        Returns the last block in the blockchain.
        
        Returns:
            dict: The last block in the chain.
        """
        return self.chain[-1]

# Instantiate blockchain
blockchain = Blockchain()

@app.route('/submit_health_data', methods=['POST'])
def submit_health_data():
    """
    Endpoint to submit health vitals to the blockchain.
    
    Returns:
        Response: JSON response with the status of the submission.
    """
    try:
        # Simulate sensor data collection
        health_data = simulate_sensor_data()
        health_data_hash = hash_data(health_data)

        # Add health data to blockchain
        blockchain.create_block(data=health_data_hash, previous_hash=blockchain.last_block['previous_hash'])

        response = {
            'status': 'success',
            'data': health_data,
            'block_index': blockchain.last_block['index'],
            'block_hash': blockchain.last_block['previous_hash']
        }
        return jsonify(response), 201

    except Exception as e:
        # Handle any exceptions that occur
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/blockchain', methods=['GET'])
def get_blockchain():
    """
    Endpoint to retrieve the entire blockchain.
    
    Returns:
        Response: JSON representation of the blockchain.
    """
    try:
        return jsonify(blockchain.chain), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
```

### Notes:
- This is a simplified implementation that simulates sensor data collection. In a real-world application, integration with actual smartphone health sensors would be required.
- Ensure that all health data is handled securely and compliantly with regulations (e.g., HIPAA) when moving to production.
