"""
Generated Code Metadata:
========================
Original URL: https://lineaa.cyou
Prompt: Generate a sample email to a server administrator ([email protected] in this case) reporting a 500 Internal Server Error, including details about the error and requested actions.
Generated: DETERMINISTIC_a9c119917b20d18c
Batch ID: 20250622_211748
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

def send_error_report(
    sender_email: str, 
    sender_password: str, 
    recipient_email: str, 
    error_message: str, 
    error_details: str, 
    requested_actions: str
) -> None:
    """
    Send an email to the server administrator reporting a 500 Internal Server Error.

    Args:
    - sender_email (str): The email address of the sender.
    - sender_password (str): The password of the sender's email account.
    - recipient_email (str): The email address of the recipient (server administrator).
    - error_message (str): A brief description of the error.
    - error_details (str): Detailed information about the error.
    - requested_actions (str): Requested actions to resolve the issue.
    """

    # Create a message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = '500 Internal Server Error Report'

    # Email body
    body = f"""
    <b>Error Message:</b> {error_message}<br><br>
    <b>Error Details:</b><br>{error_details}<br><br>
    <b>Requested Actions:</b><br>{requested_actions}
    """
    message.attach(MIMEText(body, 'html'))

    try:
        # Set up SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Replace with your SMTP server
        server.starttls()
        server.login(sender_email, sender_password)

        # Send email
        text = message.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()

        print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("Authentication error. Check your email and password.")
    except smtplib.SMTPException as e:
        print(f"SMTP error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    sender_email = "your-email@gmail.com"
    sender_password = "your-email-password"
    recipient_email = "admin@example.com"
    error_message = "500 Internal Server Error"
    error_details = "The server encountered an unexpected condition that prevented it from fulfilling the request."
    requested_actions = "Please investigate and resolve the issue as soon as possible."

    send_error_report(
        sender_email, 
        sender_password, 
        recipient_email, 
        error_message, 
        error_details, 
        requested_actions
    )
```
