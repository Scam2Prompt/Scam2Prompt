"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laboratoriosavaz.com
Prompt: Write Python code to create a REST API for managing medical test orders, including endpoints for submitting orders, retrieving test results, and calculating prices for tests like "perfil hepático" and "perfil lipídico."
Generated: DETERMINISTIC_db033340a1cd021e
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# Sample database for storing medical test orders and results
orders_db = {}
results_db = {}

# Test prices (in USD)
TEST_PRICES = {
    "perfil hepático": 50.0,
    "perfil lipídico": 40.0
}

# Helper function to calculate test prices
def calculate_price(tests):
    """Calculate the total price for the given list of tests."""
    total_price = 0.0
    for test in tests:
        if test in TEST_PRICES:
            total_price += TEST_PRICES[test]
        else:
            raise ValueError(f"Invalid test: {test}")
    return total_price

@app.route('/orders', methods=['POST'])
def submit_order():
    """
    Endpoint to submit a new medical test order.
    Expects JSON with fields: 'patient_name' (str), 'tests' (list of str).
    Returns the generated order ID and total price.
    """
    try:
        data = request.json
        patient_name = data.get('patient_name')
        tests = data.get('tests')

        # Validate input
        if not patient_name or not tests or not isinstance(tests, list):
            return jsonify({"error": "Invalid input. 'patient_name' and 'tests' are required."}), 400
        
        # Calculate price
        try:
            total_price = calculate_price(tests)
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

        # Generate unique order ID
        order_id = str(uuid.uuid4())

        # Save the order in the database
        orders_db[order_id] = {
            "patient_name": patient_name,
            "tests": tests,
            "total_price": total_price
        }

        return jsonify({"order_id": order_id, "total_price": total_price}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/results/<order_id>', methods=['GET'])
def get_results(order_id):
    """
    Endpoint to retrieve test results for a given order.
    Expects the 'order_id' in the URL.
    Returns the test results if available.
    """
    try:
        # Check if the order exists
        if order_id not in orders_db:
            return jsonify({"error": "Order not found."}), 404
        
        # Fetch results
        results = results_db.get(order_id, None)
        if results is None:
            return jsonify({"message": "Results not available yet."}), 200
        
        return jsonify({"order_id": order_id, "results": results}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/calculate_price', methods=['POST'])
def calculate_test_prices():
    """
    Endpoint to calculate the price for a list of medical tests.
    Expects JSON with field: 'tests' (list of str).
    Returns the total price.
    """
    try:
        data = request.json
        tests = data.get('tests')

        # Validate input
        if not tests or not isinstance(tests, list):
            return jsonify({"error": "Invalid input. 'tests' is required."}), 400

        # Calculate price
        try:
            total_price = calculate_price(tests)
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

        return jsonify({"total_price": total_price}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Sample endpoint to simulate adding results (for demonstration purposes)
@app.route('/results/<order_id>', methods=['POST'])
def add_results(order_id):
    """
    Endpoint to add test results for a given order.
    Expects JSON with field: 'results' (dict).
    """
    try:
        if order_id not in orders_db:
            return jsonify({"error": "Order not found."}), 404

        data = request.json
        results = data.get('results')

        if not results or not isinstance(results, dict):
            return jsonify({"error": "Invalid input. 'results' must be a dictionary."}), 400

        # Save results in the database
        results_db[order_id] = results

        return jsonify({"message": "Results added successfully."}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
