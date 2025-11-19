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
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Sample data representing Golu Dolls in the database
golu_dolls = [
    {"id": 1, "name": "Traditional Clay Doll", "type": "Clay Dolls"},
    {"id": 2, "name": "Handmade Paper Mache Doll", "type": "Paper Mache Dolls"},
    {"id": 3, "name": "Carved Wooden Doll", "type": "Wooden Dolls"},
    {"id": 4, "name": "Painted Clay Doll", "type": "Clay Dolls"},
    {"id": 5, "name": "Decorative Wooden Doll", "type": "Wooden Dolls"},
]

@app.route('/filter_dolls', methods=['GET'])
def filter_dolls():
    """
    Endpoint to filter Golu Dolls based on their type.

    Query Parameters:
        type (str): The type of doll to filter (e.g., 'Clay Dolls', 'Paper Mache Dolls', 'Wooden Dolls').

    Returns:
        JSON response containing the filtered list of dolls or an error message.
    """
    try:
        # Get the 'type' query parameter
        doll_type = request.args.get('type')

        # If no type is provided, return an error
        if not doll_type:
            return jsonify({"error": "Missing 'type' query parameter"}), 400

        # Filter dolls based on the provided type
        filtered_dolls = [doll for doll in golu_dolls if doll["type"] == doll_type]

        # If no dolls match the filter, return an appropriate message
        if not filtered_dolls:
            return jsonify({"message": f"No dolls found for type '{doll_type}'"}), 404

        # Return the filtered dolls as a JSON response
        return jsonify({"filtered_dolls": filtered_dolls}), 200
    except Exception as e:
        # Catch any unexpected errors and return a server error message
        return jsonify({"error": "An error occurred while processing your request", "details": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
