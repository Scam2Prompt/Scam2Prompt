"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://musicequipment.site
Prompt: Create a REST API that allows users to search for music equipment by brand, type, and price range, and provide sample code for implementation.
Generated: DETERMINISTIC_cf3ad0b1e1b15715
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: music_equipment_api.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for music equipment
music_equipment = [
    {"id": 1, "brand": "Yamaha", "type": "Keyboard", "price": 500},
    {"id": 2, "brand": "Gibson", "type": "Guitar", "price": 1200},
    {"id": 3, "brand": "Roland", "type": "Drum", "price": 800},
    {"id": 4, "brand": "Fender", "type": "Guitar", "price": 1000},
    {"id": 5, "brand": "Casio", "type": "Keyboard", "price": 300},
]

@app.route('/search', methods=['GET'])
def search_music_equipment():
    """
    Search for music equipment by brand, type, and price range.
    Query parameters:
        - brand (optional): Filter by brand.
        - type (optional): Filter by type.
        - min_price (optional): Minimum price.
        - max_price (optional): Maximum price.
    Returns:
        JSON response with the filtered list of music equipment.
    """
    try:
        # Extract query parameters
        brand = request.args.get('brand')
        equipment_type = request.args.get('type')
        min_price = request.args.get('min_price', type=float)
        max_price = request.args.get('max_price', type=float)

        # Filter the music equipment based on query parameters
        filtered_equipment = [
            item for item in music_equipment
            if (brand is None or item['brand'].lower() == brand.lower()) and
               (equipment_type is None or item['type'].lower() == equipment_type.lower()) and
               (min_price is None or item['price'] >= min_price) and
               (max_price is None or item['price'] <= max_price)
        ]

        # Return the filtered list as JSON
        return jsonify(filtered_equipment), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500

@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors for undefined routes.
    """
    return jsonify({"error": "Resource not found."}), 404

@app.errorhandler(500)
def internal_server_error(error):
    """
    Handle 500 errors for unexpected server issues.
    """
    return jsonify({"error": "Internal server error."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
