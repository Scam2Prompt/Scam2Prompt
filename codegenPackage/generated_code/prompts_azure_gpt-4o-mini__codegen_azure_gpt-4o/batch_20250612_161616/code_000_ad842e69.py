"""
Generated Code Metadata:
========================
Original URL: https://divinecollections.net
Prompt: Generate a code snippet for an e-commerce site that allows users to filter Golu Dolls by type, such as Clay Dolls, Paper Mache Dolls, and Wooden Dolls.
Generated: DETERMINISTIC_ad842e694fbb956b
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Sample data representing Golu Dolls in the inventory
golu_dolls = [
    {"id": 1, "name": "Clay Doll 1", "type": "Clay Dolls", "price": 15.99},
    {"id": 2, "name": "Paper Mache Doll 1", "type": "Paper Mache Dolls", "price": 12.99},
    {"id": 3, "name": "Wooden Doll 1", "type": "Wooden Dolls", "price": 20.99},
    {"id": 4, "name": "Clay Doll 2", "type": "Clay Dolls", "price": 18.99},
    {"id": 5, "name": "Paper Mache Doll 2", "type": "Paper Mache Dolls", "price": 14.99},
    {"id": 6, "name": "Wooden Doll 2", "type": "Wooden Dolls", "price": 22.99},
]

@app.route('/filter-dolls', methods=['GET'])
def filter_dolls():
    """
    Endpoint to filter Golu Dolls by type.
    Query parameter: type (e.g., 'Clay Dolls', 'Paper Mache Dolls', 'Wooden Dolls')
    Returns: JSON response with filtered dolls.
    """
    try:
        # Get the 'type' query parameter from the request
        doll_type = request.args.get('type')
        
        # Validate the input
        if not doll_type:
            return jsonify({"error": "Missing 'type' query parameter"}), 400
        
        # Filter the dolls based on the type
        filtered_dolls = [doll for doll in golu_dolls if doll["type"] == doll_type]
        
        # If no dolls match the filter, return an empty list
        if not filtered_dolls:
            return jsonify({"message": f"No dolls found for type '{doll_type}'", "data": []}), 200
        
        # Return the filtered dolls as a JSON response
        return jsonify({"message": "Dolls filtered successfully", "data": filtered_dolls}), 200
    
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
