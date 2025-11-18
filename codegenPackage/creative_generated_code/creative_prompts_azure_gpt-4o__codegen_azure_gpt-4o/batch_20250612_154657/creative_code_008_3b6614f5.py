"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seedify.me
Prompt: Write a script in Python that integrates with email APIs to send weekly tips, hacks, and shortcuts for health, happiness, and success, as described on the Seedify website.
Generated: DETERMINISTIC_3b6614f5b5364617
Batch ID: 20250612_154657
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
import schedule
import time
import logging

# Setup logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration (replace these placeholders with actual values)
SMTP_SERVER = "smtp.gmail.com"  # Example: Gmail SMTP server
SMTP_PORT = 587  # Common SMTP port for TLS
EMAIL_ADDRESS = "your_email@example.com"  # Your email address
EMAIL_PASSWORD = "your_password"  # Your email password

# Recipient email list
RECIPIENTS = [
    "recipient1@example.com",
    "recipient2@example.com",
    "recipient3@example.com",
]

# Weekly tips content
TIPS = [
    "Tip #1: Drink plenty of water to stay hydrated throughout the day.",
    "Tip #2: Get at least 7-8 hours of sleep to improve your mental and physical health.",
    "Tip #3: Take short breaks during work to boost productivity and reduce stress.",
    "Tip #4: Incorporate mindfulness practices, such as meditation, into your routine.",
    "Tip #5: Exercise regularly to maintain a healthy body and mind.",
    "Tip #6: Set small, achievable goals to steadily work toward bigger successes.",
    "Tip #7: Practice gratitude daily to increase happiness and positivity.",
]

def send_email(subject, body, recipients):
    """
    Sends an email using the provided subject, body, and recipient list.
    
    Args:
        subject (str): The subject of the email.
        body (str): The content of the email.
        recipients (list): List of email addresses to receive the email.
    """
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        # Connect to the SMTP server
        logging.info("Connecting to SMTP server...")
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure TLS
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Login to email account
            logging.info("Successfully logged in to SMTP server.")
            
            # Send email to each recipient
            for recipient in recipients:
                msg['To'] = recipient
                server.sendmail(EMAIL_ADDRESS, recipient, msg.as_string())
                logging.info(f"Email sent to {recipient}")
                
    except Exception as e:
        logging.error(f"Failed to send email: {e}")
        raise

def weekly_email_job():
    """
    Scheduled job to send weekly tips via email.
    """
    logging.info("Preparing to send weekly email...")
    subject = "Weekly Tips for Health, Happiness, and Success"
    body = "\n\n".join(TIPS)  # Combine all tips into the email body
    send_email(subject, body, RECIPIENTS)
    logging.info("Weekly email sent successfully.")

# Schedule the email job to run every Monday at 9 AM
schedule.every().monday.at("09:00").do(weekly_email_job)

logging.info("Email scheduler started.")
try:
    # Keep the scheduler running
    while True:
        schedule.run_pending()
        time.sleep(1)  # Sleep to prevent busy-waiting
except KeyboardInterrupt:
    logging.info("Email scheduler stopped by user.")
```
