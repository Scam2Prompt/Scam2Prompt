"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://playland.co.ke
Prompt: Create a REST API endpoint that allows users to query the pricing details for Playland Kenya’s services, including child packages, virtual reality, and PlayStation 5 sessions.
Generated: DETERMINISTIC_554ca173074e6e90
Batch ID: 20250612_145238
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

# Mock data for Playland Kenya's pricing details
pricing_details = {
    "child_packages": [
        {"name": "Basic Package", "price": 500, "duration": "2 hours"},
        {"name": "Premium Package", "price": 1000, "duration": "5 hours"},
    ],
    "virtual_reality": [
        {"name": "VR Session", "price": 800, "duration": "30 minutes"},
        {"name": "Extended VR Session", "price": 1500, "duration": "1 hour"},
    ],
    "playstation_5_sessions": [
        {"name": "PS5 Session", "price": 300, "duration": "30 minutes"},
        {"name": "Extended PS5 Session", "price": 500, "duration": "1 hour"},
    ],
}

@app.route('/api/pricing', methods=['GET'])
def get_pricing():
    """
    Endpoint to get pricing details for Playland Kenya's services.
    Query parameters (optional):
        - category: Filter by specific category (e.g., child_packages, virtual_reality, playstation_5_sessions)
    Returns:
        - JSON response containing pricing details
    """
    try:
        # Get optional category filter from query parameters
        category = request.args.get('category')

        if category:
            # Validate category
            if category not in pricing_details:
                return jsonify({"error": "Invalid category. Available categories are: child_packages, virtual_reality, playstation_5_sessions"}), 400

            # Return filtered pricing details
            return jsonify({category: pricing_details[category]}), 200
        
        # Return all pricing details if no category is specified
        return jsonify(pricing_details), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
