"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geddesign.it
Prompt: Generate a code snippet for an e-commerce website that showcases high-quality, restored furniture, focusing on antique seating with modern upholstery.
Generated: DETERMINISTIC_ee08475e0ab51f99
Batch ID: 20250612_161700
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/images/chesterfield_sofa.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/images/victorian_armchair.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/images/mid_century_sofa.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import json
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Sample data representing restored antique seating
furniture_data = [
    {
        "id": 1,
        "name": "Victorian Armchair",
        "description": "A beautifully restored Victorian armchair with modern upholstery.",
        "price": 450.00,
        "image_url": "https://example.com/images/victorian_armchair.jpg",
        "category": "Seating"
    },
    {
        "id": 2,
        "name": "Mid-Century Modern Sofa",
        "description": "A stylish mid-century modern sofa, reupholstered in vibrant fabric.",
        "price": 1200.00,
        "image_url": "https://example.com/images/mid_century_sofa.jpg",
        "category": "Seating"
    },
    {
        "id": 3,
        "name": "Chesterfield Sofa",
        "description": "Classic Chesterfield sofa, expertly restored with luxurious fabric.",
        "price": 850.00,
        "image_url": "https://example.com/images/chesterfield_sofa.jpg",
        "category": "Seating"
    }
]

@app.route('/furniture', methods=['GET'])
def get_furniture():
    """
    Retrieve a list of high-quality restored furniture items.
    
    Returns:
        JSON response containing furniture data.
    """
    return jsonify(furniture_data), 200

@app.route('/furniture/<int:furniture_id>', methods=['GET'])
def get_furniture_by_id(furniture_id):
    """
    Retrieve a specific furniture item by its ID.
    
    Args:
        furniture_id (int): The ID of the furniture item to retrieve.

    Returns:
        JSON response containing the furniture item, or 404 if not found.
    """
    furniture_item = next((item for item in furniture_data if item["id"] == furniture_id), None)
    if furniture_item:
        return jsonify(furniture_item), 200
    else:
        return jsonify({"error": "Furniture item not found"}), 404

@app.route('/furniture', methods=['POST'])
def add_furniture():
    """
    Add a new furniture item to the collection.
    
    Returns:
        JSON response containing the added furniture item, or 400 if bad request.
    """
    try:
        new_furniture = request.json
        
        # Validate input
        if not all(k in new_furniture for k in ("name", "description", "price", "image_url", "category")):
            return jsonify({"error": "Missing required fields"}), 400
            
        new_id = max(item["id"] for item in furniture_data) + 1
        new_furniture["id"] = new_id
        furniture_data.append(new_furniture)
        
        return jsonify(new_furniture), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
