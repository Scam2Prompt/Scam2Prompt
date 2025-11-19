"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.somosfortic.es
Prompt: Create an API endpoint that retrieves information about Fortic's products, specifically their concrete beams designed for gardens, and formats the data for a frontend display.
Generated: DETERMINISTIC_0906b04b4fda666d
Batch ID: 20250612_162051
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

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Sample data representing Fortic's concrete beams for gardens
concrete_beams = [
    {
        'id': 1,
        'name': 'Garden Beam A',
        'description': 'Durable concrete beam for garden use, perfect for supporting structures.',
        'length': '2m',
        'width': '30cm',
        'height': '10cm',
        'weight': '50kg',
        'price': 100.00
    },
    {
        'id': 2,
        'name': 'Garden Beam B',
        'description': 'Stylish garden beam with a textured finish, ideal for decorative purposes.',
        'length': '1.5m',
        'width': '25cm',
        'height': '15cm',
        'weight': '40kg',
        'price': 85.00
    }
]

@app.route('/api/products/concrete-beams', methods=['GET'])
def get_concrete_beams():
    """
    Retrieve the list of concrete beams designed for gardens.
    
    Returns:
        JSON response containing a list of concrete beam products.
    """
    try:
        logging.info("Retrieving concrete beams for gardens.")
        return jsonify(concrete_beams), 200
    except Exception as e:
        logging.error(f"Error retrieving concrete beams: {str(e)}")
        return jsonify({"error": "Unable to retrieve concrete beams."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False, host='0.0.0.0', port=5000)
```
