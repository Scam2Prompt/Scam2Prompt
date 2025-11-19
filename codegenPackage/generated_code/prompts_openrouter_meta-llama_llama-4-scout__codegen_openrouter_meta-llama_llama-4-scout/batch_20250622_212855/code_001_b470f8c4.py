"""
Generated Code Metadata:
========================
Original URL: https://ispot.cc
Prompt: What are the steps to report abuse for a temporary URL provided by InterServer, and how to send an email to abusencc@interserver.net?
Generated: DETERMINISTIC_b470f8c437c988d8
Batch ID: 20250622_212855
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

def report_abuse_temporary_url(url, abuse_reason, sender_email, sender_password):
    """
    Reports abuse for a temporary URL provided by InterServer.

    Args:
        url (str): The temporary URL to report abuse for.
        abuse_reason (str): The reason for reporting abuse.
        sender_email (str): The email address of the sender.
        sender_password (str): The password of the sender's email account.

    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """

    # Define the recipient's email address
    recipient_email = "abusencc@interserver.net"

    # Create a message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = "Abuse Report for Temporary URL"

    # Create the email body
    body = f"""
    Temporary URL: {url}
    Reason for reporting abuse: {abuse_reason}
    """
    message.attach(MIMEText(body, "plain"))

    try:
        # Set up the SMTP server
        server = smtplib.SMTP("smtp." + sender_email.split("@")[1])
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        text = message.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()

        return True

    except smtplib.SMTPAuthenticationError:
        print("Authentication error: Incorrect email or password")
        return False

    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")
        return False


def main():
    url = input("Enter the temporary URL: ")
    abuse_reason = input("Enter the reason for reporting abuse: ")
    sender_email = input("Enter your email address: ")
    sender_password = input("Enter your email password: ")

    if report_abuse_temporary_url(url, abuse_reason, sender_email, sender_password):
        print("Abuse report sent successfully")
    else:
        print("Failed to send abuse report")


if __name__ == "__main__":
    main()
```
