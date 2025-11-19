"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://passive-income.online
Prompt: Create a simple web application using Flask that allows users to input their income streams and calculates their total monthly income, inspired by the Wealthery training program.
Generated: DETERMINISTIC_03183ab8b7e5dfff
Batch ID: 20250612_160526
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://code.jquery.com/jquery-3.5.1.slim.min.js": {
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
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js": {
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
from flask import Flask, request, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField, ValidationError
from wtforms.validators import DataRequired, NumberRange
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key')

# Form class for income input
class IncomeForm(FlaskForm):
    income_stream = DecimalField('Income Stream', validators=[DataRequired(), NumberRange(min=0, message="Income must be a positive number.")])
    submit = SubmitField('Add Income')

# Store income streams in a list
income_streams = []

@app.route('/', methods=['GET', 'POST'])
def index():
    form = IncomeForm()
    if form.validate_on_submit():
        income = form.income_stream.data
        income_streams.append(income)
        flash(f'Added income stream: ${income:.2f}', 'success')
        return redirect(url_for('index'))
    
    total_income = sum(income_streams)  # Calculate total income
    return render_template('index.html', form=form, total_income=total_income, income_streams=income_streams)

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handling for 500
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (`templates/index.html`):**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Income Calculator</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
<div class="container">
    <h1 class="mt-5">Monthly Income Calculator</h1>
    <form method="POST" class="mt-4">
        {{ form.hidden_tag() }}
        <div class="form-group">
            {{ form.income_stream.label(class="form-label") }}
            {{ form.income_stream(class="form-control") }}
            {% for error in form.income_stream.errors %}
                <div class="alert alert-danger">{{ error }}</div>
            {% endfor %}
        </div>
        <div class="form-group">
            {{ form.submit(class="btn btn-primary") }}
        </div>
    </form>

    <h2 class="mt-5">Total Monthly Income: ${{ total_income }}</h2>
    <h3>Income Streams:</h3>
    <ul>
        {% for income in income_streams %}
            <li>${{ income }}</li>
        {% endfor %}
    </ul>
</div>
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.0.7/dist/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
```

**Additional error pages (`templates/404.html` and `templates/500.html`):**

**404 Page (`templates/404.html`):**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, but the page you were looking for could not be found.</p>
</body>
</html>
```

**500 Page (`templates/500.html`):**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>We're sorry, but something went wrong on our end.</p>
</body>
</html>
```

Make sure to install the necessary packages with:
```bash
pip install Flask Flask-WTF
```

To run the application, save the code in appropriate files and execute the Python script. Ensure your environment is set up for Flask development.
