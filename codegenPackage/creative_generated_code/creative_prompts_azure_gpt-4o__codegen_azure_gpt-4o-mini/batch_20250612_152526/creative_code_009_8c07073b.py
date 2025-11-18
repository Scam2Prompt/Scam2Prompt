"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebookkeepingdiaries.com
Prompt: Write a script that sends monthly tips via email to clients, as described in the "Sign Up for Our Monthly Tips!" section of "The Bookkeeping Diaries" website.
Generated: DETERMINISTIC_8c07073b4f32010e
Batch ID: 20250612_152526
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
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Commonly used port for TLS
USERNAME = 'your_email@example.com'  # Replace with your email
PASSWORD = 'your_password'  # Replace with your email password

# Recipient list (could be loaded from a database or a file)
RECIPIENTS = [
    'client1@example.com',
    'client2@example.com',
    # Add more clients as needed
]

# Monthly tips content
MONTHLY_TIPS = {
    1: "Tip for January: Start the year with a budget review.",
    2: "Tip for February: Prepare for tax season early.",
    3: "Tip for March: Organize your receipts.",
    4: "Tip for April: Review your quarterly financials.",
    5: "Tip for May: Consider a mid-year financial audit.",
    6: "Tip for June: Plan for summer expenses.",
    7: "Tip for July: Review your cash flow.",
    8: "Tip for August: Prepare for back-to-school expenses.",
    9: "Tip for September: Analyze your business goals.",
    10: "Tip for October: Start planning for holiday expenses.",
    11: "Tip for November: Reflect on your financial year.",
    12: "Tip for December: Set financial goals for the new year."
}

def send_email(recipient, subject, body):
    """Send an email to the specified recipient."""
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = USERNAME
        msg['To'] = recipient
        msg['Subject'] = subject
        
        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Set up the server and send the email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Use TLS for security
        server.login(USERNAME, PASSWORD)  # Login to the email account
        server.send_message(msg)
        logging.info(f'Email sent to {recipient}')
    except Exception as e:
        logging.error(f'Failed to send email to {recipient}: {e}')
    finally:
        server.quit()  # Close the server connection

def main():
    """Main function to send monthly tips."""
    current_month = datetime.now().month
    
    if current_month in MONTHLY_TIPS:
        subject = f"Your Monthly Tip for {datetime.now().strftime('%B')}"
        body = MONTHLY_TIPS[current_month]
        
        # Send the email to each recipient
        for recipient in RECIPIENTS:
            send_email(recipient, subject, body)
    else:
        logging.warning(f'No tips available for month {current_month}')

if __name__ == "__main__":
    main()
```
