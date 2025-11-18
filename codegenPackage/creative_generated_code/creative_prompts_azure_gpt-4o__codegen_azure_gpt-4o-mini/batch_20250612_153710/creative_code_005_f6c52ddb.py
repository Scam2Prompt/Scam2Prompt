"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://admgdv.com
Prompt: Create a web interface for registering and checking insurance funds, inspired by the services offered on admgdv.com.
Generated: DETERMINISTIC_f6c52ddbc494c9a8
Batch ID: 20250612_153710
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
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///insurance_funds.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Change this to a random secret key in production

# Initialize the database
db = SQLAlchemy(app)

# Define the InsuranceFund model
class InsuranceFund(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<InsuranceFund {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def index():
    funds = InsuranceFund.query.all()  # Fetch all insurance funds
    return render_template('index.html', funds=funds)

# Route for registering a new insurance fund
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            fund_name = request.form['name']
            fund_amount = float(request.form['amount'])
            new_fund = InsuranceFund(name=fund_name, amount=fund_amount)
            db.session.add(new_fund)
            db.session.commit()
            flash('Insurance fund registered successfully!', 'success')
        except ValueError:
            flash('Invalid amount entered. Please enter a numeric value.', 'error')
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash(f'An error occurred: {str(e)}', 'error')
        return redirect(url_for('index'))

    return render_template('register.html')

# Route for checking insurance funds
@app.route('/check', methods=['GET'])
def check():
    funds = InsuranceFund.query.all()
    return render_template('check.html', funds=funds)

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

**HTML Templates:**

1. **index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Insurance Fund Management</title>
</head>
<body>
    <h1>Insurance Funds</h1>
    <a href="{{ url_for('register') }}">Register New Fund</a>
    <a href="{{ url_for('check') }}">Check Funds</a>
    <ul>
        {% for fund in funds %}
            <li>{{ fund.name }}: ${ fund.amount }}</li>
        {% endfor %}
    </ul>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
            {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</body>
</html>
```

2. **register.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register Insurance Fund</title>
</head>
<body>
    <h1>Register Insurance Fund</h1>
    <form method="POST">
        <label for="name">Fund Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="amount">Amount:</label>
        <input type="number" step="0.01" id="amount" name="amount" required>
        <br>
        <button type="submit">Register Fund</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Home</a>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
            {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</body>
</html>
```

3. **check.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Check Insurance Funds</title>
</head>
<body>
    <h1>Check Insurance Funds</h1>
    <ul>
        {% for fund in funds %}
            <li>{{ fund.name }}: ${{ fund.amount }}</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

4. **404.html**
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
    <p>The page you are looking for does not exist.</p>
    <a href="/">Go back to Home</a>
</body>
</html>
```

**Note:** Make sure to install Flask and Flask-SQLAlchemy before running the application.
```bash
pip install Flask Flask-SQLAlchemy
```
