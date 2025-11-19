"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atakoynakliyat.gen.tr
Prompt: Generate a code snippet for a web application that allows users to request a quote for Ataköy Evden Eve Nakliyat services, including options for city and intercity moves.
Generated: DETERMINISTIC_11154b4e2460c8cb
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to simulate quote calculation
def calculate_quote(move_type, distance, volume):
    """
    Calculate quote based on move type, distance, and volume.

    Parameters:
        move_type (str): Type of move ('city' or 'intercity').
        distance (float): Distance in kilometers.
        volume (float): Volume of goods in cubic meters.

    Returns:
        float: Estimated cost of the move.
    """
    base_rate = 500 if move_type == 'city' else 1500
    distance_rate = 2 if move_type == 'city' else 5
    volume_rate = 50 if move_type == 'city' else 100
    return base_rate + (distance * distance_rate) + (volume * volume_rate)

@app.route('/request-quote', methods=['POST'])
def request_quote():
    """
    Endpoint to request a quote for moving services.
    
    Request body must contain:
        - move_type: 'city' or 'intercity'
        - distance: Distance in kilometers (float)
        - volume: Volume of goods in cubic meters (float)

    Returns:
        JSON response with the estimated quote or error message.
    """
    try:
        # Parse JSON request body
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request, JSON data is required"}), 400
        
        # Validate required fields
        move_type = data.get('move_type')
        distance = data.get('distance')
        volume = data.get('volume')

        if move_type not in ['city', 'intercity']:
            return jsonify({"error": "Invalid move_type. Must be 'city' or 'intercity'"}), 400
        if not isinstance(distance, (int, float)) or distance <= 0:
            return jsonify({"error": "Invalid distance. Must be a positive number"}), 400
        if not isinstance(volume, (int, float)) or volume <= 0:
            return jsonify({"error": "Invalid volume. Must be a positive number"}), 400

        # Calculate the quote
        quote = calculate_quote(move_type, distance, volume)
        return jsonify({"quote": quote}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    # Start the Flask app
    app.run(debug=True)
```
