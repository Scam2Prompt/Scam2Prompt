"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tsunarloyni-connext.pages.dev
Prompt: Generate code for a web application that allows users to customize car designs based on driver ambitions.
Generated: DETERMINISTIC_79ec497f2f1ea6a6
Batch ID: 20250612_155449
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import CarDesignForm

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car_designs.db'
db = SQLAlchemy(app)

# Define the CarDesign model
class CarDesign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ambition = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(30), nullable=False)
    features = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f"<CarDesign {self.ambition}, {self.color}>"

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for car design customization
@app.route('/customize', methods=['GET', 'POST'])
def customize():
    form = CarDesignForm()
    if form.validate_on_submit():
        # Create a new CarDesign instance
        new_design = CarDesign(
            ambition=form.ambition.data,
            color=form.color.data,
            features=form.features.data
        )
        try:
            # Add to the database
            db.session.add(new_design)
            db.session.commit()
            flash('Car design customized successfully!', 'success')
            return redirect(url_for('view_designs'))
        except Exception as e:
            db.session.rollback()
            flash('Error customizing car design. Please try again.', 'danger')
            app.logger.error(f"Error occurred: {e}")

    return render_template('customize.html', form=form)

# Route to view all designs
@app.route('/designs')
def view_designs():
    designs = CarDesign.query.all()
    return render_template('designs.html', designs=designs)

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Main block to run the application
if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```python
# forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class CarDesignForm(FlaskForm):
    ambition = StringField('Driver Ambition', validators=[DataRequired()])
    color = StringField('Car Color', validators=[DataRequired()])
    features = TextAreaField('Additional Features', validators=[DataRequired()])
    submit = SubmitField('Customize Car Design')
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Car Design Customization</title>
</head>
<body>
    <h1>Welcome to Car Design Customization</h1>
    <a href="{{ url_for('customize') }}">Customize Your Car</a>
    <a href="{{ url_for('view_designs') }}">View Designs</a>
</body>
</html>
```

```html
<!-- templates/customize.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customize Car Design</title>
</head>
<body>
    <h1>Customize Your Car</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <p>
            {{ form.ambition.label }}<br>
            {{ form.ambition(size=32) }}<br>
            {% for error in form.ambition.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.color.label }}<br>
            {{ form.color(size=32) }}<br>
            {% for error in form.color.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.features.label }}<br>
            {{ form.features(rows=5, cols=32) }}<br>
            {% for error in form.features.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>{{ form.submit() }}</p>
    </form>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

```html
<!-- templates/designs.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Car Designs</title>
</head>
<body>
    <h1>All Customized Car Designs</h1>
    <ul>
        {% for design in designs %}
            <li>{{ design.ambition }} - {{ design.color }} - Features: {{ design.features }}</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('home') }}">Back to Home</a>
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
    <h1>404 Not Found</h1>
    <p>Sorry, the page you're looking for does not exist.</p>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

Make sure to install Flask and Flask-WTF to run the application:

```bash
pip install Flask Flask-WTF Flask-SQLAlchemy
```
