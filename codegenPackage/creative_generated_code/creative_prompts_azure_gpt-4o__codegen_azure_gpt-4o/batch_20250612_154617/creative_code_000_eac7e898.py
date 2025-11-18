"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dow.spb.ru
Prompt: Write Python code to automate the ordering process for materials like Betaseal 1001 adhesive and primers from the official distributor "Гарант" in Russia, using their contact email and phone number provided on the site.
Generated: DETERMINISTIC_eac7e8981837191a
Batch ID: 20250612_154617
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

# Logging configuration
logging.basicConfig(
    filename="order_automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def send_order_email(distributor_email, distributor_phone, materials, sender_email, email_password):
    """
    Automates the ordering process for materials from the distributor.

    Args:
        distributor_email (str): Email address of the distributor.
        distributor_phone (str): Phone number of the distributor.
        materials (list): List of materials to be ordered.
        sender_email (str): Email address of the sender (your email).
        email_password (str): Password for the sender's email (for authentication).

    Returns:
        None
    """
    try:
        # Create email content
        subject = "Order Request for Materials"
        body = f"Dear Гарант,\n\nI would like to place an order for the following materials:\n\n"
        body += "\n".join(materials)
        body += f"\n\nPlease contact me via email or phone to confirm the order.\n\nContact Info:\nPhone: {distributor_phone}\nEmail: {distributor_email}\n\nBest regards,\n"
        
        # Set up MIME structure
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = distributor_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Connect to SMTP server
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure connection
        server.login(sender_email, email_password)

        # Send email
        server.send_message(message)
        logging.info(f"Order email sent successfully to {distributor_email}.")
        print("Order email sent successfully!")
    except smtplib.SMTPException as e:
        logging.error(f"Failed to send order email: {str(e)}")
        print("Failed to send order email. Please check the logs for details.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        print("An unexpected error occurred. Please check the logs for details.")
    finally:
        server.quit()


# Example of usage
if __name__ == "__main__":
    # Replace these placeholders with actual values
    distributor_email = "distributor@example.com"  # Replace with the distributor's email
    distributor_phone = "+7-XXX-XXX-XXXX"          # Replace with the distributor's phone number
    materials = ["Betaseal 1001 Adhesive", "Primer A", "Primer B"]
    sender_email = "your_email@example.com"        # Replace with your email
    email_password = "your_email_password"         # Replace with your email password

    send_order_email(distributor_email, distributor_phone, materials, sender_email, email_password)
```
