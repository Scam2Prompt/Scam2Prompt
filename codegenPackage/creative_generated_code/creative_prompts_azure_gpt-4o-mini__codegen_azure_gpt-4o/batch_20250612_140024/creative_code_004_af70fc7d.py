"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoairdrop.code.blog
Prompt: How can I create a simple API that tracks cryptocurrency airdrops, based on the insights provided in the Crypto Airdrop blog?
Generated: DETERMINISTIC_af70fc7de4edd3b0
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# In-memory storage for airdrop data
airdrop_data = []

# Endpoint to get all airdrop data
@app.route('/airdrops', methods=['GET'])
def get_airdrops():
    """
    Fetch all tracked cryptocurrency airdrops.
    Returns:
        JSON response containing a list of all airdrops.
    """
    return jsonify({'airdrops': airdrop_data}), 200

# Endpoint to add a new airdrop
@app.route('/airdrops', methods=['POST'])
def add_airdrop():
    """
    Add a new cryptocurrency airdrop to the tracking system.
    Request JSON format:
    {
        "name": "Airdrop Name",
        "token": "Token Name",
        "start_date": "YYYY-MM-DD",
        "end_date": "YYYY-MM-DD",
        "details": "Additional information about the airdrop"
    }
    Returns:
        JSON response indicating success or failure.
    """
    try:
        # Parse request JSON
        data = request.json
        name = data.get('name')
        token = data.get('token')
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        details = data.get('details')

        # Validate required fields
        if not name or not token or not start_date or not end_date:
            return jsonify({'error': 'Missing required fields: name, token, start_date, end_date'}), 400

        # Validate date format
        try:
            start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
            end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError:
            return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD.'}), 400

        # Add airdrop to storage
        airdrop = {
            'id': len(airdrop_data) + 1,
            'name': name,
            'token': token,
            'start_date': start_date_obj.strftime('%Y-%m-%d'),
            'end_date': end_date_obj.strftime('%Y-%m-%d'),
            'details': details
        }
        airdrop_data.append(airdrop)

        logging.info(f"New airdrop added: {airdrop}")
        return jsonify({'message': 'Airdrop added successfully.', 'airdrop': airdrop}), 201

    except Exception as e:
        logging.error(f"Error adding airdrop: {e}")
        return jsonify({'error': 'An error occurred while adding the airdrop.'}), 500

# Endpoint to get details of a specific airdrop by ID
@app.route('/airdrops/<int:airdrop_id>', methods=['GET'])
def get_airdrop(airdrop_id):
    """
    Fetch details of a specific airdrop by its ID.
    Args:
        airdrop_id: The ID of the airdrop to fetch.
    Returns:
        JSON response with the airdrop details if found, or an error message.
    """
    airdrop = next((a for a in airdrop_data if a['id'] == airdrop_id), None)
    if airdrop:
        return jsonify({'airdrop': airdrop}), 200
    else:
        return jsonify({'error': f'Airdrop with ID {airdrop_id} not found.'}), 404

# Main entry point for the application
if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
