"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-home-f.blogspot.com
Prompt: Generate a Python script to automate email subscription for sending updates on interior design trends and exclusive materials, similar to the "Fique por Dentro" feature on the website.
Generated: DETERMINISTIC_82f7c394fdc70452
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.message import EmailMessage
import csv
import os

# Configuration
SMTP_SERVER = 'smtp.gmail.com'  # Replace with your email provider's SMTP server
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@example.com'  # Replace with your email address
EMAIL_PASSWORD = 'your_email_password'  # Replace with your email password
SUBSCRIPTION_FILE = 'subscriptions.csv'  # File to store email subscriptions

def send_subscription_email(subscriber_email):
    """
    Sends a subscription confirmation email to the subscriber.
    
    Args:
        subscriber_email (str): Email address of the subscriber.
    """
    try:
        # Create email message
        msg = EmailMessage()
        msg['Subject'] = 'Subscription Confirmation: Interior Design Updates'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = subscriber_email
        msg.set_content("Thank you for subscribing to updates on interior design trends and exclusive materials!")

        # Connect to SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"Confirmation email sent to {subscriber_email}.")
    except Exception as e:
        print(f"Failed to send email to {subscriber_email}: {e}")

def save_subscription(subscriber_email):
    """
    Saves the subscriber's email address to the subscription file.
    
    Args:
        subscriber_email (str): Email address of the subscriber.
    """
    try:
        # Ensure the subscription file exists or create it
        file_exists = os.path.isfile(SUBSCRIPTION_FILE)
        
        # Open the file in append mode and write the email address
        with open(SUBSCRIPTION_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:  # Add headers if file does not exist
                writer.writerow(['Email'])
            writer.writerow([subscriber_email])
        print(f"Subscription saved for {subscriber_email}.")
    except Exception as e:
        print(f"Failed to save subscription for {subscriber_email}: {e}")

def subscribe_user():
    """
    Collects user input for email subscription and processes the subscription.
    """
    subscriber_email = input("Enter your email address to subscribe: ").strip()
    
    # Basic email validation
    if '@' not in subscriber_email or '.' not in subscriber_email:
        print("Invalid email address. Please try again.")
        return
    
    save_subscription(subscriber_email)
    send_subscription_email(subscriber_email)

if __name__ == '__main__':
    print("Welcome to the Interior Design Updates Subscription System!")
    subscribe_user()
```

### Notes:
1. Replace `your_email@example.com` and `your_email_password` with valid credentials for the email account you wish to use.
2. Ensure the SMTP server and port match your email provider's configuration.
3. For production, use environment variables or a secrets manager to store sensitive data such as email credentials.
