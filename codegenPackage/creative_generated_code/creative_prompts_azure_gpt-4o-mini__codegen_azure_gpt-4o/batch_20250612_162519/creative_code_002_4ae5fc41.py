"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoinconectswap.blogspot.com
Prompt: Create an API endpoint in Flask that returns a JSON object containing various shoe types like 'sapato social' and 'tenis de esporte' as outlined in the content from Lara Sapatos em Geral.
Generated: DETERMINISTIC_4ae5fc41b332f81f
Batch ID: 20250612_162519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify

app = Flask(__name__)

# List of shoe types to be returned by the endpoint
shoe_types = [
    {"id": 1, "type": "Sapato Social", "description": "Elegant formal shoes for professional or formal occasions."},
    {"id": 2, "type": "Tênis de Esporte", "description": "Sport shoes designed for physical activities and comfort."},
    {"id": 3, "type": "Chinelo", "description": "Casual flip-flops for relaxed settings or warm conditions."},
    {"id": 4, "type": "Bota", "description": "Sturdy boots suitable for outdoor activities or colder climates."},
    {"id": 5, "type": "Sandália", "description": "Open-toe footwear for casual wear during warm weather."}
]

@app.route('/api/shoe-types', methods=['GET'])
def get_shoe_types():
    """
    API Endpoint to fetch all shoe types.
    Returns:
        JSON object containing a list of shoe types.
    """
    try:
        return jsonify({"status": "success", "data": shoe_types}), 200
    except Exception as e:
        # Return a generic error message with status code 500 if something goes wrong
        return jsonify({"status": "error", "message": "An error occurred while processing your request."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)  # Set debug=False in production for security
```
