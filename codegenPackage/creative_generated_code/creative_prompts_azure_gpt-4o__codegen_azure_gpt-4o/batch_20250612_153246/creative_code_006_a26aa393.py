"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simho.in
Prompt: Write code to generate automated email templates for HR inquiries, using the contact information and service categories listed on the SIMHO website.
Generated: DETERMINISTIC_a26aa39312ab0741
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def generate_email_template(name: str, email: str, inquiry_topic: str, message_body: str) -> str:
    """
    Generate an automated email template for HR inquiries.

    Args:
        name (str): The name of the recipient.
        email (str): The email address of the recipient.
        inquiry_topic (str): The topic of the HR inquiry (e.g., "Benefits", "Payroll").
        message_body (str): The main message to be included in the email.

    Returns:
        str: A formatted email template ready to be sent.
    """
    template = f"""
    Dear {name},

    Thank you for reaching out regarding "{inquiry_topic}". Below is the information you provided:

    -----------------------------------------------------
    Email: {email}
    Inquiry Topic: {inquiry_topic}
    -----------------------------------------------------

    Message:
    {message_body}
    
    Our HR team will review your inquiry and respond to you shortly. If you need immediate assistance, please contact our HR support line.

    Best regards,
    SIMHO HR Team
    """
    return template

def send_email(sender_email: str, sender_password: str, recipient_email: str, subject: str, email_body: str):
    """
    Send an email using SMTP.

    Args:
        sender_email (str): The email address of the sender.
        sender_password (str): The password for the sender's email account.
        recipient_email (str): The email address of the recipient.
        subject (str): The subject of the email.
        email_body (str): The body of the email.

    Raises:
        Exception: If email sending fails due to SMTP or authentication issues.
    """
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(email_body, 'plain'))
        
        # Connect to the SMTP server and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure connection
            server.login(sender_email, sender_password)
            server.send_message(msg)

        print(f"Email successfully sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
if __name__ == "__main__":
    # Gather recipient details
    recipient_name = "Jane Doe"
    recipient_email = "jane.doe@example.com"
    inquiry_topic = "Benefits"
    message_body = "I would like to inquire about the health insurance plan for employees."

    # Generate email template
    email_body = generate_email_template(recipient_name, recipient_email, inquiry_topic, message_body)

    # Send the email
    sender_email = "your-email@example.com"
    sender_password = "your-password"  # Use environment variables or secure storage for credentials
    subject = f"HR Inquiry - {inquiry_topic}"

    send_email(sender_email, sender_password, recipient_email, subject, email_body)
```

Note: Replace `your-email@example.com` and `your-password` with your credentials, or use environment variables for secure configuration. Ensure SMTP settings match your email provider's specifications. This code assumes Gmail as the email provider; for other providers, update the SMTP server and port accordingly.
