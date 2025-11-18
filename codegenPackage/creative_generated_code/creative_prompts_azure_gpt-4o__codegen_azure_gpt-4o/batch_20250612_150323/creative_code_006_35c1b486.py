"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Develop a web application using Flask that allows users to input their HVAC system details and receive financing plan recommendations, including rent-to-own options and "same as cash" plans, as described by Quality Sheet Metal, Inc.
Generated: DETERMINISTIC_35c1b486999d7150
Batch ID: 20250612_150323
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
import traceback

app = Flask(__name__)

# Sample financing plans (this would typically come from a database)
FINANCING_PLANS = [
    {"name": "Rent-to-Own", "description": "Pay monthly and own the system after 36 months.", "eligibility": "No credit check required."},
    {"name": "Same as Cash", "description": "Pay in full within 12 months with zero interest.", "eligibility": "Requires credit approval."},
]

@app.route('/')
def home():
    """Default route to display a welcome message."""
    return "Welcome to Quality Sheet Metal, Inc. Financing Recommendations!"

@app.route('/recommendations', methods=['POST'])
def get_recommendations():
    """
    Endpoint to receive HVAC system details and return financing recommendations.
    
    Request Payload:
    {
        "system_type": "string",
        "model": "string",
        "price": "float",
        "credit_score": "int"
    }
    
    Response:
    {
        "recommendations": [
            {
                "name": "string",
                "description": "string",
                "eligibility": "string"
            }
        ]
    }
    """
    try:
        # Parse and validate the payload
        data = request.json
        if not data:
            raise BadRequest("Request payload is missing or invalid.")
        if not all(k in data for k in ("system_type", "model", "price", "credit_score")):
            raise BadRequest("Missing required fields: 'system_type', 'model', 'price', 'credit_score'.")

        # Extract user inputs
        system_type = data["system_type"]
        model = data["model"]
        price = data["price"]
        credit_score = data["credit_score"]

        # Perform basic validation on inputs
        if not isinstance(system_type, str) or not system_type.strip():
            raise BadRequest("'system_type' must be a non-empty string.")
        if not isinstance(model, str) or not model.strip():
            raise BadRequest("'model' must be a non-empty string.")
        if not isinstance(price, (int, float)) or price <= 0:
            raise BadRequest("'price' must be a positive number.")
        if not isinstance(credit_score, int) or credit_score < 0:
            raise BadRequest("'credit_score' must be a non-negative integer.")

        # Logic to recommend financing plans
        recommendations = []
        for plan in FINANCING_PLANS:
            # Example logic: Add all plans for demonstration purposes
            recommendations.append(plan)

        response = {"recommendations": recommendations}
        return jsonify(response), 200

    except BadRequest as e:
        # Handle client-side errors
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # General error handling for server issues
        traceback.print_exc()
        return jsonify({"error": "An internal server error occurred."}), 500

if __name__ == '__main__':
    # Run the Flask app on localhost, port 5000
    app.run(debug=False)  # Set debug=False for production
```
