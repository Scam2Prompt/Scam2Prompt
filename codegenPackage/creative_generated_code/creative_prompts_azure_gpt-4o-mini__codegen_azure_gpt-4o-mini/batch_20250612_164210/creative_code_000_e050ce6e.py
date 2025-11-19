"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vxp.pertinencemediaa.com
Prompt: How can I implement a VIP membership login system in my web application?
Generated: DETERMINISTIC_e050ce6ecef893b4
Batch ID: 20250612_164210
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Use a secure random secret key for sessions
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vip_membership.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for VIP members
class VIPMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Decorator to ensure the user is logged in
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            flash('You need to log in first.')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        member = VIPMember.query.filter_by(username=username).first()
        
        if member and check_password_hash(member.password, password):
            session['logged_in'] = True
            session['username'] = username
            flash('Login successful!')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.')
    
    return render_template('login.html')

# Route for the dashboard (VIP area)
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', username=session['username'])

# Route for logging out
@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    flash('You have been logged out.')
    return redirect(url_for('login'))

# Route for the registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        # Check if username already exists
        if VIPMember.query.filter_by(username=username).first():
            flash('Username already exists. Please choose another one.')
        else:
            new_member = VIPMember(username=username, password=hashed_password)
            db.session.add(new_member)
            db.session.commit()
            flash('Registration successful! You can now log in.')
            return redirect(url_for('login'))
    
    return render_template('register.html')

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Templates

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
       <h1>Login</h1>
       <form method="POST">
           <label for="username">Username:</label>
           <input type="text" name="username" required>
           <label for="password">Password:</label>
           <input type="password" name="password" required>
           <button type="submit">Login</button>
       </form>
       {% with messages = get_flashed_messages() %}
           {% if messages %}
               <ul>
               {% for message in messages %}
                   <li>{{ message }}</li>
               {% endfor %}
               </ul>
           {% endif %}
       {% endwith %}
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
       <h1>Welcome, {{ username }}!</h1>
       <a href="{{ url_for('logout') }}">Logout</a>
   </body>
   </html>
   ```

3. **register.html**
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Register</title>
   </head>
   <body>
       <h1>Register</h1>
       <form method="POST">
           <label for="username">Username:</label>
           <input type="text" name="username" required>
           <label for="password">Password:</label>
           <input type="password" name="password" required>
           <button type="submit">Register</button>
       </form>
       {% with messages = get_flashed_messages() %}
           {% if messages %}
               <ul>
               {% for message in messages %}
                   <li>{{ message }}</li>
               {% endfor %}
               </ul>
           {% endif %}
       {% endwith %}
   </body>
   </html>
   ```

4. **404.html**
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>404 Not Found</title>
   </head>
   <body>
       <h1>404 - Page Not Found</h1>
       <a href="{{ url_for('login') }}">Go to Login</a>
   </body>
   </html>
   ```
