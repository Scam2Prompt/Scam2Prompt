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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_email(to_email, subject, body):
    """
    Sends an email to the specified address.

    Args:
        to_email (str): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The body of the email.
    
    Raises:
        Exception: Raises an exception if the email fails to send.
    """
    from_email = 'your_email@example.com'  # Replace with your email address
    password = 'your_password'  # Replace with your email password or app-specific password

    # Create a multipart email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        # Establish a secure session with Gmail's outgoing SMTP server using your gmail account
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Use TLS encryption
            server.login(from_email, password)  # Log in to the server
            server.send_message(msg)  # Send the email
            logging.info("Email sent successfully to %s", to_email)
    except Exception as e:
        logging.error("Failed to send email: %s", e)
        raise

def request_electrician_service():
    """
    Constructs and sends an email request for residential electrical services.
    """
    # Define recipient email and email content
    electrician_email = 'electrician_service@example.com'  # Replace with the electrician's email address
    subject = "Request for Residential Electrical Work"
    body = (
        "Dear Electrician Service,\n\n"
        "I am looking for a qualified electrician to assist with some residential electrical work. "
        "Could you please provide me with an estimate for reasonable pricing and availability?\n\n"
        "Thank you,\n"
        "Your Name\n"
        "Your Address\n"
        "Your Phone Number\n"
    )

    try:
        send_email(electrician_email, subject, body)
    except Exception as e:
        logging.error("Error while requesting electrician service: %s", e)

if __name__ == '__main__':
    request_electrician_service()
```

**Note:** Remember to replace placeholder values (like `your_email@example.com`, `your_password`, and `electrician_service@example.com`) with actual email addresses and relevant information before running the script. Ensure that you follow your email provider's guidelines regarding sending emails programmatically, and consider using an app password if using Gmail.
