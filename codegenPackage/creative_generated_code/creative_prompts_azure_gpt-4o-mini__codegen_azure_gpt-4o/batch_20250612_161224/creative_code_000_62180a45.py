"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zushi.shop
Prompt: How can I implement a password-protected access feature for an online store like ZUSHI WAVE SHOP?
Generated: DETERMINISTIC_62180a4579635266
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'super_secret_key'  # Change this to an environment variable for production

# Store hashed password securely (example for demo purposes)
STORED_PASSWORD_HASH = generate_password_hash("securepassword123")

@app.route('/')
def home():
    """
    Home page route. Redirects to the login page if not authenticated.
    """
    if 'user_authenticated' in session and session['user_authenticated']:
        return render_template('store.html')  # Render store page if authenticated
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login route to authenticate user with a password.
    """
    if request.method == 'POST':
        password = request.form.get('password', '')
        
        # Validate password
        if check_password_hash(STORED_PASSWORD_HASH, password):
            session['user_authenticated'] = True
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error="Invalid password. Please try again.")
    
    # Render login page for GET requests
    return render_template('login.html')

@app.route('/logout')
def logout():
    """
    Logout route to clear authentication state.
    """
    session.pop('user_authenticated', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Notes:
1. HTML templates such as `login.html` and `store.html` should be created in the `templates` folder for rendering.
2. Replace `super_secret_key` with a secure environment variable in production.
3. `STORED_PASSWORD_HASH` should be stored in a secure database for real-world applications.
4. Enable HTTPS for secure password transmission.
