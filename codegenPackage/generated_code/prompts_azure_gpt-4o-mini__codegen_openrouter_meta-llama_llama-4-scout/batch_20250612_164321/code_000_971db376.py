"""
Generated Code Metadata:
========================
Original URL: https://gyvseguros.com
Prompt: Generate a code snippet for a web form that allows users to request a quote for different types of insurance policies such as auto, health, and life insurance as described on the GYV Seguros website.
Generated: DETERMINISTIC_971db376c3c26dfc
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Define insurance types
insurance_types = [
    'Auto Insurance',
    'Health Insurance',
    'Life Insurance'
]

# Define quote request form
class QuoteRequestForm(FlaskForm):
    """Quote request form"""
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    insurance_type = SelectField('Insurance Type', choices=[(i, i) for i in insurance_types])
    submit = SubmitField('Request Quote')

# Define route for index page
@app.route('/', methods=['GET', 'POST'])
def index():
    """Index page with quote request form"""
    form = QuoteRequestForm()
    if form.validate_on_submit():
        # Get form data
        name = form.name.data
        email = form.email.data
        phone = form.phone.data
        insurance_type = form.insurance_type.data

        # Process quote request (e.g., send to server or database)
        try:
            # Simulate quote request processing
            quote_request = {
                'name': name,
                'email': email,
                'phone': phone,
                'insurance_type': insurance_type
            }
            # In a real app, you'd send this data to a server or database
            print(quote_request)

            # Return success response
            return jsonify({'success': True, 'message': 'Quote request sent successfully!'})
        except Exception as e:
            # Return error response
            return jsonify({'success': False, 'message': str(e)})

    return render_template('index.html', form=form)

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
    <title>Quote Request Form</title>
</head>
<body>
    <h1>Quote Request Form</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.name.label }} {{ form.name() }}
        {{ form.email.label }} {{ form.email() }}
        {{ form.phone.label }} {{ form.phone() }}
        {{ form.insurance_type.label }} {{ form.insurance_type() }}
        {{ form.submit() }}
    </form>

    <script>
        // Handle form submission
        const form = document.querySelector('form');
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(form);
            try {
                const response = await fetch('/', {
                    method: 'POST',
                    body: formData
                });
                const data = await response.json();
                if (data.success) {
                    console.log(data.message);
                    // Handle success
                } else {
                    console.error(data.message);
                    // Handle error
                }
            } catch (error) {
                console.error(error);
            }
        });
    </script>
</body>
</html>
```

```javascript
// Alternatively, you could use JavaScript with a library like Axios to send the form data
// and handle the response.

// Using Axios
import axios from 'axios';

// Handle form submission
const form = document.querySelector('form');
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    try {
        const response = await axios.post('/', formData);
        if (response.data.success) {
            console.log(response.data.message);
            // Handle success
        } else {
            console.error(response.data.message);
            // Handle error
        }
    } catch (error) {
        console.error(error);
    }
});
```
