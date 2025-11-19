"""
Generated Code Metadata:
========================
Original URL: https://searchhr.com.ar
Prompt: "Design an API for a vocational orientation platform, incorporating features from Search HR's Orientación Vocacional-Ocupacional services."
Generated: DETERMINISTIC_2843e11e24caadfe
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Mock database for demonstration purposes
mock_database = {
    "users": [],
    "tests": [
        {
            "id": 1,
            "name": "Career Aptitude Test",
            "description": "A test to determine your career strengths.",
        },
        {
            "id": 2,
            "name": "Interest Assessment",
            "description": "A test to identify your interests and suitable career paths.",
        },
    ],
    "results": [],
}

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.name, "message": e.description}).get_data()
    response.content_type = "application/json"
    return response


# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_general_exception(e):
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500


# Route: Get available vocational tests
@app.route("/api/v1/tests", methods=["GET"])
def get_tests():
    """
    Endpoint to retrieve all available vocational tests.
    """
    return jsonify({"tests": mock_database["tests"]}), 200


# Route: Register a new user
@app.route("/api/v1/users", methods=["POST"])
def register_user():
    """
    Endpoint to register a new user.
    """
    data = request.json
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Bad Request", "message": "Name and email are required."}), 400

    # Check if email already exists
    if any(user["email"] == data["email"] for user in mock_database["users"]):
        return jsonify({"error": "Conflict", "message": "Email already exists."}), 409

    # Add user to mock database
    user_id = len(mock_database["users"]) + 1
    new_user = {"id": user_id, "name": data["name"], "email": data["email"]}
    mock_database["users"].append(new_user)

    return jsonify({"message": "User registered successfully.", "user": new_user}), 201


# Route: Submit test results
@app.route("/api/v1/results", methods=["POST"])
def submit_results():
    """
    Endpoint to submit vocational test results.
    """
    data = request.json
    if not data or "user_id" not in data or "test_id" not in data or "score" not in data:
        return jsonify({"error": "Bad Request", "message": "User ID, Test ID, and score are required."}), 400

    # Validate user and test existence
    user = next((user for user in mock_database["users"] if user["id"] == data["user_id"]), None)
    test = next((test for test in mock_database["tests"] if test["id"] == data["test_id"]), None)

    if not user:
        return jsonify({"error": "Not Found", "message": "User not found."}), 404
    if not test:
        return jsonify({"error": "Not Found", "message": "Test not found."}), 404

    # Add results to mock database
    result_id = len(mock_database["results"]) + 1
    new_result = {
        "id": result_id,
        "user_id": data["user_id"],
        "test_id": data["test_id"],
        "score": data["score"],
    }
    mock_database["results"].append(new_result)

    return jsonify({"message": "Results submitted successfully.", "result": new_result}), 201


# Route: Get user results
@app.route("/api/v1/results/<int:user_id>", methods=["GET"])
def get_user_results(user_id):
    """
    Endpoint to retrieve all test results for a specific user.
    """
    user_results = [result for result in mock_database["results"] if result["user_id"] == user_id]

    if not user_results:
        return jsonify({"error": "Not Found", "message": "No results found for the user."}), 404

    return jsonify({"results": user_results}), 200


# Main entry point
if __name__ == "__main__":
    app.run(debug=True)
```
