"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lineaa.cyou
Prompt: How do I contact a server administrator regarding a 500 Internal Server Error, and what information should I provide?
Generated: DETERMINISTIC_d1a877221a0dc22e
Batch ID: 20250612_164057
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

def send_error_report(server_admin_email, user_email, error_details):
    """
    Sends an email to the server administrator regarding a 500 Internal Server Error.

    Parameters:
    server_admin_email (str): The email address of the server administrator.
    user_email (str): The email address of the user reporting the error.
    error_details (str): Details about the error that occurred.

    Returns:
    bool: True if the email was sent successfully, False otherwise.
    """

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = user_email
    msg['To'] = server_admin_email
    msg['Subject'] = '500 Internal Server Error Report'

    # Email body content
    body = f"""
    Dear Server Administrator,

    I encountered a 500 Internal Server Error while trying to access the application. 
    Below are the details of the error:

    Error Details:
    {error_details}

    Please look into this issue at your earliest convenience.

    Thank you,
    {user_email}
    """

    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login('your_email@example.com', 'your_password')  # Authenticate
            server.send_message(msg)  # Send the email
        return True
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
        return False

# Example usage
if __name__ == "__main__":
    SERVER_ADMIN_EMAIL = 'admin@example.com'
    USER_EMAIL = 'user@example.com'
    ERROR_DETAILS = "The error occurred when accessing the /dashboard endpoint."

    success = send_error_report(SERVER_ADMIN_EMAIL, USER_EMAIL, ERROR_DETAILS)
    if success:
        print("Error report sent successfully.")
    else:
        print("Failed to send error report.")
```
