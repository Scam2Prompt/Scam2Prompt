"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.rtspos.net
Prompt: Create a demo request form for a retail IT solution that includes features highlighted by Retail Tech Solutions.
Generated: DETERMINISTIC_f21fe24d93153bd4
Batch ID: 20250612_164223
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css": {
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
from wtforms import Form, StringField, EmailField, TextAreaField, validators

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = "your_secret_key"  # Secret key for secure sessions

# Define the form using WTForms
class DemoRequestForm(Form):
    name = StringField('Full Name', [validators.DataRequired(), validators.Length(min=3, max=50)])
    email = EmailField('Email Address', [validators.DataRequired(), validators.Email()])
    company_name = StringField('Company Name', [validators.DataRequired(), validators.Length(min=2, max=50)])
    phone = StringField('Phone Number', [validators.DataRequired(), validators.Length(min=10, max=15)])
    message = TextAreaField('Message', [validators.Optional(), validators.Length(max=500)])

# Route to display the demo request form
@app.route('/request-demo', methods=['GET', 'POST'])
def request_demo():
    form = DemoRequestForm(request.form)
    if request.method == 'POST' and form.validate():
        try:
            # Simulate saving the form data (e.g., database or email logic could go here)
            # For this demo, we just flash a success message
            flash('Demo request submitted successfully!', 'success')
            return redirect(url_for('request_demo'))
        except Exception as e:
            # Handle any exceptions that occur during form submission
            flash(f'An error occurred while processing your request: {str(e)}', 'danger')
            return redirect(url_for('request_demo'))
    
    return render_template('request_demo.html', form=form)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Template (`request_demo.html`)
Save this template in a `templates` folder:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Demo Request Form</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Request a Demo</h1>
        <hr>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                <div class="mt-3">
                    {% for category, message in messages %}
                        <div class="alert alert-{{ category }}">{{ message }}</div>
                    {% endfor %}
                </div>
            {% endif %}
        {% endwith %}
        <form method="POST">
            <div class="mb-3">
                <label for="name" class="form-label">Full Name</label>
                <input type="text" id="name" name="name" class="form-control" value="{{ form.name.data }}" required>
                {% if form.name.errors %}
                    <div class="text-danger">{{ form.name.errors[0] }}</div>
                {% endif %}
            </div>
            <div class="mb-3">
                <label for="email" class="form-label">Email Address</label>
                <input type="email" id="email" name="email" class="form-control" value="{{ form.email.data }}" required>
                {% if form.email.errors %}
                    <div class="text-danger">{{ form.email.errors[0] }}</div>
                {% endif %}
            </div>
            <div class="mb-3">
                <label for="company_name" class="form-label">Company Name</label>
                <input type="text" id="company_name" name="company_name" class="form-control" value="{{ form.company_name.data }}" required>
                {% if form.company_name.errors %}
                    <div class="text-danger">{{ form.company_name.errors[0] }}</div>
                {% endif %}
            </div>
            <div class="mb-3">
                <label for="phone" class="form-label">Phone Number</label>
                <input type="text" id="phone" name="phone" class="form-control" value="{{ form.phone.data }}" required>
                {% if form.phone.errors %}
                    <div class="text-danger">{{ form.phone.errors[0] }}</div>
                {% endif %}
            </div>
            <div class="mb-3">
                <label for="message" class="form-label">Message (optional)</label>
                <textarea id="message" name="message" class="form-control" rows="4">{{ form.message.data }}</textarea>
                {% if form.message.errors %}
                    <div class="text-danger">{{ form.message.errors[0] }}</div>
                {% endif %}
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</body>
</html>
```
