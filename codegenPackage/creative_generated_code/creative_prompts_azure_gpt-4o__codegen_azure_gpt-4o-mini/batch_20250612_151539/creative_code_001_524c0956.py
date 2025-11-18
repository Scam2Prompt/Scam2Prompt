"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://osaic.dev.dpai.tech
Prompt: Generate a Python script to validate user credentials for a platform similar to "docupace-dev-osaic" and redirect users to a specific UI upon successful login.
Generated: DETERMINISTIC_524c09567b8c5e91
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
from flask import Flask, request, redirect, url_for, render_template, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Sample user database (In a real application, this should be securely stored)
USER_DB = {
    "user1": hashlib.sha256("password1".encode()).hexdigest(),
    "user2": hashlib.sha256("password2".encode()).hexdigest(),
}

def validate_credentials(username, password):
    """
    Validates the user credentials against the stored user database.

    Args:
        username (str): The username provided by the user.
        password (str): The password provided by the user.

    Returns:
        bool: True if credentials are valid, False otherwise.
    """
    # Hash the password before comparing to stored hash
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    return USER_DB.get(username) == password_hash

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handles user login. If the user is authenticated, they are redirected to the dashboard.
    """
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Validate the credentials
        if validate_credentials(username, password):
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    """
    Displays the dashboard after successful login.
    """
    return render_template('dashboard.html')

@app.errorhandler(404)
def not_found(error):
    """
    Handles 404 errors.
    """
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Handles 500 errors.
    """
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

**Note:**
- This code assumes that you have Flask installed (`pip install Flask`) and have created the necessary HTML templates (`login.html`, `dashboard.html`, `404.html`, `500.html`) in a `templates` directory. 
- Replace `'your_secret_key'` with a secure random key for session management. 
- The user database in this example is hardcoded; in a production scenario, consider using a proper database with secure access.
