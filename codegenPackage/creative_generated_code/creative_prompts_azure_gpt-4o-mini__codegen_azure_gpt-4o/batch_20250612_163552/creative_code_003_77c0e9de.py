"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bplservicescenter.com
Prompt: Develop a code snippet that sends an email notification to support@bplservicescenter.com when a BPL washing machine repair request is submitted.
Generated: DETERMINISTIC_77c0e9de1c0decbc
Batch ID: 20250612_163552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.message import EmailMessage

def send_email_notification(customer_name, customer_email, repair_details):
    """
    Sends an email notification to the support team when a repair request is submitted.

    Parameters:
    customer_name (str): Name of the customer submitting the repair request.
    customer_email (str): Email address of the customer.
    repair_details (str): Details of the repair request.

    Returns:
    None
    """
    # Email configuration
    support_email = "support@bplservicescenter.com"
    subject = "New BPL Washing Machine Repair Request"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "your-email@gmail.com"  # Replace with your email
    sender_password = "your-email-password"  # Replace with your email password

    # Construct the email message
    email_body = f"""
    Hello Support Team,

    A new repair request has been submitted.

    Customer Name: {customer_name}
    Customer Email: {customer_email}
    Repair Details:
    {repair_details}

    Please address this request promptly.

    Best Regards,
    BPL Services Center System
    """

    try:
        # Create the email object
        msg = EmailMessage()
        msg.set_content(email_body)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = support_email

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)  # Login to the SMTP server
            server.send_message(msg)  # Send the email

        print("Email notification sent successfully.")

    except Exception as e:
        print(f"Failed to send email notification: {e}")

# Example usage
send_email_notification(
    customer_name="John Doe",
    customer_email="john.doe@example.com",
    repair_details="The washing machine is not spinning properly."
)
```

**Note:** Replace `your-email@gmail.com` and `your-email-password` with valid credentials of the sender email account. Ensure you use an app-specific password or set up proper authentication if using services like Gmail.
