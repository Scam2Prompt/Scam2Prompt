"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lucid-portal.evpump.net
Prompt: Can you provide a code snippet for a login form that includes email and password fields, inspired by the EvPump portal?
Generated: DETERMINISTIC_3469aba3613b244a
Batch ID: 20250612_155432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash

# Initialize the Flask application
app = Flask(__name__)

# Set a secret key for session data and flash messages
app.secret_key = 'your_secret_key_here'

# Dummy user data for authentication. In production, use a secure database.
USER_DATA = {
    "test@example.com": "securepassword123"
}

@app.route('/')
def home():
    """
    Home route to display the login form.
    """
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    """
    Route to handle login form submission.
    """
    try:
        # Get form data
        email = request.form.get('email')
        password = request.form.get('password')

        # Validate form data
        if not email or not password:
            flash("Email and Password are required.", "error")
            return redirect(url_for('home'))

        # Check if the credentials match the dummy data
        if email in USER_DATA and USER_DATA[email] == password:
            flash("Login successful!", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid email or password.", "error")
            return redirect(url_for('home'))
    except Exception as e:
        # Log the error and display a generic error message
        print(f"Error occurred during login: {e}")
        flash("An unexpected error occurred. Please try again later.", "error")
        return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    """
    Dashboard route after successful login.
    """
    return "Welcome to the EvPump Portal Dashboard!"

# Run the application
if __name__ == '__main__':
    # Enable debug mode for development. Disable in production.
    app.run(debug=True)
```

```html
<!-- login.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EvPump Portal Login</title>
    <style>
        /* Basic styling for the login form */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
        }
        .login-container {
            max-width: 400px;
            margin: 100px auto;
            padding: 20px;
            background: #fff;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
        }
        .login-container h1 {
            text-align: center;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
        }
        .form-group input {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 3px;
        }
        .btn-submit {
            width: 100%;
            padding: 10px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 3px;
            cursor: pointer;
        }
        .btn-submit:hover {
            background-color: #0056b3;
        }
        .flash {
            color: red;
            text-align: center;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h1>Login</h1>
        <!-- Flash messages for errors or success -->
        {% with messages = get_flashed_messages(with_categories=True) %}
        {% if messages %}
        <div class="flash">
            {% for category, message in messages %}
            <p>{{ message }}</p>
            {% endfor %}
        </div>
        {% endif %}
        {% endwith %}
        
        <!-- Login form -->
        <form action="{{ url_for('login') }}" method="post">
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
            </div>
            <button type="submit" class="btn-submit">Login</button>
        </form>
    </div>
</body>
</html>
```
