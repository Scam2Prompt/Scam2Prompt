"""
Generated Code Metadata:
========================
Original URL: https://akashinfo.tech
Prompt: Develop a simple web application that showcases the services provided by Akash Infotech, emphasizing tech support and product selection for individual customer needs.
Generated: DETERMINISTIC_a1d5fa3f4ec3ff3e
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**akash_infotech_web_app.py**
```python
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

# Create a Flask application instance
app = Flask(__name__)
app.config['SECRET_KEY'] = 'akash_infotech_secret_key'

# Define a form for customer tech support requests
class TechSupportForm(FlaskForm):
    """Form for customer tech support requests"""
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    issue = StringField('Issue', validators=[DataRequired()])
    submit = SubmitField('Submit Request')

# Define a form for product selection
class ProductSelectionForm(FlaskForm):
    """Form for product selection"""
    product = SelectField('Select Product', 
                          choices=['Software', 'Hardware', 'Consulting'], 
                          validators=[DataRequired()])
    submit = SubmitField('Select Product')

# Sample in-memory data store for products and tech support requests
products = [
    {'id': 1, 'name': 'Software', 'description': 'Our software solutions'},
    {'id': 2, 'name': 'Hardware', 'description': 'Our hardware solutions'},
    {'id': 3, 'name': 'Consulting', 'description': 'Our consulting services'}
]

tech_support_requests = []

# Route for the home page
@app.route('/')
def index():
    """Home page route"""
    return render_template('index.html', products=products)

# Route for tech support requests
@app.route('/tech_support', methods=['GET', 'POST'])
def tech_support():
    """Tech support request route"""
    form = TechSupportForm()
    if form.validate_on_submit():
        tech_support_requests.append({
            'name': form.name.data,
            'email': form.email.data,
            'issue': form.issue.data
        })
        return redirect(url_for('index'))
    return render_template('tech_support.html', form=form)

# Route for product selection
@app.route('/product_selection', methods=['GET', 'POST'])
def product_selection():
    """Product selection route"""
    form = ProductSelectionForm()
    if form.validate_on_submit():
        selected_product = form.product.data
        return render_template('product_details.html', product=next((p for p in products if p['name'] == selected_product), None))
    return render_template('product_selection.html', form=form)

# Error handler for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    """404 error handler"""
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**templates/index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Akash Infotech</title>
</head>
<body>
    <h1>Akash Infotech</h1>
    <p>Welcome to Akash Infotech, your one-stop-shop for all your tech needs.</p>
    <h2>Our Products</h2>
    <ul>
    {% for product in products %}
        <li>{{ product.name }} - {{ product.description }}</li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('tech_support') }}">Get Tech Support</a></p>
    <p><a href="{{ url_for('product_selection') }}">Select a Product</a></p>
</body>
</html>
```

**templates/tech_support.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tech Support</title>
</head>
<body>
    <h1>Tech Support</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.name.label }} {{ form.name() }}
        {{ form.email.label }} {{ form.email() }}
        {{ form.issue.label }} {{ form.issue() }}
        {{ form.submit() }}
    </form>
</body>
</html>
```

**templates/product_selection.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Selection</title>
</head>
<body>
    <h1>Product Selection</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.product.label }} {{ form.product() }}
        {{ form.submit() }}
    </form>
</body>
</html>
```

**templates/product_details.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Details</title>
</head>
<body>
    <h1>Product Details</h1>
    {% if product %}
        <h2>{{ product.name }}</h2>
        <p>{{ product.description }}</p>
    {% else %}
        <p>Product not found.</p>
    {% endif %}
</body>
</html>
```

**templates/404.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Error</title>
</head>
<body>
    <h1>404 Error</h1>
    <p>Page not found.</p>
</body>
</html>
```
