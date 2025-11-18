"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finishdrop.com
Prompt: Write a script to send automated emails containing e-commerce site credentials and onboarding materials, similar to the post-purchase process described on FinishDrop.
Generated: DETERMINISTIC_c53b559aa0d43ac3
Batch ID: 20250612_151752
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

# Configure logging to capture any runtime errors
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_email(to_email, subject, body):
    """
    Sends an email with the specified subject and body to the given email address.

    Args:
        to_email (str): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The body of the email.
    
    Raises:
        Exception: If there is an error sending the email.
    """
    try:
        # Email configuration
        from_email = 'your_email@example.com'  # Replace with your email
        password = 'your_password'  # Replace with your email account password
        
        # Create a multipart email
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))
        
        # Connect to the email server
        with smtplib.SMTP('smtp.example.com', 587) as server:  # Replace with your SMTP server
            server.starttls()  # Use TLS encryption
            server.login(from_email, password)  # Login to the email account
            server.send_message(msg)  # Send the email

        logging.info(f"Email sent successfully to {to_email}")

    except Exception as e:
        logging.error(f"Failed to send email to {to_email}: {e}")
        raise

def main():
    """
    Main function to execute the email sending process.
    """
    # Define email recipients and content
    recipient_email = 'recipient@example.com'  # Replace with recipient's email
    email_subject = 'Welcome to our E-commerce Platform!'
    
    # Create the email body with onboarding materials
    email_body = (
        "Dear Customer,\n\n"
        "Thank you for your purchase! Here are your credentials and onboarding materials:\n\n"
        "Username: your_username\n"  # Replace with actual username
        "Password: your_password\n"    # Replace with actual password
        "Onboarding Guide: [Link to Guide]\n\n"
        "Best regards,\n"
        "The E-commerce Team"
    )

    # Send the email
    send_email(recipient_email, email_subject, email_body)

if __name__ == "__main__":
    main()
```
