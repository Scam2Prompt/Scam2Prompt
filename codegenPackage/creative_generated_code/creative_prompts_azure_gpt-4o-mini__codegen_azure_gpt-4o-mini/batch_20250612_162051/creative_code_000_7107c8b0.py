"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Generate a code snippet for a web application that allows users to request a quote for high-pressure cleaning and disinfection services for poultry buildings in Aire sur l’Adour.
Generated: DETERMINISTIC_7107c8b0b2ac0913
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import re

app = Flask(__name__)

# Configuration for Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Update with your mail server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'  # Update with your email
app.config['MAIL_PASSWORD'] = 'your_password'  # Update with your email password
mail = Mail(app)

@app.route('/request-quote', methods=['POST'])
def request_quote():
    """
    Endpoint to handle quote requests for high-pressure cleaning and disinfection services.
    Expects a JSON payload with the user's details and service requirements.
    """
    data = request.get_json()

    # Validate incoming data
    errors = validate_request(data)
    if errors:
        return jsonify({'errors': errors}), 400

    name = data['name']
    email = data['email']
    service_details = data['service_details']
    
    try:
        # Send confirmation email to the user
        send_confirmation_email(name, email, service_details)
        return jsonify({'message': 'Quote request submitted successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def validate_request(data):
    """
    Validate the incoming request data.
    Returns a list of error messages if validation fails.
    """
    errors = []
    if 'name' not in data or not data['name']:
        errors.append('Name is required.')
    if 'email' not in data or not is_valid_email(data['email']):
        errors.append('Valid email is required.')
    if 'service_details' not in data or not data['service_details']:
        errors.append('Service details are required.')
    return errors

def is_valid_email(email):
    """
    Validate the email format using a simple regex.
    """
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def send_confirmation_email(name, email, service_details):
    """
    Send a confirmation email to the user with their request details.
    """
    msg = Message('Quote Request Confirmation',
                  sender='your_email@example.com',  # Update with your email
                  recipients=[email])

    msg.body = f"""Hello {name},

Thank you for your request for a quote for high-pressure cleaning and disinfection services for poultry buildings in Aire sur l’Adour.

Service Details:
{service_details}

We will get back to you shortly.

Best regards,
Your Company Name
"""

    mail.send(msg)

if __name__ == '__main__':
    app.run(debug=True)
```

### Note:
- Replace `smtp.example.com`, `your_email@example.com`, and `your_password` with your actual email service details.
- Ensure that Flask and Flask-Mail are installed in your environment. You can install them using `pip install Flask Flask-Mail`.
- Make sure to handle sensitive information like email credentials securely in a production environment, potentially using environment variables.
