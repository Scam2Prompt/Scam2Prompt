"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Develop a web application prototype for clients to design and customize their own cosmetic brand, incorporating the full-service workflow described by Fabricare Cosméticos.
Generated: DETERMINISTIC_0704e2650c7b429e
Batch ID: 20250612_153517
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
from wtforms import Form, StringField, SelectField, TextAreaField, validators
import os

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # Randomly generate a secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    color = db.Column(db.String(50), nullable=False)
    scent = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

# Create the database
db.create_all()

# Form for product customization
class ProductForm(Form):
    name = StringField('Product Name', [validators.Length(min=1, max=100)])
    description = TextAreaField('Description', [validators.Length(min=10)])
    color = SelectField('Color', choices=[('red', 'Red'), ('blue', 'Blue'), ('green', 'Green')])
    scent = SelectField('Scent', choices=[('floral', 'Floral'), ('citrus', 'Citrus'), ('woody', 'Woody')])

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Route for customizing a product
@app.route('/customize', methods=['GET', 'POST'])
def customize():
    form = ProductForm(request.form)
    
    if request.method == 'POST' and form.validate():
        # Capture form data
        new_product = Product(
            name=form.name.data,
            description=form.description.data,
            color=form.color.data,
            scent=form.scent.data
        )
        
        try:
            # Add new product to the database
            db.session.add(new_product)
            db.session.commit()
            flash('Product customized successfully!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            # Rollback in case of error
            db.session.rollback()
            flash(f'Error customizing product: {str(e)}', 'danger')
    
    return render_template('customize.html', form=form)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Files:**
*Create a `templates` directory and add the following HTML files:*

1. **index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cosmetic Brand Designer</title>
</head>
<body>
    <h1>Welcome to Fabricare Cosméticos</h1>
    <a href="{{ url_for('customize') }}">Customize Your Product</a>
</body>
</html>
```

2. **customize.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customize Product</title>
</head>
<body>
    <h1>Customize Your Cosmetic Product</h1>
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
            {{ form.description.label }}<br>
            {{ form.description(rows=4, cols=32) }}<br>
            {% for error in form.description.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.color.label }}<br>
            {{ form.color() }}<br>
        </p>
        <p>
            {{ form.scent.label }}<br>
            {{ form.scent() }}<br>
        </p>
        <p>
            <input type="submit" value="Customize">
        </p>
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
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

This code provides a basic Flask web application that allows users to customize cosmetic products, complete with a simple database and form handling.
