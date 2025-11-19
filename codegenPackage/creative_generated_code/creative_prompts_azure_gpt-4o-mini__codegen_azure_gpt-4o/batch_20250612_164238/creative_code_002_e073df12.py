"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coastalboatrentals.co.za
Prompt: Create a REST API endpoint specification for retrieving information about the boats offered by Coastal Boat Rentals, including their features and rental prices.
Generated: DETERMINISTIC_e073df127857e3a6
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's the code for the REST API endpoint specification using Python with Flask:

```python
from flask import Flask, jsonify, request

# Create a Flask application instance
app = Flask(__name__)

# Mock data representing the boats offered by Coastal Boat Rentals
boats = [
    {
        "id": 1,
        "name": "Sea Breeze",
        "features": ["GPS Navigation", "Life Jackets", "Cooler"],
        "rental_price": 150.0  # Price per hour in USD
    },
    {
        "id": 2,
        "name": "Wave Rider",
        "features": ["Fishing Rod Holders", "Bluetooth Speakers", "Sun Deck"],
        "rental_price": 200.0  # Price per hour in USD
    },
    {
        "id": 3,
        "name": "Ocean Explorer",
        "features": ["Cabin", "Kitchenette", "Wi-Fi"],
        "rental_price": 300.0  # Price per hour in USD
    }
]

@app.route('/api/boats', methods=['GET'])
def get_boats():
    """
    Endpoint to retrieve information about the boats offered by Coastal Boat Rentals.
    
    HTTP Method: GET
    URL Path: /api/boats
    
    Query Parameters (optional):
      - name: Filter boats by name (case-insensitive)
    
    Response:
      - JSON array of boats with their details (id, name, features, rental_price).
    """
    try:
        # Get query parameter for filtering by name (optional)
        name_filter = request.args.get('name', None)
        
        if name_filter:
            # Filter boats by name (case-insensitive)
            filtered_boats = [
                boat for boat in boats
                if name_filter.lower() in boat["name"].lower()
            ]
            return jsonify(filtered_boats), 200
        
        # Return all boats if no filter is provided
        return jsonify(boats), 200
    
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while retrieving the boats.", "details": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

This code provides a REST API endpoint at `/api/boats` for retrieving information about boats available for rental. It includes optional filtering by boat name using query parameters.
