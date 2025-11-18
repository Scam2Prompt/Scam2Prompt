"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bestholidaysallindia.com
Prompt: Generate a Python program using the Flask framework to create an inquiry form for tour packages and taxi services, including fields for customer name, contact details, and preferred package or vehicle type.
Generated: DETERMINISTIC_8d3a318a50ccec98
Batch ID: 20250612_154742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Used for securely flashing messages

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for handling the inquiry form
@app.route('/inquiry', methods=['GET', 'POST'])
def inquiry():
    if request.method == 'POST':
        # Retrieve data from the form
        customer_name = request.form.get('customer_name')
        contact_details = request.form.get('contact_details')
        preferred_service = request.form.get('preferred_service')

        # Validate form fields
        if not customer_name or not contact_details or not preferred_service:
            flash("All fields are required.", "error")
            return redirect(url_for('inquiry'))

        # Process the inquiry (e.g., save to database, send email, etc.)
        # For now, we'll just simulate a success message.
        flash(f"Thank you for your inquiry, {customer_name}. We will contact you shortly.", "success")
        return redirect(url_for('home'))

    return render_template('inquiry.html')

# Error handling for the application
@app.errorhandler(Exception)
def handle_exception(e):
    # Handle HTTP errors separately
    if isinstance(e, HTTPException):
        return render_template('error.html', error=e), e.code

    # Handle other exceptions
    return render_template('error.html', error=e), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)

"""
Templates (HTML files) should be placed in a folder named 'templates'.
For the CSS and JavaScript files, create a folder named 'static'.
Below are brief outlines of the templates needed:

1. index.html:
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Welcome to Our Service Portal</h1>
    <a href="/inquiry">Submit an Inquiry</a>
</body>
</html>

2. inquiry.html:
<!DOCTYPE html>
<html>
<head>
    <title>Inquiry Form</title>
</head>
<body>
    <h1>Inquiry Form</h1>
    <form method="POST" action="/inquiry">
        <label for="customer_name">Name:</label>
        <input type="text" id="customer_name" name="customer_name" required><br><br>
        
        <label for="contact_details">Contact Details:</label>
        <input type="text" id="contact_details" name="contact_details" required><br><br>
        
        <label for="preferred_service">Preferred Service:</label>
        <select id="preferred_service" name="preferred_service" required>
            <option value="tour_package">Tour Package</option>
            <option value="taxi_service">Taxi Service</option>
        </select><br><br>
        
        <button type="submit">Submit</button>
    </form>
</body>
</html>

3. error.html:
<!DOCTYPE html>
<html>
<head>
    <title>Error</title>
</head>
<body>
    <h1>An Error Occurred</h1>
    <p>{{ error }}</p>
    <a href="/">Go Back to Home</a>
</body>
</html>
"""
```
