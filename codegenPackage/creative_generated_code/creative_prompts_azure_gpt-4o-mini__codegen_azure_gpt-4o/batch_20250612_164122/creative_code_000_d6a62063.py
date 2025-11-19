"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://natureexcursionsafaris.com
Prompt: Generate a code snippet for a web application that allows users to customize their Tanzania safari itinerary, incorporating features for selecting luxury lodges and budget camping options.
Generated: DETERMINISTIC_d6a62063ca205de5
Batch ID: 20250612_164122
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

# Sample data for lodges and camping options
lodges = [
    {"id": 1, "name": "Luxury Lodge Serengeti", "price_per_night": 300},
    {"id": 2, "name": "Luxury Lodge Ngorongoro", "price_per_night": 350},
]

camping_options = [
    {"id": 1, "name": "Budget Camping Serengeti", "price_per_night": 50},
    {"id": 2, "name": "Budget Camping Ngorongoro", "price_per_night": 60},
]

@app.route('/itinerary', methods=['POST'])
def create_itinerary():
    """
    Endpoint for customizing a Tanzania safari itinerary.
    Accepts JSON input with selected lodges and camping options.
    Returns the total cost and details of the itinerary.
    """
    try:
        # Parse the JSON request body
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request. Please provide JSON data."}), 400

        selected_lodges = data.get('selected_lodges', [])
        selected_camping = data.get('selected_camping', [])

        itinerary_details = {"lodges": [], "camping": []}
        total_cost = 0

        # Validate and calculate lodge selections
        for lodge_id in selected_lodges:
            lodge = next((l for l in lodges if l["id"] == lodge_id), None)
            if not lodge:
                return jsonify({"error": f"Lodge with ID {lodge_id} not found."}), 404
            itinerary_details["lodges"].append(lodge)
            total_cost += lodge["price_per_night"]

        # Validate and calculate camping selections
        for camping_id in selected_camping:
            camping = next((c for c in camping_options if c["id"] == camping_id), None)
            if not camping:
                return jsonify({"error": f"Camping option with ID {camping_id} not found."}), 404
            itinerary_details["camping"].append(camping)
            total_cost += camping["price_per_night"]

        # Return the finalized itinerary and cost
        return jsonify({
            "itinerary": itinerary_details,
            "total_cost": total_cost
        }), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@app.route('/lodges', methods=['GET'])
def get_lodges():
    """
    Endpoint to retrieve the list of available luxury lodges.
    """
    return jsonify({"lodges": lodges}), 200

@app.route('/camping', methods=['GET'])
def get_camping_options():
    """
    Endpoint to retrieve the list of available budget camping options.
    """
    return jsonify({"camping_options": camping_options}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
