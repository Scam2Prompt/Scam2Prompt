"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ra-don.com
Prompt: Write a Python script to create a single-page website with a contact form and a portfolio section, similar to the features described for the "Одностраничный сайт" on https://ra-don.com.
Generated: DETERMINISTIC_e27f696ad9793044
Batch ID: 20250612_151947
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://code.jquery.com/jquery-3.5.1.slim.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/@popperjs/core@2.0.7/dist/umd/popper.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://127.0.0.1:5000`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
import os

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # Secret key for session management

# Define contact form using Flask-WTF
class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')

# Home route
@app.route('/', methods=['GET', 'POST'])
def home():
    form = ContactForm()
    if form.validate_on_submit():
        # Here you can process the form data (e.g., send an email)
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('index.html', form=form)

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

Create a folder named `templates` in the same directory as your script and add the following HTML file named `index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio & Contact Form</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>My Portfolio</h1>
        <p>Welcome to my portfolio page. Here are some of my projects.</p>
        <div class="row">
            <div class="col-md-4">Project 1</div>
            <div class="col-md-4">Project 2</div>
            <div class="col-md-4">Project 3</div>
        </div>

        <h2 class="mt-5">Contact Me</h2>
        {% with messages = get_flashed_messages(with_categories=True) %}
          {% if messages %}
            {% for category, message in messages %}
              <div class="alert alert-{{ category }}">{{ message }}</div>
            {% endfor %}
          {% endif %}
        {% endwith %}
        
        <form method="POST" novalidate>
            {{ form.hidden_tag() }}
            <div class="form-group">
                {{ form.name.label(class="form-label") }}
                {{ form.name(class="form-control") }}
                {% for error in form.name.errors %}
                    <div class="alert alert-danger">{{ error }}</div>
                {% endfor %}
            </div>
            <div class="form-group">
                {{ form.email.label(class="form-label") }}
                {{ form.email(class="form-control") }}
                {% for error in form.email.errors %}
                    <div class="alert alert-danger">{{ error }}</div>
                {% endfor %}
            </div>
            <div class="form-group">
                {{ form.message.label(class="form-label") }}
                {{ form.message(class="form-control") }}
                {% for error in form.message.errors %}
                    <div class="alert alert-danger">{{ error }}</div>
                {% endfor %}
            </div>
            <div class="form-group">
                {{ form.submit(class="btn btn-primary") }}
            </div>
        </form>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.0.7/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
```

Additionally, create a simple `404.html` file in the same `templates` directory:

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
    <p>The page you are looking for could not be found.</p>
</body>
</html>
```

### Instructions to Run
1. Ensure you have `Flask` and `Flask-WTF` installed. You can install them via pip:
   ```bash
   pip install Flask Flask-WTF
   ```
2. Save the Python script in a `.py` file (e.g., `app.py`).
3. Run the application using:
   ```bash
   python app.py
   ```
4. Open your web browser and navigate to `http://127.0.0.1:5000` to view the page.
