"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://distribution-menuiserie.fr
Prompt: Generate a code snippet for a web application that allows users to request a quote for high-quality windows and doors from a menu distribution service in Oise and Val d'Oise.
Generated: DETERMINISTIC_f85acc57e15a4c0a
Batch ID: 20250612_140107
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
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
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_mail import Mail, Message

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key for production

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Replace with your SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'your_password'  # Replace with your password
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@example.com'
mail = Mail(app)

# Define a form for the quote request
class QuoteRequestForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    product_type = SelectField('Product Type', choices=[('windows', 'Windows'), ('doors', 'Doors')], validators=[DataRequired()])
    message = TextAreaField('Additional Information', validators=[DataRequired()])
    submit = SubmitField('Request Quote')

# Home route to display the quote request form
@app.route('/', methods=['GET', 'POST'])
def index():
    form = QuoteRequestForm()
    if form.validate_on_submit():
        try:
            # Send email with the quote request
            msg = Message("Quote Request from {}".format(form.name.data))
            msg.body = f"Name: {form.name.data}\nEmail: {form.email.data}\nProduct Type: {form.product_type.data}\nMessage: {form.message.data}"
            mail.send(msg)
            flash('Your request has been sent! We will get back to you shortly.', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash('An error occurred while sending your request. Please try again later.', 'danger')
            app.logger.error(f"Error sending email: {e}")
    
    return render_template('index.html', form=form)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- Save this as templates/index.html -->
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Request a Quote</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>Request a Quote for Windows and Doors</h1>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        <form method="POST">
            {{ form.hidden_tag() }}
            <div class="form-group">
                {{ form.name.label(class="form-label") }}
                {{ form.name(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.email.label(class="form-label") }}
                {{ form.email(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.product_type.label(class="form-label") }}
                {{ form.product_type(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.message.label(class="form-label") }}
                {{ form.message(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.submit(class="btn btn-primary") }}
            </div>
        </form>
    </div>
</body>
</html>
```
