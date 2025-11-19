"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harda-ke.org
Prompt: Generate a code snippet for a web application that allows users to donate to HARDA's projects focused on water and sanitation in the Horn of Africa.
Generated: DETERMINISTIC_c071d5e5a43bfb97
Batch ID: 20250612_155916
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
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
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Form for donation
class DonationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    email = StringField('Email', validators=[DataRequired()])
    amount = DecimalField('Donation Amount ($)', validators=[DataRequired(), NumberRange(min=1)], places=2)
    message = TextAreaField('Message', validators=[Length(max=500)])
    submit = SubmitField('Donate')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = DonationForm()
    
    if form.validate_on_submit():
        try:
            # Process the donation information
            name = form.name.data
            email = form.email.data
            amount = form.amount.data
            message = form.message.data
            
            # Log donation information (in a real application, save to DB or payment processing)
            logging.info(f"Donation received: Name={name}, Email={email}, Amount=${amount}, Message={message}")
            
            flash('Thank you for your donation!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            logging.error(f"Error processing donation: {e}")
            flash('An error occurred while processing your donation. Please try again.', 'danger')
    
    return render_template('donate.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
```

**Template (donate.html):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Donate to HARDA</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Donate to HARDA</h1>
        <p>Your support helps improve water and sanitation in the Horn of Africa.</p>
        
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                <div class="alert alert-dismissible fade show mt-3" role="alert">
                    {% for category, message in messages %}
                        <div class="alert alert-{{ category }}">{{ message }}</div>
                    {% endfor %}
                </div>
            {% endif %}
        {% endwith %}
        
        <form method="POST" class="mt-3">
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
                {{ form.amount.label(class="form-label") }}
                {{ form.amount(class="form-control") }}
                {% for error in form.amount.errors %}
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
</body>
</html>
```
