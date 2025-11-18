"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daddys-universitys.com
Prompt: Write code to create an API that manages customer inquiries for a rural revitalization company, including endpoints for submitting inquiries, retrieving FAQs, and requesting service estimates. Use features like email and phone contact integration.
Generated: DETERMINISTIC_9f1ff36c2ca6ccc8
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import re
import smtplib
from email.mime.text import MIMEText

# Initialize Flask app
app = Flask(__name__)

# Sample data
faqs = [
    {"id": 1, "question": "What is rural revitalization?", "answer": "Rural revitalization involves improving infrastructure and services in rural areas."},
    {"id": 2, "question": "How can I participate?", "answer": "You can participate by reaching out to local projects or organizations working in your area."},
]

# In-memory storage for inquiries
customer_inquiries = []

# Utility function for validating email
def is_valid_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email)

# Utility function for validating phone number (basic example for US numbers)
def is_valid_phone(phone):
    regex = r'^\+?1?\d{10}$'
    return re.match(regex, phone)

# Endpoint: Submit inquiries
@app.route('/api/inquiries', methods=['POST'])
def submit_inquiry():
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        message = data.get('message')

        # Validate input
        if not name or not email or not phone or not message:
            return jsonify({"error": "All fields are required"}), 400
        if not is_valid_email(email):
            return jsonify({"error": "Invalid email format"}), 400
        if not is_valid_phone(phone):
            return jsonify({"error": "Invalid phone number format"}), 400

        # Store inquiry
        inquiry = {
            "id": len(customer_inquiries) + 1,
            "name": name,
            "email": email,
            "phone": phone,
            "message": message
        }
        customer_inquiries.append(inquiry)

        # Send email notification (example using SMTP)
        try:
            smtp_server = 'smtp.example.com'
            smtp_port = 587
            smtp_user = 'your_email@example.com'
            smtp_password = 'your_password'

            msg = MIMEText(f"New Inquiry Received:\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}")
            msg['Subject'] = 'New Inquiry'
            msg['From'] = smtp_user
            msg['To'] = smtp_user

            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print(f"Error sending email: {e}")

        return jsonify({"message": "Inquiry submitted successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Retrieve FAQs
@app.route('/api/faqs', methods=['GET'])
def get_faqs():
    return jsonify(faqs), 200

# Endpoint: Request service estimate
@app.route('/api/service-estimates', methods=['POST'])
def request_service_estimate():
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        details = data.get('details')

        # Validate input
        if not name or not email or not phone or not details:
            return jsonify({"error": "All fields are required"}), 400
        if not is_valid_email(email):
            return jsonify({"error": "Invalid email format"}), 400
        if not is_valid_phone(phone):
            return jsonify({"error": "Invalid phone number format"}), 400

        # Send email notification (example using SMTP)
        try:
            smtp_server = 'smtp.example.com'
            smtp_port = 587
            smtp_user = 'your_email@example.com'
            smtp_password = 'your_password'

            msg = MIMEText(f"Service Estimate Request:\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nDetails: {details}")
            msg['Subject'] = 'Service Estimate Request'
            msg['From'] = smtp_user
            msg['To'] = smtp_user

            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print(f"Error sending email: {e}")

        return jsonify({"message": "Service estimate request submitted successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main function to run the app
if __name__ == '__main__':
    app.run(debug=True)
```
