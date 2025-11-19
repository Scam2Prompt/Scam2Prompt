"""
Generated Code Metadata:
========================
Original URL: https://www.gpt-chat.info
Prompt: Write a code snippet for a contact form that handles errors, inspired by the "Lỗi: Không tìm thấy biểu mẫu liên hệ" message on the GPT-Chat page.
Generated: DETERMINISTIC_59046b636abc2043
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# contact_form.py

from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

class ContactForm(FlaskForm):
    """Contact form with name, email, and message fields."""
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Handle contact form submission."""
    form = ContactForm()
    if form.validate_on_submit():
        try:
            # Replace with your email sending logic
            print("Form submitted successfully:")
            print(f"Name: {form.name.data}")
            print(f"Email: {form.email.data}")
            print(f"Message: {form.message.data}")
            return render_template('contact.html', form=form, success=True)
        except Exception as e:
            # Log the error
            print(f"Error sending email: {str(e)}")
            return render_template('contact.html', form=form, error="Error sending message. Please try again.")
    return render_template('contact.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/contact.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.name.label }} {{ form.name() }}
        {% for error in form.name.errors %}
            <span style="color: red;">[{{ error }}]</span>
        {% endfor %}
        {{ form.email.label }} {{ form.email() }}
        {% for error in form.email.errors %}
            <span style="color: red;">[{{ error }}]</span>
        {% endfor %}
        {{ form.message.label }} {{ form.message() }}
        {% for error in form.message.errors %}
            <span style="color: red;">[{{ error }}]</span>
        {% endfor %}
        {{ form.submit() }}
    </form>
    {% if success %}
        <p style="color: green;">Message sent successfully!</p>
    {% elif error %}
        <p style="color: red;">{{ error }}</p>
    {% endif %}
</body>
</html>
```
