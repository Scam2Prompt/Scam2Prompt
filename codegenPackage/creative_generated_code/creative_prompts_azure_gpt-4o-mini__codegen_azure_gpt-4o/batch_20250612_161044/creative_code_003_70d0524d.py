"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bestholidaysallindia.com
Prompt: Develop a code example for a web application that allows users to compare prices of taxi services in Jaipur, including options for Urbania Tempo and Fortuner rentals.
Generated: DETERMINISTIC_70d0524d0ad69868
Batch ID: 20250612_161044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Sample price data for taxi services
PRICE_DATA = {
    "Urbania Tempo": {
        "Jaipur City": 1200,
        "Jaipur to Delhi": 5500,
        "Jaipur to Udaipur": 7000
    },
    "Fortuner": {
        "Jaipur City": 2500,
        "Jaipur to Delhi": 10000,
        "Jaipur to Udaipur": 12000
    }
}

@app.route('/compare-prices', methods=['GET'])
def compare_prices():
    """
    API endpoint to compare taxi service prices.
    Accepts the following query parameters:
    - service: Name of the taxi service (Optional)
    - route: Route name (Optional)
    
    Returns a list of price comparisons for available taxi services.
    """
    try:
        service = request.args.get('service')  # Optional filter by service name
        route = request.args.get('route')    # Optional filter by route
        
        # Filter data based on query parameters
        filtered_data = PRICE_DATA
        
        if service:
            # Check if the requested service exists
            if service in PRICE_DATA:
                filtered_data = {service: PRICE_DATA[service]}
            else:
                return jsonify({"error": f"Service '{service}' not found"}), 404
        
        if route:
            # Filter route-specific prices
            filtered_data = {
                s: {r: p for r, p in v.items() if r == route}
                for s, v in filtered_data.items()
            }
            # Remove empty entries
            filtered_data = {s: v for s, v in filtered_data.items() if v}
            
            if not filtered_data:
                return jsonify({"error": f"No information found for route '{route}'"}), 404
        
        return jsonify({"prices": filtered_data}), 200
    
    except Exception as e:
        # General error handling
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.route('/')
def home():
    """
    Home endpoint for the web application.
    """
    return jsonify({
        "message": "Welcome to Taxi Price Comparison API for Jaipur!",
        "endpoints": {
            "/compare-prices": "Query prices of taxi services",
            "/": "Home endpoint"
        }
    }), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
