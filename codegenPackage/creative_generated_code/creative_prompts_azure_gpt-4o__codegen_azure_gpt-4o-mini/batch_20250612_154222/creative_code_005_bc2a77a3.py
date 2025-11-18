"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supportfix.online
Prompt: Create a REST API endpoint for querying available repair services by appliance type (e.g., washing machine, refrigerator) and supported brands (e.g., Toshiba, Samsung).
Generated: DETERMINISTIC_bc2a77a3911ef547
Batch ID: 20250612_154222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)

# Sample data representing available repair services
REPAIR_SERVICES = [
    {"id": 1, "appliance": "washing machine", "brand": "Toshiba"},
    {"id": 2, "appliance": "refrigerator", "brand": "Samsung"},
    {"id": 3, "appliance": "washing machine", "brand": "Samsung"},
    {"id": 4, "appliance": "dryer", "brand": "LG"},
]

# Schema for validating query parameters
class QuerySchema(Schema):
    appliance_type = fields.String(required=True)
    brand = fields.String(required=True)

@app.route('/api/repair-services', methods=['GET'])
def get_repair_services():
    """
    Endpoint to query available repair services by appliance type and brand.
    
    Query parameters:
        - appliance_type (str): The type of appliance (e.g., washing machine).
        - brand (str): The brand of the appliance (e.g., Toshiba).
    
    Returns:
        JSON response containing a list of matching repair services.
    """
    # Validate query parameters
    try:
        args = QuerySchema().load(request.args)
    except ValidationError as err:
        return jsonify({"error": "Invalid input", "messages": err.messages}), 400

    appliance_type = args['appliance_type'].lower()
    brand = args['brand'].lower()

    # Filter the repair services based on query parameters
    matching_services = [
        service for service in REPAIR_SERVICES
        if service['appliance'].lower() == appliance_type and service['brand'].lower() == brand
    ]

    if not matching_services:
        return jsonify({"message": "No matching repair services found."}), 404

    return jsonify(matching_services), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
