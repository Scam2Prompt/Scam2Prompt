"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mechanics.ae
Prompt: Write code to implement a search feature for car repair services by brand and model, allowing users to filter services like engine repair, transmission repair, and AC repair.
Generated: DETERMINISTIC_bd4311395bd1915f
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Sample data representing car repair services
repair_services = [
    {
        "service_id": 1,
        "brand": "Toyota",
        "model": "Corolla",
        "services": ["engine repair", "transmission repair", "AC repair"]
    },
    {
        "service_id": 2,
        "brand": "Honda",
        "model": "Civic",
        "services": ["engine repair", "AC repair"]
    },
    {
        "service_id": 3,
        "brand": "Ford",
        "model": "Mustang",
        "services": ["transmission repair", "AC repair"]
    },
    {
        "service_id": 4,
        "brand": "Toyota",
        "model": "Camry",
        "services": ["engine repair", "AC repair"]
    }
]

@app.route('/search', methods=['GET'])
def search_services():
    """
    Search for car repair services by brand, model, and type of service.
    Query parameters:
        - brand: The brand of the car (optional)
        - model: The model of the car (optional)
        - service: The type of repair service (optional)
    Returns:
        - JSON response with filtered repair services.
    """
    try:
        # Retrieve query parameters
        brand = request.args.get('brand', None)
        model = request.args.get('model', None)
        service = request.args.get('service', None)

        # Filter services based on query parameters
        filtered_services = repair_services
        if brand:
            filtered_services = [r for r in filtered_services if r['brand'].lower() == brand.lower()]
        if model:
            filtered_services = [r for r in filtered_services if r['model'].lower() == model.lower()]
        if service:
            filtered_services = [r for r in filtered_services if service.lower() in [s.lower() for s in r['services']]]

        # Return filtered results
        return jsonify({
            "success": True,
            "data": filtered_services
        }), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
