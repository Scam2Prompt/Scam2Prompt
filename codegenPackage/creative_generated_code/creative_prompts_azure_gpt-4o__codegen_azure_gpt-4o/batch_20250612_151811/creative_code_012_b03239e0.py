"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capitalhandelssystem.com
Prompt: Create a dashboard interface for tracking cryptocurrency investments, withdrawals, and referral bonuses, inspired by the member area features described on Capitalhandelssystem.
Generated: DETERMINISTIC_b03239e0d050ac00
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for a cryptocurrency investment tracking dashboard in Python using the Flask framework. The code covers user authentication, tracking of investments, withdrawals, and referral bonuses, and includes error handling and proper documentation.

```python
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

# Initialize Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crypto_dashboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    referral_bonus = db.Column(db.Float, default=0.0)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    transaction_type = db.Column(db.String(50), nullable=False)  # 'investment' or 'withdrawal'
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

# Create database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Home route
@app.route('/')
def home():
    if 'user_id' in session:
        user = User.query.filter_by(id=session['user_id']).first()
        transactions = Transaction.query.filter_by(user_id=user.id).all()
        return render_template('dashboard.html', user=user, transactions=transactions)
    return redirect(url_for('login'))

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if user already exists
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            flash('Username or email already exists!', 'error')
            return redirect(url_for('register'))

        # Create user
        new_user = User(
            username=username,
            email=email,
            password=generate_password_hash(password)
        )
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Authenticate user
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        flash('Invalid username or password!', 'error')
    return render_template('login.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

# Add transaction route
@app.route('/transaction', methods=['POST'])
def add_transaction():
    if 'user_id' not in session:
        flash('Please log in to perform this action.', 'error')
        return redirect(url_for('login'))

    user = User.query.filter_by(id=session['user_id']).first()
    transaction_type = request.form['transaction_type']
    amount = float(request.form['amount'])

    if transaction_type not in ['investment', 'withdrawal']:
        flash('Invalid transaction type.', 'error')
        return redirect(url_for('home'))

    if transaction_type == 'withdrawal' and amount > sum(t.amount for t in Transaction.query.filter_by(user_id=user.id, transaction_type='investment').all()):
        flash('Insufficient funds for withdrawal.', 'error')
        return redirect(url_for('home'))

    transaction = Transaction(user_id=user.id, transaction_type=transaction_type, amount=amount)
    db.session.add(transaction)
    db.session.commit()
    flash('Transaction recorded successfully.', 'success')
    return redirect(url_for('home'))

# Referral bonus route
@app.route('/referral', methods=['POST'])
def add_referral_bonus():
    if 'user_id' not in session:
        flash('Please log in to perform this action.', 'error')
        return redirect(url_for('login'))

    user = User.query.filter_by(id=session['user_id']).first()
    referral_bonus = float(request.form['referral_bonus'])

    user.referral_bonus += referral_bonus
    db.session.commit()
    flash('Referral bonus added successfully.', 'success')
    return redirect(url_for('home'))

# Error handling
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

# Run application
if __name__ == '__main__':
    app.run(debug=True)
```

### Templates
Below are the HTML templates you'll need to save in a `templates` directory.

#### `login.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Login</button>
    </form>
    <a href="/register">Register</a>
</body>
</html>
```

#### `register.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="email" name="email" placeholder="Email" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Register</button>
    </form>
    <a href="/login">Login</a>
</body>
</html>
```

#### `dashboard.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Dashboard</title>
</head>
<body>
    <h1>Welcome, {{ user.username }}</h1>
    <h2>Your Referral Bonus: {{ user.referral_bonus }}</h2>
    <h3>Transactions:</h3>
    <ul>
        {% for transaction in transactions %}
        <li>{{ transaction.transaction_type }} - {{ transaction.amount }} - {{ transaction.date }}</li>
        {% endfor %}
    </ul>
    <form method="POST" action="/transaction">
        <h3>Add Transaction:</h3>
        <select name="transaction_type">
            <option value="investment">Investment</option>
            <option value="withdrawal">Withdrawal</option>
        </select>
        <input type="number" name="amount" step="0.01" placeholder="Amount" required>
        <button type="submit">Add</button>
    </form>
    <form method="POST" action="/referral">
        <h3>Add Referral Bonus:</h3>
        <input type="number" name="referral_bonus" step="0.01" placeholder="Bonus Amount" required>
        <button type="submit">Add</button>
    </form>
    <a href="/logout">Logout</a>
</body>
</html>
```

#### `404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>404 Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="/">Go Back to Dashboard</a>
</body>
</html>
```

#### `500.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>500 Internal Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <a href="/">Go Back to Dashboard</a>
</body>
</html>
```
