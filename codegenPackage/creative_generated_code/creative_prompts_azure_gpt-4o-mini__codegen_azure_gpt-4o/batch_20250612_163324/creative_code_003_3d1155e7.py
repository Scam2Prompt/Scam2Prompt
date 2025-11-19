"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bharatnews18.com
Prompt: Develop an API that provides information about mid-range smartphones in 2025, specifically including details about the Nothing Phone (1) and its design elements.
Generated: DETERMINISTIC_3d1155e760467f6d
Batch ID: 20250612_163324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data about mid-range smartphones in 2025
SMARTPHONES = [
    {
        "id": 1,
        "name": "Nothing Phone (1)",
        "release_year": 2025,
        "price_range": "mid-range",
        "features": {
            "design": "Transparent back with LED glyph interface",
            "processor": "Snapdragon 7 Gen 1",
            "display": "6.55-inch OLED, 120Hz",
            "camera": "50MP dual rear camera setup",
            "battery": "4500mAh with fast charging",
            "software": "Nothing OS 2.0 based on Android 15"
        }
    },
    {
        "id": 2,
        "name": "Pixel 7a",
        "release_year": 2025,
        "price_range": "mid-range",
        "features": {
            "design": "Plastic back with aluminum frame",
            "processor": "Google Tensor G3",
            "display": "6.1-inch OLED, 90Hz",
            "camera": "64MP wide and 12MP ultrawide",
            "battery": "4385mAh with fast charging",
            "software": "Android 15"
        }
    }
]

# Endpoint to fetch all mid-range smartphones
@app.route('/api/smartphones', methods=['GET'])
def get_smartphones():
    """
    Endpoint to fetch the list of mid-range smartphones in 2025.
    """
    return jsonify({"smartphones": SMARTPHONES}), 200

# Endpoint to fetch a specific smartphone by ID
@app.route('/api/smartphones/<int:smartphone_id>', methods=['GET'])
def get_smartphone(smartphone_id):
    """
    Endpoint to fetch details of a specific smartphone using its ID.
    """
    smartphone = next((phone for phone in SMARTPHONES if phone["id"] == smartphone_id), None)
    if smartphone is None:
        return jsonify({"error": "Smartphone not found"}), 404
    return jsonify(smartphone), 200

# Error handling for unsupported routes
@app.errorhandler(404)
def not_found_error(error):
    """
    Error handler for undefined routes.
    """
    return jsonify({"error": "Resource not found"}), 404

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
