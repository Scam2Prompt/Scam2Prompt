"""
Generated Code Metadata:
========================
Original URL: https://geteasycrypto.com
Prompt: Generate a Python script to send an email to the webmaster of a domain, using the example provided in the CentOS-WebPanel HTTP test page.
Generated: DETERMINISTIC_c19b8208976e50c3
Batch ID: 20250612_151912
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
import argparse

def send_email(
    sender_email: str, 
    sender_password: str, 
    recipient_email: str, 
    subject: str, 
    body: str, 
    smtp_server: str = "smtp.gmail.com", 
    smtp_port: int = 587
):
    """
    Send an email to the specified recipient.

    Args:
        sender_email (str): The email address of the sender.
        sender_password (str): The password of the sender's email account.
        recipient_email (str): The email address of the recipient.
        subject (str): The subject of the email.
        body (str): The body of the email.
        smtp_server (str, optional): The SMTP server to use. Defaults to "smtp.gmail.com".
        smtp_port (int, optional): The port to use for the SMTP server. Defaults to 587.
    """

    # Create a message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the body to the message
    msg.attach(MIMEText(body, 'plain'))

    # Set up the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send the email
    text = msg.as_string()
    server.sendmail(sender_email, recipient_email, text)
    server.quit()

def get_webmaster_email(domain: str) -> str:
    """
    Get the webmaster email for the specified domain.

    Args:
        domain (str): The domain to get the webmaster email for.

    Returns:
        str: The webmaster email for the specified domain.
    """
    return f"webmaster@{domain}"

def main():
    parser = argparse.ArgumentParser(description="Send an email to the webmaster of a domain.")
    parser.add_argument("-s", "--sender_email", required=True, help="The email address of the sender.")
    parser.add_argument("-p", "--sender_password", required=True, help="The password of the sender's email account.")
    parser.add_argument("-d", "--domain", required=True, help="The domain to send the email to.")
    parser.add_argument("-sub", "--subject", required=True, help="The subject of the email.")
    parser.add_argument("-b", "--body", required=True, help="The body of the email.")

    args = parser.parse_args()

    recipient_email = get_webmaster_email(args.domain)

    try:
        send_email(
            sender_email=args.sender_email, 
            sender_password=args.sender_password, 
            recipient_email=recipient_email, 
            subject=args.subject, 
            body=args.body
        )
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("Authentication error. Check your email and password.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
