"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esperai.com
Prompt: What steps should I take to submit a serious inquiry for the domain available at esperai.com?
Generated: DETERMINISTIC_c4bfcdf956ffe235
Batch ID: 20250612_162701
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to submit a serious inquiry for a domain (e.g., esperai.com).
This script assumes the inquiry is submitted via email or a web form.
Replace placeholders with actual information before running the script.
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
DOMAIN_NAME = "esperai.com"  # Replace with the domain name you want to inquire about
INQUIRY_EMAIL = "owner@example.com"  # Replace with the domain owner's email address
SENDER_EMAIL = "your-email@example.com"  # Replace with your email address
SENDER_NAME = "Your Full Name"  # Replace with your full name
SMTP_SERVER = "smtp.gmail.com"  # Replace with your email provider's SMTP server
SMTP_PORT = 587  # SMTP port (common: 587 for TLS)
EMAIL_PASSWORD = "your-email-password"  # Replace with your email account's password

def send_inquiry(domain, inquiry_email, sender_email, sender_name, smtp_server, smtp_port, email_password):
    """
    Sends a serious inquiry regarding a domain availability via email.

    Args:
        domain (str): The domain name to inquire about.
        inquiry_email (str): The recipient email address (domain owner).
        sender_email (str): The sender email address.
        sender_name (str): The sender's full name.
        smtp_server (str): SMTP server for sending the email.
        smtp_port (int): SMTP port.
        email_password (str): Password for the sender email account.

    Returns:
        None
    """

    try:
        # Create the email message
        subject = f"Inquiry About Domain Availability: {domain}"
        body = f"""
        Dear Domain Owner,

        My name is {sender_name}, and I am interested in acquiring the domain "{domain}".
        Please let me know if the domain is available for purchase or if you are open to negotiations. 
        I would be happy to discuss pricing or any other relevant details.

        Thank you for your time, and I look forward to your response.

        Best regards,
        {sender_name}
        {sender_email}
        """

        # Create a MIME message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = inquiry_email
        message["Subject"] = subject

        # Attach the email body
        message.attach(MIMEText(body, "plain"))

        # Connect to SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, email_password)
            server.send_message(message)

        print("Inquiry email sent successfully.")

    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main execution
if __name__ == "__main__":
    send_inquiry(
        domain=DOMAIN_NAME,
        inquiry_email=INQUIRY_EMAIL,
        sender_email=SENDER_EMAIL,
        sender_name=SENDER_NAME,
        smtp_server=SMTP_SERVER,
        smtp_port=SMTP_PORT,
        email_password=EMAIL_PASSWORD
    )
```

**Important Note:**  
Before running this script:  
- Replace placeholder values (`DOMAIN_NAME`, `INQUIRY_EMAIL`, etc.) with actual information.  
- Ensure that you have properly configured SMTP access for sending the email (e.g., using a Gmail account may require enabling "Less Secure Apps" or creating an App Password).  
- Never hard-code sensitive information like passwords in production. Use environment variables or secure storage solutions instead.
