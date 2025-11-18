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
app = Flask(__name__)

# Sample data representing available repair services
REPAIR_SERVICES = [
    {"id": 1, "appliance": "washing machine", "brand": "Samsung", "service": "Drum replacement"},
    {"id": 2, "appliance": "washing machine", "brand": "LG", "service": "Motor repair"},
    {"id": 3, "appliance": "refrigerator", "brand": "Toshiba", "service": "Coolant refill"},
    {"id": 4, "appliance": "refrigerator", "brand": "Samsung", "service": "Compressor repair"},
]

@app.route('/api/repair-services', methods=['GET'])
def get_repair_services():
    """
    Endpoint to query available repair services by appliance type and supported brands.
    Query Parameters:
      - appliance: Type of appliance (e.g., 'washing machine', 'refrigerator').
      - brand: Brand name (e.g., 'Samsung', 'Toshiba').

    Returns:
      JSON response containing the list of matching repair services.
    """
    try:
        # Extract query parameters
        appliance = request.args.get('appliance', '').lower()  # Default to empty string if not provided
        brand = request.args.get('brand', '').lower()          # Default to empty string if not provided

        # Validate input parameters
        if not appliance and not brand:
            return jsonify({"error": "At least one of 'appliance' or 'brand' must be provided"}), 400

        # Filter repair services based on query parameters
        filtered_services = [
            service for service in REPAIR_SERVICES
            if (not appliance or service['appliance'].lower() == appliance) and
               (not brand or service['brand'].lower() == brand)
        ]

        # Return filtered repair services as JSON response
        return jsonify({"repair_services": filtered_services}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred while processing your request", "details": str(e)}), 500

# Entry point for running the application
if __name__ == '__main__':
    app.run(debug=True)
```
