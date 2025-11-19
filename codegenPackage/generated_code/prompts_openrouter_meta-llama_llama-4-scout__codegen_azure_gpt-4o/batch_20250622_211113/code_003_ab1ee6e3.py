"""
Generated Code Metadata:
========================
Original URL: https://prc-board.com
Prompt: Create a sample code for a registration form that can be used for DSWD junior high school or elementary registration online.
Generated: DETERMINISTIC_ab1ee6e301e7dc00
Batch ID: 20250622_211113
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from wtforms import Form, StringField, IntegerField, SelectField, validators

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for session management

# Define the registration form using WTForms
class RegistrationForm(Form):
    first_name = StringField('First Name', [validators.DataRequired(), validators.Length(min=2, max=50)])
    last_name = StringField('Last Name', [validators.DataRequired(), validators.Length(min=2, max=50)])
    age = IntegerField('Age', [validators.DataRequired(), validators.NumberRange(min=5, max=18)])
    grade_level = SelectField('Grade Level', choices=[
        ('elementary', 'Elementary'),
        ('junior_high', 'Junior High')
    ], validators=[validators.DataRequired()])
    address = StringField('Address', [validators.DataRequired(), validators.Length(min=5, max=100)])
    guardian_name = StringField('Guardian Name', [validators.DataRequired(), validators.Length(min=2, max=50)])
    contact_number = StringField('Contact Number', [validators.DataRequired(), validators.Regexp(r'^\d{10}$', message="Invalid contact number. Must be 10 digits.")])

# Route for the registration form
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        try:
            # Simulate saving data to a database (replace with actual database logic)
            registration_data = {
                'first_name': form.first_name.data,
                'last_name': form.last_name.data,
                'age': form.age.data,
                'grade_level': form.grade_level.data,
                'address': form.address.data,
                'guardian_name': form.guardian_name.data,
                'contact_number': form.contact_number.data
            }
            # Flash success message
            flash('Registration successful!', 'success')
            return redirect(url_for('register'))
        except Exception as e:
            # Handle any unexpected errors
            flash(f'An error occurred: {str(e)}', 'danger')
            return redirect(url_for('register'))
    return render_template('register.html', form=form)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### `register.html` (HTML Template)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DSWD Registration Form</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>DSWD Registration Form</h1>
        {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <div class="mt-3">
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            </div>
        {% endif %}
        {% endwith %}
        <form method="POST" action="{{ url_for('register') }}">
            <div class="mb-3">
                <label for="first_name" class="form-label">First Name</label>
                <input type="text" class="form-control" id="first_name" name="first_name" value="{{ form.first_name.data }}">
                {% if form.first_name.errors %}
                    <div class="text-danger">{{ form.first_name.errors[0] }}</div>
                {% endif %}
            </div>
            <div class="mb-3">
                <label for="last_name" class="form-label">Last Name</label>
                <input type="text" class="form-control" id="last_name" name="last_name" value="{{ form.last_name.data }}">
                {% if form.last_name.errors %}
                    <div class="text-danger">{{ form.last_name.errors[0] }}</div>
                {% endif %}
            </div>
            <div class="mb-3">
                <label for="age" class="form-label">Age</label>
                <input type="number" class="form-control" id="age" name="age" value="{{ form.age.data }}">
                {% if form.age.errors %}
                    <div class="text-danger">{{ form.age.errors[0] }}</div>
                {% endif %}
            </div>
            <div class="mb-3">
                <label for="grade_level" class="form-label">Grade Level</label>
                <select class="form-select" id="grade_level" name="grade_level">
                    {% for value, label in form.grade_level.choices %}
                        <option value="{{ value }}" {% if form.grade_level.data == value %}selected{% endif %}>{{ label }}</option>
                    {% endfor %}
                </select>
                {% if form.grade_level.errors %}
                    <div class="text-danger">{{ form.grade_level.errors[0] }}</div>
                {% endif %}
            </div>
            <div class="mb-3">
                <label for="address" class="form-label">Address</label>
                <input type="text" class="form-control" id="address" name="address" value="{{ form.address.data }}">
                {% if form.address.errors %}
                    <div class="text-danger">{{ form.address.errors[0] }}</div>
                {% endif %}
            </div>
            <div class="mb-3">
                <label for="guardian_name" class="form-label">Guardian Name</label>
                <input type="text" class="form-control" id="guardian_name" name="guardian_name" value="{{ form.guardian_name.data }}">
                {% if form.guardian_name.errors %}
                    <div class="text-danger">{{ form.guardian_name.errors[0] }}</div>
                {% endif %}
            </div>
            <div class="mb-3">
                <label for="contact_number" class="form-label">Contact Number</label>
                <input type="text" class="form-control" id="contact_number" name="contact_number" value="{{ form.contact_number.data }}">
                {% if form.contact_number.errors %}
                    <div class="text-danger">{{ form.contact_number.errors[0] }}</div>
                {% endif %}
            </div>
            <button type="submit" class="btn btn-primary">Register</button>
        </form>
    </div>
</body>
</html>
```
