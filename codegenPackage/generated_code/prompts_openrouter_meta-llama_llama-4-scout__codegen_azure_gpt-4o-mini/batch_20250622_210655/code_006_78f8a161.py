"""
Generated Code Metadata:
========================
Original URL: https://nuevaciudad.com.co
Prompt: Design a user interface for a property management system that allows owners and renters to access their accounts, make payments, and view property information, inspired by Inmobiliaria Nueva Ciudad's online services.
Generated: DETERMINISTIC_78f8a161603ca460
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///property_management.db'  # Database URI
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(10), nullable=False)  # 'owner' or 'renter'

# Define the Property model
class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(200), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

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
        role = request.form['role']
        
        # Error handling for existing username
        if User.query.filter_by(username=username).first():
            flash('Username already exists. Please choose another one.', 'danger')
            return redirect(url_for('register'))
        
        # Create a new user
        new_user = User(username=username, password=generate_password_hash(password), role=role)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        # Error handling for invalid credentials
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['role'] = user.role
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password. Please try again.', 'danger')
    
    return render_template('login.html')

# Route for user dashboard
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('You need to log in first.', 'warning')
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    properties = Property.query.filter_by(owner_id=user.id).all() if user.role == 'owner' else []
    
    return render_template('dashboard.html', user=user, properties=properties)

# Route for making payments (placeholder)
@app.route('/make_payment', methods=['POST'])
def make_payment():
    if 'user_id' not in session:
        flash('You need to log in first.', 'warning')
        return redirect(url_for('login'))
    
    # Payment processing logic would go here
    flash('Payment processed successfully!', 'success')
    return redirect(url_for('dashboard'))

# Route for viewing property information
@app.route('/properties')
def properties():
    all_properties = Property.query.all()
    return render_template('properties.html', properties=all_properties)

# Route for logging out
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('role', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Templates (for completeness)

**home.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Property Management System</title>
</head>
<body>
    <h1>Welcome to the Property Management System</h1>
    <a href="{{ url_for('register') }}">Register</a>
    <a href="{{ url_for('login') }}">Login</a>
</body>
</html>
```

**register.html**
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
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <select name="role" required>
            <option value="owner">Owner</option>
            <option value="renter">Renter</option>
        </select>
        <button type="submit">Register</button>
    </form>
</body>
</html>
```

**login.html**
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
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

**dashboard.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
</head>
<body>
    <h1>Welcome, {{ user.username }}</h1>
    <h2>Your Properties</h2>
    <ul>
        {% for property in properties %}
            <li>{{ property.address }}</li>
        {% else %}
            <li>No properties found.</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('make_payment') }}">Make Payment</a>
    <a href="{{ url_for('logout') }}">Logout</a>
</body>
</html>
```

**properties.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Properties</title>
</head>
<body>
    <h1>All Properties</h1>
    <ul>
        {% for property in properties %}
            <li>{{ property.address }}</li>
        {% else %}
            <li>No properties available.</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('dashboard') }}">Back to Dashboard</a>
</body>
</html>
```

### Note
- Ensure to install Flask and Flask-SQLAlchemy using pip before running the application.
- Replace `'your_secret_key'` with a secure random key for production use.
- This code is a basic structure and can be expanded with additional features such as payment processing, property management, and user roles.
