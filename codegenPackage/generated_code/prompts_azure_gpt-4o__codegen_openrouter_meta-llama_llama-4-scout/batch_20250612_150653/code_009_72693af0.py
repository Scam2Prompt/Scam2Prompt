"""
Generated Code Metadata:
========================
Original URL: https://www.paradigmagbi.ru
Prompt: Design a user interface for a web application that allows users to select reinforced concrete products (ЖБИ) by category and region, inspired by the ordering and selection process described on paradigmagbi.ru.
Generated: DETERMINISTIC_72693af014c6365c
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

# Define a form for filtering products
class ProductFilterForm(FlaskForm):
    category = SelectField('Category', choices=[
        ('all', 'All'),
        ('beams', 'Beams'),
        ('slabs', 'Slabs'),
        ('columns', 'Columns'),
        ('foundations', 'Foundations')
    ], validators=[DataRequired()])
    region = SelectField('Region', choices=[
        ('moscow', 'Moscow'),
        ('saint_petersburg', 'Saint Petersburg'),
        ('yekaterinburg', 'Yekaterinburg'),
        ('kazan', 'Kazan')
    ], validators=[DataRequired()])

# Mock data for products
products = {
    'beams': [
        {'id': 1, 'name': 'Beam 1', 'region': 'moscow'},
        {'id': 2, 'name': 'Beam 2', 'region': 'saint_petersburg'}
    ],
    'slabs': [
        {'id': 3, 'name': 'Slab 1', 'region': 'moscow'},
        {'id': 4, 'name': 'Slab 2', 'region': 'yekaterinburg'}
    ],
    'columns': [
        {'id': 5, 'name': 'Column 1', 'region': 'kazan'},
        {'id': 6, 'name': 'Column 2', 'region': 'moscow'}
    ],
    'foundations': [
        {'id': 7, 'name': 'Foundation 1', 'region': 'saint_petersburg'},
        {'id': 8, 'name': 'Foundation 2', 'region': 'yekaterinburg'}
    ]
}

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ProductFilterForm()
    if form.validate_on_submit():
        category = form.category.data
        region = form.region.data
        filtered_products = [product for product in [item for sublist in products.values() for item in sublist] if product['region'] == region and (category == 'all' or [k for k, v in products.items() if product in v][0] == category)]
        return render_template('results.html', products=filtered_products)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ЖБИ Products</title>
</head>
<body>
    <h1>Select Products</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.category.label }} {{ form.category() }}
        {{ form.region.label }} {{ form.region() }}
        <input type="submit" value="Filter">
    </form>
</body>
</html>
```

```html
<!-- templates/results.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ЖБИ Products Results</title>
</head>
<body>
    <h1>Products</h1>
    <ul>
    {% for product in products %}
        <li>{{ product.name }} ({{ product.region }})</li>
    {% endfor %}
    </ul>
</body>
</html>
```

```python
# requirements.txt

Flask
Flask-WTF
```
