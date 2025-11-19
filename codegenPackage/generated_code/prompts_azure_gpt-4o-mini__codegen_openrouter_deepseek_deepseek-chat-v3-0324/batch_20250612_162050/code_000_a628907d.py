"""
Generated Code Metadata:
========================
Original URL: https://nellyservis.sk
Prompt: Generate a code snippet for a web application that allows users to request a quote for window installation services, similar to the offerings on NellyServis.
Generated: DETERMINISTIC_a628907d6c5e10f8
Batch ID: 20250612_162050
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js": {
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
from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, validators
import logging
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Should be changed in production

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class QuoteRequestForm(FlaskForm):
    """Form for requesting a window installation quote."""
    name = StringField('Full Name', validators=[validators.InputRequired()])
    email = StringField('Email', validators=[validators.InputRequired(), validators.Email()])
    phone = StringField('Phone Number', validators=[validators.InputRequired()])
    address = StringField('Address', validators=[validators.InputRequired()])
    window_type = SelectField('Window Type', choices=[
        ('single', 'Single Pane'),
        ('double', 'Double Pane'),
        ('triple', 'Triple Pane'),
        ('custom', 'Custom')
    ], validators=[validators.InputRequired()])
    quantity = IntegerField('Number of Windows', validators=[
        validators.InputRequired(),
        validators.NumberRange(min=1, max=100)
    ])
    width = IntegerField('Width (cm)', validators=[
        validators.InputRequired(),
        validators.NumberRange(min=50, max=300)
    ])
    height = IntegerField('Height (cm)', validators=[
        validators.InputRequired(),
        validators.NumberRange(min=50, max=300)
    ])
    additional_notes = StringField('Additional Notes')

@app.route('/', methods=['GET', 'POST'])
def request_quote():
    """Handle quote requests."""
    form = QuoteRequestForm()
    
    if request.method == 'POST' and form.validate():
        try:
            # Process the form data
            quote_data = {
                'timestamp': datetime.now().isoformat(),
                'name': form.name.data,
                'email': form.email.data,
                'phone': form.phone.data,
                'address': form.address.data,
                'window_type': form.window_type.data,
                'quantity': form.quantity.data,
                'width': form.width.data,
                'height': form.height.data,
                'additional_notes': form.additional_notes.data
            }
            
            # In a real application, you would:
            # 1. Save to database
            # 2. Send confirmation email
            # 3. Calculate quote price
            
            logger.info(f"New quote request received: {quote_data}")
            
            return jsonify({
                'status': 'success',
                'message': 'Your quote request has been received. We will contact you shortly.'
            })
        
        except Exception as e:
            logger.error(f"Error processing quote request: {str(e)}")
            return jsonify({
                'status': 'error',
                'message': 'An error occurred while processing your request. Please try again later.'
            }), 500
    
    # For GET requests or invalid POST, render the form
    return render_template('quote_form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/quote_form.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Window Installation Quote Request</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1 class="mb-4">Window Installation Quote Request</h1>
        
        <form id="quoteForm" method="POST" novalidate>
            {{ form.hidden_tag() }}
            
            <div class="mb-3">
                {{ form.name.label(class="form-label") }}
                {{ form.name(class="form-control") }}
                {% for error in form.name.errors %}
                    <div class="invalid-feedback" style="display: block;">{{ error }}</div>
                {% endfor %}
            </div>
            
            <div class="mb-3">
                {{ form.email.label(class="form-label") }}
                {{ form.email(class="form-control") }}
                {% for error in form.email.errors %}
                    <div class="invalid-feedback" style="display: block;">{{ error }}</div>
                {% endfor %}
            </div>
            
            <div class="mb-3">
                {{ form.phone.label(class="form-label") }}
                {{ form.phone(class="form-control") }}
                {% for error in form.phone.errors %}
                    <div class="invalid-feedback" style="display: block;">{{ error }}</div>
                {% endfor %}
            </div>
            
            <div class="mb-3">
                {{ form.address.label(class="form-label") }}
                {{ form.address(class="form-control") }}
                {% for error in form.address.errors %}
                    <div class="invalid-feedback" style="display: block;">{{ error }}</div>
                {% endfor %}
            </div>
            
            <div class="mb-3">
                {{ form.window_type.label(class="form-label") }}
                {{ form.window_type(class="form-select") }}
                {% for error in form.window_type.errors %}
                    <div class="invalid-feedback" style="display: block;">{{ error }}</div>
                {% endfor %}
            </div>
            
            <div class="row mb-3">
                <div class="col-md-4">
                    {{ form.quantity.label(class="form-label") }}
                    {{ form.quantity(class="form-control") }}
                    {% for error in form.quantity.errors %}
                        <div class="invalid-feedback" style="display: block;">{{ error }}</div>
                    {% endfor %}
                </div>
                <div class="col-md-4">
                    {{ form.width.label(class="form-label") }}
                    {{ form.width(class="form-control") }}
                    {% for error in form.width.errors %}
                        <div class="invalid-feedback" style="display: block;">{{ error }}</div>
                    {% endfor %}
                </div>
                <div class="col-md-4">
                    {{ form.height.label(class="form-label") }}
                    {{ form.height(class="form-control") }}
                    {% for error in form.height.errors %}
                        <div class="invalid-feedback" style="display: block;">{{ error }}</div>
                    {% endfor %}
                </div>
            </div>
            
            <div class="mb-3">
                {{ form.additional_notes.label(class="form-label") }}
                {{ form.additional_notes(class="form-control", rows="3") }}
            </div>
            
            <button type="submit" class="btn btn-primary">Request Quote</button>
        </form>
        
        <div id="responseMessage" class="mt-3"></div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        document.getElementById('quoteForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const form = e.target;
            const formData = new FormData(form);
            const responseDiv = document.getElementById('responseMessage');
            
            try {
                const response = await fetch('/', {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'Accept': 'application/json'
                    }
                });
                
                const data = await response.json();
                
                if (data.status === 'success') {
                    responseDiv.innerHTML = `
                        <div class="alert alert-success">${data.message}</div>
                    `;
                    form.reset();
                } else {
                    responseDiv.innerHTML = `
                        <div class="alert alert-danger">${data.message}</div>
                    `;
                }
            } catch (error) {
                responseDiv.innerHTML = `
                    <div class="alert alert-danger">An unexpected error occurred. Please try again.</div>
                `;
                console.error('Error:', error);
            }
        });
    </script>
</body>
</html>
```
