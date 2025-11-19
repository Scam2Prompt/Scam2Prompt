"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starmissteenindia.com
Prompt: Create an API that handles the registration process for a modeling contest, including validation for age and educational qualifications as seen in Star Miss Teen India 2025.
Generated: DETERMINISTIC_d747d136c6557289
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Constants for validation
MIN_AGE = 14
MAX_AGE = 19
VALID_EDUCATIONAL_QUALIFICATIONS = ["High School", "Intermediate", "Undergraduate"]

# In-memory storage for registrations (In production, replace with a database)
registrations = []

@app.route('/register', methods=['POST'])
def register_contestant():
    """
    API endpoint to register a contestant for the modeling contest.
    """
    try:
        # Parse JSON data from request
        data = request.get_json()

        # Input validation
        name = data.get('name')
        dob = data.get('dob')  # Date of birth in YYYY-MM-DD format
        education = data.get('education')

        if not name or not dob or not education:
            return jsonify({"error": "Name, Date of Birth, and Educational Qualification are required."}), 400
        
        # Validate date format
        try:
            dob_date = datetime.strptime(dob, '%Y-%m-%d')
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

        # Calculate age
        today = datetime.today()
        age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
        
        # Check age constraints
        if age < MIN_AGE or age > MAX_AGE:
            return jsonify({"error": f"Age must be between {MIN_AGE} and {MAX_AGE} years."}), 400

        # Check educational qualifications
        if education not in VALID_EDUCATIONAL_QUALIFICATIONS:
            return jsonify({"error": f"Educational qualification must be one of {VALID_EDUCATIONAL_QUALIFICATIONS}."}), 400

        # Store registration (In production, persist to database)
        contestant = {
            "name": name,
            "dob": dob,
            "age": age,
            "education": education
        }
        registrations.append(contestant)

        # Respond with success message
        return jsonify({"message": "Registration successful!", "contestant": contestant}), 201

    except Exception as e:
        # Generic error handler
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route('/registrations', methods=['GET'])
def get_registrations():
    """
    API endpoint to retrieve all registrations.
    """
    return jsonify({"registrations": registrations})


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
