"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitdegree.pages.dev
Prompt: Generate a script that calculates the expiration date of unused Bits based on Blockpit's policies and alerts users before their Bits expire.
Generated: DETERMINISTIC_a8685c31a93e2227
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define constants for Blockpit's expiration policy
EXPIRATION_PERIOD_DAYS = 365  # Bits expire after 365 days of inactivity
ALERT_PERIOD_DAYS = 30        # Alert the user 30 days before expiration

# Email configuration (replace with actual values)
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
EMAIL_USERNAME = "your_email@example.com"
EMAIL_PASSWORD = "your_password"
SENDER_EMAIL = "your_email@example.com"

def calculate_expiration_date(last_activity_date):
    """
    Calculate the expiration date of Bits based on the last activity date.
    :param last_activity_date: datetime object representing the last activity date
    :return: expiration_date as a datetime object
    """
    return last_activity_date + datetime.timedelta(days=EXPIRATION_PERIOD_DAYS)

def should_send_alert(expiration_date, current_date):
    """
    Determine if an alert should be sent based on the expiration date and current date.
    :param expiration_date: datetime object representing the expiration date
    :param current_date: datetime object representing the current date
    :return: True if alert should be sent, False otherwise
    """
    days_until_expiration = (expiration_date - current_date).days
    return 0 < days_until_expiration <= ALERT_PERIOD_DAYS

def send_alert_email(user_email, expiration_date):
    """
    Send an alert email to the user about their Bits expiration.
    :param user_email: string representing the user's email address
    :param expiration_date: datetime object representing the expiration date
    """
    try:
        # Create the email content
        subject = "Alert: Your Bits are about to expire!"
        body = f"Dear user,\n\nYour Bits will expire on {expiration_date.strftime('%Y-%m-%d')}. Please use them before this date to avoid losing them.\n\nBest regards,\nBlockpit Team"
        
        # Create email message
        message = MIMEMultipart()
        message["From"] = SENDER_EMAIL
        message["To"] = user_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))
        
        # Connect to SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.sendmail(SENDER_EMAIL, user_email, message.as_string())
        print(f"Alert email sent to {user_email}")
    except Exception as e:
        print(f"Failed to send email to {user_email}. Error: {e}")

def process_user_bits(user_last_activity_dates):
    """
    Process a list of users' last activity dates and calculate expiration dates, sending alerts as needed.
    :param user_last_activity_dates: dictionary with user emails as keys and last activity dates as values
    """
    current_date = datetime.datetime.now()
    
    for user_email, last_activity_date in user_last_activity_dates.items():
        try:
            # Calculate expiration date
            expiration_date = calculate_expiration_date(last_activity_date)
            
            # Check if an alert should be sent
            if should_send_alert(expiration_date, current_date):
                send_alert_email(user_email, expiration_date)
        except Exception as e:
            print(f"Error processing user {user_email}. Error: {e}")

# Example list of users and their last activity dates
# Replace with actual data in production
user_activity_data = {
    "user1@example.com": datetime.datetime(2022, 10, 1),
    "user2@example.com": datetime.datetime(2023, 1, 15),
    "user3@example.com": datetime.datetime(2022, 11, 10),
}

# Process users and send alerts
process_user_bits(user_activity_data)
```
