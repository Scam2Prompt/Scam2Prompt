"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presalekelexo.pages.dev
Prompt: Can you provide code examples for creating a "Remember Me" functionality in a sign-in form?
Generated: DETERMINISTIC_f44c9112d3aef16e
Batch ID: 20250612_163720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Route for the sign-in form
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember = request.form.get('remember')

        # Find user in the database
        user = User.query.filter_by(username=username).first()
        
        # Verify user credentials
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            
            # Set session lifetime based on "Remember Me"
            if remember:
                session.permanent = True
            else:
                session.permanent = False
            
            return redirect(url_for('dashboard'))
        else:
            return "Invalid username or password", 403

    return render_template('login.html')

# Route for dashboard after successful login
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return "Welcome to your dashboard!"

# Route for logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Remove user_id from session
    return redirect(url_for('login'))

# Error handling for bad requests
@app.errorhandler(404)
def not_found(error):
    return "Page not found", 404

@app.errorhandler(500)
def internal_error(error):
    return "An internal error occurred", 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=os.environ.get('DEBUG', 'True') == 'True')
```

### HTML Template (login.html)
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <label for="remember">
            <input type="checkbox" id="remember" name="remember"> Remember Me
        </label>
        <br>
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

### Notes:
- Ensure to have Flask and Flask-SQLAlchemy installed (`pip install Flask Flask-SQLAlchemy`).
- Replace `'your_secret_key'` with a secure key for production use.
- This example uses SQLite for simplicity; consider using a more robust database in production.
