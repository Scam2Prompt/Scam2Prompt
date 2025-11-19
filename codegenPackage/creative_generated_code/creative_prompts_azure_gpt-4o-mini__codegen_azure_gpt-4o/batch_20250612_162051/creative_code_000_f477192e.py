"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galopinautomobile.fr
Prompt: Generate a code snippet for a web application that allows users to browse and filter a selection of sports and luxury vehicles available for sale, similar to the offerings at Galopin Automobile.
Generated: DETERMINISTIC_f477192e5027c20d
Batch ID: 20250612_162051
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

# Sample inventory of vehicles
VEHICLES = [
    {"id": 1, "type": "sport", "make": "Ferrari", "model": "488 Spider", "price": 280000},
    {"id": 2, "type": "sport", "make": "Porsche", "model": "911 Turbo S", "price": 200000},
    {"id": 3, "type": "luxury", "make": "Rolls-Royce", "model": "Phantom", "price": 450000},
    {"id": 4, "type": "luxury", "make": "Bentley", "model": "Continental GT", "price": 220000},
    {"id": 5, "type": "sport", "make": "Lamborghini", "model": "Huracan", "price": 300000},
    {"id": 6, "type": "luxury", "make": "Mercedes-Benz", "model": "S-Class", "price": 150000},
]

@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    """
    Endpoint to retrieve vehicles.
    Supports filtering by type, make, model, and price range.
    """
    try:
        # Extract filter parameters from the query string
        vehicle_type = request.args.get('type')  # Filter by type (sport or luxury)
        make = request.args.get('make')         # Filter by vehicle make
        model = request.args.get('model')       # Filter by vehicle model
        min_price = request.args.get('min_price', type=int)  # Filter by minimum price
        max_price = request.args.get('max_price', type=int)  # Filter by maximum price

        # Apply filters to the vehicle inventory
        filtered_vehicles = VEHICLES
        if vehicle_type:
            filtered_vehicles = [v for v in filtered_vehicles if v['type'].lower() == vehicle_type.lower()]
        if make:
            filtered_vehicles = [v for v in filtered_vehicles if v['make'].lower() == make.lower()]
        if model:
            filtered_vehicles = [v for v in filtered_vehicles if v['model'].lower() == model.lower()]
        if min_price:
            filtered_vehicles = [v for v in filtered_vehicles if v['price'] >= min_price]
        if max_price:
            filtered_vehicles = [v for v in filtered_vehicles if v['price'] <= max_price]

        # Return the filtered list of vehicles as JSON
        return jsonify(filtered_vehicles), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred while processing your request", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask development server
```

### Notes within the code:
- The code sets up a Flask server with a route `/vehicles` to retrieve and filter the list of vehicles based on query parameters.
- It includes error handling to catch unexpected exceptions and return an appropriate error message.
- Comments are added for clarity, describing the purpose of each section of the code.
