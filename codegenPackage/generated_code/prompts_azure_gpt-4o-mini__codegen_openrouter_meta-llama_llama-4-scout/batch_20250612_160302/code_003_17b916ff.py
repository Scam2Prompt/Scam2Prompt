"""
Generated Code Metadata:
========================
Original URL: https://idex.xyz
Prompt: How do I implement a domain purchase inquiry system that captures user details like on Idex.xyz?
Generated: DETERMINISTIC_17b916ffbff3859d
Batch ID: 20250612_160302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Domain Purchase Inquiry System**
=====================================

### Requirements

* Python 3.8+
* Flask 2.0+
* Flask-SQLAlchemy 2.5+
* Flask-WTF 1.0+

### Code
```python
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///domain_inquiries.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone_number = db.Column(db.String(20), nullable=False)
    domain_name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.phone_number}', '{self.domain_name}')"

class DomainInquiryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    domain_name = StringField('Domain Name', validators=[DataRequired()])
    submit = SubmitField('Submit Inquiry')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = DomainInquiryForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data, phone_number=form.phone_number.data, domain_name=form.domain_name.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('success'))
    return render_template('index.html', form=form)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**templates/index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Domain Purchase Inquiry</title>
</head>
<body>
    <h1>Domain Purchase Inquiry</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.name.label }} {{ form.name() }}
        {{ form.email.label }} {{ form.email() }}
        {{ form.phone_number.label }} {{ form.phone_number() }}
        {{ form.domain_name.label }} {{ form.domain_name() }}
        {{ form.submit() }}
    </form>
</body>
</html>
```

**templates/success.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Success</title>
</head>
<body>
    <h1>Domain Inquiry Submitted Successfully!</h1>
</body>
</html>
```

**requirements.txt**
```
Flask==2.0.2
Flask-SQLAlchemy==2.5.1
Flask-WTF==1.0.1
```
