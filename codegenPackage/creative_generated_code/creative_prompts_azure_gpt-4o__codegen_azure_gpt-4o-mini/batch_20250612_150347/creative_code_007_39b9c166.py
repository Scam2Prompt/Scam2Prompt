"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://conext.info
Prompt: Create a step-by-step guide to connect MapOS with an external authentication system and handle incorrect login attempts gracefully.
Generated: DETERMINISTIC_39b9c166e4dd65cd
Batch ID: 20250612_150347
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://external-auth-service.com/api/auth": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from flask import Flask, request, jsonify, session, redirect, url_for, render_template
from werkzeug.security import generate_password_hash, check_password_hash
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure random key in production

# Simulated database for users (In production, use a proper database)
users_db = {
    "user@example.com": generate_password_hash("securepassword"),  # Storing hashed password
}

# External authentication service URL
AUTH_SERVICE_URL = "https://external-auth-service.com/api/auth"

def authenticate_with_external_service(username, password):
    """Authenticate user with an external authentication service."""
    try:
        response = requests.post(AUTH_SERVICE_URL, json={"username": username, "password": password})
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        return response.json()  # Assuming the service returns user data on success
    except requests.RequestException as e:
        logging.error(f"Error connecting to external auth service: {e}")
        return None

@app.route("/login", methods=["GET", "POST"])
def login():
    """Handle user login."""
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Attempt to authenticate with the external service
        user_data = authenticate_with_external_service(email, password)

        if user_data:
            # Successful authentication
            session['user'] = user_data  # Store user info in session
            return redirect(url_for("dashboard"))
        else:
            # Handle failed login attempt
            logging.warning(f"Failed login attempt for user: {email}")
            return jsonify({"error": "Invalid credentials. Please try again."}), 401

    # Render the login form if GET request
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    """Dashboard view for logged-in users."""
    if 'user' not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html", user=session['user'])

@app.route("/logout")
def logout():
    """Log the user out and clear session."""
    session.pop('user', None)  # Remove user info from session
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)  # Set to False in production
```

**Note**: Ensure you have Flask and Requests installed in your Python environment. You can install them via pip:

```bash
pip install Flask requests
```
