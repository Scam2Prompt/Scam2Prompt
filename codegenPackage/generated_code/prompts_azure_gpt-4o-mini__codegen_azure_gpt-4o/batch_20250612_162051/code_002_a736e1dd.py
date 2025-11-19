"""
Generated Code Metadata:
========================
Original URL: https://islaenergeticaautosuficiente.com
Prompt: Generate a code snippet for a web application that allows users to input their energy consumption data and receive recommendations for improving energy efficiency, inspired by Digar Green's consulting services.
Generated: DETERMINISTIC_a736e1ddd17f3ab2
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample recommendations based on energy consumption
RECOMMENDATIONS = {
    "low": "Your energy consumption is low. Keep up the good work! Consider using energy-efficient appliances to maintain this level.",
    "medium": "Your energy consumption is moderate. Consider using LED lighting, unplugging devices when not in use, and optimizing heating/cooling systems.",
    "high": "Your energy consumption is high. We recommend conducting an energy audit, upgrading to energy-efficient appliances, and exploring renewable energy options like solar panels."
}

def get_recommendation(consumption):
    """
    Returns energy efficiency recommendations based on consumption level.
    """
    if consumption < 100:
        return RECOMMENDATIONS["low"]
    elif 100 <= consumption <= 300:
        return RECOMMENDATIONS["medium"]
    else:
        return RECOMMENDATIONS["high"]

@app.route('/energy', methods=['POST'])
def energy_efficiency():
    """
    Endpoint to receive energy consumption data and return recommendations.
    """
    try:
        # Parse JSON input
        data = request.get_json()
        if not data or 'consumption' not in data:
            return jsonify({"error": "Invalid input. Please provide 'consumption' in the request body."}), 400

        # Validate that consumption is a positive number
        consumption = data['consumption']
        if not isinstance(consumption, (int, float)) or consumption < 0:
            return jsonify({"error": "Consumption must be a positive number."}), 400

        # Get recommendation based on consumption
        recommendation = get_recommendation(consumption)

        # Return the recommendation
        return jsonify({
            "consumption": consumption,
            "recommendation": recommendation
        }), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
