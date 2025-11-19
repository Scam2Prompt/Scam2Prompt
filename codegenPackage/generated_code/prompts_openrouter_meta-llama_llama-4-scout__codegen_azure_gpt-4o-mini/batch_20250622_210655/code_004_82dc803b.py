"""
Generated Code Metadata:
========================
Original URL: https://prgmea.pk
Prompt: Generate a sample email template for inquiring about sustainable apparel manufacturing practices among PRGMEA member suppliers.
Generated: DETERMINISTIC_82dc803bc808c770
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def create_email_template(supplier_name, sender_email, recipient_email):
    """
    Create an email template for inquiring about sustainable apparel manufacturing practices.

    Parameters:
    supplier_name (str): The name of the supplier.
    sender_email (str): The email address of the sender.
    recipient_email (str): The email address of the recipient.

    Returns:
    MIMEMultipart: The constructed email message.
    """
    # Create the email container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = f"Inquiry About Sustainable Apparel Manufacturing Practices"

    # Email body content
    body = f"""
    Dear {supplier_name},

    I hope this message finds you well. As part of our commitment to sustainability and ethical practices in the apparel industry, we are reaching out to inquire about your manufacturing practices.

    Specifically, we would like to understand:
    - The materials you use in your production processes.
    - Any certifications or standards you adhere to regarding sustainability.
    - Your approach to waste management and resource conservation.

    We believe that transparency in these areas is crucial for fostering trust and collaboration within our industry. We would greatly appreciate any information you can provide regarding your sustainable practices.

    Thank you for your time, and we look forward to your response.

    Best regards,
    [Your Name]
    [Your Position]
    [Your Company]
    [Your Contact Information]
    """

    # Attach the body to the email
    msg.attach(MIMEText(body, 'plain'))

    return msg

def send_email(smtp_server, smtp_port, sender_email, sender_password, recipient_email, email_message):
    """
    Send an email using the specified SMTP server.

    Parameters:
    smtp_server (str): The SMTP server address.
    smtp_port (int): The port number for the SMTP server.
    sender_email (str): The email address of the sender.
    sender_password (str): The password for the sender's email account.
    recipient_email (str): The email address of the recipient.
    email_message (MIMEMultipart): The email message to be sent.

    Returns:
    None
    """
    try:
        # Set up the server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)  # Log in to the email account
            server.send_message(email_message)  # Send the email
            print("Email sent successfully.")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")

# Example usage
if __name__ == "__main__":
    supplier_name = "ABC Apparel"
    sender_email = "your_email@example.com"
    recipient_email = "supplier_email@example.com"
    smtp_server = "smtp.example.com"
    smtp_port = 587
    sender_password = "your_password"

    # Create the email message
    email_message = create_email_template(supplier_name, sender_email, recipient_email)

    # Send the email
    send_email(smtp_server, smtp_port, sender_email, sender_password, recipient_email, email_message)
```
