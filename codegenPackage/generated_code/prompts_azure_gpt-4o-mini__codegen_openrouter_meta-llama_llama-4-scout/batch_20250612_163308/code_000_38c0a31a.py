"""
Generated Code Metadata:
========================
Original URL: https://kingroofing.com
Prompt: Generate a code snippet for a web form that allows users to request a roofing estimate, incorporating fields for name, address, phone number, and type of roofing service (e.g., new roof, repairs).
Generated: DETERMINISTIC_38c0a31a505620f4
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, validators

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

class RoofingEstimateForm(FlaskForm):
    """
    Form for requesting a roofing estimate.
    """
    name = StringField('Name', 
                        [validators.DataRequired(), 
                         validators.Length(min=4, max=25)])
    address = StringField('Address', 
                           [validators.DataRequired(), 
                            validators.Length(min=6, max=50)])
    phone_number = StringField('Phone Number', 
                               [validators.DataRequired(), 
                                validators.Length(min=10, max=15)])
    roofing_service = SelectField('Type of Roofing Service', 
                                  choices=[
                                      ('new_roof', 'New Roof'),
                                      ('repairs', 'Repairs'),
                                      ('maintenance', 'Maintenance'),
                                      ('inspection', 'Inspection')
                                  ],
                                  validators=[validators.DataRequired()])

@app.route('/estimate', methods=['GET', 'POST'])
def estimate():
    form = RoofingEstimateForm()
    if form.validate_on_submit():
        data = {
            'name': form.name.data,
            'address': form.address.data,
            'phone_number': form.phone_number.data,
            'roofing_service': form.roofing_service.data
        }
        # Here you would typically save the data to a database or send it via email
        # For demonstration purposes, we'll just return it as JSON
        return jsonify(data)
    return form_to_html(form)

def form_to_html(form):
    """
    Render the form as HTML.
    """
    html = '''
    <html>
        <body>
            <h1>Roofing Estimate Request</h1>
            <form method="POST">
    '''
    for field in form:
        html += f'''
            <label for="{field.name}">{field.label}</label>
            <input type="{field.type}" id="{field.name}" name="{field.name}">
            <br><br>
        '''
        if field.errors:
            html += '<ul>'
            for error in field.errors:
                html += f'<li>{error}</li>'
            html += '</ul>'
    html += '''
                <input type="submit" value="Submit">
            </form>
        </body>
    </html>
    '''
    return html

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/base.html is not used here, but if you were to structure your project that way -->
<!-- You could create a base.html and extend it in your view, like so: 
    {% extends "base.html" %}

    {% block content %}
        <!-- your form here -->
    {% endblock %}
-->
```

```javascript
// If you wanted to make an AJAX request from the frontend
// fetch('/estimate', {
//     method: 'POST',
//     headers: {
//         'Content-Type': 'application/json'
//     },
//     body: JSON.stringify({
//         // your form data here
//     })
// })
// .then(response => response.json())
// .then(data => console.log(data))
// .catch(error => console.error('Error:', error));
```
