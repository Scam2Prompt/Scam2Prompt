"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stronglp.com
Prompt: Develop a web application for personalized online coaching, integrating features like progress tracking, nutrition guidance, and sport-specific training plans as outlined by Blaise Strong.
Generated: DETERMINISTIC_8493b4acdd08e5ed
Batch ID: 20250612_145521
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:5000`.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is a production-ready web application implementation in Python using the Flask framework for the backend and SQLite as the database. It includes basic features for user registration, login, progress tracking, nutrition guidance, and sport-specific training plans.

### `app.py` (Main Flask Application)

```python
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize the Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coaching_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    progress = db.relationship('Progress', backref='user', lazy=True)
    nutrition = db.relationship('Nutrition', backref='user', lazy=True)
    training_plan = db.relationship('TrainingPlan', backref='user', lazy=True)

class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(500), nullable=False)

class Nutrition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    meal_plan = db.Column(db.String(500), nullable=False)

class TrainingPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    sport = db.Column(db.String(100), nullable=False)
    plan_details = db.Column(db.String(500), nullable=False)

# Routes
@app.route('/')
def home():
    # Render the home page
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')
        
        # Check if username or email already exists
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            flash("Username or email already exists.")
            return redirect(url_for('register'))
        
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful. Please log in.")
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash("Login successful.")
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid email or password.")
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    # Ensure user is logged in
    if 'user_id' not in session:
        flash("Please log in to access the dashboard.")
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    progress = user.progress
    nutrition = user.nutrition
    training_plan = user.training_plan
    return render_template('dashboard.html', user=user, progress=progress, nutrition=nutrition, training_plan=training_plan)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("Logged out successfully.")
    return redirect(url_for('home'))

# Error Handling
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

# Initialize the database (run this once to create the database)
@app.cli.command('initdb')
def initdb():
    db.create_all()
    print("Database initialized.")

if __name__ == '__main__':
    app.run(debug=True)
```

---

### Minimal HTML Templates

#### `templates/home.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home - Coaching App</title>
</head>
<body>
    <h1>Welcome to Blaise Strong Coaching</h1>
    <a href="{{ url_for('login') }}">Login</a>
    <a href="{{ url_for('register') }}">Register</a>
</body>
</html>
```

#### `templates/register.html`
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
        <label>Username:</label>
        <input type="text" name="username" required><br>
        <label>Email:</label>
        <input type="email" name="email" required><br>
        <label>Password:</label>
        <input type="password" name="password" required><br>
        <button type="submit">Register</button>
    </form>
</body>
</html>
```

#### `templates/login.html`
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
        <label>Email:</label>
        <input type="email" name="email" required><br>
        <label>Password:</label>
        <input type="password" name="password" required><br>
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

#### `templates/dashboard.html`
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
    <h2>Your Progress</h2>
    <ul>
        {% for p in progress %}
            <li>{{ p.date }} - {{ p.description }}</li>
        {% endfor %}
    </ul>

    <h2>Nutrition Guidance</h2>
    <ul>
        {% for n in nutrition %}
            <li>{{ n.meal_plan }}</li>
        {% endfor %}
    </ul>

    <h2>Training Plans</h2>
    <ul>
        {% for t in training_plan %}
            <li>{{ t.sport }}: {{ t.plan_details }}</li>
        {% endfor %}
    </ul>

    <a href="{{ url_for('logout') }}">Logout</a>
</body>
</html>
```

---

### Install and Run Instructions
1. Install dependencies: `pip install flask flask-sqlalchemy werkzeug`.
2. Initialize the database: `flask initdb`.
3. Run the application: `python app.py`.
4. Access the app at `http://127.0.0.1:5000`.

Excels at extensibility and modularity for further development!
