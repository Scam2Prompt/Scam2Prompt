"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dentistasuzano.com.br
Prompt: Create an API endpoint for a dental clinic that retrieves information about various orthodontic appliances available, including conventional and aesthetic options.
Generated: DETERMINISTIC_9414910e8041f97b
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

app = Flask(__name__)

# Sample data representing orthodontic appliances available in the clinic
ORTHODONTIC_APPLIANCES = [
    {
        "id": 1,
        "name": "Metal Braces",
        "type": "Conventional",
        "description": "Traditional braces made of high-grade stainless steel.",
        "price": 2500
    },
    {
        "id": 2,
        "name": "Ceramic Braces",
        "type": "Aesthetic",
        "description": "Tooth-colored braces that are less visible than metal braces.",
        "price": 3500
    },
    {
        "id": 3,
        "name": "Clear Aligners",
        "type": "Aesthetic",
        "description": "Custom-made invisible trays for teeth alignment.",
        "price": 4500
    },
    {
        "id": 4,
        "name": "Lingual Braces",
        "type": "Aesthetic",
        "description": "Braces placed on the back side of teeth, hidden from view.",
        "price": 4000
    }
]

@app.route('/api/orthodontic-appliances', methods=['GET'])
def get_orthodontic_appliances():
    """
    API endpoint to retrieve information about orthodontic appliances available in the clinic.
    :return: JSON response with a list of orthodontic appliances.
    """
    try:
        # Retrieve optional query params for filtering by type
        appliance_type = request.args.get('type', None)
        
        if appliance_type:
            # Filter appliances based on 'type' query parameter (if provided)
            filtered_appliances = [
                appliance for appliance in ORTHODONTIC_APPLIANCES
                if appliance['type'].lower() == appliance_type.lower()
            ]
            return jsonify(filtered_appliances), 200
        
        # Return all appliances if no filter is applied
        return jsonify(ORTHODONTIC_APPLIANCES), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the application on localhost
    app.run(debug=True)
```
