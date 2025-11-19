"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thedaybrightener.com
Prompt: How can I implement a sweepstakes entry form for a backyard movie night promotion similar to The Day Brightener Sweepstakes?
Generated: DETERMINISTIC_1546ae3f032837ac
Batch ID: 20250612_155150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# In-memory database to store entries (use a proper database in production)
entries = []

# Helper function to validate email addresses
def is_valid_email(email):
    # Regex pattern to validate email format
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Route for displaying the sweepstakes form (GET request)
@app.route('/sweepstakes', methods=['GET'])
def display_form():
    # Simple HTML form for sweepstakes entry
    form_html = """
    <html>
        <body>
            <h1>Backyard Movie Night Sweepstakes Entry Form</h1>
            <form action="/sweepstakes" method="POST">
                <label for="name">Name:</label><br>
                <input type="text" id="name" name="name" required><br><br>
                <label for="email">Email:</label><br>
                <input type="email" id="email" name="email" required><br><br>
                <label for="phone">Phone Number:</label><br>
                <input type="text" id="phone" name="phone" required><br><br>
                <input type="submit" value="Submit Entry">
            </form>
        </body>
    </html>
    """
    return form_html

# Route for handling form submissions (POST request)
@app.route('/sweepstakes', methods=['POST'])
def submit_entry():
    try:
        # Get form data
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        phone = request.form.get('phone', '').strip()

        # Validate inputs
        if not name or not email or not phone:
            return jsonify({"error": "All fields are required"}), 400

        if not is_valid_email(email):
            return jsonify({"error": "Invalid email format"}), 400

        # Add the entry to the in-memory database
        entries.append({"name": name, "email": email, "phone": phone})

        # Return success response
        return jsonify({"message": "Entry successfully submitted!"}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route to view all entries (GET request, for admin purposes)
@app.route('/admin/view-entries', methods=['GET'])
def view_entries():
    # Return all entries as JSON (in production, secure this endpoint)
    return jsonify(entries), 200

# Entry point for the application
if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
