"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalarbitrageinvest.com
Prompt: Generate a code snippet that demonstrates how to handle user authentication for Global Arbitrage Investments using cookies.
Generated: DETERMINISTIC_fe1a87b2ff7a7807
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, redirect, url_for, make_response, session, render_template
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key
app.config['SESSION_COOKIE_NAME'] = 'global_arbitrage_session'

# Simulated database for users; in production, use a real database
users_db = {
    "user@example.com": generate_password_hash("password123")
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handles user login."""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user_password_hash = users_db.get(email)

        # Validate user credentials
        if user_password_hash and check_password_hash(user_password_hash, password):
            # Store user email in session
            session['user_email'] = email
            response = make_response(redirect(url_for('dashboard')))
            response.set_cookie('user_email', email)  # Set cookie for user
            return response
        else:
            # Flash an error message or handle it accordingly
            return "Invalid credentials", 401
    
    # Render login page for GET request
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Handles user logout."""
    session.pop('user_email', None)  # Remove user from session
    response = make_response(redirect(url_for('login')))
    response.delete_cookie('user_email')  # Delete user cookie
    return response

@app.route('/dashboard')
def dashboard():
    """Protected dashboard route."""
    if 'user_email' not in session:
        return redirect(url_for('login'))  # Redirect to login if not authenticated
    return f"Welcome to your dashboard, {session['user_email']}!"

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

**Notes:**
- Ensure to install Flask and Werkzeug before running the code.
- Adjust the `secret_key` to a secure random value for production.
- In a real application, replace the simulated user database with a proper database solution and secure password management.
