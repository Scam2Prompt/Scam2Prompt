"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rplanet-io.vercel.app
Prompt: Outline an API endpoint for managing the AI development process in the R-Planet game, detailing how base expansion affects droid consumption of Wecanite.
Generated: DETERMINISTIC_1c954b1984d89948
Batch ID: 20250612_162913
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

# Mock database to store base expansions and droid consumption data
database = {
    "base_expansion": [],  # List to store base expansion details
    "droid_consumption": {}  # Map to store Wecanite consumption per droid
}

@app.route('/api/expand_base', methods=['POST'])
def expand_base():
    """
    API endpoint to handle base expansion.
    Calculates and updates droid Wecanite consumption based on expansion.
    """
    try:
        # Parse incoming JSON data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input. Please provide JSON payload."}), 400

        # Extract required fields
        base_name = data.get("base_name")
        expansion_size = data.get("expansion_size")  # Number indicating size of expansion
        droid_count = data.get("droid_count")  # Number of droids in the base

        if not base_name or not isinstance(expansion_size, int) or not isinstance(droid_count, int):
            return jsonify({"error": "Missing or invalid parameters."}), 400

        # Calculate Wecanite consumption
        # Example formula: Wecanite consumption increases with expansion size and droid count
        consumption_rate = 0.05  # Base rate of Wecanite consumption per droid per unit expansion
        wecanite_consumption = expansion_size * droid_count * consumption_rate

        # Update database
        database["base_expansion"].append({
            "base_name": base_name,
            "expansion_size": expansion_size,
            "droid_count": droid_count,
            "wecanite_consumption": wecanite_consumption
        })
        database["droid_consumption"][base_name] = wecanite_consumption

        # Return success response
        return jsonify({
            "message": "Base expansion recorded successfully.",
            "base_name": base_name,
            "expansion_size": expansion_size,
            "droid_count": droid_count,
            "wecanite_consumption": wecanite_consumption
        }), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/api/get_consumption/<base_name>', methods=['GET'])
def get_consumption(base_name):
    """
    API endpoint to retrieve Wecanite consumption for a given base.
    """
    try:
        # Check if base exists in the database
        if base_name not in database["droid_consumption"]:
            return jsonify({"error": f"No consumption data found for base: {base_name}"}), 404
        
        # Retrieve and return consumption data
        consumption = database["droid_consumption"][base_name]
        return jsonify({
            "base_name": base_name,
            "wecanite_consumption": consumption
        }), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)  # Use debug mode for development; turn off in production
```
