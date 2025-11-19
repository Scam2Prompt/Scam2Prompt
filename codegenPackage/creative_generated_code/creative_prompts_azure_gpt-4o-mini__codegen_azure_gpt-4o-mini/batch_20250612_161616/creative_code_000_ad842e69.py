"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://divinecollections.net
Prompt: Generate a code snippet for an e-commerce site that allows users to filter Golu Dolls by type, such as Clay Dolls, Paper Mache Dolls, and Wooden Dolls.
Generated: DETERMINISTIC_ad842e694fbb956b
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify

# Create a Flask application instance
app = Flask(__name__)

# Sample data representing Golu Dolls
golu_dolls = [
    {"id": 1, "type": "Clay", "name": "Clay Golu Doll 1"},
    {"id": 2, "type": "Paper Mache", "name": "Paper Mache Golu Doll 1"},
    {"id": 3, "type": "Wooden", "name": "Wooden Golu Doll 1"},
    {"id": 4, "type": "Clay", "name": "Clay Golu Doll 2"},
    {"id": 5, "type": "Wooden", "name": "Wooden Golu Doll 2"},
]

@app.route('/filter_dolls', methods=['GET'])
def filter_dolls():
    """
    Endpoint to filter Golu Dolls by type.
    
    Query Parameters:
    - type (str): The type of Golu Doll to filter by (e.g., Clay, Paper Mache, Wooden).
    
    Returns:
    - A JSON response containing the filtered list of Golu Dolls.
    """
    try:
        # Get the 'type' query parameter from the request
        doll_type = request.args.get('type')
        
        # Validate the input
        if not doll_type:
            return jsonify({"error": "Type parameter is required."}), 400
        
        # Filter the dolls based on the provided type
        filtered_dolls = [doll for doll in golu_dolls if doll['type'].lower() == doll_type.lower()]
        
        # Return the filtered list as a JSON response
        return jsonify(filtered_dolls), 200

    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True)
```
