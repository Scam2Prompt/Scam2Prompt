"""
Generated Code Metadata:
========================
Original URL: https://claim.manatoken.net
Prompt: How can I build a web application that mimics the functionality of Stumble! for discovering and rating websites?
Generated: DETERMINISTIC_eb957733f580229a
Batch ID: 20250612_160633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Stumble!-like Web Application**
=====================================

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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stumble.db'
db = SQLAlchemy(app)


class Website(db.Model):
    """Represents a website in the database."""
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(100), unique=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f"Website('{self.url}', '{self.title}')"


class RatingForm(FlaskForm):
    """Form for rating a website."""
    rating = IntegerField('Rating (1-5)', validators=[DataRequired()])
    submit = SubmitField('Rate')


@app.route('/')
def index():
    """Displays a list of websites."""
    websites = Website.query.all()
    return render_template('index.html', websites=websites)


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    """Handles website submission."""
    form = WebsiteForm()
    if form.validate_on_submit():
        website = Website(url=form.url.data, title=form.title.data, description=form.description.data)
        db.session.add(website)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('submit.html', form=form)


@app.route('/rate/<int:website_id>', methods=['GET', 'POST'])
def rate(website_id):
    """Handles rating a website."""
    website = Website.query.get_or_404(website_id)
    form = RatingForm()
    if form.validate_on_submit():
        website.rating = form.rating.data
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('rate.html', website=website, form=form)


@app.errorhandler(404)
def not_found(error):
    """Handles 404 errors."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
```

```python
# forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class WebsiteForm(FlaskForm):
    """Form for submitting a website."""
    url = StringField('URL', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Stumble!-like Web Application</title>
  </head>
  <body>
    <h1>Websites</h1>
    <ul>
    {% for website in websites %}
      <li>
        <a href="{{ website.url }}">{{ website.title }}</a>
        ({{ website.rating }}/5)
        <a href="{{ url_for('rate', website_id=website.id) }}">Rate</a>
      </li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('submit') }}">Submit a website</a></p>
  </body>
</html>
```

```html
<!-- templates/submit.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Submit a Website</title>
  </head>
  <body>
    <h1>Submit a Website</h1>
    <form method="POST">
      {{ form.hidden_tag() }}
      {{ form.url.label }} {{ form.url() }}
      {{ form.title.label }} {{ form.title() }}
      {{ form.description.label }} {{ form.description() }}
      {{ form.submit() }}
    </form>
  </body>
</html>
```

```html
<!-- templates/rate.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Rate a Website</title>
  </head>
  <body>
    <h1>Rate a Website</h1>
    <p>{{ website.title }} ({{ website.url }})</p>
    <form method="POST">
      {{ form.hidden_tag() }}
      {{ form.rating.label }} {{ form.rating() }}
      {{ form.submit() }}
    </form>
  </body>
</html>
```

```html
<!-- templates/404.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>404 Error</title>
  </head>
  <body>
    <h1>404 Error</h1>
    <p>Page not found.</p>
  </body>
</html>
```

```bash
# Run the application
flask db init
flask db migrate
flask db upgrade
python app.py
```
