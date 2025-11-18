"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: Write code to send automated email notifications for weekly promotions on products like "LUVA DE SEGUR WK10 LATEX FORT G" and "TINTA SPRAY VERNIZ."
Generated: DETERMINISTIC_3ca2cf01d36d5b33
Batch ID: 20250612_145144
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/product1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/product2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
import logging

# Set up logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, filename='email_notification.log', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = "smtp.gmail.com"  # Replace with your email provider's SMTP server
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_email_password"  # Replace with your email password

# Product promotions
PROMOTIONS = [
    {"name": "LUVA DE SEGUR WK10 LATEX FORT G", "discount": "20%", "url": "https://example.com/product1"},
    {"name": "TINTA SPRAY VERNIZ", "discount": "15%", "url": "https://example.com/product2"},
]

# Recipient list
RECIPIENTS = [
    "recipient1@example.com",
    "recipient2@example.com"
]

def create_email_content(promotions):
    """
    Generate the HTML content for the promotional email.
    :param promotions: List of dictionaries containing product promotions.
    :return: HTML string for the email content.
    """
    html_content = "<h1>Weekly Promotions</h1>"
    html_content += "<ul>"
    for promo in promotions:
        html_content += f"<li><strong>{promo['name']}</strong>: {promo['discount']} off! <a href='{promo['url']}'>View Product</a></li>"
    html_content += "</ul>"
    html_content += "<p>Don't miss out on these exclusive deals!</p>"
    return html_content

def send_email(subject, html_content, recipients):
    """
    Send an email to the specified recipients with the given content.
    :param subject: Subject line for the email.
    :param html_content: HTML content for the email body.
    :param recipients: List of email addresses to send the email to.
    :return: None
    """
    try:
        # Initialize the email message
        message = MIMEMultipart()
        message["From"] = EMAIL_ADDRESS
        message["Subject"] = subject

        # Add recipients
        message["To"] = ", ".join(recipients)

        # Attach the HTML content to the email
        message.attach(MIMEText(html_content, "html"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, recipients, message.as_string())
            logging.info("Email sent successfully to: %s", recipients)
    except Exception as e:
        logging.error("Failed to send email: %s", e)

def schedule_weekly_email():
    """
    Schedule the email to be sent once a week.
    :return: None
    """
    # Generate the email content
    subject = f"Weekly Promotions - {datetime.now().strftime('%Y-%m-%d')}"
    html_content = create_email_content(PROMOTIONS)

    # Send the email
    send_email(subject, html_content, RECIPIENTS)
    logging.info("Weekly email scheduled.")

if __name__ == "__main__":
    # To simulate weekly scheduling, call the function directly.
    # In production, use a task scheduler like cron or Celery.
    schedule_weekly_email()
```

**Note:** Replace placeholders like `your_email@example.com` and `your_email_password` with actual values. Ensure your email provider allows SMTP access and configure application-specific passwords if necessary for security.
