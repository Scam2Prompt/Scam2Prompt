"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marinekiosk.gr
Prompt: Suggest an API or library for implementing age verification on a website, ensuring users confirm they are over 18 before accessing cannabis product details like "CHARAS 100% CB9 AMNESIA."
Generated: DETERMINISTIC_587d87f5411c1477
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask-based age verification API for a website
# This API ensures users confirm they are over 18 before accessing restricted product details.

from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Helper function to calculate age based on date of birth
def calculate_age(dob):
    try:
        birth_date = datetime.strptime(dob, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age
    except ValueError:
        return None

@app.route('/verify-age', methods=['POST'])
def verify_age():
    """
    Endpoint to verify age. 
    Expects a JSON payload with 'date_of_birth' in 'YYYY-MM-DD' format.
    Returns access status based on age verification.
    """
    try:
        # Get request data
        data = request.get_json()
        if not data or 'date_of_birth' not in data:
            return jsonify({"error": "Invalid request. 'date_of_birth' is required."}), 400
        
        dob = data['date_of_birth']
        age = calculate_age(dob)
        
        if age is None:
            return jsonify({"error": "Invalid date format. Use 'YYYY-MM-DD'."}), 400
        
        if age >= 18:
            return jsonify({"status": "Access granted", "message": "You are eligible to view product details."}), 200
        else:
            return jsonify({"status": "Access denied", "message": "You must be 18 or older to view product details."}), 403

    except Exception as e:
        # Generic error handling
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask server
    app.run(debug=True)
```

### Notes:
- The code uses `Flask`, a lightweight Python web framework, to implement the age verification API.
- It includes input validation, error handling, and clear documentation in comments.
