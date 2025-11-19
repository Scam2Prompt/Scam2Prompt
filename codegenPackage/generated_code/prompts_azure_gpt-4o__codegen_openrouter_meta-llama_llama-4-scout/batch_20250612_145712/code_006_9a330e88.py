"""
Generated Code Metadata:
========================
Original URL: https://meyerseim.com
Prompt: Develop a web application feature to allow registered users to contribute genealogical data, similar to the user registration system on the Meyer/Seim family site.
Generated: DETERMINISTIC_9a330e8818c401dc
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Genealogical Data Contribution Feature**
=============================================

### Dependencies

* Python 3.9+
* Flask 2.0+
* Flask-SQLAlchemy 2.5+
* Flask-WTF 1.0+

### Code

```python
# app.py

from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///genealogy.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class GenealogicalData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('genealogical_data', lazy=True))
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"GenealogicalData('{self.name}', '{self.description}')"

class ContributionForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Contribute')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contribute', methods=['GET', 'POST'])
def contribute():
    form = ContributionForm()
    if form.validate_on_submit():
        try:
            user_id = 1  # Replace with current user ID
            data = GenealogicalData(user_id=user_id, name=form.name.data, description=form.description.data)
            db.session.add(data)
            db.session.commit()
            flash('Genealogical data contributed successfully!')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash('Error contributing genealogical data: ' + str(e))
    return render_template('contribute.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/contribute.html -->

<form method="POST">
    {{ form.hidden_tag() }}
    {{ form.name.label }} {{ form.name() }}
    {{ form.description.label }} {{ form.description() }}
    {{ form.submit() }}
</form>
```

```html
<!-- templates/index.html -->

<p><a href="{{ url_for('contribute') }}">Contribute Genealogical Data</a></p>
```

```python
# models.py (optional, for separate model definitions)

from app import db

# Models defined in app.py, no additional models needed
```

```python
# requirements.txt

Flask==2.0.2
Flask-SQLAlchemy==2.5.1
Flask-WTF==1.0.1
```

### Database Initialization

Run the following commands to initialize the database:

```bash
flask db init
flask db migrate
flask db upgrade
```
