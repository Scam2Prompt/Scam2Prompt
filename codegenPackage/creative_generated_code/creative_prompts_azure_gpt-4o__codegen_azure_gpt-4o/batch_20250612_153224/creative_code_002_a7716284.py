"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magicbear.com.br
Prompt: Generate code to send automated email notifications (e.g., contato@magicbear.com.br) to parents about updates in a bilingual school program using Python.
Generated: DETERMINISTIC_a771628402f1e6be
Batch ID: 20250612_153224
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

# Function to send email notifications
def send_email_notification(subject, body, recipient_email, sender_email, sender_password):
    """
    Sends an email notification to a specified recipient.

    Args:
        subject (str): The subject of the email.
        body (str): The body of the email.
        recipient_email (str): The recipient's email address.
        sender_email (str): The sender's email address.
        sender_password (str): The sender's email account password.

    Returns:
        None
    """
    try:
        # Set up the MIME structure of the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the body message to the email
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        logging.info("Connecting to SMTP server...")
        with smtplib.SMTP('smtp.gmail.com', 587) as server:  # Example: Gmail SMTP server (adjust if needed)
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)  # Log in to the email server
            server.send_message(msg)  # Send the email
            logging.info(f"Email sent successfully to {recipient_email}")
    
    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

# Main function to demonstrate email sending
def main():
    """
    Main function to send an example email notification to parents.
    """
    # Example email details (replace with actual values for production use)
    sender_email = "contato@magicbear.com.br"
    sender_password = "your-email-password"  # Replace with a secure password or use environment variables
    recipient_email = "parent@example.com"  # Replace with the parent's email address
    subject = "Bilingual Program Update"
    body = (
        "Dear Parents,\n\n"
        "We are excited to share updates about our bilingual school program. "
        "Please check your parent portal for more details.\n\n"
        "Best regards,\n"
        "Magic Bear School Team"
    )

    # Send the email notification
    send_email_notification(subject, body, recipient_email, sender_email, sender_password)

# Entry point of the script
if __name__ == "__main__":
    main()
```
