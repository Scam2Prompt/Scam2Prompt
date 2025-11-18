"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://admgdv.com
Prompt: Create a web interface for registering and checking insurance funds, inspired by the services offered on admgdv.com.
Generated: DETERMINISTIC_f6c52ddbc494c9a8
Batch ID: 20250612_153710
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

Here’s a production-ready Python Flask application with a simple web interface for registering and checking insurance funds. Note that this example uses SQLite as a database for simplicity:

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key for production

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///insurance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Model for Insurance Funds
class InsuranceFund(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each entry
    name = db.Column(db.String(100), nullable=False)  # Name of the individual/entity
    fund_amount = db.Column(db.Float, nullable=False)  # Amount of insurance funds

    def __repr__(self):
        return f"<InsuranceFund {self.name} - ${self.fund_amount}>"

# Route for the homepage
@app.route('/')
def index():
    try:
        insurance_funds = InsuranceFund.query.all()  # Fetch all insurance funds from the database
        return render_template('index.html', insurance_funds=insurance_funds)
    except Exception as e:
        flash(f"Error loading funds: {str(e)}", 'danger')
        return render_template('index.html', insurance_funds=[])

# Route for registering a new insurance fund
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            # Collect form data
            name = request.form['name']
            fund_amount = request.form['fund_amount']

            # Validate inputs
            if not name or not fund_amount or float(fund_amount) <= 0:
                flash("Invalid input. Please provide a valid name and fund amount.", 'warning')
                return redirect(url_for('register'))

            # Create a new InsuranceFund object and add to the database
            new_fund = InsuranceFund(name=name, fund_amount=float(fund_amount))
            db.session.add(new_fund)
            db.session.commit()

            flash("Insurance fund registered successfully!", 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f"Error registering fund: {str(e)}", 'danger')
            return redirect(url_for('register'))

    return render_template('register.html')

# Route for checking specific insurance fund
@app.route('/check', methods=['GET', 'POST'])
def check():
    if request.method == 'POST':
        try:
            name = request.form['name']

            if not name:
                flash("Please enter a name to check.", 'warning')
                return redirect(url_for('check'))

            fund = InsuranceFund.query.filter_by(name=name).first()

            if fund:
                flash(f"Insurance Fund for {fund.name}: ${fund.fund_amount}", 'info')
            else:
                flash(f"No record found for '{name}'.", 'warning')

            return redirect(url_for('check'))
        except Exception as e:
            flash(f"Error checking fund: {str(e)}", 'danger')
            return redirect(url_for('check'))

    return render_template('check.html')

# Error handling for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Create and initialize the database
@app.before_first_request
def setup():
    db.create_all()  # Create database tables if they don't exist

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

### Templates (`templates` folder)
Below are the HTML templates for the application:

#### `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Insurance Funds</title>
</head>
<body>
    <h1>Insurance Funds</h1>
    <a href="/register">Register a New Fund</a>
    <a href="/check">Check Insurance Fund</a>
    <ul>
        {% for fund in insurance_funds %}
        <li>{{ fund.name }}: ${{ fund.fund_amount }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### `register.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register Fund</title>
</head>
<body>
    <h1>Register a New Insurance Fund</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="fund_amount">Fund Amount:</label>
        <input type="number" id="fund_amount" name="fund_amount" step="0.01" required>
        <br>
        <button type="submit">Register</button>
    </form>
    <a href="/">Back to Home</a>
</body>
</html>
```

#### `check.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Check Fund</title>
</head>
<body>
    <h1>Check Insurance Fund</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <button type="submit">Check</button>
    </form>
    <a href="/">Back to Home</a>
</body>
</html>
```

#### `404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="/">Go to Home</a>
</body>
</html>
```

### Setup Instructions
1. Install dependencies:
   ```bash
   pip install flask flask_sqlalchemy
   ```
2. Run the application:
   ```bash
   python app.py
   ```
3. Access the web interface at `http://127.0.0.1:5000`.

Make sure to replace `app.secret_key` with a secure key for production environments. Also, consider using a more robust database (e.g., PostgreSQL) for large-scale usage in production systems.
