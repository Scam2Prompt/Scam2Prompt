"""
Generated Code Metadata:
========================
Original URL: https://pharmachoicecanada.ca
Prompt: Provide a sample code for a web application that helps new pharmacy owners understand the steps to take when looking to change banners or sell their pharmacy, inspired by PharmaChoice's independent program.
Generated: DETERMINISTIC_5c0093752b0fadde
Batch ID: 20250612_161700
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
from forms import PharmacyForm

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pharmacies.db'  # Database URI
db = SQLAlchemy(app)

# Define the Pharmacy model
class Pharmacy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    banner_change_steps = db.Column(db.Text, nullable=False)
    sell_steps = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Pharmacy {self.name}>'

# Route for the home page
@app.route('/')
def index():
    """Render the home page with a list of pharmacies."""
    pharmacies = Pharmacy.query.all()
    return render_template('index.html', pharmacies=pharmacies)

# Route to add a new pharmacy
@app.route('/add', methods=['GET', 'POST'])
def add_pharmacy():
    """Handle the addition of a new pharmacy."""
    form = PharmacyForm()
    if form.validate_on_submit():
        try:
            new_pharmacy = Pharmacy(
                name=form.name.data,
                banner_change_steps=form.banner_change_steps.data,
                sell_steps=form.sell_steps.data
            )
            db.session.add(new_pharmacy)
            db.session.commit()
            flash('Pharmacy added successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash(f'Error adding pharmacy: {str(e)}', 'danger')
    return render_template('add_pharmacy.html', form=form)

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    """Render a custom 404 error page."""
    return render_template('404.html'), 404

# Error handling for 500
@app.errorhandler(500)
def internal_server_error(e):
    """Render a custom 500 error page."""
    return render_template('500.html'), 500

# Main entry point
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application in debug mode
```

```python
# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class PharmacyForm(FlaskForm):
    """Form for adding a new pharmacy."""
    name = StringField('Pharmacy Name', validators=[DataRequired()])
    banner_change_steps = TextAreaField('Steps to Change Banner', validators=[DataRequired()])
    sell_steps = TextAreaField('Steps to Sell Pharmacy', validators=[DataRequired()])
    submit = SubmitField('Add Pharmacy')
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pharmacy Management</title>
</head>
<body>
    <h1>Pharmacies</h1>
    <a href="{{ url_for('add_pharmacy') }}">Add New Pharmacy</a>
    <ul>
        {% for pharmacy in pharmacies %}
            <li>{{ pharmacy.name }} - <a href="#">{{ pharmacy.banner_change_steps }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/add_pharmacy.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Pharmacy</title>
</head>
<body>
    <h1>Add New Pharmacy</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <p>
            {{ form.name.label }}<br>
            {{ form.name(size=32) }}<br>
            {% for error in form.name.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.banner_change_steps.label }}<br>
            {{ form.banner_change_steps(rows=5, cols=32) }}<br>
            {% for error in form.banner_change_steps.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.sell_steps.label }}<br>
            {{ form.sell_steps(rows=5, cols=32) }}<br>
            {% for error in form.sell_steps.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>{{ form.submit() }}</p>
    </form>
</body>
</html>
```

```html
<!-- templates/404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
</body>
</html>
```

```html
<!-- templates/500.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>500 Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>Something went wrong on our end. Please try again later.</p>
</body>
</html>
```
