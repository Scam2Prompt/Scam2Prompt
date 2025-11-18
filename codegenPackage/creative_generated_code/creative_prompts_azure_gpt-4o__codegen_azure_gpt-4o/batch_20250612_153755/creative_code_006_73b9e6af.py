"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalinvest-financial.com
Prompt: Develop a bug bounty program submission form for identifying vulnerabilities in web applications and APIs, inspired by GlobalInvest's active bug bounty program.
Generated: DETERMINISTIC_73b9e6af9420ddff
Batch ID: 20250612_153755
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def validate_email(email):
    """
    Validates an email address format using a regex pattern.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@app.route('/submit-bug', methods=['POST'])
def submit_bug():
    """
    Handles bug bounty program submissions.
    Validates user input and stores the submission if valid.
    """
    try:
        # Extract form data
        data = request.json
        name = data.get("name", "").strip()
        email = data.get("email", "").strip()
        vulnerability_type = data.get("vulnerability_type", "").strip()
        description = data.get("description", "").strip()
        steps_to_reproduce = data.get("steps_to_reproduce", "").strip()

        # Validate required fields
        if not name or not email or not vulnerability_type or not description or not steps_to_reproduce:
            return jsonify({"error": "All fields are required."}), 400
        
        # Validate email format
        if not validate_email(email):
            return jsonify({"error": "Invalid email format."}), 400

        # Simulate storing submission (e.g., save to a database)
        # In production, you would replace this with actual database interaction
        submission = {
            "name": name,
            "email": email,
            "vulnerability_type": vulnerability_type,
            "description": description,
            "steps_to_reproduce": steps_to_reproduce
        }
        # Log or store the submission (placeholder for database interaction)
        print("Bug submission received:", submission)

        # Respond to the user
        return jsonify({"message": "Bug bounty submission received. Thank you!"}), 200

    except Exception as e:
        # Catch unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
