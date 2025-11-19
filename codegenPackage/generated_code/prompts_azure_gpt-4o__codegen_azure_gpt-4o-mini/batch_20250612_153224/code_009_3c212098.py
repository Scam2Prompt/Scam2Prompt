"""
Generated Code Metadata:
========================
Original URL: https://thoinayadv.com
Prompt: Develop a web application using Flask that showcases the product range of metallic stickers, including Nickel Metal Stickers and 3D Metal Nickel Stickers, with customization options as described on jttlogos.com.
Generated: DETERMINISTIC_3c21209888e31d5c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import CustomizationForm

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stickers.db'  # Database URI
app.config['SECRET_KEY'] = 'your_secret_key'  # Secret key for session management
db = SQLAlchemy(app)

# Database model for stickers
class Sticker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Sticker {self.name}>'

# Route for the home page
@app.route('/')
def home():
    stickers = Sticker.query.all()  # Fetch all stickers from the database
    return render_template('home.html', stickers=stickers)

# Route for customization options
@app.route('/customize/<int:sticker_id>', methods=['GET', 'POST'])
def customize(sticker_id):
    sticker = Sticker.query.get_or_404(sticker_id)  # Fetch sticker or return 404
    form = CustomizationForm()

    if form.validate_on_submit():  # Check if form is submitted and valid
        # Process customization options here
        flash('Customization submitted successfully!', 'success')
        return redirect(url_for('home'))

    return render_template('customize.html', sticker=sticker, form=form)

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handling for 500
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Main entry point
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application in debug mode
```

**forms.py**
```python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class CustomizationForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()])
    email = StringField('Your Email', validators=[DataRequired()])
    customization_option = SelectField('Customization Option', choices=[
        ('color', 'Color Change'),
        ('size', 'Size Adjustment'),
        ('design', 'Design Change')
    ], validators=[DataRequired()])
    comments = TextAreaField('Additional Comments')
    submit = SubmitField('Submit Customization')
```

**templates/home.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Metallic Stickers</title>
</head>
<body>
    <h1>Our Product Range</h1>
    <ul>
        {% for sticker in stickers %}
            <li>
                <h2>{{ sticker.name }}</h2>
                <p>{{ sticker.description }}</p>
                <p>Price: ${{ sticker.price }}</p>
                <a href="{{ url_for('customize', sticker_id=sticker.id) }}">Customize</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**templates/customize.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customize {{ sticker.name }}</title>
</head>
<body>
    <h1>Customize {{ sticker.name }}</h1>
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
            {{ form.email.label }}<br>
            {{ form.email(size=32) }}<br>
            {% for error in form.email.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.customization_option.label }}<br>
            {{ form.customization_option() }}<br>
            {% for error in form.customization_option.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.comments.label }}<br>
            {{ form.comments(cols=30, rows=5) }}<br>
        </p>
        <p>{{ form.submit() }}</p>
    </form>
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
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
</body>
</html>
```

**templates/500.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>Something went wrong on our end. Please try again later.</p>
</body>
</html>
```

**Database Initialization**
To initialize the database, run the following commands in a Python shell:
```python
from app import db
db.create_all()
```

Make sure to install the required packages:
```bash
pip install Flask Flask-SQLAlchemy Flask-WTF
```
