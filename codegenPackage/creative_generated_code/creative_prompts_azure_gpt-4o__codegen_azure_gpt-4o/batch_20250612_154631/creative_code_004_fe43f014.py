"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeinvestmentslimited.org
Prompt: Write a script to automate subscription-based updates for clients, similar to the newsletter system mentioned on Finance Investment Limited's webpage.
Generated: DETERMINISTIC_fe43f014c6b25161
Batch ID: 20250612_154631
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
from email.utils import formataddr
import sqlite3
from datetime import datetime
import traceback

# Constants
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@example.com"
EMAIL_PASSWORD = "your_secure_password"
SUBJECT = "Finance Investment Ltd: Monthly Newsletter"
FROM_NAME = "Finance Investment Ltd"

DB_PATH = "subscriptions.db"

# Function to send email
def send_email(recipient_email, recipient_name, newsletter_content):
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = formataddr((FROM_NAME, EMAIL_ADDRESS))
        msg['To'] = recipient_email
        msg['Subject'] = SUBJECT

        # Email body
        body = f"Dear {recipient_name},\n\n{newsletter_content}\n\nBest regards,\nFinance Investment Ltd"
        msg.attach(MIMEText(body, 'plain'))

        # Connect to SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, recipient_email, msg.as_string())
        print(f"Email sent successfully to {recipient_name} ({recipient_email})")
    except Exception as e:
        print(f"Failed to send email to {recipient_name} ({recipient_email}): {str(e)}")
        traceback.print_exc()

# Function to fetch subscribers from the database
def fetch_subscribers():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT name, email FROM subscribers WHERE active=1")
        subscribers = cursor.fetchall()
        conn.close()
        return subscribers
    except Exception as e:
        print(f"Error fetching subscribers: {str(e)}")
        traceback.print_exc()
        return []

# Main function to automate newsletter sending
def send_newsletter():
    try:
        # Fetch subscribers
        subscribers = fetch_subscribers()
        if not subscribers:
            print("No active subscribers found.")
            return

        # Generate newsletter content (this would typically be dynamic)
        current_date = datetime.now().strftime("%B %Y")
        newsletter_content = f"Welcome to our Finance Investment newsletter for {current_date}! Stay tuned for updates on market trends and investment strategies."
        
        # Send email to each subscriber
        for name, email in subscribers:
            send_email(email, name, newsletter_content)
    except Exception as e:
        print(f"Error during newsletter sending process: {str(e)}")
        traceback.print_exc()

# Entry point
if __name__ == "__main__":
    print("Starting newsletter automation...")
    send_newsletter()
    print("Newsletter automation completed.")
```

### Notes:
1. Replace `SMTP_SERVER`, `SMTP_PORT`, `EMAIL_ADDRESS`, and `EMAIL_PASSWORD` with your SMTP provider's credentials.
2. Ensure `subscriptions.db` exists, with a table named `subscribers` containing columns `name`, `email`, and `active`.
