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

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///insurance_funds.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
db = SQLAlchemy(app)

# Define the InsuranceFund model
class InsuranceFund(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fund_name = db.Column(db.String(100), nullable=False, unique=True)
    fund_amount = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<InsuranceFund {self.fund_name}>'

# Create the database
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def index():
    funds = InsuranceFund.query.all()  # Retrieve all insurance funds
    return render_template('index.html', funds=funds)

# Route for registering a new insurance fund
@app.route('/register', methods=['POST'])
def register():
    fund_name = request.form.get('fund_name')
    fund_amount = request.form.get('fund_amount')

    # Validate input
    if not fund_name or not fund_amount:
        flash('Fund name and amount are required!', 'danger')
        return redirect(url_for('index'))

    try:
        # Create a new insurance fund
        new_fund = InsuranceFund(fund_name=fund_name, fund_amount=float(fund_amount))
        db.session.add(new_fund)
        db.session.commit()
        flash('Insurance fund registered successfully!', 'success')
    except IntegrityError:
        db.session.rollback()
        flash('Fund name already exists. Please choose a different name.', 'danger')
    except ValueError:
        flash('Invalid amount. Please enter a valid number.', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'An error occurred: {str(e)}', 'danger')

    return redirect(url_for('index'))

# Route for checking insurance funds
@app.route('/check/<int:fund_id>')
def check(fund_id):
    fund = InsuranceFund.query.get_or_404(fund_id)  # Retrieve fund by ID
    return render_template('check.html', fund=fund)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Templates:**

1. **index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Insurance Fund Registration</title>
</head>
<body>
    <h1>Insurance Fund Registration</h1>
    <form action="{{ url_for('register') }}" method="POST">
        <input type="text" name="fund_name" placeholder="Fund Name" required>
        <input type="number" step="0.01" name="fund_amount" placeholder="Fund Amount" required>
        <button type="submit">Register Fund</button>
    </form>

    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
            {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}

    <h2>Registered Funds</h2>
    <ul>
        {% for fund in funds %}
            <li>
                <a href="{{ url_for('check', fund_id=fund.id) }}">{{ fund.fund_name }}</a> - ${{ fund.fund_amount }}
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

2. **check.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Check Insurance Fund</title>
</head>
<body>
    <h1>Insurance Fund Details</h1>
    <p>Fund Name: {{ fund.fund_name }}</p>
    <p>Fund Amount: ${{ fund.fund_amount }}</p>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

**Note:** Ensure you have Flask and Flask-SQLAlchemy installed in your environment. You can install them using pip:

```bash
pip install Flask Flask-SQLAlchemy
```
