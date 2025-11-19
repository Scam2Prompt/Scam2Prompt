"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multandesigns.com
Prompt: Create an API endpoint that allows users to filter Pakistani ethnic wear by occasion, such as weddings or casual outings, similar to the categorization on Multan Designs.
Generated: DETERMINISTIC_971a51256da5a06b
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a production-ready implementation in Python using the Flask framework for creating the API endpoint:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for Pakistani ethnic wear
ethnic_wear = [
    {"id": 1, "name": "Wedding Sherwani", "occasion": "wedding", "price": 15000},
    {"id": 2, "name": "Casual Kurta", "occasion": "casual", "price": 2500},
    {"id": 3, "name": "Formal Waistcoat", "occasion": "formal", "price": 5000},
    {"id": 4, "name": "Bridal Lehenga", "occasion": "wedding", "price": 30000},
    {"id": 5, "name": "Casual Shalwar Kameez", "occasion": "casual", "price": 3000},
]

@app.route('/api/ethnic-wear', methods=['GET'])
def filter_ethnic_wear():
    """
    API Endpoint to filter Pakistani ethnic wear based on occasion.
    Query Params:
        occasion (str): Filter ethnic wear by occasion (e.g., "wedding", "casual", "formal").
    Returns:
        JSON response containing filtered ethnic wear items.
    """
    try:
        # Get the 'occasion' query parameter
        occasion = request.args.get('occasion')

        if not occasion:
            # If no occasion provided, return all items
            return jsonify({"status": "success", "data": ethnic_wear}), 200

        # Filter ethnic wear based on the provided occasion
        filtered_wear = [item for item in ethnic_wear if item['occasion'].lower() == occasion.lower()]

        return jsonify({"status": "success", "data": filtered_wear}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

This code snippet creates a Flask-based API endpoint `/api/ethnic-wear` that accepts an optional query parameter `occasion` to filter ethnic wear items.
