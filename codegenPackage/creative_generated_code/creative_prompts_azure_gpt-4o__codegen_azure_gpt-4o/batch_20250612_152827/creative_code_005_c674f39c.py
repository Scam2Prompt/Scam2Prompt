"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laboratoriosavaz.com
Prompt: Suggest an API design for a laboratory management system that handles test categories such as "perfil hepático," "perfil lipídico," and "paquete gastro," and allows users to query available tests and submit medical orders.
Generated: DETERMINISTIC_c674f39c17051c9f
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
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Sample data for test categories
TEST_CATEGORIES = {
    "perfil hepático": ["AST", "ALT", "Bilirubin Total", "Bilirubin Direct"],
    "perfil lipídico": ["Cholesterol Total", "HDL", "LDL", "Triglycerides"],
    "paquete gastro": ["Amylase", "Lipase", "Helicobacter Pylori"]
}

# Endpoint: Get available test categories and their tests
@app.route('/api/test-categories', methods=['GET'])
def get_test_categories():
    """
    Return a JSON object with available test categories and their associated tests.
    """
    return jsonify({"test_categories": TEST_CATEGORIES}), 200


# Endpoint: Submit a medical order
@app.route('/api/medical-orders', methods=['POST'])
def submit_medical_order():
    """
    Accepts a medical order submission.
    Expects JSON payload with 'patient_name' and 'tests' fields.
    """
    try:
        # Parse JSON request
        data = request.get_json()

        # Validate input
        if not data or 'patient_name' not in data or 'tests' not in data:
            raise BadRequest("Invalid input: 'patient_name' and 'tests' fields are required.")
        
        patient_name = data['patient_name']
        tests = data['tests']

        if not isinstance(patient_name, str) or not isinstance(tests, list):
            raise BadRequest("Invalid input types: 'patient_name' must be a string and 'tests' must be a list.")

        # Check if tests are valid
        invalid_tests = [test for test in tests if not any(test in tests_list for tests_list in TEST_CATEGORIES.values())]
        if invalid_tests:
            raise BadRequest(f"Invalid tests: {', '.join(invalid_tests)}.")

        # Simulate saving the medical order (production code would involve database interaction)
        medical_order = {
            "patient_name": patient_name,
            "tests": tests,
            "status": "submitted"
        }

        return jsonify({"message": "Medical order submitted successfully", "order": medical_order}), 201

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        # Catch all other errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
