"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ifesty.com.br
Prompt: Write a function to send promotional emails to users registered on Ifesty, highlighting featured services like "Cerimonial" and "Decoração."
Generated: DETERMINISTIC_3fe99dc71601feb9
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

# Set up logging for error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_promotional_emails(users, featured_services):
    """
    Sends promotional emails to users, highlighting featured services.

    Args:
        users (list): List of user dictionaries containing 'name' and 'email'.
        featured_services (list): List of strings representing featured services.

    Returns:
        None
    """
    # Email configuration
    smtp_server = "smtp.gmail.com"  # Replace with actual SMTP server
    smtp_port = 587  # Common port for TLS
    sender_email = "your_email@example.com"  # Replace with your email
    sender_password = "your_password"  # Replace with your password

    # Construct the email content for featured services
    services_list = "\n".join(f"- {service}" for service in featured_services)
    email_subject = "Discover Our Featured Services!"
    email_body_template = """\
    Hi {name},

    We are excited to share our featured services with you:

    {services}

    Don't miss out on these amazing offerings!

    Best regards,
    Ifesty Team
    """

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade to secure connection
        server.login(sender_email, sender_password)
        logging.info("Successfully logged in to the SMTP server.")

        # Send emails to each user
        for user in users:
            try:
                # Create personalized email content
                email_body = email_body_template.format(name=user['name'], services=services_list)
                
                # Configure the email message
                message = MIMEMultipart()
                message['From'] = sender_email
                message['To'] = user['email']
                message['Subject'] = email_subject
                message.attach(MIMEText(email_body, 'plain'))
                
                # Send the email
                server.sendmail(sender_email, user['email'], message.as_string())
                logging.info(f"Promotional email successfully sent to {user['email']}.")
            except Exception as e:
                logging.error(f"Failed to send email to {user['email']}. Error: {e}")

    except Exception as e:
        logging.error(f"Failed to connect to SMTP server or send emails. Error: {e}")
    finally:
        # Ensure the SMTP server connection is closed
        server.quit()
        logging.info("SMTP server connection closed.")

# Example usage
if __name__ == "__main__":
    # List of users to send the emails to
    users = [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.com"},
    ]

    # Featured services to highlight
    featured_services = ["Cerimonial", "Decoração"]

    # Call the function
    send_promotional_emails(users, featured_services)
```

**Note:** Replace `your_email@example.com` and `your_password` with valid credentials. Use environment variables or a secure configuration file for sensitive data in production environments.
