"""
Generated Code Metadata:
========================
Original URL: https://canatechinstitute.ca
Prompt: "Design a basic web application using agile methodology for a retail business to digitalize their transaction system."
Generated: DETERMINISTIC_71d5d4f49b7f6686
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Retail Transaction System**
==========================

**Backend (Python, Flask, SQLAlchemy)**
--------------------------------------

### Requirements

* Python 3.9+
* Flask 2.0+
* SQLAlchemy 1.4+
* Flask-SQLAlchemy 2.5+

### Code

```python
# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///retail.db"
db = SQLAlchemy(app)


class User(db.Model):
    """User model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Transaction(db.Model):
    """Transaction model"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __init__(self, user_id, amount):
        self.user_id = user_id
        self.amount = amount


@app.route("/register", methods=["POST"])
def register():
    """Register a new user"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request"}), 400

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({"error": "Username already exists"}), 400

        new_user = User(username, password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@app.route("/login", methods=["POST"])
def login():
    """Login a user"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request"}), 400

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400

        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            return jsonify({"error": "Invalid credentials"}), 401

        return jsonify({"message": "User logged in successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/transactions", methods=["POST"])
def create_transaction():
    """Create a new transaction"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request"}), 400

        user_id = data.get("user_id")
        amount = data.get("amount")

        if not user_id or not amount:
            return jsonify({"error": "User ID and amount are required"}), 400

        new_transaction = Transaction(user_id, amount)
        db.session.add(new_transaction)
        db.session.commit()

        return jsonify({"message": "Transaction created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@app.route("/transactions", methods=["GET"])
def get_transactions():
    """Get all transactions"""
    try:
        transactions = Transaction.query.all()
        output = []
        for transaction in transactions:
            transaction_data = {
                "id": transaction.id,
                "user_id": transaction.user_id,
                "amount": transaction.amount,
                "timestamp": transaction.timestamp
            }
            output.append(transaction_data)
        return jsonify({"transactions": output}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**Frontend (JavaScript, HTML, CSS)**
-----------------------------------

### index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Retail Transaction System</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Retail Transaction System</h1>
    <form id="register-form">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username"><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password"><br><br>
        <button type="submit">Register</button>
    </form>
    <form id="login-form">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username"><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password"><br><br>
        <button type="submit">Login</button>
    </form>
    <form id="transaction-form">
        <label for="user_id">User ID:</label>
        <input type="text" id="user_id" name="user_id"><br><br>
        <label for="amount">Amount:</label>
        <input type="number" id="amount" name="amount"><br><br>
        <button type="submit">Create Transaction</button>
    </form>
    <div id="transactions"></div>

    <script src="script.js"></script>
</body>
</html>
```

### styles.css

```css
body {
    font-family: Arial, sans-serif;
}

form {
    margin-bottom: 20px;
}

label {
    display: inline-block;
    width: 100px;
}

input[type="text"], input[type="password"], input[type="number"] {
    width: 200px;
    height: 20px;
    margin: 5px;
    padding: 5px;
    border: 1px solid #ccc;
}

button[type="submit"] {
    width: 100px;
    height: 30px;
    background-color: #4CAF50;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #3e8e41;
}

#transactions {
    margin-top: 20px;
}
```

### script.js

```javascript
const registerForm = document.getElementById("register-form");
const loginForm = document.getElementById("login-form");
const transactionForm = document.getElementById("transaction-form");
const transactionsDiv = document.getElementById("transactions");

registerForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    try {
        const response = await fetch("/register", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password }),
        });
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error(error);
    }
});

loginForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    try {
        const response = await fetch("/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password }),
        });
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error(error);
    }
});

transactionForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const userId = document.getElementById("user_id").value;
    const amount = document.getElementById("amount").value;
    try {
        const response = await fetch("/transactions", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ user_id: userId, amount }),
        });
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error(error);
    }
});

async function getTransactions() {
    try {
        const response = await fetch("/transactions");
        const data = await response.json();
        transactionsDiv.innerHTML = "";
        data.transactions.forEach((transaction) => {
            const transactionHTML = `
                <p>Transaction ID: ${transaction
