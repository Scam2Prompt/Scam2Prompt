"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://3rdandtaylor.com
Prompt: Create a REST API endpoint that allows for the submission of a strategic marketing plan, incorporating the full-funnel approach mentioned on the 3rd & Taylor website.
Generated: DETERMINISTIC_9e02c9744ff948fc
Batch ID: 20250612_164035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Define allowed fields in the marketing plan
ALLOWED_FIELDS = [
    "campaign_name", "target_audience", "goals", "budget", 
    "top_funnel_strategy", "middle_funnel_strategy", "bottom_funnel_strategy"
]

@app.route('/submit-marketing-plan', methods=['POST'])
def submit_marketing_plan():
    """
    Endpoint to submit a strategic marketing plan using a full-funnel approach.

    Expected JSON payload:
    {
        "campaign_name": "string",
        "target_audience": "string",
        "goals": "string",
        "budget": "float",
        "top_funnel_strategy": "string",
        "middle_funnel_strategy": "string",
        "bottom_funnel_strategy": "string"
    }

    Returns:
        - 200 OK: If the submission is successful.
        - 400 Bad Request: If the payload is invalid.
    """
    try:
        # Parse incoming JSON payload
        data = request.get_json()
        if not data:
            return jsonify({"error": "Missing or invalid JSON payload"}), 400

        # Validate fields in the payload
        missing_fields = [field for field in ALLOWED_FIELDS if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400

        # Additional validation (e.g., budget must be a positive number)
        if not isinstance(data.get("budget"), (int, float)) or data["budget"] <= 0:
            return jsonify({"error": "Budget must be a positive number"}), 400

        # Save or process the marketing plan here (e.g., save to a database)
        # For the sake of this example, we'll just return the submitted data.
        return jsonify({"message": "Marketing plan submitted successfully", "data": data}), 200

    except Exception as e:
        # Catch unexpected errors and return a generic error message
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
