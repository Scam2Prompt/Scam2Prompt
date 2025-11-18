"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ptei.edu.bd
Prompt: Develop a Python application to assist users in applying for MRP (Machine Readable Passport) online, as described on the PTEI website.
Generated: DETERMINISTIC_58acf054760e9304
Batch ID: 20250612_154426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import sys

# Importing Flask for web application development
from flask import Flask, render_template, request, redirect, url_for, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Function to validate email addresses
def is_valid_email(email):
    """Validates an email address using a regex pattern."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# Function to validate phone numbers (10 digits)
def is_valid_phone_number(phone):
    """Validates a phone number (10 digits)."""
    pattern = r'^\d{10}$'
    return re.match(pattern, phone) is not None

# Function to validate the form data
def validate_form_data(data):
    """Validates user input for the MRP application form."""
    errors = []

    # Validate full name
    if not data.get('full_name'):
        errors.append("Full name is required.")

    # Validate email
    email = data.get('email')
    if not email or not is_valid_email(email):
        errors.append("Valid email address is required.")

    # Validate phone number
    phone_number = data.get('phone_number')
    if not phone_number or not is_valid_phone_number(phone_number):
        errors.append("Valid phone number is required.")

    # Validate date of birth
    date_of_birth = data.get('date_of_birth')
    if not date_of_birth:
        errors.append("Date of birth is required.")

    # Validate address
    if not data.get('address'):
        errors.append("Address is required.")

    return errors

# Route for the homepage
@app.route('/')
def home():
    """Render the homepage with the MRP application form."""
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit_application', methods=['POST'])
def submit_application():
    """Handles submission of the MRP application form."""
    try:
        # Extract form data
        form_data = request.form.to_dict()

        # Validate the form data
        errors = validate_form_data(form_data)

        # If validation errors exist, return errors to the user
        if errors:
            return jsonify({"status": "error", "errors": errors}), 400

        # Simulate saving form data to a database (or any other processing)
        # For production, replace this with actual database operations.
        # Example: db.save(form_data)

        return jsonify({"status": "success", "message": "Application submitted successfully!"}), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"status": "error", "message": "An unexpected error occurred.", "details": str(e)}), 500

# Start the Flask app
if __name__ == '__main__':
    try:
        app.run(debug=True)  # Set debug=False in production for better security
    except KeyboardInterrupt:
        print("\nApplication stopped manually.")
        sys.exit(0)
```

### Additional Notes:
1. Create an HTML file (`templates/index.html`) with the form structure to use this Flask app effectively.
2. Add proper database integration (e.g., SQLAlchemy) for production use.
3. Secure sensitive data using environment variables and follow security best practices.
