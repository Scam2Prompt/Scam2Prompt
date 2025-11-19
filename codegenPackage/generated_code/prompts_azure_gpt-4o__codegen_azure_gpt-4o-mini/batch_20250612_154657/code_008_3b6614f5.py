"""
Generated Code Metadata:
========================
Original URL: https://seedify.me
Prompt: Write a script in Python that integrates with email APIs to send weekly tips, hacks, and shortcuts for health, happiness, and success, as described on the Seedify website.
Generated: DETERMINISTIC_3b6614f5b5364617
Batch ID: 20250612_154657
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
import schedule
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Replace with your SMTP port
USERNAME = 'your_email@example.com'  # Replace with your email
PASSWORD = 'your_password'  # Replace with your email password
RECIPIENTS = ['recipient1@example.com', 'recipient2@example.com']  # List of recipients

# Function to create the email content
def create_email_content():
    """Generates the email content with health, happiness, and success tips."""
    tips = [
        "Tip 1: Stay hydrated. Drink at least 8 glasses of water a day.",
        "Tip 2: Practice gratitude. Write down three things you're grateful for each day.",
        "Tip 3: Set achievable goals. Break your goals into smaller, manageable tasks.",
        "Tip 4: Take breaks. Short breaks can improve productivity and focus.",
        "Tip 5: Get enough sleep. Aim for 7-9 hours of quality sleep each night."
    ]
    content = "<h1>Weekly Tips for Health, Happiness, and Success</h1>"
    content += "<ul>"
    for tip in tips:
        content += f"<li>{tip}</li>"
    content += "</ul>"
    return content

# Function to send the email
def send_email():
    """Sends an email with weekly tips to the specified recipients."""
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = USERNAME
        msg['To'] = ", ".join(RECIPIENTS)
        msg['Subject'] = 'Weekly Tips for Health, Happiness, and Success'
        
        # Attach the email content
        email_content = create_email_content()
        msg.attach(MIMEText(email_content, 'html'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(USERNAME, PASSWORD)
            server.send_message(msg)
            logging.info("Email sent successfully to %s", ", ".join(RECIPIENTS))
    except Exception as e:
        logging.error("Failed to send email: %s", e)

# Schedule the email to be sent weekly
schedule.every().monday.at("09:00").do(send_email)  # Change the time as needed

# Main loop to keep the script running
if __name__ == "__main__":
    logging.info("Starting the email scheduler...")
    while True:
        schedule.run_pending()
        time.sleep(1)  # Wait for one second before checking the schedule again
```

Make sure to replace the placeholders in the configuration section with your actual SMTP server details, email, and password. Additionally, ensure that the SMTP server allows sending emails from your account and that you have the necessary permissions.
