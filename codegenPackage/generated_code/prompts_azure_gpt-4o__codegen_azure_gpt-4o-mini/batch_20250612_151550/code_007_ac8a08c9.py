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

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SelectField, DecimalField, SubmitField
from wtforms.validators import DataRequired, NumberRange

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ewallet.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the User model for e-wallet transactions
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Float, default=0.0)

# Define the InvestmentPlan model
class InvestmentPlan:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

# Define available investment plans
investment_plans = [
    InvestmentPlan("Starter", 0.05),  # 5% return
    InvestmentPlan("Silver", 0.10),   # 10% return
    InvestmentPlan("Gold", 0.15)      # 15% return
]

# Create a form for investment selection
class InvestmentForm(FlaskForm):
    plan = SelectField('Select Investment Plan', choices=[(plan.name, plan.name) for plan in investment_plans], validators=[DataRequired()])
    amount = DecimalField('Investment Amount', validators=[DataRequired(), NumberRange(min=1)], places=2)
    submit = SubmitField('Calculate Profit')

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    form = InvestmentForm()
    if form.validate_on_submit():
        plan_name = form.plan.data
        amount = form.amount.data
        plan = next((p for p in investment_plans if p.name == plan_name), None)
        
        if plan:
            profit = amount * plan.rate
            flash(f'Expected Profit from {plan.name} plan: ${profit:.2f}', 'success')
        else:
            flash('Invalid investment plan selected.', 'danger')
        
        return redirect(url_for('index'))
    
    return render_template('index.html', form=form)

# Route for managing e-wallet transactions
@app.route('/ewallet', methods=['GET', 'POST'])
def ewallet():
    if request.method == 'POST':
        try:
            amount = float(request.form.get('amount', 0))
            action = request.form.get('action')
            user = User.query.first()  # Assuming a single user for simplicity
            
            if action == 'add':
                user.balance += amount
                flash(f'Added ${amount:.2f} to your e-wallet.', 'success')
            elif action == 'withdraw':
                if user.balance >= amount:
                    user.balance -= amount
                    flash(f'Withdrew ${amount:.2f} from your e-wallet.', 'success')
                else:
                    flash('Insufficient balance for withdrawal.', 'danger')
            else:
                flash('Invalid action.', 'danger')
            
            db.session.commit()
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'danger')
            db.session.rollback()
        
    user = User.query.first()  # Fetch user data
    return render_template('ewallet.html', balance=user.balance)

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Main entry point
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application in debug mode
```

### HTML Templates (index.html and ewallet.html)

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Investment Plans</title>
</head>
<body>
    <h1>Investment Plans</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.plan.label }} {{ form.plan() }}<br>
        {{ form.amount.label }} {{ form.amount() }}<br>
        {{ form.submit() }}
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
</body>
</html>
```

**ewallet.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-Wallet Management</title>
</head>
<body>
    <h1>E-Wallet Balance: ${{ balance }}</h1>
    <form method="POST">
        <input type="number" name="amount" step="0.01" required>
        <button type="submit" name="action" value="add">Add Funds</button>
        <button type="submit" name="action" value="withdraw">Withdraw Funds</button>
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
</body>
</html>
```

### Note:
- Ensure to install the required packages using `pip install Flask Flask-SQLAlchemy Flask-WTF`.
- Replace `'your_secret_key'` with a strong secret key for production use.
- The database is initialized with a single user for simplicity; consider implementing user authentication for a real application.
