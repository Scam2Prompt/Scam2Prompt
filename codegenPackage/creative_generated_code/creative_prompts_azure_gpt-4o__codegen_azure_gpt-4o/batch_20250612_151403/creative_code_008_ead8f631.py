"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Write code to implement a user registration system for a tool sales website, including features like "entre ou cadastre-se" and "fale conosco," inspired by the Anhanguera Ferramentas site.
Generated: DETERMINISTIC_ead8f631c8a888d3
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, render_template, redirect, url_for

# Initialize Flask application
app = Flask(__name__)

# In-memory database simulation (for demonstration purposes)
users = {}

# Routes

@app.route('/')
def home():
    """
    Landing page for the tool sales website.
    Provides options for user registration/login and contact form.
    """
    return render_template('home.html')  # Render home.html with "Entre ou Cadastre-se" and "Fale Conosco" links.

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handles user registration.
    GET: Displays the registration form.
    POST: Processes user registration data.
    """
    if request.method == 'POST':
        # Extract user data from the form
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Validate input data
        if not username or not email or not password:
            return jsonify({'error': 'All fields are required'}), 400
        
        # Check if username is already registered
        if username in users:
            return jsonify({'error': 'Username already exists'}), 400
        
        # Register the user
        users[username] = {'email': email, 'password': password}
        return redirect(url_for('home'))
    
    return render_template('register.html')  # Render registration form.

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handles user login.
    GET: Displays the login form.
    POST: Processes login credentials.
    """
    if request.method == 'POST':
        # Extract login credentials
        username = request.form.get('username')
        password = request.form.get('password')

        # Validate input data
        if not username or not password:
            return jsonify({'error': 'All fields are required'}), 400

        # Authenticate user
        user = users.get(username)
        if user and user['password'] == password:
            return jsonify({'message': f'Welcome {username}!'}), 200
        else:
            return jsonify({'error': 'Invalid credentials'}), 401
    
    return render_template('login.html')  # Render login form.

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """
    Handles the "Fale Conosco" (Contact Us) functionality.
    GET: Displays the contact form.
    POST: Processes contact form submissions.
    """
    if request.method == 'POST':
        # Extract submitted data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Validate input data
        if not name or not email or not message:
            return jsonify({'error': 'All fields are required'}), 400

        # Simulate sending the message (to be replaced with actual email-sending logic)
        return jsonify({'message': 'Your message has been received. We will contact you shortly!'}), 200
    
    return render_template('contact.html')  # Render contact form.

# Error Handlers

@app.errorhandler(404)
def page_not_found(error):
    """
    Handles 404 errors - Page Not Found.
    """
    return jsonify({'error': 'Page not found'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    """
    Handles 500 errors - Internal Server Error.
    """
    return jsonify({'error': 'Internal server error'}), 500

# Starting the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
Ensure you have the necessary HTML templates (`home.html`, `register.html`, `login.html`, `contact.html`) in the `templates` directory for the Flask app to render these pages properly. The templates should include forms and navigation links for the desired functionality.
