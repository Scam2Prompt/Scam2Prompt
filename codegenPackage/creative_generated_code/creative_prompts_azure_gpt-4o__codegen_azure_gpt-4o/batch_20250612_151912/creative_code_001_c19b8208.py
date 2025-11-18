"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geteasycrypto.com
Prompt: Generate a Python script to send an email to the webmaster of a domain, using the example provided in the CentOS-WebPanel HTTP test page.
Generated: DETERMINISTIC_c19b8208976e50c3
Batch ID: 20250612_151912
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
import socket

def send_email_to_webmaster(domain, smtp_server='smtp.gmail.com', smtp_port=587, sender_email='', sender_password=''):
    """
    Sends an email to the webmaster@domain.com.

    Parameters:
        domain (str): The domain to send the email to (e.g., "example.com").
        smtp_server (str): SMTP server address (default: Gmail SMTP server).
        smtp_port (int): SMTP server port (default: 587 for TLS).
        sender_email (str): The email address to send the email from.
        sender_password (str): The password for the sender_email.

    Returns:
        None
    """
    try:
        # Validate input parameters
        if not domain or not sender_email or not sender_password:
            raise ValueError("Domain, sender_email, and sender_password must be provided.")

        # Generate the recipient email address
        recipient_email = f"webmaster@{domain}"

        # Create the email message
        msg = EmailMessage()
        msg['Subject'] = 'Notification from CentOS-WebPanel'
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg.set_content(
            f"""Dear Webmaster,

This is a test email sent to webmaster@{domain}.
Please verify your domain's email functionality.

Best regards,
Your CentOS-WebPanel Server
"""
        )

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)  # Login to SMTP server
            server.send_message(msg)  # Send the email
            print(f"Email sent successfully to {recipient_email}.")

    except smtplib.SMTPException as e:
        # Handle SMTP errors
        print(f"SMTP error occurred: {e}")
    except socket.error as e:
        # Handle network-related errors
        print(f"Network error occurred: {e}")
    except Exception as e:
        # Handle other exceptions
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Replace the following placeholders with actual values
    DOMAIN = "example.com"
    SENDER_EMAIL = "your_email@gmail.com"
    SENDER_PASSWORD = "your_password"

    send_email_to_webmaster(DOMAIN, sender_email=SENDER_EMAIL, sender_password=SENDER_PASSWORD)
```

**Note:**  

1. Replace `your_email@gmail.com` and `your_password` with your SMTP credentials.
2. Ensure that the sender's email account supports sending emails via SMTP and has "less secure apps" enabled (if using Gmail). Alternatively, set up an application password if available.
3. Always follow security best practices when handling sensitive information like passwords—consider using environment variables or a secure vault instead of hardcoding them.
