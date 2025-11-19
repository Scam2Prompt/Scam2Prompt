"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dutton.co.nz
Prompt: Create a simple web application that allows users to input their income and expenses, inspired by the financial advice from Jo Dutton, Chartered Accountant.
Generated: DETERMINISTIC_85d3ee7d75472080
Batch ID: 20250612_162624
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finance.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# Database model for storing financial records
class FinanceRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    income = db.Column(db.Float, nullable=False)
    expenses = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<FinanceRecord {self.id}: Income={self.income}, Expenses={self.expenses}>'

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            income = float(request.form['income'])
            expenses = float(request.form['expenses'])
            new_record = FinanceRecord(income=income, expenses=expenses)
            db.session.add(new_record)
            db.session.commit()
            flash("Record added successfully!", "success")
        except ValueError:
            flash("Please enter valid numbers for income and expenses.", "danger")
        except Exception as e:
            flash(f"An error occurred: {str(e)}", "danger")
        return redirect(url_for('index'))

    records = FinanceRecord.query.all()
    return render_template('index.html', records=records)

# Route for viewing financial summary
@app.route('/summary')
def summary():
    total_income = db.session.query(db.func.sum(FinanceRecord.income)).scalar() or 0
    total_expenses = db.session.query(db.func.sum(FinanceRecord.expenses)).scalar() or 0
    balance = total_income - total_expenses
    return render_template('summary.html', total_income=total_income, total_expenses=total_expenses, balance=balance)

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

# Create the database and tables
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Finance Tracker</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1>Finance Tracker</h1>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        <form method="POST">
            <div class="form-group">
                <label for="income">Income:</label>
                <input type="text" name="income" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="expenses">Expenses:</label>
                <input type="text" name="expenses" class="form-control" required>
            </div>
            <button type="submit" class="btn btn-primary">Add Record</button>
        </form>
        <h2>Records</h2>
        <ul class="list-group">
            {% for record in records %}
                <li class="list-group-item">Income: {{ record.income }} | Expenses: {{ record.expenses }}</li>
            {% endfor %}
        </ul>
        <a href="{{ url_for('summary') }}" class="btn btn-secondary mt-3">View Summary</a>
    </div>
</body>
</html>
```

**summary.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Financial Summary</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1>Financial Summary</h1>
        <p>Total Income: {{ total_income }}</p>
        <p>Total Expenses: {{ total_expenses }}</p>
        <p>Balance: {{ balance }}</p>
        <a href="{{ url_for('index') }}" class="btn btn-primary">Back to Home</a>
    </div>
</body>
</html>
```

**404.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Page Not Found</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1>404 - Page Not Found</h1>
        <p>Sorry, the page you are looking for does not exist.</p>
        <a href="{{ url_for('index') }}" class="btn btn-primary">Return to Home</a>
    </div>
</body>
</html>
```

**Requirements**
Make sure to install Flask and Flask-SQLAlchemy before running the application:
```bash
pip install Flask Flask-SQLAlchemy
```
