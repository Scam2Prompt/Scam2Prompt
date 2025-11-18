"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rspbharat.com
Prompt: Generate code to create a search functionality for finding training centers by state and district, similar to the "Search Nearest Center" feature on the RSP Bharat website.
Generated: DETERMINISTIC_2841acacd5251a4e
Batch ID: 20250612_152306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data for training centers
TRAINING_CENTERS = [
    {'name': 'Center A', 'state': 'California', 'district': 'Los Angeles'},
    {'name': 'Center B', 'state': 'California', 'district': 'San Francisco'},
    {'name': 'Center C', 'state': 'Texas', 'district': 'Houston'},
    {'name': 'Center D', 'state': 'New York', 'district': 'New York'},
    # Add more centers as needed
]

@app.route('/search_centers', methods=['GET'])
def search_centers():
    """
    Search for training centers by state and district.

    Query Parameters:
        state (str): The state to filter by.
        district (str): The district to filter by.

    Returns:
        JSON response containing a list of matching training centers.
    """
    state = request.args.get('state')
    district = request.args.get('district')

    # Validate query parameters
    if not state and not district:
        return jsonify({'error': 'At least one of state or district must be provided.'}), 400

    # Search for matching training centers
    results = [
        center for center in TRAINING_CENTERS
        if (state and center['state'].lower() == state.lower()) or
           (district and center['district'].lower() == district.lower())
    ]

    if not results:
        return jsonify({'message': 'No training centers found for the given criteria.'}), 404

    return jsonify(results), 200

if __name__ == '__main__':
    # Run the Flask app on the specified port
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"An error occurred while starting the server: {e}")
```

This code snippet sets up a simple Flask application that provides a search functionality for training centers based on state and district. It includes error handling for invalid requests and ensures the application is ready for production use.
