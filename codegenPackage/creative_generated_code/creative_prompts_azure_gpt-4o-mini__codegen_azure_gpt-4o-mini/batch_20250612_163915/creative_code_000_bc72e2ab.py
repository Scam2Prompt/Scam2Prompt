"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cancen.fr
Prompt: Generate a code snippet for a web application that allows users to donate to cancer research, incorporating features mentioned on the CANCEN website.
Generated: DETERMINISTIC_bc72e2abcf845094
Batch ID: 20250612_163915
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
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired, NumberRange
import logging

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///donations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Database model for donations
class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)

# Form for donation input
class DonationForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()])
    amount = DecimalField('Donation Amount ($)', validators=[DataRequired(), NumberRange(min=1)], places=2)
    submit = SubmitField('Donate')

# Route for the homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    form = DonationForm()
    if form.validate_on_submit():
        try:
            # Create a new donation record
            new_donation = Donation(name=form.name.data, amount=form.amount.data)
            db.session.add(new_donation)
            db.session.commit()
            flash('Thank you for your donation!', 'success')
            logging.info(f'Donation received: {form.amount.data} from {form.name.data}')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            logging.error(f'Error processing donation: {e}')
            flash('An error occurred while processing your donation. Please try again.', 'danger')
    return render_template('index.html', form=form)

# Route to view donations (Admin Panel)
@app.route('/donations')
def donations():
    try:
        all_donations = Donation.query.all()
        return render_template('donations.html', donations=all_donations)
    except Exception as e:
        logging.error(f'Error fetching donations: {e}')
        flash('An error occurred while fetching donations. Please try again.', 'danger')
        return redirect(url_for('index'))

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables if they don't exist
    app.run(debug=True)  # Set debug to False in production
```

**HTML Templates (index.html and donations.html)**

`index.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Donate to Cancer Research</title>
</head>
<body>
    <h1>Donate to Cancer Research</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <div>
            {{ form.name.label }}<br>
            {{ form.name(size=32) }}<br>
            {% for error in form.name.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.amount.label }}<br>
            {{ form.amount(size=10) }}<br>
            {% for error in form.amount.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.submit() }}
        </div>
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

`donations.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Donations List</title>
</head>
<body>
    <h1>Donations to Cancer Research</h1>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Amount ($)</th>
            </tr>
        </thead>
        <tbody>
            {% for donation in donations %}
            <tr>
                <td>{{ donation.name }}</td>
                <td>{{ donation.amount }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
```

**Important Note:** Ensure to install the required packages with:
```bash
pip install Flask Flask-SQLAlchemy Flask-WTF
```

Make sure to change `'your_secret_key'` to a secure key and consider configuring production settings appropriately.
