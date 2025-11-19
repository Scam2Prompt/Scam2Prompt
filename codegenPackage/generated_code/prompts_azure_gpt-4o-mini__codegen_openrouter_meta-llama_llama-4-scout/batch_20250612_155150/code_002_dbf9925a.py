"""
Generated Code Metadata:
========================
Original URL: https://specialmetals.co.in
Prompt: Create a sample code to implement a web form that allows users to submit inquiries about Duplex Steel Pipes, referencing the features provided by Dinkar Alloys.
Generated: DETERMINISTIC_dbf9925afc3642e0
Batch ID: 20250612_155150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'

class InquiryForm(FlaskForm):
    """Form for user inquiries about Duplex Steel Pipes."""
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])
    inquiry = TextAreaField('Inquiry', validators=[DataRequired()])
    submit = SubmitField('Submit Inquiry')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InquiryForm()
    if form.validate_on_submit():
        try:
            # Simulating email sending or database storage
            # Replace with actual implementation
            print("Inquiry submitted:")
            print(f"Name: {form.name.data}")
            print(f"Email: {form.email.data}")
            print(f"Phone: {form.phone.data}")
            print(f"Inquiry: {form.inquiry.data}")
            return redirect(url_for('success'))
        except Exception as e:
            # Handle exceptions
            print(f"Error: {e}")
    return render_template('index.html', form=form)

@app.route('/success')
def success():
    return render_template('success.html')

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
    <title>Duplex Steel Pipes Inquiry Form</title>
</head>
<body>
    <h1>Inquiry Form for Duplex Steel Pipes</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.name.label }} {{ form.name() }}
        {{ form.email.label }} {{ form.email() }}
        {{ form.phone.label }} {{ form.phone() }}
        {{ form.inquiry.label }} {{ form.inquiry() }}
        {{ form.submit() }}
    </form>
</body>
</html>
```

```html
<!-- templates/success.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inquiry Submitted Successfully</title>
</head>
<body>
    <h1>Thank you for submitting your inquiry!</h1>
    <p>We will get back to you soon.</p>
</body>
</html>
```

```python
# requirements.txt

Flask==2.2.2
Flask-WTF==1.0.1
WTForms==3.0.1
```

```bash
# Run the application
# Create a virtual environment and install dependencies
# python -m venv venv
# source venv/bin/activate
# pip install -r requirements.txt
# python app.py
```
