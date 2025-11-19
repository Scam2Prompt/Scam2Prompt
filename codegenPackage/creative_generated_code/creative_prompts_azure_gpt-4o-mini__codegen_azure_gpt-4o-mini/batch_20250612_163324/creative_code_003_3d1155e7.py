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
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Sample data for mid-range smartphones in 2025
smartphones = [
    {
        "id": 1,
        "name": "Nothing Phone (1)",
        "release_year": 2025,
        "design_elements": {
            "material": "Recycled aluminum frame",
            "display": "6.55-inch OLED",
            "color_options": ["Black", "White"],
            "unique_features": [
                "Transparent design",
                "Glyph interface",
                "LED notification lights"
            ]
        },
        "specifications": {
            "processor": "Qualcomm Snapdragon 778G",
            "ram": "8GB / 12GB",
            "storage": "128GB / 256GB",
            "battery": "4500mAh",
            "camera": {
                "front": "16MP",
                "rear": "50MP + 12MP"
            }
        }
    }
]

@app.route('/api/smartphones', methods=['GET'])
def get_smartphones():
    """Fetches the list of mid-range smartphones."""
    return jsonify(smartphones)

@app.route('/api/smartphones/<int:smartphone_id>', methods=['GET'])
def get_smartphone(smartphone_id):
    """Fetches details of a specific smartphone by ID."""
    smartphone = next((phone for phone in smartphones if phone['id'] == smartphone_id), None)
    if smartphone is None:
        abort(404, description="Smartphone not found")
    return jsonify(smartphone)

@app.errorhandler(404)
def not_found(error):
    """Handles 404 errors."""
    return jsonify({"error": "Not Found", "message": error.description}), 404

@app.errorhandler(400)
def bad_request(error):
    """Handles 400 errors."""
    return jsonify({"error": "Bad Request", "message": error.description}), 400

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production
```
