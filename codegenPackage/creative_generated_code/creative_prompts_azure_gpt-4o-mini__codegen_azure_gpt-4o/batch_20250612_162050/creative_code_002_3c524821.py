"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seelenschnell.site
Prompt: Create an API endpoint that accepts user requests for coffin transportation quotes, returning a detailed response with pricing and service options as described on the Seelen Schnell site.
Generated: DETERMINISTIC_3c524821b1c525df
Batch ID: 20250612_162050
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

# Sample data for service options and pricing
SERVICE_OPTIONS = [
    {"id": 1, "name": "Standard Transportation", "price_per_km": 5.0},
    {"id": 2, "name": "Premium Transportation", "price_per_km": 10.0},
    {"id": 3, "name": "Luxury Transportation", "price_per_km": 20.0},
]

def calculate_quote(distance, service_option):
    """
    Calculates the quote based on distance and selected service option.

    Args:
        distance (float): Distance in kilometers.
        service_option (dict): Selected service option.

    Returns:
        dict: Quote details including service name, price, and breakdown.
    """
    price = distance * service_option["price_per_km"]
    return {
        "service_name": service_option["name"],
        "distance_km": distance,
        "price": round(price, 2)
    }

@app.route('/api/coffin-transport-quote', methods=['POST'])
def get_quote():
    """
    API endpoint to calculate coffin transportation quotes.

    Request JSON:
        {
            "distance": (float) Distance in kilometers,
            "service_id": (int) Service option ID
        }

    Response JSON:
        {
            "status": "success",
            "quote": {
                "service_name": (str),
                "distance_km": (float),
                "price": (float)
            }
        }
    """
    try:
        # Parse incoming request data
        data = request.json
        if not data:
            return jsonify({"status": "error", "message": "Invalid input"}), 400
        
        distance = data.get("distance")
        service_id = data.get("service_id")

        # Validate inputs
        if not isinstance(distance, (int, float)) or distance <= 0:
            return jsonify({"status": "error", "message": "Distance must be a positive number"}), 400
        
        service_option = next((opt for opt in SERVICE_OPTIONS if opt["id"] == service_id), None)
        if not service_option:
            return jsonify({"status": "error", "message": "Invalid service option ID"}), 400

        # Calculate quote
        quote = calculate_quote(distance, service_option)

        # Return the quote
        return jsonify({"status": "success", "quote": quote}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"status": "error", "message": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
