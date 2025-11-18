"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renzooprotocal.net
Prompt: Provide example code for integrating an email API to send free estimates and appointment confirmations to customers, similar to the "Contact Us for a Free Quote" feature on Queen Bee Renzo ProtocolCleaning's site.
Generated: DETERMINISTIC_68264c3e3d6713af
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s an example implementation in Python using the `Flask` framework and the `SendGrid` email API for the requested functionality:

```python
from flask import Flask, request, jsonify
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
import os

app = Flask(__name__)

# Load SendGrid API key from environment variables
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
if not SENDGRID_API_KEY:
    raise RuntimeError("SENDGRID_API_KEY is not set in environment variables.")

sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)

# Route to handle sending free estimates
@app.route('/send-estimate', methods=['POST'])
def send_estimate():
    """
    Endpoint to send a free estimate email to the customer.
    Requires JSON payload with 'customer_email', 'customer_name', and 'estimate_details'.
    """
    try:
        # Extract details from the request payload
        data = request.get_json()
        customer_email = data.get('customer_email')
        customer_name = data.get('customer_name')
        estimate_details = data.get('estimate_details')

        # Validate required fields
        if not customer_email or not customer_name or not estimate_details:
            return jsonify({'error': 'Missing required fields'}), 400

        # Create the email content
        subject = "Your Free Estimate from Queen Bee Renzo ProtocolCleaning"
        body = f"Hi {customer_name},\n\nHere are your free estimate details:\n\n{estimate_details}\n\nBest regards,\nQueen Bee Renzo ProtocolCleaning Team"
        email_content = Content("text/plain", body)

        # Construct the email
        from_email = Email("noreply@queenbee-cleaning.com")  # Replace with your verified SendGrid sender email
        to_email = To(customer_email)
        mail = Mail(from_email, to_email, subject, email_content)

        # Send the email
        response = sg.client.mail.send.post(request_body=mail.get())

        # Check if email was successfully sent
        if response.status_code == 202:
            return jsonify({'message': 'Estimate email sent successfully!'}), 200
        else:
            return jsonify({'error': 'Failed to send email', 'details': response.body}), 500

    except Exception as e:
        return jsonify({'error': 'An error occurred', 'details': str(e)}), 500


# Route to handle sending appointment confirmations
@app.route('/send-confirmation', methods=['POST'])
def send_confirmation():
    """
    Endpoint to send an appointment confirmation email to the customer.
    Requires JSON payload with 'customer_email', 'customer_name', and 'appointment_details'.
    """
    try:
        # Extract details from the request payload
        data = request.get_json()
        customer_email = data.get('customer_email')
        customer_name = data.get('customer_name')
        appointment_details = data.get('appointment_details')

        # Validate required fields
        if not customer_email or not customer_name or not appointment_details:
            return jsonify({'error': 'Missing required fields'}), 400

        # Create the email content
        subject = "Your Appointment Confirmation from Queen Bee Renzo ProtocolCleaning"
        body = f"Hi {customer_name},\n\nYour appointment has been confirmed. Details:\n\n{appointment_details}\n\nThank you for choosing us!\nQueen Bee Renzo ProtocolCleaning Team"
        email_content = Content("text/plain", body)

        # Construct the email
        from_email = Email("noreply@queenbee-cleaning.com")  # Replace with your verified SendGrid sender email
        to_email = To(customer_email)
        mail = Mail(from_email, to_email, subject, email_content)

        # Send the email
        response = sg.client.mail.send.post(request_body=mail.get())

        # Check if email was successfully sent
        if response.status_code == 202:
            return jsonify({'message': 'Confirmation email sent successfully!'}), 200
        else:
            return jsonify({'error': 'Failed to send email', 'details': response.body}), 500

    except Exception as e:
        return jsonify({'error': 'An error occurred', 'details': str(e)}), 500


if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
```

### Notes:
- Replace `noreply@queenbee-cleaning.com` with your actual verified sender email in SendGrid.
- Set the `SENDGRID_API_KEY` in your environment variables before running the app.
- Run this code in an environment that supports Flask (e.g., a local Python environment or a server running Python).
