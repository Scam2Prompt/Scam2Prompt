"""
Generated Code Metadata:
========================
Original URL: https://sarl-verdier-irrigation.fr
Prompt: Develop a simple web application that allows users to browse and request repairs for agricultural machinery, inspired by the repair services offered by SARL VERDIER.
Generated: DETERMINISTIC_d905adacb8dfeac3
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Agricultural Machinery Repair Web Application**

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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///repair_database.db'
db = SQLAlchemy(app)


# Models
class Machinery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Machinery('{self.name}', '{self.description}')"


class RepairRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    machinery_id = db.Column(db.Integer, db.ForeignKey('machinery.id'), nullable=False)
    machinery = db.relationship('Machinery', backref=db.backref('repair_requests', lazy=True))
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), nullable=False, default='Pending')

    def __repr__(self):
        return f"RepairRequest('{self.machinery.name}', '{self.description}', '{self.status}')"


# Forms
class RepairRequestForm(FlaskForm):
    machinery_id = IntegerField('Machinery ID', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')


class MachineryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')


# Routes
@app.route('/')
def index():
    machinery = Machinery.query.all()
    return render_template('index.html', machinery=machinery)


@app.route('/machinery/<int:machinery_id>')
def machinery_details(machinery_id):
    machinery = Machinery.query.get_or_404(machinery_id)
    return render_template('machinery_details.html', machinery=machinery)


@app.route('/repair_request', methods=['GET', 'POST'])
def repair_request():
    form = RepairRequestForm()
    if form.validate_on_submit():
        machinery = Machinery.query.get_or_404(form.machinery_id.data)
        repair_request = RepairRequest(machinery=machinery, description=form.description.data)
        db.session.add(repair_request)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('repair_request.html', form=form)


@app.route('/add_machinery', methods=['GET', 'POST'])
def add_machinery():
    form = MachineryForm()
    if form.validate_on_submit():
        machinery = Machinery(name=form.name.data, description=form.description.data)
        db.session.add(machinery)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_machinery.html', form=form)


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
    <title>Agricultural Machinery Repair</title>
</head>
<body>
    <h1>Machinery List</h1>
    <ul>
        {% for machinery in machinery %}
        <li>
            <a href="{{ url_for('machinery_details', machinery_id=machinery.id) }}">{{ machinery.name }}</a>
        </li>
        {% endfor %}
    </ul>
    <p><a href="{{ url_for('add_machinery') }}">Add Machinery</a></p>
    <p><a href="{{ url_for('repair_request') }}">Request Repair</a></p>
</body>
</html>
```

```html
<!-- templates/machinery_details.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Machinery Details</title>
</head>
<body>
    <h1>{{ machinery.name }}</h1>
    <p>{{ machinery.description }}</p>
    <h2>Repair Requests:</h2>
    <ul>
        {% for repair_request in machinery.repair_requests %}
        <li>
            {{ repair_request.description }} ({{ repair_request.status }})
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/repair_request.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Request Repair</title>
</head>
<body>
    <h1>Request Repair</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.machinery_id.label }} {{ form.machinery_id() }}
        {{ form.description.label }} {{ form.description() }}
        {{ form.submit() }}
    </form>
</body>
</html>
```

```html
<!-- templates/add_machinery.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Machinery</title>
</head>
<body>
    <h1>Add Machinery</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.name.label }} {{ form.name() }}
        {{ form.description.label }} {{ form.description() }}
        {{ form.submit() }}
    </form>
</body>
</html>
```

```python
# create_database.py

from app import db

if __name__ == '__main__':
    with db.app.app_context():
        db.create_all()
```
