"""
Generated Code Metadata:
========================
Original URL: https://dentistasuzano.com.br
Prompt: Create an API endpoint for a dental clinic that retrieves information about various orthodontic appliances available, including conventional and aesthetic options.
Generated: DETERMINISTIC_9414910e8041f97b
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data representing orthodontic appliances
orthodontic_appliances = [
    {
        "id": 1,
        "name": "Metal Braces",
        "type": "Conventional",
        "description": "Traditional braces made of stainless steel.",
        "price": 3000
    },
    {
        "id": 2,
        "name": "Ceramic Braces",
        "type": "Aesthetic",
        "description": "Braces made of ceramic material for a less noticeable appearance.",
        "price": 4000
    },
    {
        "id": 3,
        "name": "Invisalign",
        "type": "Aesthetic",
        "description": "Clear aligners for teeth straightening without braces.",
        "price": 5000
    },
    {
        "id": 4,
        "name": "Lingual Braces",
        "type": "Aesthetic",
        "description": "Braces placed on the inner side of the teeth for a hidden look.",
        "price": 6000
    }
]

@app.route('/api/orthodontic-appliances', methods=['GET'])
def get_orthodontic_appliances():
    """
    API endpoint to retrieve information about orthodontic appliances.
    Returns:
        JSON response containing a list of orthodontic appliances.
    """
    try:
        # Check if a query parameter for filtering by type is provided
        appliance_type = request.args.get('type')
        
        if appliance_type:
            # Filter appliances by type if the query parameter is provided
            filtered_appliances = [
                appliance for appliance in orthodontic_appliances
                if appliance['type'].lower() == appliance_type.lower()
            ]
            return jsonify(filtered_appliances), 200
        
        # Return all appliances if no filter is applied
        return jsonify(orthodontic_appliances), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors for undefined routes.
    """
    return jsonify({"error": "Endpoint not found."}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors for server issues.
    """
    return jsonify({"error": "Internal server error."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
