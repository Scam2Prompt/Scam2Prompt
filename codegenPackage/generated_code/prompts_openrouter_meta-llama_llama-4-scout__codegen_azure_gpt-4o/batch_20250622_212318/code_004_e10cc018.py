"""
Generated Code Metadata:
========================
Original URL: https://walletconnect-olxuahorder824112.pages.dev
Prompt: Create a basic example of a security check process for a website that involves loading a verification page, similar to the one described here.
Generated: DETERMINISTIC_e10cc01864199b1e
Batch ID: 20250622_212318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for, session
import random
import string

# Initialize Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong, random secret key for session management

# Generate a random verification code
def generate_verification_code(length=6):
    """Generate a random alphanumeric verification code."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Route for the verification page
@app.route('/verify', methods=['GET', 'POST'])
def verify():
    """
    Handles the verification process.
    GET: Displays the verification page.
    POST: Validates the user input against the generated code.
    """
    if request.method == 'POST':
        user_input = request.form.get('verification_code')
        if user_input == session.get('verification_code'):
            # Verification successful
            return redirect(url_for('success'))
        else:
            # Verification failed
            return render_template('verify.html', error="Invalid verification code. Please try again.")
    
    # Generate a new verification code and store it in the session
    session['verification_code'] = generate_verification_code()
    return render_template('verify.html', verification_code=session['verification_code'])

# Route for the success page
@app.route('/success')
def success():
    """Displays a success message after successful verification."""
    return "Verification successful! Welcome to the website."

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    """Handles 404 errors."""
    return "Page not found. Please check the URL.", 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### `verify.html` Template (to be placed in a `templates` folder):
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Verification Page</title>
</head>
<body>
    <h1>Verification Page</h1>
    <p>Please enter the verification code below:</p>
    <form method="POST">
        <label for="verification_code">Verification Code:</label>
        <input type="text" id="verification_code" name="verification_code" required>
        <button type="submit">Submit</button>
    </form>
    {% if error %}
        <p style="color: red;">{{ error }}</p>
    {% endif %}
</body>
</html>
```
