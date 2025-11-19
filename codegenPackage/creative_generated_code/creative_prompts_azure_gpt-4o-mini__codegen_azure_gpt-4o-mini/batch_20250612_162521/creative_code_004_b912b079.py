"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tmecryptodrainer.vercel.app
Prompt: How do I set up a first-come, first-served (FCFS) whitelist claiming mechanism for a crypto launch, based on the example from TME Crypto Drainer?
Generated: DETERMINISTIC_b912b0799aa351b0
Batch ID: 20250612_162521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import threading
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store for the whitelist and claims
whitelist = set()
claims = {}
max_claims = 100  # Maximum number of claims allowed

# Lock for thread-safe operations
lock = threading.Lock()

@app.route('/add_to_whitelist', methods=['POST'])
def add_to_whitelist():
    """
    Endpoint to add an address to the whitelist.
    Expects JSON body with a key 'address'.
    """
    data = request.json
    address = data.get('address')

    if not address:
        return jsonify({'error': 'Address is required'}), 400
    
    with lock:
        if address in whitelist:
            return jsonify({'error': 'Address already in whitelist'}), 400
        
        whitelist.add(address)
    
    return jsonify({'message': f'Address {address} added to whitelist'}), 201

@app.route('/claim', methods=['POST'])
def claim():
    """
    Endpoint for whitelisted addresses to claim their spot.
    Expects JSON body with a key 'address'.
    """
    data = request.json
    address = data.get('address')

    if not address:
        return jsonify({'error': 'Address is required'}), 400

    with lock:
        if address not in whitelist:
            return jsonify({'error': 'Address not in whitelist'}), 403
        
        if address in claims:
            return jsonify({'error': 'You have already claimed your spot'}), 403
        
        if len(claims) >= max_claims:
            return jsonify({'error': 'Maximum claims reached'}), 403
        
        claims[address] = time.time()  # Record the time of claiming

    return jsonify({'message': f'Claim successful for address {address}'}), 200

@app.route('/whitelist', methods=['GET'])
def get_whitelist():
    """
    Endpoint to retrieve the current whitelist.
    """
    return jsonify(list(whitelist)), 200

@app.route('/claims', methods=['GET'])
def get_claims():
    """
    Endpoint to retrieve the current claims.
    """
    return jsonify(claims), 200

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
```

### Notes:
- This code implements a simple Flask application with endpoints to manage a whitelist and allow claiming in a first-come, first-served manner.
- It includes error handling and thread safety using locks.
- The application is ready to run in a production environment with basic functionality for managing a whitelist for a crypto launch.
