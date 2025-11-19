"""
Generated Code Metadata:
========================
Original URL: https://1inch.uk
Prompt: Generate a template email to inquire about buying the domain name 1inch.uk, including a reasonable offer based on the provided minimum offer.
Generated: DETERMINISTIC_e35d264398cd2187
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def create_email(sender_email, recipient_email, domain_name, offer_amount):
    """
    Create a template email to inquire about purchasing a domain name.

    :param sender_email: The email address of the sender
    :param recipient_email: The email address of the recipient
    :param domain_name: The domain name being inquired about
    :param offer_amount: The offer amount for the domain
    :return: A MIMEMultipart email object
    """
    # Create the email container
    email = MIMEMultipart()
    email['From'] = sender_email
    email['To'] = recipient_email
    email['Subject'] = f'Inquiry About Purchasing {domain_name}'

    # Create the email body
    body = f"""
    Dear Domain Owner,

    I hope this message finds you well. I am writing to inquire about the possibility of purchasing the domain name {domain_name}. 

    After conducting some research, I would like to make a reasonable offer of ${offer_amount} for the domain. I believe this could be a mutually beneficial transaction.

    Please let me know if you are open to discussing this further. I look forward to your response.

    Best regards,
    [Your Name]
    [Your Contact Information]
    """

    # Attach the body to the email
    email.attach(MIMEText(body, 'plain'))
    return email

def send_email(smtp_server, smtp_port, sender_email, sender_password, recipient_email, email):
    """
    Send the email using the specified SMTP server.

    :param smtp_server: The SMTP server address
    :param smtp_port: The SMTP server port
    :param sender_email: The email address of the sender
    :param sender_password: The password for the sender's email account
    :param recipient_email: The email address of the recipient
    :param email: The MIMEMultipart email object to send
    """
    try:
        # Establish a secure session with the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)  # Log in to the email account
            server.sendmail(sender_email, recipient_email, email.as_string())  # Send the email
            print("Email sent successfully.")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")

# Example usage
if __name__ == "__main__":
    # Define email parameters
    sender_email = "your_email@example.com"
    sender_password = "your_password"
    recipient_email = "owner@example.com"
    domain_name = "1inch.uk"
    offer_amount = 1000  # Example offer amount

    # Create the email
    email = create_email(sender_email, recipient_email, domain_name, offer_amount)

    # Send the email
    send_email("smtp.example.com", 587, sender_email, sender_password, recipient_email, email)
```
