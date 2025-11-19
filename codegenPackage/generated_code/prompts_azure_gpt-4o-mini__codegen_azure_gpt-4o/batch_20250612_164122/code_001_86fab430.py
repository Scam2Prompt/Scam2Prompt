"""
Generated Code Metadata:
========================
Original URL: https://handyfix.co.nz
Prompt: Write a Python script that sends an email request to Handyfix for a handyman job, using the provided contact details and service requirements.
Generated: DETERMINISTIC_86fab430257aa604
Batch ID: 20250612_164122
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

def send_handyman_request(sender_email, sender_password, recipient_email, subject, service_details):
    """
    Sends an email request to Handyfix for a handyman job.

    Parameters:
        sender_email (str): The email address of the sender.
        sender_password (str): The password for the sender's email account.
        recipient_email (str): The email address of Handyfix.
        subject (str): The subject of the email.
        service_details (str): The details of the handyman service request.

    Returns:
        None
    """
    try:
        # Create the email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        # Attach the service details to the email
        message.attach(MIMEText(service_details, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)  # Log in to the email account
            server.send_message(message)  # Send the email

        print("Email sent successfully!")

    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Replace these values with actual data
    sender_email = "your_email@gmail.com"
    sender_password = "your_email_password"
    recipient_email = "handyfix@example.com"
    subject = "Handyman Service Request"
    service_details = (
        "Hello Handyfix,\n\n"
        "I would like to request a handyman for the following job:\n"
        "- Fixing a leaking faucet in the kitchen\n"
        "- Repairing a broken door hinge\n\n"
        "Please let me know your availability and pricing.\n\n"
        "Thank you,\n"
        "John Doe\n"
        "Contact: +1234567890"
    )

    send_handyman_request(sender_email, sender_password, recipient_email, subject, service_details)
```
