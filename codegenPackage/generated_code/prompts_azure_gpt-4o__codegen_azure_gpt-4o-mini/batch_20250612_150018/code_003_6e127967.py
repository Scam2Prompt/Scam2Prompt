"""
Generated Code Metadata:
========================
Original URL: https://isoplas.com
Prompt: Write code to automate the generation of contact forms for a packaging manufacturer, including fields for product inquiries about ABS Atlas trays and bakery trays, as described on Isoplas Corporation's website.
Generated: DETERMINISTIC_6e127967ec31037f
Batch ID: 20250612_150018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key

# Define the contact form using Flask-WTF
class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    product_type = SelectField('Product Type', choices=[
        ('ABS Atlas Tray', 'ABS Atlas Tray'),
        ('Bakery Tray', 'Bakery Tray')
    ], validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Here you would typically handle the form submission, e.g., save to a database or send an email
        try:
            # Simulate processing the form data
            name = form.name.data
            email = form.email.data
            product_type = form.product_type.data
            message = form.message.data
            
            # Log or process the data (e.g., save to a database)
            print(f"Received inquiry from {name} ({email}) about {product_type}: {message}")
            
            flash('Your inquiry has been submitted successfully!', 'success')
            return redirect(url_for('contact'))
        except Exception as e:
            # Handle any errors that occur during processing
            flash(f'An error occurred: {str(e)}', 'danger')
    
    return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

**HTML Template (contact.html)**

```html
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
        <div>
            {{ form.name.label }}<br>
            {{ form.name(size=32) }}<br>
            {% for error in form.name.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.email.label }}<br>
            {{ form.email(size=32) }}<br>
            {% for error in form.email.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.product_type.label }}<br>
            {{ form.product_type() }}<br>
            {% for error in form.product_type.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.message.label }}<br>
            {{ form.message(cols=30, rows=5) }}<br>
            {% for error in form.message.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.submit() }}
        </div>
    </form>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
            {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</body>
</html>
```

**Requirements:**
- Install Flask and Flask-WTF using pip:
```bash
pip install Flask Flask-WTF
```

**Run the application:**
- Save the Python code in a file (e.g., `app.py`) and the HTML code in a folder named `templates` as `contact.html`.
- Run the application with:
```bash
python app.py
```
