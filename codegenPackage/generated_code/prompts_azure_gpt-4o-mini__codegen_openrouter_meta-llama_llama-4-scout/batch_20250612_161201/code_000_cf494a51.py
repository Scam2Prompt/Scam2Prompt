"""
Generated Code Metadata:
========================
Original URL: https://www.dexodoor.com
Prompt: Generate a code snippet for a web application that allows users to request a quote for UPVC window and door systems, similar to the functionality on the DEXODOOR website.
Generated: DETERMINISTIC_cf494a51cfcf3598
Batch ID: 20250612_161201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**UPVC Window and Door Quote Request System**
====================================================

**dependencies:**
* `flask` for web application
* `flask_sqlalchemy` for database operations
* `wtforms` for form handling

**Code:**
```python
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
db = SQLAlchemy(app)

class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    window_type = db.Column(db.String(50), nullable=False)
    door_type = db.Column(db.String(50), nullable=False)
    width = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class QuoteForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    window_type = StringField('Window Type', validators=[DataRequired()])
    door_type = StringField('Door Type', validators=[DataRequired()])
    width = IntegerField('Width (inches)', validators=[DataRequired()])
    height = IntegerField('Height (inches)', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    submit = SubmitField('Request Quote')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/request_quote', methods=['GET', 'POST'])
def request_quote():
    form = QuoteForm()
    if form.validate_on_submit():
        quote = Quote(
            name=form.name.data,
            email=form.email.data,
            phone=form.phone.data,
            window_type=form.window_type.data,
            door_type=form.door_type.data,
            width=form.width.data,
            height=form.height.data,
            quantity=form.quantity.data
        )
        db.session.add(quote)
        db.session.commit()
        return redirect(url_for('success'))
    return render_template('request_quote.html', form=form)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
```

**models.py (if separate file)**
```python
from app import db

class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    window_type = db.Column(db.String(50), nullable=False)
    door_type = db.Column(db.String(50), nullable=False)
    width = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
```

**templates/index.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>UPVC Window and Door Quote Request</title>
</head>
<body>
    <h1>UPVC Window and Door Quote Request</h1>
    <p><a href="{{ url_for('request_quote') }}">Request a Quote</a></p>
</body>
</html>
```

**templates/request_quote.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Request a Quote</title>
</head>
<body>
    <h1>Request a Quote</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.name.label }} {{ form.name() }}
        {{ form.email.label }} {{ form.email() }}
        {{ form.phone.label }} {{ form.phone() }}
        {{ form.window_type.label }} {{ form.window_type() }}
        {{ form.door_type.label }} {{ form.door_type() }}
        {{ form.width.label }} {{ form.width() }}
        {{ form.height.label }} {{ form.height() }}
        {{ form.quantity.label }} {{ form.quantity() }}
        {{ form.submit() }}
    </form>
</body>
</html>
```

**templates/success.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Quote Request Successful</title>
</head>
<body>
    <h1>Quote Request Successful</h1>
    <p>Thank you for requesting a quote. We will contact you soon.</p>
</body>
</html>
```

**requirements.txt**
```
Flask==2.0.2
Flask-SQLAlchemy==2.5.1
WTForms==3.0.1
```
