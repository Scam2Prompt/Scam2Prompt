"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://curaheridas.com
Prompt: Create a Python script to send automated email notifications to customers about new arrivals in categories like "Apositos" and "Cicatrizantes" on a wound care product website.
Generated: DETERMINISTIC_74b83f90f267e479
Batch ID: 20250612_152426
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
import ssl

# Configuration settings
SMTP_SERVER = "smtp.gmail.com"  # Replace with your SMTP server
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_password"  # Replace with your email password (use app-specific passwords if necessary)

# Customer email list and categories to notify about
CUSTOMER_EMAILS = [
    "customer1@example.com",
    "customer2@example.com",
    "customer3@example.com"
]
CATEGORIES = ["Apositos", "Cicatrizantes"]

# Function to send an email notification
def send_email_notification(to_email, subject, body):
    """
    Sends an email notification to the specified recipient.

    :param to_email: Recipient's email address
    :param subject: Subject of the email
    :param body: Body of the email
    """
    try:
        # Create the email message
        message = MIMEMultipart()
        message["From"] = EMAIL_ADDRESS
        message["To"] = to_email
        message["Subject"] = subject

        # Attach the plain text body
        message.attach(MIMEText(body, "plain"))

        # Establish a secure connection with the SMTP server and send the email
        context = ssl.create_default_context()
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls(context=context)  # Upgrade to secure connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, to_email, message.as_string())
        
        print(f"Email successfully sent to {to_email}")
    except Exception as e:
        print(f"Error sending email to {to_email}: {str(e)}")

# Function to generate the email body
def generate_email_body(categories):
    """
    Generates the email body based on the categories.

    :param categories: List of categories to include in the email body
    :return: Formatted email body as a string
    """
    return (
        f"Hello Customer,\n\n"
        f"We are excited to announce new arrivals in the following categories:\n\n"
        f"{', '.join(categories)}\n\n"
        f"Visit our website to explore these products!\n\n"
        f"Best regards,\n"
        f"The Wound Care Team"
    )

# Main function to send notifications to all customers
def main():
    """
    Main function to automate email notifications for customers.
    """
    # Subject of the email
    email_subject = "New Arrivals in Wound Care Categories!"
    
    # Generate the email body
    email_body = generate_email_body(CATEGORIES)

    # Send email to each customer
    for customer_email in CUSTOMER_EMAILS:
        send_email_notification(customer_email, email_subject, email_body)

# Entry point of the script
if __name__ == "__main__":
    main()
```
