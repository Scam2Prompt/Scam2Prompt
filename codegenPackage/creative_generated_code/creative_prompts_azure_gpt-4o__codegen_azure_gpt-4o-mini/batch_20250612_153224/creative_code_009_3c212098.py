"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thoinayadv.com
Prompt: Develop a web application using Flask that showcases the product range of metallic stickers, including Nickel Metal Stickers and 3D Metal Nickel Stickers, with customization options as described on jttlogos.com.
Generated: DETERMINISTIC_3c21209888e31d5c
Batch ID: 20250612_153224
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
from forms import CustomStickerForm

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stickers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a strong secret key
db = SQLAlchemy(app)

# Define the Sticker model
class Sticker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Sticker {self.name}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()
    # Sample data
    if Sticker.query.count() == 0:
        sample_stickers = [
            Sticker(name='Nickel Metal Sticker', description='High-quality nickel metal sticker.', price=1.50),
            Sticker(name='3D Metal Nickel Sticker', description='Unique 3D design with nickel finish.', price=2.00)
        ]
        db.session.bulk_save_objects(sample_stickers)
        db.session.commit()

# Route for the homepage
@app.route('/')
def index():
    stickers = Sticker.query.all()
    return render_template('index.html', stickers=stickers)

# Route for customizing a sticker
@app.route('/customize/<int:sticker_id>', methods=['GET', 'POST'])
def customize(sticker_id):
    sticker = Sticker.query.get_or_404(sticker_id)
    form = CustomStickerForm()

    if form.validate_on_submit():
        # Here you can handle the customization logic
        flash(f'Custom sticker created for {sticker.name}!', 'success')
        return redirect(url_for('index'))

    return render_template('customize.html', form=form, sticker=sticker)

# Error handler for 404 errors
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### forms.py
```python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DecimalField
from wtforms.validators import DataRequired, Length

class CustomStickerForm(FlaskForm):
    name = StringField('Sticker Name', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])
    submit = SubmitField('Customize Sticker')
```

### templates/index.html
```html
<!doctype html>
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

### templates/customize.html
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customize Sticker</title>
</head>
<body>
    <h1>Customize {{ sticker.name }}</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.name.label }} {{ form.name() }}<br>
        {{ form.description.label }} {{ form.description() }}<br>
        {{ form.price.label }} {{ form.price() }}<br>
        {{ form.submit() }}
    </form>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

### templates/404.html
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="{{ url_for('index') }}">Return Home</a>
</body>
</html>
```

### templates/500.html
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <a href="{{ url_for('index') }}">Return Home</a>
</body>
</html>
``` 

### Requirements
Create a `requirements.txt` file to list necessary dependencies:
```
Flask==2.0.3
Flask-SQLAlchemy==2.5.1
Flask-WTF==1.0.0
WTForms==2.3.3
```

### Note
Make sure to install Flask and other dependencies using:
```bash
pip install -r requirements.txt
```

Then, run the application using:
```bash
python app.py
```
