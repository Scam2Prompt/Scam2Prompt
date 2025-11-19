"""
Generated Code Metadata:
========================
Original URL: https://loyalty.finance
Prompt: Generate a professional email template to inquire about making an offer on the loyalty.finance domain.
Generated: DETERMINISTIC_b1c00a72b6abc76b
Batch ID: 20250622_211906
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

def generate_email_template(domain_name, buyer_name, buyer_email, buyer_phone):
    """
    Generate a professional email template to inquire about making an offer on a domain.

    Args:
        domain_name (str): The name of the domain.
        buyer_name (str): The name of the buyer.
        buyer_email (str): The email address of the buyer.
        buyer_phone (str): The phone number of the buyer.

    Returns:
        str: The generated email template.
    """

    # Define the email template
    email_template = MIMEMultipart()
    email_template['From'] = buyer_email
    email_template['To'] = 'domain-owner@example.com'  # Replace with actual domain owner email
    email_template['Subject'] = f"Expression of Interest in loyalty.finance Domain"

    # Define the email body
    email_body = f"""
Dear Domain Owner,

I am reaching out to express my interest in acquiring the loyalty.finance domain. My name is {buyer_name} and I am a representative of [Company Name]. 

We believe that the loyalty.finance domain would be a valuable asset to our company, and we are eager to discuss the possibility of making an offer.

Could you please let me know if the domain is available for sale and if so, what the asking price is? I would also appreciate any information you can provide about the domain's history and any existing infrastructure.

You can reach me directly at {buyer_email} or {buyer_phone}.

Thank you for your time and consideration.

Best regards,
{buyer_name}
"""

    # Attach the email body to the email template
    email_template.attach(MIMEText(email_body, 'plain'))

    return email_template

def send_email(email_template, smtp_server, smtp_port, smtp_username, smtp_password):
    """
    Send an email using a specified SMTP server.

    Args:
        email_template (MIMEMultipart): The email template to send.
        smtp_server (str): The SMTP server to use.
        smtp_port (int): The SMTP port to use.
        smtp_username (str): The SMTP username to use.
        smtp_password (str): The SMTP password to use.

    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """

    try:
        # Create an SMTP object
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Send the email
        text = email_template.as_string()
        server.sendmail(email_template['From'], email_template['To'], text)
        server.quit()

        return True

    except Exception as e:
        print(f"Error sending email: {e}")
        return False

# Example usage
if __name__ == "__main__":
    domain_name = "loyalty.finance"
    buyer_name = "John Doe"
    buyer_email = "john.doe@example.com"
    buyer_phone = "123-456-7890"

    email_template = generate_email_template(domain_name, buyer_name, buyer_email, buyer_phone)

    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_username = "john.doe@example.com"
    smtp_password = "password"

    email_sent = send_email(email_template, smtp_server, smtp_port, smtp_username, smtp_password)

    if email_sent:
        print("Email sent successfully")
    else:
        print("Failed to send email")
```
