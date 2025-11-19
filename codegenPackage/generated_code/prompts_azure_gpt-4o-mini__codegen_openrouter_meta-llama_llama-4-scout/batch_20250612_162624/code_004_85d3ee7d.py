"""
Generated Code Metadata:
========================
Original URL: https://dutton.co.nz
Prompt: Create a simple web application that allows users to input their income and expenses, inspired by the financial advice from Jo Dutton, Chartered Accountant.
Generated: DETERMINISTIC_85d3ee7d75472080
Batch ID: 20250612_162624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Financial Tracker Web Application**
=====================================

**app.py**
```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///financial_tracker.db"
db = SQLAlchemy(app)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f"Transaction('{self.type}', '{self.amount}', '{self.description}')"

@app.route("/")
def index():
    transactions = Transaction.query.all()
    income = sum(t.amount for t in transactions if t.type == "income")
    expenses = sum(t.amount for t in transactions if t.type == "expense")
    balance = income - expenses
    return render_template("index.html", transactions=transactions, income=income, expenses=expenses, balance=balance)

@app.route("/add_transaction", methods=["POST"])
def add_transaction():
    try:
        type = request.form["type"]
        amount = float(request.form["amount"])
        description = request.form.get("description", "")
        transaction = Transaction(type=type, amount=amount, description=description)
        db.session.add(transaction)
        db.session.commit()
        return redirect(url_for("index"))
    except Exception as e:
        return render_template("error.html", error=str(e))

@app.route("/delete_transaction/<int:transaction_id>")
def delete_transaction(transaction_id):
    try:
        transaction = Transaction.query.get(transaction_id)
        if transaction:
            db.session.delete(transaction)
            db.session.commit()
        return redirect(url_for("index"))
    except Exception as e:
        return render_template("error.html", error=str(e))

if __name__ == "__main__":
    app.run(debug=True)
```

**templates/index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Financial Tracker</title>
    <style>
        table {
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 10px;
        }
    </style>
</head>
<body>
    <h1>Financial Tracker</h1>
    <form action="{{ url_for('add_transaction') }}" method="post">
        <label for="type">Type:</label>
        <select id="type" name="type">
            <option value="income">Income</option>
            <option value="expense">Expense</option>
        </select><br><br>
        <label for="amount">Amount:</label>
        <input type="number" id="amount" name="amount" step="0.01"><br><br>
        <label for="description">Description:</label>
        <input type="text" id="description" name="description"><br><br>
        <input type="submit" value="Add Transaction">
    </form>
    <table>
        <tr>
            <th>Type</th>
            <th>Amount</th>
            <th>Description</th>
            <th>Actions</th>
        </tr>
        {% for transaction in transactions %}
        <tr>
            <td>{{ transaction.type }}</td>
            <td>{{ transaction.amount }}</td>
            <td>{{ transaction.description }}</td>
            <td><a href="{{ url_for('delete_transaction', transaction_id=transaction.id) }}">Delete</a></td>
        </tr>
        {% endfor %}
    </table>
    <p>Income: {{ income }}</p>
    <p>Expenses: {{ expenses }}</p>
    <p>Balance: {{ balance }}</p>
</body>
</html>
```

**templates/error.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
</head>
<body>
    <h1>Error</h1>
    <p>{{ error }}</p>
    <p><a href="{{ url_for('index') }}">Back to index</a></p>
</body>
</html>
```

**requirements.txt**
```
Flask
Flask-SQLAlchemy
```
