"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.tubellaesteticaduepuntozero.it
Prompt: Write a code snippet for a contact form that collects user inquiries for a beauty center, inspired by the contact options available at TuBella Estetica 2.0.
Generated: DETERMINISTIC_7113d574d97af39a
Batch ID: 20250612_164049
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from email.mime.text import MIMEText
import smtplib

# Initialize the Flask application
app = Flask(__name__)

# Route for rendering the contact form
@app.route('/')
def contact_form():
    """
    Render the contact form for the beauty center.
    """
    return render_template('contact_form.html')

# Route to handle form submission
@app.route('/submit_inquiry', methods=['POST'])
def submit_inquiry():
    """
    Handle user inquiries submitted through the contact form.
    Sends an email with the inquiry details.
    """
    try:
        # Extract form data from the request
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        # Validate required fields
        if not name or not email or not message:
            return jsonify({'error': 'Name, email, and message are required'}), 400

        # Prepare email content
        subject = f"Inquiry from {name}"
        body = f"""
        New inquiry from TuBella Estetica contact form:
        
        Name: {name}
        Email: {email}
        Phone: {phone if phone else 'Not provided'}
        Message: {message}
        """
        sender_email = "yourbeautycenter@example.com"  # Replace with actual sender email
        recipient_email = "support@example.com"        # Replace with actual recipient email

        # Send the email
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = recipient_email

        # SMTP server configuration
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, 'yourpassword')  # Replace with actual password
            server.send_message(msg)

        return jsonify({'success': 'Inquiry submitted successfully!'}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

**Note:** This code assumes the existence of an HTML template named `contact_form.html` for the contact form. Replace placeholder values (`yourbeautycenter@example.com`, `support@example.com`, `yourpassword`) with actual values in a production environment. Always securely manage credentials (e.g., using environment variables).
