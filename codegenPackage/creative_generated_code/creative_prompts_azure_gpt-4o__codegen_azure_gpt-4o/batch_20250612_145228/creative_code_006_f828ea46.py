"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sgfcfinance.com
Prompt: Write code to generate automated email updates for SGFC Finance's newsletter subscribers, including weekly updates on financial literacy programs and community initiatives.
Generated: DETERMINISTIC_f828ea4653728db5
Batch ID: 20250612_145228
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
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, filename='email_updates.log', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# SMTP Server Configuration
SMTP_HOST = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@example.com'  # Replace with your email
EMAIL_PASSWORD = 'your_password'  # Replace with your email password

# Mock database of subscribers
subscribers = [
    {'name': 'John Doe', 'email': 'johndoe@example.com'},
    {'name': 'Jane Smith', 'email': 'janesmith@example.com'},
    {'name': 'Bob Johnson', 'email': 'bobjohnson@example.com'}
]

# Email content template
EMAIL_SUBJECT = "Weekly Updates: Financial Literacy Programs and Initiatives"
EMAIL_TEMPLATE = """
<html>
<body>
    <h1>Hello {name},</h1>
    <p>Here are your weekly updates from SGFC Finance:</p>
    <h2>Financial Literacy Programs</h2>
    <ul>
        <li>Program A: Learn to Budget (Monday, 4 PM)</li>
        <li>Program B: Investing Basics (Wednesday, 6 PM)</li>
    </ul>
    <h2>Community Initiatives</h2>
    <ul>
        <li>Free Credit Counseling Workshops</li>
        <li>Local Small Business Support Events</li>
    </ul>
    <p>We hope to see you participate!</p>
    <p>Best regards,<br>SGFC Finance Team</p>
</body>
</html>
"""

def send_email(to_name, to_email):
    try:
        # Create a MIME object for the email
        msg = MIMEMultipart("alternative")
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = EMAIL_SUBJECT

        # Personalize the email content
        email_content = EMAIL_TEMPLATE.format(name=to_name)
        
        # Attach the email body
        msg.attach(MIMEText(email_content, 'html'))

        # Connect to the SMTP server
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
        
        # Log success
        logging.info(f"Email sent successfully to {to_name} <{to_email}>.")
    
    except Exception as e:
        # Log any errors that occur
        logging.error(f"Failed to send email to {to_name} <{to_email}>: {str(e)}")

def send_newsletter_to_all_subscribers():
    # Iterate through the list of subscribers and send emails
    for subscriber in subscribers:
        send_email(subscriber['name'], subscriber['email'])

if __name__ == "__main__":
    # Log the start of the script
    logging.info("Starting the newsletter email sending script.")
    
    # Send newsletter emails
    send_newsletter_to_all_subscribers()
    
    # Log the completion of the script
    logging.info("Completed sending all newsletter emails.")
```
