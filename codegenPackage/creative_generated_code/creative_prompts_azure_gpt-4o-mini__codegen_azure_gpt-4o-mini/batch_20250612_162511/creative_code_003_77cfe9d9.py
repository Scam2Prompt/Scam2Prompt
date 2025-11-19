"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrurnbridge.xyz
Prompt: Explain how to handle automatic redirects in a web application and provide a code example.
Generated: DETERMINISTIC_77cfe9d9aad70504
Batch ID: 20250612_162511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, redirect, url_for, request, abort

app = Flask(__name__)

@app.route('/')
def home():
    """Serve the home page."""
    return "Welcome to the Home Page!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login. Redirects to dashboard if successful."""
    if request.method == 'POST':
        # Here, you would check the credentials (this is just a placeholder)
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == 'admin' and password == 'secret':
            # On successful login, redirect to the dashboard
            return redirect(url_for('dashboard'))
        else:
            # If login fails, show an error message (could be improved)
            return "Login Failed. Please try again.", 401

    # Render login form for GET requests
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/dashboard')
def dashboard():
    """Serve the dashboard page."""
    return "Welcome to the Dashboard!"

@app.route('/redirect-example')
def redirect_example():
    """Example route that redirects to the home page."""
    # This simulates a condition where a redirect is needed
    if request.args.get('redirect') == 'true':
        return redirect(url_for('home'))
    
    return "No redirect occurred."

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors and provide a user-friendly message."""
    return "Page not found. Please check the URL.", 404

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

This code provides a simple Flask web application with automatic redirects upon successful user login and an example route demonstrating redirection based on query parameters. It includes basic error handling for 404 errors and appropriate comments for clarity.
