"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-foundation.web.app
Prompt: Create a sample application questionnaire for the Sui Foundation's Developer Grants Program, ensuring it emphasizes the project's impact on decentralization.
Generated: DETERMINISTIC_756add81d3aca771
Batch ID: 20250612_162311
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Function to validate user input
def validate_input(data):
    required_fields = ["project_name", "team_name", "email", "project_description", "impact_on_decentralization"]
    missing_fields = [field for field in required_fields if field not in data or not data[field]]
    if missing_fields:
        return False, f"Missing required fields: {', '.join(missing_fields)}"
    
    # Validate email format
    if "@" not in data["email"] or "." not in data["email"]:
        return False, "Invalid email format."
    
    return True, None

# Endpoint to submit the questionnaire
@app.route('/submit-questionnaire', methods=['POST'])
def submit_questionnaire():
    """
    Endpoint to handle submissions for the Developer Grants Program questionnaire.
    Expects a JSON payload with the following fields:
    - project_name: Name of the project.
    - team_name: Name of the team or organization.
    - email: Contact email address.
    - project_description: Detailed description of the project.
    - impact_on_decentralization: Explanation of how the project impacts decentralization.
    """
    try:
        # Parse JSON request data
        data = request.get_json()

        # Validate input fields
        is_valid, error_msg = validate_input(data)
        if not is_valid:
            return jsonify({"success": False, "error": error_msg}), 400

        # Questionnaire data (could be saved to a database here)
        questionnaire = {
            "submission_date": datetime.utcnow().isoformat(),
            "project_name": data["project_name"],
            "team_name": data["team_name"],
            "email": data["email"],
            "project_description": data["project_description"],
            "impact_on_decentralization": data["impact_on_decentralization"]
        }

        # Simulate storing the data (e.g., save to a database here)
        # For the purpose of this example, just return the data back
        return jsonify({"success": True, "data": questionnaire}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"success": False, "error": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    # Use debug mode in development only, not in production
    app.run(debug=True)
```
