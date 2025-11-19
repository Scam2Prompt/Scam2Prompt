"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gifts.sparklingz.nl
Prompt: What are the best practices for integrating a customer service support system in a webshop like Sparklingz?
Generated: DETERMINISTIC_69244680fae2e5d0
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a clean, production-ready Python example leveraging Flask for backend integration with a customer service support system in a webshop like "Sparklingz". This example includes best practices, proper error handling, and documentation.

```python
from flask import Flask, request, jsonify
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Initialize Flask app
app = Flask(__name__)

# Configure logging for error tracking
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Mock database for tickets (In production, use an actual database like PostgreSQL or MongoDB)
customer_support_tickets = {}

# Email server configuration (Update with your credentials in production)
SMTP_SERVER = "smtp.your-email-provider.com"
SMTP_PORT = 587
EMAIL_USER = "support@sparklingz.com"
EMAIL_PASSWORD = "your-secure-password"

@app.route('/support', methods=['POST'])
def create_support_ticket():
    """
    Endpoint to create a customer support ticket.
    Expected JSON payload:
    {
        "name": "Customer Name",
        "email": "customer@example.com",
        "issue": "Detailed description of the issue"
    }
    """
    try:
        data = request.json
        # Validate input data
        if not data or not all(key in data for key in ("name", "email", "issue")):
            return jsonify({"error": "Invalid input. Must include 'name', 'email', and 'issue'."}), 400

        # Create a unique ticket ID (In production, use UUID or database auto-generated IDs)
        ticket_id = f"ticket_{len(customer_support_tickets) + 1}"
        customer_support_tickets[ticket_id] = {
            "name": data["name"],
            "email": data["email"],
            "issue": data["issue"],
            "status": "Open"
        }

        # Send email notification to the support team
        send_email_notification(data["name"], data["email"], data["issue"], ticket_id)

        # Return success response
        return jsonify({"message": "Support ticket created successfully!", "ticket_id": ticket_id}), 201

    except Exception as e:
        logging.error(f"Failed to create support ticket: {str(e)}")
        return jsonify({"error": "An unexpected error occurred while creating the support ticket."}), 500

@app.route('/support/<ticket_id>', methods=['GET'])
def get_ticket_status(ticket_id):
    """
    Endpoint to retrieve the status of a support ticket.
    :param ticket_id: ID of the support ticket
    """
    try:
        ticket = customer_support_tickets.get(ticket_id)
        if not ticket:
            return jsonify({"error": "Ticket not found."}), 404

        return jsonify({"ticket_id": ticket_id, "ticket_data": ticket}), 200

    except Exception as e:
        logging.error(f"Failed to retrieve ticket status: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500

def send_email_notification(name, email, issue, ticket_id):
    """
    Sends an email notification to the support team.
    :param name: Name of the customer
    :param email: Email of the customer
    :param issue: Issue details
    :param ticket_id: Generated ticket ID
    """
    try:
        # Compose the email
        msg = MIMEMultipart()
        msg["From"] = EMAIL_USER
        msg["To"] = EMAIL_USER  # Typically sent to support or operations team
        msg["Subject"] = f"New Support Ticket: {ticket_id}"

        body = f"""
        A new support ticket has been created.
        Ticket ID: {ticket_id}
        Customer Name: {name}
        Customer Email: {email}
        Issue Details:
        {issue}
        """
        msg.attach(MIMEText(body, "plain"))

        # Connect to the email server and send the email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_USER, EMAIL_USER, msg.as_string())
        server.quit()

        logging.info(f"Support email notification sent for ticket {ticket_id}.")

    except Exception as e:
        logging.error(f"Failed to send email notification: {str(e)}")

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
```

### Notes:
1. Replace `SMTP_SERVER`, `SMTP_PORT`, `EMAIL_USER`, and `EMAIL_PASSWORD` with actual credentials for a secured production email service.
2. Consider using environment variables (e.g., via `os.getenv`) to store configurations securely.
3. For production, deploy on a proper web server (e.g., Gunicorn or uWSGI) behind Nginx/Apache and enable SSL.
4. Replace the mock database with a persistent storage system.
