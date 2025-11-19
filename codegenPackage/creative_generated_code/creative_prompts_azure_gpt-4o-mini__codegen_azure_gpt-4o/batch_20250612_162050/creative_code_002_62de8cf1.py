"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trindadetelecom.com.br
Prompt: Create a REST API endpoint that allows users to submit their internet speed needs and receive recommendations for Trindade Telecom's plans.
Generated: DETERMINISTIC_62de8cf1bf32a2b9
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

# Sample data for Trindade Telecom's plans
PLANS = [
    {"name": "Basic", "speed": 50, "price": 29.99},
    {"name": "Standard", "speed": 100, "price": 49.99},
    {"name": "Premium", "speed": 200, "price": 79.99},
    {"name": "Ultimate", "speed": 500, "price": 129.99},
]


@app.route('/recommend-plan', methods=['POST'])
def recommend_plan():
    """
    REST API endpoint to recommend a telecom plan based on user speed requirements.
    Accepts JSON input with the user's required speed and provides a list of suitable plans.
    """
    try:
        # Parse the JSON input from the request
        data = request.get_json()

        # Validate that 'required_speed' is provided and is a positive number
        if 'required_speed' not in data or not isinstance(data['required_speed'], (int, float)):
            return jsonify({"error": "Invalid input. Please provide 'required_speed' as a positive number."}), 400

        required_speed = data['required_speed']
        if required_speed <= 0:
            return jsonify({"error": "'required_speed' must be greater than 0."}), 400

        # Filter plans that meet or exceed the required speed
        suitable_plans = [plan for plan in PLANS if plan['speed'] >= required_speed]

        # If no plans are found, return a message indicating no recommendations
        if not suitable_plans:
            return jsonify({"message": "No plans available for the requested speed.", "required_speed": required_speed}), 200

        # Respond with the list of suitable plans
        return jsonify({
            "message": "Recommended plans for your internet speed needs.",
            "required_speed": required_speed,
            "plans": suitable_plans
        }), 200

    except Exception as e:
        # Catch any unexpected errors and return an internal server error response
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

This code defines a REST API endpoint using Flask, allowing users to submit their internet speed requirements and receive recommendations for telecom plans. To test it, run the script and use a tool like Postman or cURL to make a POST request to the `/recommend-plan` endpoint with JSON data specifying the `required_speed`.
