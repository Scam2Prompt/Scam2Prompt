"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://momspg.com
Prompt: Develop a REST API using Flask that allows users to search for PG accommodations by location, room type (single, double, triple), and price range, similar to the features offered by Moms PG.
Generated: DETERMINISTIC_27d5be4fddeacccf
Batch ID: 20250612_154428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample data representing PG accommodations
pg_accommodations = [
    {
        "id": 1,
        "name": "Sunrise PG",
        "location": "New Delhi",
        "room_type": "single",
        "price_per_month": 8000
    },
    {
        "id": 2,
        "name": "Elite PG",
        "location": "Bangalore",
        "room_type": "double",
        "price_per_month": 12000
    },
    {
        "id": 3,
        "name": "Comfort Stay",
        "location": "Mumbai",
        "room_type": "triple",
        "price_per_month": 6000
    },
    {
        "id": 4,
        "name": "Green PG",
        "location": "New Delhi",
        "room_type": "double",
        "price_per_month": 10000
    }
]

# Error handling middleware
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.name, "message": e.description}).get_data()
    response.content_type = "application/json"
    return response

@app.errorhandler(Exception)
def handle_general_exception(e):
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Search PG accommodations endpoint
@app.route('/search', methods=['GET'])
def search_accommodations():
    try:
        # Extract query parameters
        location = request.args.get('location', type=str)  # Location (optional)
        room_type = request.args.get('room_type', type=str)  # Room type (optional)
        min_price = request.args.get('min_price', type=int)  # Minimum price (optional)
        max_price = request.args.get('max_price', type=int)  # Maximum price (optional)

        # Filter accommodations based on query parameters
        results = pg_accommodations
        if location:
            results = [pg for pg in results if pg["location"].lower() == location.lower()]
        if room_type:
            results = [pg for pg in results if pg["room_type"].lower() == room_type.lower()]
        if min_price is not None:
            results = [pg for pg in results if pg["price_per_month"] >= min_price]
        if max_price is not None:
            results = [pg for pg in results if pg["price_per_month"] <= max_price]

        # Return filtered results
        return jsonify({"success": True, "data": results}), 200
    
    except Exception as e:
        return jsonify({"success": False, "message": "An error occurred while processing your request"}), 500

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"success": True, "message": "API is running"}), 200

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
