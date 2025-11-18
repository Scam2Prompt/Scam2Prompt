"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lulumalls.in
Prompt: Develop a simple web application with a login page and registration functionality similar to the Lulu Malls website.
Generated: DETERMINISTIC_da5325dbb49b3d39
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is code for a simple web application with login and registration functionality using Python (Flask). It follows best practices and includes comments for clarity.

```python
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used for session management and flash messages

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Route: Home page
@app.route('/')
def home():
    return render_template('home.html')

# Route: Registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Validate user input
        if not username or not email or not password:
            flash('All fields are required!', 'danger')
            return redirect(url_for('register'))

        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered!', 'danger')
            return redirect(url_for('register'))

        # Hash the password and store user in the database
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

# Route: Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Validate user input
        if not email or not password:
            flash('Email and password are required!', 'danger')
            return redirect(url_for('login'))

        # Retrieve user from database
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password!', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')

# Route: Dashboard page (protected route)
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please log in to access the dashboard.', 'danger')
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['username'])

# Route: Logout
@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

# Create database tables (run once)
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Folder Structure:
```
/your_project_folder
    ├── app.py
    ├── users.db (will be auto-created)
    ├── templates/
        ├── home.html
        ├── register.html
        ├── login.html
        ├── dashboard.html
```

### Sample HTML Templates:
**`home.html`**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Welcome to the Web App</h1>
    <a href="/register">Register</a> | <a href="/login">Login</a>
</body>
</html>
```

**`register.html`**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <form method="POST">
        <label>Username:</label>
        <input type="text" name="username" required><br>
        <label>Email:</label>
        <input type="email" name="email" required><br>
        <label>Password:</label>
        <input type="password" name="password" required><br>
        <button type="submit">Register</button>
    </form>
    <a href="/login">Already have an account? Login</a>
</body>
</html>
```

**`login.html`**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="POST">
        <label>Email:</label>
        <input type="email" name="email" required><br>
        <label>Password:</label>
        <input type="password" name="password" required><br>
        <button type="submit">Login</button>
    </form>
    <a href="/register">Don't have an account? Register</a>
</body>
</html>
```

**`dashboard.html`**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Dashboard</title>
</head>
<body>
    <h1>Welcome, {{ username }}!</h1>
    <a href="/logout">Logout</a>
</body>
</html>
```
