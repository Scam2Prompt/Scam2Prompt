"""
Generated Code Metadata:
========================
Original URL: https://financeimpactpro.com
Prompt: Create a dashboard interface using Python and Flask to display account balances, transaction history, and profit calculations for users of Finance Impact Pro.
Generated: DETERMINISTIC_cb151aa6fe7d1b38
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finance_impact_pro.db'
app.config['SECRET_KEY'] = 'secret_key_here'
db = SQLAlchemy(app)


# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    accounts = db.relationship('Account', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.username}')"

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    balance = db.Column(db.Float, nullable=False, default=0.0)
    transactions = db.relationship('Transaction', backref='account', lazy=True)

    def __repr__(self):
        return f"Account('{self.id}', '{self.balance}')"


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    amount = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"Transaction('{self.id}', '{self.amount}', '{self.type}')"


# Routes
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            return redirect(url_for('dashboard'))
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/dashboard')
def dashboard():
    user = User.query.first()
    accounts = user.accounts
    return render_template('dashboard.html', accounts=accounts)


@app.route('/account/<int:account_id>')
def account(account_id):
    account = Account.query.get_or_404(account_id)
    transactions = account.transactions
    return render_template('account.html', account=account, transactions=transactions)


@app.route('/calculate_profit/<int:account_id>')
def calculate_profit(account_id):
    account = Account.query.get_or_404(account_id)
    transactions = account.transactions
    profit = sum(t.amount if t.type == 'deposit' else -t.amount for t in transactions)
    return render_template('profit.html', profit=profit)


# Error handlers
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/base.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Finance Impact Pro</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <nav>
        <ul>
            <li><a href="{{ url_for('index') }}">Home</a></li>
            <li><a href="{{ url_for('login') }}">Login</a></li>
            <li><a href="{{ url_for('register') }}">Register</a></li>
        </ul>
    </nav>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

```html
<!-- templates/index.html -->

{% extends 'base.html' %}

{% block content %}
    <h1>Welcome to Finance Impact Pro</h1>
{% endblock %}
```

```html
<!-- templates/login.html -->

{% extends 'base.html' %}

{% block content %}
    <h1>Login</h1>
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username"><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
{% endblock %}
```

```html
<!-- templates/register.html -->

{% extends 'base.html' %}

{% block content %}
    <h1>Register</h1>
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username"><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password"><br><br>
        <input type="submit" value="Register">
    </form>
{% endblock %}
```

```html
<!-- templates/dashboard.html -->

{% extends 'base.html' %}

{% block content %}
    <h1>Dashboard</h1>
    <h2>Accounts:</h2>
    <ul>
    {% for account in accounts %}
        <li>
            <a href="{{ url_for('account', account_id=account.id) }}">{{ account.id }} ({{ account.balance }})</a>
        </li>
    {% endfor %}
    </ul>
{% endblock %}
```

```html
<!-- templates/account.html -->

{% extends 'base.html' %}

{% block content %}
    <h1>Account {{ account.id }}</h1>
    <h2>Balance: {{ account.balance }}</h2>
    <h2>Transactions:</h2>
    <ul>
    {% for transaction in transactions %}
        <li>{{ transaction.date }} - {{ transaction.amount }} ({{ transaction.type }})</li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('calculate_profit', account_id=account.id) }}">Calculate Profit</a></p>
{% endblock %}
```

```html
<!-- templates/profit.html -->

{% extends 'base.html' %}

{% block content %}
    <h1>Profit Calculation</h1>
    <p>Profit: {{ profit }}</p>
{% endblock %}
```

```css
/* static/style.css */

body {
    font-family: Arial, sans-serif;
}

nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: space-between;
}

nav li {
    margin-right: 20px;
}

nav a {
    text-decoration: none;
    color: #337ab7;
}

main {
    max-width: 800px;
    margin: 40px auto;
    padding: 20px;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
```
