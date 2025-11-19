"""
Generated Code Metadata:
========================
Original URL: https://imaginrayones.com
Prompt: Create a script to test email sending functionality using Plesk's mail service test page.
Generated: DETERMINISTIC_9c3d7b5ec3e0af2d
Batch ID: 20250612_152827
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
import ssl

def send_test_email(
    sender_email: str, 
    recipient_email: str, 
    mail_server: str, 
    mail_port: int, 
    password: str, 
    ssl_enabled: bool = True
):
    """
    Send a test email using the provided mail server settings.

    Args:
    - sender_email (str): The email address of the sender.
    - recipient_email (str): The email address of the recipient.
    - mail_server (str): The hostname or IP address of the mail server.
    - mail_port (int): The port number of the mail server.
    - password (str): The password for the sender's email account.
    - ssl_enabled (bool): Whether to use SSL/TLS encryption. Defaults to True.
    """

    # Create a secure SSL context
    context = ssl.create_default_context()

    try:
        # Set up the SMTP server
        if ssl_enabled:
            server = smtplib.SMTP_SSL(mail_server, mail_port, context=context)
        else:
            server = smtplib.SMTP(mail_server, mail_port)
            server.starttls(context=context)

        # Log in to the mail server
        server.login(sender_email, password)

        # Create a message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = "Test Email from Plesk Mail Service"

        # Set the body of the message
        body = "This is a test email sent from the Plesk mail service test page."
        message.attach(MIMEText(body, "plain"))

        # Send the email
        text = message.as_string()
        server.sendmail(sender_email, recipient_email, text)

        print("Test email sent successfully.")

    except smtplib.SMTPAuthenticationError:
        print("Authentication error: Unable to log in to the mail server.")
    except smtplib.SMTPException as e:
        print(f"SMTP error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Quit the SMTP server
        if 'server' in locals():
            server.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send a test email using Plesk's mail service.")
    parser.add_argument("-s", "--sender", required=True, help="Sender's email address.")
    parser.add_argument("-r", "--recipient", required=True, help="Recipient's email address.")
    parser.add_argument("-m", "--mail-server", required=True, help="Mail server hostname or IP address.")
    parser.add_argument("-p", "--port", type=int, required=True, help="Mail server port number.")
    parser.add_argument("-w", "--password", required=True, help="Sender's email password.")
    parser.add_argument("--no-ssl", action="store_false", dest="ssl_enabled", help="Disable SSL/TLS encryption.")

    args = parser.parse_args()

    send_test_email(
        sender_email=args.sender, 
        recipient_email=args.recipient, 
        mail_server=args.mail_server, 
        mail_port=args.port, 
        password=args.password, 
        ssl_enabled=args.ssl_enabled
    )
```
