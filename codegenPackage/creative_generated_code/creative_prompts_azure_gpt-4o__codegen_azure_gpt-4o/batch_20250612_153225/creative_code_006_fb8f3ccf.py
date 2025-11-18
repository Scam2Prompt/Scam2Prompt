"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://efeitoharmonie.com.br
Prompt: Suggest tools or libraries for creating a virtual consultation form for hair transplant clinics, inspired by the contact form on the Efeito Harmonie website.
Generated: DETERMINISTIC_fb8f3ccf29509ad6
Batch ID: 20250612_153225
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Certainly! Below is an example of a clean, production-ready implementation in Python using the Flask framework for creating a virtual consultation form. It uses WTForms for form validation and email sending via Flask-Mail.

```python
from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
from wtforms import Form, StringField, TextAreaField, IntegerField, SelectField, validators

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a strong secret key

# Configuration for email
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Update with your SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'  # Update with your email
app.config['MAIL_PASSWORD'] = 'your_email_password'  # Update with your email password
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@example.com'  # Update with sender email
mail = Mail(app)

# Consultation form using WTForms
class ConsultationForm(Form):
    name = StringField('Full Name', [validators.DataRequired(), validators.Length(min=3, max=50)])
    email = StringField('Email Address', [validators.DataRequired(), validators.Email(message='Invalid email format')])
    phone = StringField('Phone Number', [validators.DataRequired(), validators.Length(min=10, max=15)])
    age = IntegerField('Age', [validators.DataRequired(), validators.NumberRange(min=18, max=100, message="Age must be between 18 and 100")])
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], validators=[validators.DataRequired()])
    concerns = TextAreaField('Hair Concerns/Description', [validators.DataRequired(), validators.Length(max=500)])

@app.route('/', methods=['GET', 'POST'])
def consultation_form():
    form = ConsultationForm(request.form)
    
    if request.method == 'POST' and form.validate():
        try:
            # Send email with consultation details
            msg = Message('Hair Transplant Consultation Request', recipients=['clinic_email@example.com'])  # Update recipient email
            msg.body = (
                f"Name: {form.name.data}\n"
                f"Email: {form.email.data}\n"
                f"Phone: {form.phone.data}\n"
                f"Age: {form.age.data}\n"
                f"Gender: {form.gender.data}\n"
                f"Concerns: {form.concerns.data}"
            )
            mail.send(msg)
            flash('Your consultation request has been submitted successfully!', 'success')
            return redirect('/')
        except Exception as e:
            # Log the error and show a message to the user
            app.logger.error(f"Error sending email: {e}")
            flash('An error occurred while submitting your request. Please try again later.', 'danger')
    
    return render_template('form.html', form=form)

# HTML template (place in a file named 'templates/form.html')
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hair Transplant Consultation Form</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css">
</head>
<body>
<div class="container mt-5">
    <h1>Hair Transplant Consultation Form</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <div class="mb-3">
            <label for="name" class="form-label">Full Name</label>
            {{ form.name(class="form-control") }}
        </div>
        <div class="mb-3">
            <label for="email" class="form-label">Email Address</label>
            {{ form.email(class="form-control") }}
        </div>
        <div class="mb-3">
            <label for="phone" class="form-label">Phone Number</label>
            {{ form.phone(class="form-control") }}
        </div>
        <div class="mb-3">
            <label for="age" class="form-label">Age</label>
            {{ form.age(class="form-control") }}
        </div>
        <div class="mb-3">
            <label for="gender" class="form-label">Gender</label>
            {{ form.gender(class="form-control") }}
        </div>
        <div class="mb-3">
            <label for="concerns" class="form-label">Hair Concerns/Description</label>
            {{ form.concerns(class="form-control", rows="4") }}
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <div class="mt-3">
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            </div>
        {% endif %}
    {% endwith %}
</div>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)
```

Ensure you update placeholders like SMTP server, sender email, and recipient email with proper values before deploying the code.
