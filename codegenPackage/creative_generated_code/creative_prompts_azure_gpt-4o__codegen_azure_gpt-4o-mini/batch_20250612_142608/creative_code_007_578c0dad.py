"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cointaap.com
Prompt: Develop a function to securely submit trading requests via email for a crypto trading platform like Cointaap.
Generated: DETERMINISTIC_578c0dadd24b6375
Batch ID: 20250612_142608
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
import os
import ssl

def send_trading_request(email_recipient, trading_request, email_sender, email_password):
    """
    Sends a trading request via email to the specified recipient.

    :param email_recipient: str, recipient's email address
    :param trading_request: str, details of the trading request
    :param email_sender: str, sender's email address
    :param email_password: str, sender's email app password
    :raises ValueError: if any of the required parameters are empty
    :raises Exception: if an error occurs during email sending
    """

    # Validate input parameters
    if not email_recipient or not trading_request or not email_sender or not email_password:
        raise ValueError("All parameters must be non-empty strings.")

    # Create the email message
    message = MIMEMultipart()
    message["From"] = email_sender
    message["To"] = email_recipient
    message["Subject"] = "Trading Request Submission"

    # Attach the trading request details to the email
    message.attach(MIMEText(trading_request, "plain"))

    # Setup the secure connection and send the email
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls(context=context)  # Upgrade to a secure connection
            server.login(email_sender, email_password)  # Login to the email server
            server.sendmail(email_sender, email_recipient, message.as_string())  # Send the email

    except smtplib.SMTPException as e:
        raise Exception(f"Failed to send email: {e}")

# Example usage
if __name__ == "__main__":
    try:
        email_to = "recipient@example.com"
        trading_request_details = "Buy 0.5 BTC at $30,000"
        sender_email = "your_email@gmail.com"  # Use a valid email address
        app_password = os.getenv("EMAIL_APP_PASSWORD")  # Securely fetch the password from environment

        send_trading_request(email_to, trading_request_details, sender_email, app_password)
        print("Trading request sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")
```
