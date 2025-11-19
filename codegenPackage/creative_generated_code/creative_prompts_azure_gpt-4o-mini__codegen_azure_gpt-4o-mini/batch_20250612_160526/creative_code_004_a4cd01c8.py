"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalbit-investment.com
Prompt: Create a simple web application that allows users to register and choose an investment plan based on the options provided by Global Bit Investment.
Generated: DETERMINISTIC_a4cd01c8da9b7f04
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with your secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///investments.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# User model for storing user data
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    investment_plan = db.Column(db.String(50), nullable=False)

# Investment plans available
INVESTMENT_PLANS = ['Basic', 'Standard', 'Premium']

@app.route('/')
def home():
    return render_template('home.html', plans=INVESTMENT_PLANS)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        investment_plan = request.form['investment_plan']
        
        # Validate input data
        if not username or not password or investment_plan not in INVESTMENT_PLANS:
            flash('Invalid input. Please fill out all fields correctly.', 'danger')
            return redirect(url_for('register'))
        
        # Hash the password
        hashed_password = generate_password_hash(password, method='sha256')
        
        # Create a new user instance
        new_user = User(username=username, password=hashed_password, investment_plan=investment_plan)
        
        # Add the user to the database
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred: {str(e)}', 'danger')
            return redirect(url_for('register'))
        
    return render_template('register.html', plans=INVESTMENT_PLANS)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

if __name__ == '__main__':
    # Create the database tables if they do not exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### HTML Templates

**home.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Investment Home</title>
</head>
<body>
    <h1>Welcome to Global Bit Investment</h1>
    <h2>Select Your Investment Plan</h2>
    <ul>
        {% for plan in plans %}
            <li>{{ plan }}</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('register') }}">Register</a>
    <a href="{{ url_for('login') }}">Login</a>
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

**register.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" name="username" required>
        <label for="password">Password:</label>
        <input type="password" name="password" required>
        <label for="investment_plan">Investment Plan:</label>
        <select name="investment_plan" required>
            {% for plan in plans %}
                <option value="{{ plan }}">{{ plan }}</option>
            {% endfor %}
        </select>
        <button type="submit">Register</button>
    </form>
    <a href="{{ url_for('home') }}">Back to Home</a>
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

**login.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
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
    <a href="{{ url_for('home') }}">Back to Home</a>
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

### Instructions
- Ensure you have Flask and Flask-SQLAlchemy installed in your Python environment:
```bash
pip install Flask Flask-SQLAlchemy
```
- Replace `'your_secret_key'` with a secure random secret key.
- Run the application using `python <filename>.py`.
