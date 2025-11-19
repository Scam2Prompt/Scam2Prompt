"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.homes
Prompt: Develop a RESTful API endpoint that allows users to search for modern homes in Estepona, including parameters for budget and desired features like underground parking.
Generated: DETERMINISTIC_96cd0c19bbfefeca
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Sample data: Modern homes in Estepona
homes = [
    {
        "id": 1,
        "location": "Estepona",
        "type": "modern",
        "price": 250000,
        "features": ["underground parking", "garden", "pool"]
    },
    {
        "id": 2,
        "location": "Estepona",
        "type": "modern",
        "price": 300000,
        "features": ["underground parking", "solar panels"]
    },
    {
        "id": 3,
        "location": "Estepona",
        "type": "modern",
        "price": 200000,
        "features": ["garden"]
    }
]

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/search-homes', methods=['GET'])
def search_homes():
    """
    Endpoint to search for modern homes in Estepona based on budget and desired features.
    Query Parameters:
        - max_budget: Maximum budget (int)
        - features: Desired features (comma-separated string)
    Returns:
        JSON response with matching homes.
    """
    try:
        # Parse query parameters
        max_budget = request.args.get('max_budget', type=int)
        features = request.args.get('features', type=str)

        # Validate max_budget parameter
        if max_budget is None:
            return jsonify({"error": "Missing required parameter: max_budget"}), 400

        # Parse features into a list if provided
        desired_features = features.split(',') if features else []

        # Filter homes based on criteria
        matching_homes = [
            home for home in homes
            if home["price"] <= max_budget and all(feature in home["features"] for feature in desired_features)
        ]

        # Log the request and response
        logging.info(f"Search request: max_budget={max_budget}, features={desired_features}")
        logging.info(f"Number of matching homes: {len(matching_homes)}")

        return jsonify(matching_homes), 200

    except Exception as e:
        # Log any unexpected error
        logging.error(f"An error occurred: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
