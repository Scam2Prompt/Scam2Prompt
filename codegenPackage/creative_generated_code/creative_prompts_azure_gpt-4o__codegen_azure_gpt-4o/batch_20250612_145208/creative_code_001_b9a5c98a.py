"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://millennium-capital.com
Prompt: Generate code for a contact form that allows users to submit proposals for joint ventures or licensing opportunities, referencing the structure described on Millennium Capital's site.
Generated: DETERMINISTIC_b9a5c98abc1debc8
Batch ID: 20250612_145208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, render_template, jsonify
import re

# Initialize Flask application
app = Flask(__name__)

# Regular expression for email validation
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# Route for rendering the contact form
@app.route('/')
def contact_form():
    """
    Renders the contact form for submitting proposals.
    """
    return render_template('contact_form.html')  # HTML file should contain the form structure

# Route for handling form submissions
@app.route('/submit', methods=['POST'])
def submit_proposal():
    """
    Handles form submissions and validates input data.
    """
    try:
        # Retrieve form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        company = request.form.get('company')
        proposal_details = request.form.get('proposal_details')

        # Input validation
        if not name or not email or not company or not proposal_details:
            return jsonify({'error': 'All required fields must be filled out.'}), 400

        if not re.match(EMAIL_REGEX, email):
            return jsonify({'error': 'Invalid email format.'}), 400

        if phone and not phone.isdigit():
            return jsonify({'error': 'Phone number must contain only digits.'}), 400

        # Simulate saving the data to a database (replace with actual DB logic in production)
        # Example: save_to_database(name, email, phone, company, proposal_details)

        # Return success response
        return jsonify({'message': 'Proposal submitted successfully.'}), 200

    except Exception as e:
        # Return error response for unexpected issues
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

# Run the application
if __name__ == '__main__':
    # Use debug mode for development; set debug=False in production for better security
    app.run(debug=True)
```

### HTML Structure (`contact_form.html`)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
</head>
<body>
    <h1>Contact Form</h1>
    <form method="POST" action="/submit">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>

        <label for="phone">Phone (optional):</label>
        <input type="text" id="phone" name="phone"><br><br>

        <label for="company">Company:</label>
        <input type="text" id="company" name="company" required><br><br>

        <label for="proposal_details">Proposal Details:</label><br>
        <textarea id="proposal_details" name="proposal_details" rows="5" cols="40" required></textarea><br><br>

        <button type="submit">Submit Proposal</button>
    </form>
</body>
</html>
```
