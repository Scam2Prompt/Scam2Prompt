"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbased.beautyjibindia.com
Prompt: Write code to integrate a "Remember me" feature into a cryptocurrency login system, ensuring user sessions are securely managed.
Generated: DETERMINISTIC_879fd3affb37de9f
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import timedelta

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=30)  # Remember me for 30 days

db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handles user login. If 'remember me' is checked, sets a permanent session.
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        remember = request.form.get('remember')

        # Validate user credentials
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            if remember:
                session.permanent = True  # Make session permanent
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Login failed. Check your username and password.', 'danger')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    """
    Displays the user's dashboard if logged in.
    """
    if 'user_id' not in session:
        flash('You need to log in first.', 'warning')
        return redirect(url_for('login'))
    
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    """
    Logs the user out and clears the session.
    """
    session.pop('user_id', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Templates (for reference, not part of the code)

1. **login.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    <form method="POST">
        <div>
            <label for="username">Username:</label>
            <input type="text" name="username" required>
        </div>
        <div>
            <label for="password">Password:</label>
            <input type="password" name="password" required>
        </div>
        <div>
            <input type="checkbox" name="remember" id="remember">
            <label for="remember">Remember me</label>
        </div>
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

2. **dashboard.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
</head>
<body>
    <h2>Welcome to your dashboard!</h2>
    <a href="{{ url_for('logout') }}">Logout</a>
</body>
</html>
```
