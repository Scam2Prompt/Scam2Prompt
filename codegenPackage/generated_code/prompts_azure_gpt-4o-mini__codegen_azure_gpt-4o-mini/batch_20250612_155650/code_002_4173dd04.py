"""
Generated Code Metadata:
========================
Original URL: https://www.hopexchange.com
Prompt: Create a code snippet for a web application that offers resources and support for individuals dealing with pregnancy loss, inspired by the mission of HopeXchange.
Generated: DETERMINISTIC_4173dd04dd1c0944
Batch ID: 20250612_155650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import ResourceForm
import logging

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resources.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Database model for resources
class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Resource {self.title}>'

# Route for the home page
@app.route('/')
def home():
    """Render the home page with a list of resources."""
    resources = Resource.query.all()
    return render_template('home.html', resources=resources)

# Route to add a new resource
@app.route('/add', methods=['GET', 'POST'])
def add_resource():
    """Handle the addition of a new resource."""
    form = ResourceForm()
    if form.validate_on_submit():
        new_resource = Resource(
            title=form.title.data,
            description=form.description.data,
            link=form.link.data
        )
        db.session.add(new_resource)
        db.session.commit()
        flash('Resource added successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('add_resource.html', form=form)

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    """Render a custom 404 error page."""
    return render_template('404.html'), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(e):
    """Render a custom 500 error page."""
    db.session.rollback()
    return render_template('500.html'), 500

# Main entry point
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application

```

```html
<!-- templates/home.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HopeXchange Resources</title>
</head>
<body>
    <h1>Resources for Pregnancy Loss</h1>
    <a href="{{ url_for('add_resource') }}">Add a New Resource</a>
    <ul>
        {% for resource in resources %}
            <li>
                <strong>{{ resource.title }}</strong>: {{ resource.description }} 
                <a href="{{ resource.link }}" target="_blank">Learn More</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/add_resource.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Resource</title>
</head>
<body>
    <h1>Add a New Resource</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <p>
            {{ form.title.label }}<br>
            {{ form.title(size=32) }}<br>
            {% for error in form.title.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.description.label }}<br>
            {{ form.description(rows=5) }}<br>
            {% for error in form.description.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.link.label }}<br>
            {{ form.link(size=32) }}<br>
            {% for error in form.link.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            <input type="submit" value="Add Resource">
        </p>
    </form>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

```python
# forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, URL

class ResourceForm(FlaskForm):
    """Form for adding a new resource."""
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    link = StringField('Link', validators=[DataRequired(), URL()])
    submit = SubmitField('Add Resource')
```

Make sure to install the required packages before running the application:
```bash
pip install Flask Flask-SQLAlchemy Flask-WTF
```
