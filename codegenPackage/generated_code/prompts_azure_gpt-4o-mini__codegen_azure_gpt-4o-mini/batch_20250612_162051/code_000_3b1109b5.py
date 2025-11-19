"""
Generated Code Metadata:
========================
Original URL: https://createxpro.com
Prompt: Generate a code snippet for a web application that allows users to customize promotional items using CreatexPro's unique personalization techniques like serigraphy and DTF printing.
Generated: DETERMINISTIC_3b1109b5dc649964
Batch ID: 20250612_162051
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
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
import logging

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define a form for user input
class CustomizationForm(FlaskForm):
    item_name = StringField('Item Name', validators=[DataRequired()])
    personalization_method = SelectField('Personalization Method', 
                                          choices=[('serigraphy', 'Serigraphy'), 
                                                   ('dtf', 'DTF Printing')],
                                          validators=[DataRequired()])
    submit = SubmitField('Customize Item')

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    form = CustomizationForm()
    if form.validate_on_submit():
        # Log the customization request
        logging.info(f"Customization request: {form.item_name.data} using {form.personalization_method.data}")
        flash('Your customization request has been submitted!', 'success')
        return redirect(url_for('home'))
    return render_template('index.html', form=form)

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handling for 500
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customize Promotional Items</title>
</head>
<body>
    <h1>Customize Your Promotional Item</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <div>
            {{ form.item_name.label }}<br>
            {{ form.item_name(size=32) }}<br>
            {% for error in form.item_name.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.personalization_method.label }}<br>
            {{ form.personalization_method() }}<br>
            {% for error in form.personalization_method.errors %}
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

```html
<!-- 404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you are looking for does not exist.</p>
</body>
</html>
```

```html
<!-- 500.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>Sorry, something went wrong on our end.</p>
</body>
</html>
```
