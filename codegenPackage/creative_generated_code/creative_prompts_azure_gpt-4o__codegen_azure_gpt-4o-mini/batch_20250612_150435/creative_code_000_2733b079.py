"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://piclink.me
Prompt: Write code to generate a customizable bio link page using a service like PicLink, allowing users to add links to their social media and websites.
Generated: DETERMINISTIC_2733b0793fdbbe2b
Batch ID: 20250612_150435
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
from wtforms import Form, StringField, SubmitField, validators
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the app with a SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)  # Generates a random secret key for session management

# Initialize the database
db = SQLAlchemy(app)

# Define a model for the bio link entries
class BioLink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<BioLink {self.title}: {self.url}>'

# Create a form for adding new links
class BioLinkForm(Form):
    title = StringField('Link Title', [validators.Length(min=1, max=100)])
    url = StringField('Link URL', [validators.Length(min=1, max=255), validators.URL()])
    submit = SubmitField('Add Link')

# Route for displaying the bio link page
@app.route('/')
def index():
    links = BioLink.query.all()  # Fetch all links from the database
    return render_template('index.html', links=links)

# Route for adding a new link
@app.route('/add', methods=['GET', 'POST'])
def add_link():
    form = BioLinkForm(request.form)
    if request.method == 'POST' and form.validate():
        # Create a new link
        new_link = BioLink(title=form.title.data, url=form.url.data)
        try:
            db.session.add(new_link)  # Add the new link to the session
            db.session.commit()  # Commit the session to save the link
            flash('Link added successfully!', 'success')
            return redirect(url_for('index'))  # Redirect to the main page
        except Exception as e:
            db.session.rollback()  # Rollback in case of any errors
            flash(f'Error adding link: {str(e)}', 'danger')
    return render_template('add_link.html', form=form)

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Main block to run the application
if __name__ == '__main__':
    db.create_all()  # Create the database tables if they do not exist
    app.run(debug=True)  # Start the Flask application in debug mode
```

### HTML Templates

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bio Link Page</title>
</head>
<body>
    <h1>Your Bio Links</h1>
    <ul>
        {% for link in links %}
            <li><a href="{{ link.url }}" target="_blank">{{ link.title }}</a></li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('add_link') }}">Add a new link</a>
</body>
</html>
```

**add_link.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add a Bio Link</title>
</head>
<body>
    <h1>Add a Bio Link</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <div>
            {{ form.title.label }}<br>
            {{ form.title(size=32) }}<br>
            {% for error in form.title.errors %}
                <span>{{ error }}</span>
            {% endfor %}
        </div>
        <div>
            {{ form.url.label }}<br>
            {{ form.url(size=32) }}<br>
            {% for error in form.url.errors %}
                <span>{{ error }}</span>
            {% endfor %}
        </div>
        <div>
            {{ form.submit() }}
        </div>
    </form>
    <a href="{{ url_for('index') }}">Back to Links</a>
</body>
</html>
```

**404.html**
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
    <a href="{{ url_for('index') }}">Return Home</a>
</body>
</html>
```

### Requirements
Make sure to install the necessary packages using pip:
```bash
pip install Flask Flask-SQLAlchemy Flask-WTF
```
