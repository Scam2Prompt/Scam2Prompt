"""
Generated Code Metadata:
========================
Original URL: https://sarl-verdier-irrigation.fr
Prompt: Develop a web application to manage a store's inventory of motoculture and irrigation equipment, including features for customer inquiries and product recommendations, inspired by SARL VERDIER's services.
Generated: DETERMINISTIC_4a042a3d88472cfc
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Motoculture and Irrigation Equipment Inventory Management Web Application**

### Dependencies

* Python 3.9+
* Flask 2.0+
* Flask-SQLAlchemy 2.5+
* Flask-WTF 1.0+

### Code

```python
# app.py

from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Product('{self.name}', '{self.description}', {self.price})"

class InquiryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    message = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RecommendationForm(FlaskForm):
    product_type = StringField('Product Type', validators=[DataRequired()])
    submit = SubmitField('Get Recommendations')

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/inquiry', methods=['GET', 'POST'])
def inquiry():
    form = InquiryForm()
    if form.validate_on_submit():
        # Handle inquiry submission
        print(f"Inquiry from {form.name.data} ({form.email.data}): {form.message.data}")
        return redirect(url_for('index'))
    return render_template('inquiry.html', form=form)

@app.route('/recommendations', methods=['GET', 'POST'])
def recommendations():
    form = RecommendationForm()
    if form.validate_on_submit():
        # Handle recommendation request
        product_type = form.product_type.data
        products = Product.query.filter_by(name=product_type).all()
        return render_template('recommendations.html', products=products)
    return render_template('recommendations.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
```

```python
# models.py

from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Product('{self.name}', '{self.description}', {self.price})"
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Motoculture and Irrigation Equipment Inventory Management</title>
</head>
<body>
    <h1>Products</h1>
    <ul>
    {% for product in products %}
        <li>{{ product.name }} ({{ product.price }})</li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('inquiry') }}">Make an Inquiry</a></p>
    <p><a href="{{ url_for('recommendations') }}">Get Product Recommendations</a></p>
</body>
</html>
```

```html
<!-- templates/inquiry.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Make an Inquiry</title>
</head>
<body>
    <h1>Make an Inquiry</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.name.label }} {{ form.name() }}
        {{ form.email.label }} {{ form.email() }}
        {{ form.message.label }} {{ form.message() }}
        {{ form.submit() }}
    </form>
</body>
</html>
```

```html
<!-- templates/recommendations.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Get Product Recommendations</title>
</head>
<body>
    <h1>Get Product Recommendations</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.product_type.label }} {{ form.product_type() }}
        {{ form.submit() }}
    </form>
    {% if products %}
        <h2>Recommended Products</h2>
        <ul>
        {% for product in products %}
            <li>{{ product.name }} ({{ product.price }})</li>
        {% endfor %}
        </ul>
    {% endif %}
</body>
</html>
```

```bash
# requirements.txt

Flask==2.0.2
Flask-SQLAlchemy==2.5.1
Flask-WTF==1.0.1
```

```bash
# run.sh

#!/bin/bash

# Create database
flask db init
flask db migrate
flask db upgrade

# Run application
flask run
```
