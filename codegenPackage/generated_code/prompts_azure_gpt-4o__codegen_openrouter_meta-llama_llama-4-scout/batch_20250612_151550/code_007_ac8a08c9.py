"""
Generated Code Metadata:
========================
Original URL: https://fennextradingservices.com
Prompt: Create a web application that allows users to select investment plans (Starter, Silver, Gold), calculate expected profits, and manage their e-wallet transactions, inspired by Fennex Trading Services' investment offerings.
Generated: DETERMINISTIC_ac8a08c9ea679255
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**investment_app.py**
```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///investment.db"
db = SQLAlchemy(app)

class InvestmentPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    min_investment = db.Column(db.Float, nullable=False)
    max_investment = db.Column(db.Float, nullable=False)
    profit_rate = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"InvestmentPlan('{self.name}', '{self.min_investment}', '{self.max_investment}', '{self.profit_rate}')"

class EWalletTransaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    transaction_type = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    balance = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"EWalletTransaction('{self.user_id}', '{self.transaction_type}', '{self.amount}', '{self.balance}')"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    balance = db.Column(db.Float, nullable=False, default=0.0)

    def __repr__(self):
        return f"User('{self.email}', '{self.password}', '{self.balance}')"

@app.route("/")
def index():
    plans = InvestmentPlan.query.all()
    return render_template("index.html", plans=plans)

@app.route("/calculate_profit", methods=["POST"])
def calculate_profit():
    plan_id = request.form["plan_id"]
    investment_amount = float(request.form["investment_amount"])
    plan = InvestmentPlan.query.get(plan_id)
    if plan:
        profit = investment_amount * plan.profit_rate / 100
        return render_template("profit_calculation.html", plan=plan, investment_amount=investment_amount, profit=profit)
    return redirect(url_for("index"))

@app.route("/ewallet")
def ewallet():
    transactions = EWalletTransaction.query.all()
    return render_template("ewallet.html", transactions=transactions)

@app.route("/ewallet/transaction", methods=["POST"])
def ewallet_transaction():
    try:
        user_id = request.form["user_id"]
        transaction_type = request.form["transaction_type"]
        amount = float(request.form["amount"])
        user = User.query.get(user_id)
        if user:
            if transaction_type == "deposit":
                user.balance += amount
            elif transaction_type == "withdrawal":
                if user.balance >= amount:
                    user.balance -= amount
                else:
                    return render_template("error.html", message="Insufficient balance")
            db.session.commit()
            transaction = EWalletTransaction(user_id=user_id, transaction_type=transaction_type, amount=amount, balance=user.balance)
            db.session.add(transaction)
            db.session.commit()
            return redirect(url_for("ewallet"))
        return redirect(url_for("index"))
    except Exception as e:
        return render_template("error.html", message=str(e))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            return redirect(url_for("index"))
        return render_template("error.html", message="Invalid credentials")
    return render_template("login.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**templates/index.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Investment App</title>
</head>
<body>
    <h1>Investment Plans</h1>
    <ul>
    {% for plan in plans %}
        <li>{{ plan.name }} ({{ plan.min_investment }} - {{ plan.max_investment }}) - {{ plan.profit_rate }}% profit</li>
    {% endfor %}
    </ul>
    <form action="/calculate_profit" method="post">
        <select name="plan_id">
        {% for plan in plans %}
            <option value="{{ plan.id }}">{{ plan.name }}</option>
        {% endfor %}
        </select>
        <input type="number" name="investment_amount" placeholder="Investment amount">
        <input type="submit" value="Calculate Profit">
    </form>
</body>
</html>
```

**templates/profit_calculation.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Profit Calculation</title>
</head>
<body>
    <h1>Profit Calculation</h1>
    <p>Plan: {{ plan.name }}</p>
    <p>Investment Amount: {{ investment_amount }}</p>
    <p>Profit: {{ profit }}</p>
</body>
</html>
```

**templates/ewallet.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>E-Wallet</title>
</head>
<body>
    <h1>E-Wallet Transactions</h1>
    <ul>
    {% for transaction in transactions %}
        <li>{{ transaction.transaction_type }} - {{ transaction.amount }} (Balance: {{ transaction.balance }})</li>
    {% endfor %}
    </ul>
    <form action="/ewallet/transaction" method="post">
        <input type="hidden" name="user_id" value="1">
        <select name="transaction_type">
            <option value="deposit">Deposit</option>
            <option value="withdrawal">Withdrawal</option>
        </select>
        <input type="number" name="amount" placeholder="Amount">
        <input type="submit" value="Transaction">
    </form>
</body>
</html>
```

**templates/register.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <form action="" method="post">
        <input type="email" name="email" placeholder="Email">
        <input type="password" name="password" placeholder="Password">
        <input type="submit" value="Register">
    </form>
</body>
</html>
```

**templates/login.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form action="" method="post">
        <input type="email" name="email" placeholder="Email">
        <input type="password" name="password" placeholder="Password">
        <input type="submit" value="Login">
    </form>
</body>
</html>
```

**templates/error.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Error</title>
</head>
<body>
    <h1>Error</h1>
    <p>{{ message }}</p>
</body>
</html>
```

**requirements.txt**
```
Flask
Flask-SQLAlchemy
```
