"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laboratoriosavaz.com
Prompt: Generate code using Flask or Django to implement a feature that calculates the cost of medical tests based on user input, including tests like "hemograma completo" and "examen completo de orina."
Generated: DETERMINISTIC_746e6d9f634f2426
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code using Flask:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Dictionary to store medical test costs
TEST_COSTS = {
    "hemograma completo": 50.00,  # Cost in dollars
    "examen completo de orina": 30.00
}

@app.route('/calculate_cost', methods=['POST'])
def calculate_cost():
    """
    Endpoint to calculate the total cost of selected medical tests.
    Expects a JSON payload with a list of test names.
    Example payload:
    {
        "tests": ["hemograma completo", "examen completo de orina"]
    }
    """
    try:
        # Parse JSON data from the request
        data = request.json
        if not data or 'tests' not in data:
            return jsonify({"error": "Invalid input. Please provide a list of tests."}), 400

        tests = data['tests']
        if not isinstance(tests, list):
            return jsonify({"error": "Invalid format. 'tests' should be a list."}), 400

        # Calculate the total cost
        total_cost = 0.0
        unavailable_tests = []

        for test in tests:
            if test in TEST_COSTS:
                total_cost += TEST_COSTS[test]
            else:
                unavailable_tests.append(test)

        response = {
            "total_cost": round(total_cost, 2),  # Total cost rounded to 2 decimal places
            "unavailable_tests": unavailable_tests
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
