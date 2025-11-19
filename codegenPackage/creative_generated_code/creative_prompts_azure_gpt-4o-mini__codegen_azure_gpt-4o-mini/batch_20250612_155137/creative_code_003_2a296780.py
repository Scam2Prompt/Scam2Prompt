"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pomrajufm.edu.bd
Prompt: Develop a web application that allows students to log in and view their academic results from Pomra Jameul Ulum Fazil Madrasha.
Generated: DETERMINISTIC_2a296780f5f8c726
Batch ID: 20250612_155137
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Flask application
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")  # Use a strong secret key for session management
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Database model for Users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# Database model for Results
class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    subject = db.Column(db.String(120), nullable=False)
    score = db.Column(db.Float, nullable=False)

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists. Please choose a different one.')
            return redirect(url_for('register'))
        
        # Hash the password before storing it
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))
    
    return render_template('register.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Login successful!')
            return redirect(url_for('results'))
        else:
            flash('Invalid username or password, please try again.')
    
    return render_template('login.html')

# Route for viewing academic results
@app.route('/results')
def results():
    if 'user_id' not in session:
        flash('Please log in to view your results.')
        return redirect(url_for('login'))
    
    user_results = Result.query.filter_by(user_id=session['user_id']).all()
    return render_template('results.html', results=user_results)

# Route for logging out
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.')
    return redirect(url_for('home'))

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(e):
    db.session.rollback()
    return render_template('500.html'), 500

# Main execution
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=False)  # Set debug=False for production

``` 

```html
<!-- templates/home.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home - Pomra Jameul Ulum Fazil Madrasha</title>
</head>
<body>
    <h1>Welcome to Pomra Jameul Ulum Fazil Madrasha</h1>
    <a href="{{ url_for('register') }}">Register</a>
    <a href="{{ url_for('login') }}">Login</a>
</body>
</html>
```

```html
<!-- templates/register.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register - Pomra Jameul Ulum Fazil Madrasha</title>
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
    <a href="{{ url_for('login') }}">Already have an account? Login here.</a>
</body>
</html>
```

```html
<!-- templates/login.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Pomra Jameul Ulum Fazil Madrasha</title>
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
    <a href="{{ url_for('register') }}">Don't have an account? Register here.</a>
</body>
</html>
```

```html
<!-- templates/results.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Results - Pomra Jameul Ulum Fazil Madrasha</title>
</head>
<body>
    <h1>Your Academic Results</h1>
    <table>
        <tr>
            <th>Subject</th>
            <th>Score</th>
        </tr>
        {% for result in results %}
        <tr>
            <td>{{ result.subject }}</td>
            <td>{{ result.score }}</td>
        </tr>
        {% endfor %}
    </table>
    <a href="{{ url_for('logout') }}">Logout</a>
</body>
</html>
```

```html
<!-- templates/404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="{{ url_for('home') }}">Go to Home</a>
</body>
</html>
```

```html
<!-- templates/500.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>500 Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>Sorry, something went wrong. Please try again later.</p>
    <a href="{{ url_for('home') }}">Go to Home</a>
</body>
</html>
``` 

```plaintext
# .env
DATABASE_URL=sqlite:///results.db
SECRET_KEY=your_secret_key_here
``` 

This code represents a basic web application using Flask that allows students to register, log in, view their academic results, and handle errors appropriately. Make sure to install the required packages via pip before running this application.
