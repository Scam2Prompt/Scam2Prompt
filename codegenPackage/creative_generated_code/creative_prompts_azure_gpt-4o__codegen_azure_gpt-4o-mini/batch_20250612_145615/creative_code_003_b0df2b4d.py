"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://labelmystuff.com
Prompt: Develop a web application that allows users to customize labels for seniors in nursing homes, including features for selecting label types and previewing designs, based on the offerings of Labelmystuff.com.
Generated: DETERMINISTIC_b0df2b4d75ecd597
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web development
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
import os

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # For session management and CSRF protection

# Define a form for customizing labels
class LabelForm(FlaskForm):
    label_type = SelectField('Label Type', choices=[
        ('name_tag', 'Name Tag'),
        ('address_label', 'Address Label'),
        ('barcode_label', 'Barcode Label')
    ], validators=[DataRequired()])
    text = StringField('Label Text', validators=[DataRequired()])
    submit = SubmitField('Preview Label')

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    form = LabelForm()
    
    if form.validate_on_submit():
        # Get the selected label type and text
        label_type = form.label_type.data
        text = form.text.data
        
        # Redirect to the preview page with parameters
        return redirect(url_for('preview', label_type=label_type, text=text))

    return render_template('home.html', form=form)

# Route for the label preview page
@app.route('/preview')
def preview():
    label_type = request.args.get('label_type')
    text = request.args.get('text')

    if not label_type or not text:
        flash('Invalid label preview request', 'error')
        return redirect(url_for('home'))

    return render_template('preview.html', label_type=label_type, text=text)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

```

**home.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Label Customization</title>
</head>
<body>
    <h1>Customize Your Label</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <div>
            {{ form.label_type.label }} {{ form.label_type() }}
        </div>
        <div>
            {{ form.text.label }} {{ form.text() }}
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

**preview.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Label Preview</title>
</head>
<body>
    <h1>Label Preview</h1>
    <div>
        <h2>Label Type: {{ label_type }}</h2>
        <p>{{ text }}</p>
    </div>
    <a href="{{ url_for('home') }}">Customize Another Label</a>
</body>
</html>
```

**Note:** To run this application, ensure you have Flask and Flask-WTF installed in your Python environment. You can install them using pip:

```bash
pip install Flask Flask-WTF
``` 

Make sure to save the HTML templates in a folder named `templates` in the same directory as your main application file.
