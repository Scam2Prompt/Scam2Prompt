"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jlelectricista.com
Prompt: Write a Python script to automate the process of contacting a local electrician service, ensuring to include a request for residential electrical work with reasonable pricing.
Generated: DETERMINISTIC_e7c56cb494160c5e
Batch ID: 20250612_161700
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
import sys

def send_email(to_email, subject, body):
    """
    Sends an email using SMTP.
    
    Parameters:
        to_email (str): Recipient email address.
        subject (str): Subject of the email.
        body (str): Body of the email.
    
    Raises:
        Exception: If there is an issue with sending the email.
    """
    # Configure the SMTP settings
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    from_email = "your_email@gmail.com"  # Replace with your email
    from_password = "your_email_password"  # Replace with your email password (use secure methods instead of plaintext)

    try:
        # Create the email message
        message = MIMEMultipart()
        message["From"] = from_email
        message["To"] = to_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to secure encrypted SSL/TLS
        server.login(from_email, from_password)

        # Send the email
        server.sendmail(from_email, to_email, message.as_string())
        print(f"Email sent successfully to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}", file=sys.stderr)
    finally:
        server.quit()


def main():
    """
    Main function to automate contacting a local electrician service.
    """
    # Email and message details (customize as needed)
    electrician_email = "local.electrician@gmail.com"  # Replace with the electrician's email
    subject = "Request for Residential Electrical Work"
    body = (
        "Hello,\n\n"
        "I am in need of residential electrical services and would appreciate a reasonable quote for the work. "
        "Please let me know your availability and pricing details.\n\n"
        "Thank you,\n"
        "Your Name"
    )

    try:
        # Send the email
        send_email(electrician_email, subject, body)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```

**Note**: 
- Replace `your_email@gmail.com` and `your_email_password` with valid credentials for sending the email. Use environment variables or a more secure method to store credentials instead of hardcoding them.
- Make sure the `electrician_email` is updated with the actual recipient's email address.
- Ensure you have enabled "Less Secure Apps" or use an app-specific password with Gmail if you're using it.
