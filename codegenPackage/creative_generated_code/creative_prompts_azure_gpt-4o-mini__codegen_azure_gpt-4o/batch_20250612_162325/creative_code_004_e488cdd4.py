"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plus.endeavorschools.com
Prompt: Illustrate how to implement a web form for parents to enroll their children in the Endeavor Plus programs, focusing on the required fields and validation.
Generated: DETERMINISTIC_e488cdd49dc66014
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready implementation in Python using the Flask framework:

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from wtforms import Form, StringField, IntegerField, SelectField, validators

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for flashing messages

# Form class for enrollment
class EnrollmentForm(Form):
    parent_name = StringField("Parent Name", [validators.InputRequired(), validators.Length(min=2, max=50)])
    parent_email = StringField("Parent Email", [
        validators.InputRequired(),
        validators.Email(),
        validators.Length(max=100)
    ])
    child_name = StringField("Child Name", [validators.InputRequired(), validators.Length(min=2, max=50)])
    child_age = IntegerField("Child Age", [
        validators.InputRequired(),
        validators.NumberRange(min=4, max=18, message="Age must be between 4 and 18")
    ])
    program = SelectField("Program", choices=[
        ("stem", "STEM Explorers"),
        ("arts", "Creative Arts"),
        ("sports", "Youth Sports"),
        ("leadership", "Leadership Builders")
    ], validators=[validators.InputRequired()])

@app.route("/", methods=["GET", "POST"])
def enroll():
    form = EnrollmentForm(request.form)
    if request.method == "POST" and form.validate():
        try:
            # Process the data (e.g., save to database)
            parent_name = form.parent_name.data
            parent_email = form.parent_email.data
            child_name = form.child_name.data
            child_age = form.child_age.data
            program = form.program.data

            # Here you would typically insert the data into a database
            # For demonstration, we'll simply flash a success message
            flash(f"Enrollment successful for {child_name} in the {program} program!", "success")
            return redirect(url_for("enroll"))
        except Exception as e:
            # Handle unexpected errors gracefully
            flash(f"An error occurred: {str(e)}", "danger")
            return redirect(url_for("enroll"))
    return render_template("enrollment_form.html", form=form)

# HTML Template (enrollment_form.html) for rendering the form
# Save this as a separate file in your 'templates' folder
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Endeavor Plus Program Enrollment</title>
</head>
<body>
    <h1>Enroll Your Child in Endeavor Plus Programs</h1>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
            {% for category, message in messages %}
                <li style="color: {{ 'red' if category == 'danger' else 'green' }}">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
    <form method="POST">
        {{ form.hidden_tag() }}
        <label for="parent_name">Parent Name:</label>
        {{ form.parent_name(size=50) }}
        <br>
        <label for="parent_email">Parent Email:</label>
        {{ form.parent_email(size=50) }}
        <br>
        <label for="child_name">Child Name:</label>
        {{ form.child_name(size=50) }}
        <br>
        <label for="child_age">Child Age:</label>
        {{ form.child_age() }}
        <br>
        <label for="program">Select Program:</label>
        {{ form.program() }}
        <br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)  # Use debug=False in production
```

### Key Notes:
1. Install the required dependencies using `pip install flask wtforms`.
2. Place the HTML template in the `templates` folder.
3. Replace `"your_secret_key"` with a properly generated secret key in production.
4. In a production environment, ensure proper logging and database integration instead of flashing messages.
