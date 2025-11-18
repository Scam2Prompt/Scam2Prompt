"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://steamgames.in
Prompt: Write a script to send automated email notifications to customers from a store like Steam Key when new game keys are added or discounts are applied.
Generated: DETERMINISTIC_af57281c3b4f7f1b
Batch ID: 20250612_151917
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
from typing import List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configurations
SMTP_SERVER = "smtp.gmail.com"  # Replace with your SMTP server (e.g., Gmail, Yahoo)
SMTP_PORT = 587  # Port for SMTP server
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_email_password"  # Replace with your email password

# A mock function to simulate retrieval of customer emails
def get_customer_emails() -> List[str]:
    """
    Retrieve a list of customer email addresses from the database.
    Replace this mock function with an actual database query.
    """
    return ["customer1@example.com", "customer2@example.com"]

# A mock function to simulate retrieval of new game keys or discounted items
def get_new_promotions() -> str:
    """
    Retrieve new game keys or discounts available.
    Replace this mock function with an actual database query.
    """
    return "New Game Keys: Game1, Game2\nDiscounts: Game3 - 50% off"

# Function to send email notifications
def send_email_notification(recipient_email: str, subject: str, body: str):
    """
    Sends an email notification to a customer.
    Args:
        recipient_email (str): Email address of the customer.
        subject (str): Subject of the email.
        body (str): Body of the email.
    """
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = recipient_email
        msg["Subject"] = subject

        # Attach the email body
        msg.attach(MIMEText(body, "plain"))

        # Establish connection to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Log in to the SMTP server
            server.send_message(msg)  # Send the email

        logging.info(f"Email sent successfully to {recipient_email}")
    except Exception as e:
        logging.error(f"Failed to send email to {recipient_email}. Error: {e}")

# Main script to send notifications
def main():
    """
    Main function to send email notifications to customers when promotions are available.
    """
    logging.info("Starting email notification script...")

    # Retrieve customer emails and promotions
    customer_emails = get_customer_emails()
    promotions = get_new_promotions()

    # Email subject and body
    email_subject = "🎮 New Promotions Available at Steam Key!"
    email_body = f"Hello!\n\nCheck out our latest promotions:\n\n{promotions}\n\nBest regards,\nSteam Key Team"

    # Send notifications to all customers
    for email in customer_emails:
        send_email_notification(email, email_subject, email_body)

    logging.info("Email notifications sent to all customers.")

if __name__ == "__main__":
    main()
```
