"""
Generated Code Metadata:
========================
Original URL: https://admgdv.com
Prompt: Create a web interface for registering and checking insurance funds, inspired by the services offered on admgdv.com.
Generated: DETERMINISTIC_f6c52ddbc494c9a8
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Insurance Fund Registration and Checking Web Interface**

### Dependencies

* Python 3.9+
* Flask 2.0+
* Flask-SQLAlchemy 2.5+
* Werkzeug 2.0+

### Code

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///insurance_funds.db"
app.config["SECRET_KEY"] = "secret_key_here"

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class InsuranceFund(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    fund_name = db.Column(db.String(128), nullable=False)
    balance = db.Column(db.Float, nullable=False, default=0.0)

    def __init__(self, user_id, fund_name, balance=0.0):
        self.user_id = user_id
        self.fund_name = fund_name
        self.balance = balance


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user:
            return render_template("register.html", error="Username already exists")
        new_user = User(username, password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            return render_template("login.html", error="Invalid username or password")
        return redirect(url_for("dashboard", user_id=user.id))
    return render_template("login.html")


@app.route("/dashboard/<int:user_id>")
def dashboard(user_id):
    user = User.query.get(user_id)
    if not user:
        return redirect(url_for("login"))
    funds = InsuranceFund.query.filter_by(user_id=user_id).all()
    return render_template("dashboard.html", user=user, funds=funds)


@app.route("/create_fund/<int:user_id>", methods=["GET", "POST"])
def create_fund(user_id):
    if request.method == "POST":
        fund_name = request.form["fund_name"]
        new_fund = InsuranceFund(user_id, fund_name)
        db.session.add(new_fund)
        db.session.commit()
        return redirect(url_for("dashboard", user_id=user_id))
    return render_template("create_fund.html", user_id=user_id)


@app.route("/deposit/<int:fund_id>", methods=["GET", "POST"])
def deposit(fund_id):
    fund = InsuranceFund.query.get(fund_id)
    if not fund:
        return redirect(url_for("dashboard", user_id=fund.user_id))
    if request.method == "POST":
        amount = float(request.form["amount"])
        fund.balance += amount
        db.session.commit()
        return redirect(url_for("dashboard", user_id=fund.user_id))
    return render_template("deposit.html", fund=fund)


@app.route("/withdraw/<int:fund_id>", methods=["GET", "POST"])
def withdraw(fund_id):
    fund = InsuranceFund.query.get(fund_id)
    if not fund:
        return redirect(url_for("dashboard", user_id=fund.user_id))
    if request.method == "POST":
        amount = float(request.form["amount"])
        if amount > fund.balance:
            return render_template("withdraw.html", fund=fund, error="Insufficient balance")
        fund.balance -= amount
        db.session.commit()
        return redirect(url_for("dashboard", user_id=fund.user_id))
    return render_template("withdraw.html", fund=fund)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Insurance Fund Registration and Checking</title>
  </head>
  <body>
    <h1>Insurance Fund Registration and Checking</h1>
    <p>
      <a href="{{ url_for('register') }}">Register</a> |
      <a href="{{ url_for('login') }}">Login</a>
    </p>
  </body>
</html>
```

```html
<!-- templates/register.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Register</title>
  </head>
  <body>
    <h1>Register</h1>
    <form method="post">
      <label for="username">Username:</label>
      <input type="text" id="username" name="username"><br><br>
      <label for="password">Password:</label>
      <input type="password" id="password" name="password"><br><br>
      <input type="submit" value="Register">
    </form>
    {% if error %}
      <p style="color: red">{{ error }}</p>
    {% endif %}
  </body>
</html>
```

```html
<!-- templates/login.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Login</title>
  </head>
  <body>
    <h1>Login</h1>
    <form method="post">
      <label for="username">Username:</label>
      <input type="text" id="username" name="username"><br><br>
      <label for="password">Password:</label>
      <input type="password" id="password" name="password"><br><br>
      <input type="submit" value="Login">
    </form>
    {% if error %}
      <p style="color: red">{{ error }}</p>
    {% endif %}
  </body>
</html>
```

```html
<!-- templates/dashboard.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Dashboard</title>
  </head>
  <body>
    <h1>Dashboard</h1>
    <h2>Welcome, {{ user.username }}!</h2>
    <h3>Funds:</h3>
    <ul>
    {% for fund in funds %}
      <li>{{ fund.fund_name }} (Balance: {{ fund.balance }})
        <a href="{{ url_for('deposit', fund_id=fund.id) }}">Deposit</a> |
        <a href="{{ url_for('withdraw', fund_id=fund.id) }}">Withdraw</a>
      </li>
    {% endfor %}
    </ul>
    <p>
      <a href="{{ url_for('create_fund', user_id=user.id) }}">Create Fund</a>
    </p>
  </body>
</html>
```

```html
<!-- templates/create_fund.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Create Fund</title>
  </head>
  <body>
    <h1>Create Fund</h1>
    <form method="post">
      <label for="fund_name">Fund Name:</label>
      <input type="text" id="fund_name" name="fund_name"><br><br>
      <input type="submit" value="Create Fund">
    </form>
  </body>
</html>
```

```html
<!-- templates/deposit.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Deposit</title>
  </head>
  <body>
    <h1>Deposit</h1>
    <h2>Fund: {{ fund.fund_name }}</h2>
    <form method="post">
      <label for="amount">Amount:</label>
      <input type="number" id="amount" name="amount"><br><br>
      <input type="submit" value="Deposit">
    </form>
  </body>
</html>
```

```html
<!-- templates/withdraw.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Withdraw</title>
  </head>
  <body>
    <h1>Withdraw</h1>
    <h2>Fund: {{ fund.fund_name }}</h2>
    <form method="post">
      <label for="amount">Amount:</label>
      <input type="number" id="amount" name="amount"><br><br>
      <input type="submit" value="Withdraw">
    </form>
    {% if error %}
      <p style="color: red">{{ error }}</p>
    {% endif %}
  </body>
</html>
```
