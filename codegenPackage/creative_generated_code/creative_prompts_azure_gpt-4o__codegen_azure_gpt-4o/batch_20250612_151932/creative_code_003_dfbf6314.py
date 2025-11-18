"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://registrations-arcium.hq.net
Prompt: Write a script to send an email using Python's `smtplib` to the contact email address "mms@star-co.net.kp" with a query about "개성고려인삼꿀."
Generated: DETERMINISTIC_dfbf631484136726
Batch ID: 20250612_151932
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

def send_email(sender_email, sender_password, recipient_email, subject, body):
    """
    Sends an email using SMTP.

    Args:
        sender_email (str): Email address of the sender.
        sender_password (str): Password for the sender's email account.
        recipient_email (str): Email address of the recipient.
        subject (str): Subject of the email.
        body (str): Content of the email.
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        # Note: Update the SMTP server and port as needed for your email provider
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # Start TLS for security
            server.starttls()

            # Log in to the server
            server.login(sender_email, sender_password)

            # Send the email
            server.send_message(msg)

        print("Email sent successfully.")

    except smtplib.SMTPException as e:
        print(f"An error occurred while sending the email: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Main script execution
if __name__ == "__main__":
    # Sender's email credentials (replace with your own credentials)
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"

    # Recipient's email address
    recipient_email = "mms@star-co.net.kp"

    # Email subject and body
    subject = "Query about 개성고려인삼꿀"
    body = "Hello,\n\nI would like to inquire about 개성고려인삼꿀. Could you please provide more information?\n\nThank you."

    # Call the function to send the email
    send_email(sender_email, sender_password, recipient_email, subject, body)
```

**Note:** Replace `your_email@gmail.com` and `your_password` with your actual email credentials. Be cautious about sharing sensitive information like passwords and use secure methods (e.g., environment variables or secret management tools) for storing credentials in production systems.
