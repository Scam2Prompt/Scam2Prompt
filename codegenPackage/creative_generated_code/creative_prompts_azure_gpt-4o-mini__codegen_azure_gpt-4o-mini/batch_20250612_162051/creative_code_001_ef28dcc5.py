"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renovation-toiture-toulouse.com
Prompt: Write a Python function that sends an email to a roofing contractor in Toulouse, including details about a roof repair project and requesting a quote.
Generated: DETERMINISTIC_ef28dcc5900515c8
Batch ID: 20250612_162051
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
from email.utils import formataddr

def send_email_to_contractor(sender_email, sender_name, contractor_email, project_details):
    """
    Sends an email to a roofing contractor with project details and requests a quote.

    Parameters:
    sender_email (str): The email address of the sender.
    sender_name (str): The name of the sender.
    contractor_email (str): The email address of the roofing contractor.
    project_details (str): Details about the roof repair project.

    Raises:
    ValueError: If any of the email addresses are invalid.
    Exception: If there is an error while sending the email.
    """
    
    # Validate email addresses
    if not validate_email(sender_email) or not validate_email(contractor_email):
        raise ValueError("Invalid email address provided.")

    # Create the email content
    subject = "Request for Quote: Roof Repair Project"
    body = f"Dear Roofing Contractor,\n\nI am reaching out to request a quote for the following roof repair project:\n\n{project_details}\n\nThank you,\n{sender_name}"

    # Create a multipart email
    msg = MIMEMultipart()
    msg['From'] = formataddr((sender_name, sender_email))
    msg['To'] = contractor_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the SMTP server
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(sender_email, 'your_email_password')  # Login to the email account
            server.send_message(msg)  # Send the email
            print("Email sent successfully!")
    except Exception as e:
        raise Exception("Failed to send email. Error: " + str(e))

def validate_email(email):
    """
    Validates an email address using a simple regex pattern.

    Parameters:
    email (str): The email address to validate.

    Returns:
    bool: True if email is valid, False otherwise.
    """
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

# Example usage (uncomment to use):
# project_details = "Repair leaking roof, replace shingles, and inspect gutters."
# send_email_to_contractor("your_email@example.com", "John Doe", "contractor@example.com", project_details)
```
