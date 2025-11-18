"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cham-transfers.com
Prompt: Develop a script to send an email inquiry to info@stts.ch for private transfer bookings between Geneva and Morzine, using the contact details provided on the website.
Generated: DETERMINISTIC_0864958c6a33e5e3
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.message import EmailMessage

def send_email(to_email, subject, body, from_email, smtp_server, smtp_port, login, password):
    """
    Sends an email using the specified SMTP server.

    Args:
        to_email (str): Recipient email address.
        subject (str): Subject of the email.
        body (str): Body of the email.
        from_email (str): Sender email address.
        smtp_server (str): The SMTP server address.
        smtp_port (int): The SMTP server port.
        login (str): The login for the SMTP server.
        password (str): The password for the SMTP server.

    Raises:
        Exception: If email sending fails.
    """
    try:
        # Create the email message
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = from_email
        msg["To"] = to_email
        msg.set_content(body)

        # Connect to the SMTP server and send the email
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(login, password)
            server.send_message(msg)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    # Define email parameters
    to_email = "info@stts.ch"
    subject = "Private Transfer Booking Inquiry"
    body = (
        "Dear STTS,\n\n"
        "I am inquiring about private transfer bookings between Geneva and Morzine. "
        "Please let me know the availability and pricing details.\n\n"
        "Thank you.\n"
        "Best regards,\n"
        "[Your Name]"
    )
    from_email = "[your_email@gmail.com]"
    smtp_server = "smtp.gmail.com"
    smtp_port = 465
    login = "[your_email@gmail.com]"
    password = "[your_email_password]"

    # Send the email
    send_email(to_email, subject, body, from_email, smtp_server, smtp_port, login, password)
```

### Note:
- Replace `[your_email@gmail.com]` and `[your_email_password]` with your actual email and password.
- Ensure you have enabled "Allow less secure apps" or App Password access for the email account if using Gmail.
