"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sgsp.org.br
Prompt: Develop a code snippet that sends an email to the SGSP contact address with inquiries about membership benefits.
Generated: DETERMINISTIC_161698c44f0aa752
Batch ID: 20250612_162050
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

def send_email(to_email, subject, body, from_email, smtp_server, smtp_port, login_user, login_password):
    """
    Sends an email to the specified recipient with the given subject and body.
    
    Args:
        to_email (str): Recipient email address.
        subject (str): Email subject line.
        body (str): Email body content.
        from_email (str): Sender email address.
        smtp_server (str): SMTP server address.
        smtp_port (int): SMTP server port.
        login_user (str): Login username for SMTP server.
        login_password (str): Login password for SMTP server.
    
    Returns:
        None
    """
    try:
        # Create a multipart email message
        message = MIMEMultipart()
        message['From'] = from_email
        message['To'] = to_email
        message['Subject'] = subject

        # Attach the plain text body to the email
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Use TLS for secure connection
            server.login(login_user, login_password)
            server.send_message(message)
            print("Email sent successfully.")
    
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Configuration parameters
TO_EMAIL = "contact@sgsp.org"  # SGSP contact email for inquiries
SUBJECT = "Inquiry About Membership Benefits"
BODY = """Dear SGSP Team,

I am writing to inquire about the membership benefits offered by SGSP. 
Could you please provide detailed information regarding the benefits, eligibility, and application process?

Thank you for your assistance.

Best regards,
[Your Name]
"""
FROM_EMAIL = "your-email@example.com"  # Replace with your email address
SMTP_SERVER = "smtp.example.com"       # Replace with your SMTP server address
SMTP_PORT = 587                        # Common SMTP port for TLS
LOGIN_USER = "your-email@example.com"  # Replace with your SMTP login username
LOGIN_PASSWORD = "your-password"       # Replace with your SMTP password

# Send the email
send_email(TO_EMAIL, SUBJECT, BODY, FROM_EMAIL, SMTP_SERVER, SMTP_PORT, LOGIN_USER, LOGIN_PASSWORD)
```

### Notes for Deployment:
- Replace placeholder values (e.g., `your-email@example.com`, `smtp.example.com`) with your actual email configuration details.
- Ensure credentials are stored securely, e.g., using environment variables or a secure secrets manager.
- Test the SMTP configuration to confirm compatibility with the email provider.
