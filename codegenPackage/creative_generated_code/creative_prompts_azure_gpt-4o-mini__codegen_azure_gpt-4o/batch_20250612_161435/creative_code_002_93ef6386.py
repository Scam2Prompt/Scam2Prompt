"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://förderohr.de
Prompt: Create an API endpoint that provides users with a quote for high-pressure cleaning services based on the type of blockage, inspired by the pricing model of ElbeRohr.
Generated: DETERMINISTIC_93ef63868d147552
Batch ID: 20250612_161435
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

# Service pricing model inspired by ElbeRohr
PRICING_MODEL = {
    "minor": 50,  # Minor blockage, cost in dollars
    "moderate": 100,  # Moderate blockage, cost in dollars
    "severe": 200  # Severe blockage, cost in dollars
}

@app.route("/api/quote", methods=["POST"])
def get_quote():
    """
    API endpoint to provide a quote for high-pressure cleaning services
    based on the type of blockage.

    Request Body (JSON):
    {
        "blockage_type": "minor" | "moderate" | "severe"
    }

    Response:
    {
        "blockage_type": "minor",
        "quote": 50
    }
    """
    try:
        # Parse input JSON request
        data = request.get_json()
        if not data or "blockage_type" not in data:
            return jsonify({"error": "Invalid request format. 'blockage_type' is required."}), 400

        blockage_type = data["blockage_type"].lower()

        # Validate blockage_type and calculate the quote
        if blockage_type not in PRICING_MODEL:
            return jsonify({"error": f"Invalid blockage_type '{blockage_type}'. Allowed values are: minor, moderate, severe."}), 400

        quote = PRICING_MODEL[blockage_type]

        # Respond with the quote
        return jsonify({"blockage_type": blockage_type, "quote": quote}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```
