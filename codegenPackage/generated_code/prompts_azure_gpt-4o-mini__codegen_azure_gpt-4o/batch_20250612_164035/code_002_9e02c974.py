"""
Generated Code Metadata:
========================
Original URL: https://3rdandtaylor.com
Prompt: Create a REST API endpoint that allows for the submission of a strategic marketing plan, incorporating the full-funnel approach mentioned on the 3rd & Taylor website.
Generated: DETERMINISTIC_9e02c9744ff948fc
Batch ID: 20250612_164035
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

# In-memory storage for marketing plans (for demonstration purposes)
marketing_plans = []

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

@app.route('/api/marketing-plan', methods=['POST'])
def submit_marketing_plan():
    """
    Endpoint to submit a strategic marketing plan.
    Expects a JSON payload with the following structure:
    {
        "title": "Plan Title",
        "description": "Detailed description of the plan",
        "full_funnel_approach": {
            "awareness": "Details about awareness strategy",
            "consideration": "Details about consideration strategy",
            "conversion": "Details about conversion strategy",
            "retention": "Details about retention strategy"
        }
    }
    """
    try:
        # Parse the JSON payload
        data = request.get_json()
        if not data:
            return jsonify({"error": "Bad Request", "message": "Request body must be JSON"}), 400

        # Validate required fields
        required_fields = ["title", "description", "full_funnel_approach"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": "Bad Request", "message": f"Missing required field: {field}"}), 400

        # Validate full_funnel_approach structure
        funnel_fields = ["awareness", "consideration", "conversion", "retention"]
        if not isinstance(data["full_funnel_approach"], dict):
            return jsonify({"error": "Bad Request", "message": "full_funnel_approach must be an object"}), 400
        for field in funnel_fields:
            if field not in data["full_funnel_approach"]:
                return jsonify({"error": "Bad Request", "message": f"Missing field in full_funnel_approach: {field}"}), 400

        # Store the marketing plan (in-memory for demonstration)
        marketing_plan = {
            "id": len(marketing_plans) + 1,
            "title": data["title"],
            "description": data["description"],
            "full_funnel_approach": data["full_funnel_approach"]
        }
        marketing_plans.append(marketing_plan)

        # Return success response
        return jsonify({"message": "Marketing plan submitted successfully", "plan": marketing_plan}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
