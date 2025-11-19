"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flammedeauinc.ca
Prompt: Write a Python script that automates the process of sending a service request for plumbing and heating repairs to a specified email address.
Generated: DETERMINISTIC_46cf7d5880795e70
Batch ID: 20250612_162051
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

def send_service_request_email(sender_email, sender_password, recipient_email, subject, message_body):
    """
    Sends a service request email for plumbing and heating repairs.

    Parameters:
    sender_email (str): The sender's email address.
    sender_password (str): The sender's email account password.
    recipient_email (str): The recipient's email address.
    subject (str): The subject of the email.
    message_body (str): The body of the email.

    Returns:
    None
    """
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(message_body, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:  # Using Gmail's SMTP server
            server.starttls()  # Upgrade the connection to secure encrypted SSL/TLS
            server.login(sender_email, sender_password)  # Login using sender's credentials
            server.send_message(msg)  # Send the email
            print("Service request email sent successfully.")

    except smtplib.SMTPException as e:
        # Handle errors related to SMTP
        print(f"Failed to send email: {e}")

    except Exception as e:
        # Handle any other errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Example usage:
    # Replace the placeholders below with actual values.
    sender_email = "your_email@gmail.com"  # Sender's email address
    sender_password = "your_password"      # Sender's email password
    recipient_email = "support@plumbingcompany.com"  # Recipient's email address
    subject = "Urgent: Plumbing and Heating Service Request"  # Email subject
    message_body = (
        "Dear Support Team,\n\n"
        "I am experiencing issues with my plumbing and heating systems. "
        "Please contact me to schedule a repair as soon as possible.\n\n"
        "Best regards,\n"
        "John Doe\nContact: (123) 456-7890"
    )  # Email body

    # Call the function to send the email
    send_service_request_email(sender_email, sender_password, recipient_email, subject, message_body)
```
