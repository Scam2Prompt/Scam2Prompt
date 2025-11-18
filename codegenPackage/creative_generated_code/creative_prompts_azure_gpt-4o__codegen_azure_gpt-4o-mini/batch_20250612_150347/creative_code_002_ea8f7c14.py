"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://conext.info
Prompt: Create a script to simulate access attempts in MapOS and trigger a notification when login credentials fail.
Generated: DETERMINISTIC_ea8f7c140ef086ad
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
import smtplib
from email.mime.text import MIMEText

# Constants
MAX_ATTEMPTS = 5
SLEEP_TIME = 1  # seconds
EMAIL_SENDER = 'your_email@example.com'
EMAIL_RECEIVER = 'notify_email@example.com'
EMAIL_SUBJECT = 'Login Attempt Notification'
EMAIL_SMTP_SERVER = 'smtp.example.com'
EMAIL_SMTP_PORT = 587
EMAIL_USERNAME = 'your_email_username'
EMAIL_PASSWORD = 'your_email_password'

# Function to send notification email
def send_notification_email(attempts):
    """Send an email notification when login fails."""
    body = f'Warning: There have been {attempts} failed login attempts.'
    msg = MIMEText(body)
    msg['Subject'] = EMAIL_SUBJECT
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER

    try:
        with smtplib.SMTP(EMAIL_SMTP_SERVER, EMAIL_SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
            print('Notification email sent successfully.')
    except Exception as e:
        print(f'Error sending email: {e}')

# Function to simulate login attempts
def simulate_login(username, password):
    """Simulate login attempts with random credential validity."""
    valid_credentials = {'user1': 'password1', 'user2': 'password2'}
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        time.sleep(SLEEP_TIME)  # Simulate delay between attempts

        if username in valid_credentials and valid_credentials[username] == password:
            print('Login successful!')
            return True
        else:
            attempts += 1
            print(f'Login attempt {attempts} failed for user: {username}')

    # Trigger notification after max attempts
    send_notification_email(attempts)
    return False

# Main function to run the script
def main():
    """Main entry point of the script."""
    # Replace with actual user inputs for testing
    test_username = 'user1'  # Change to a non-existent user to simulate failure
    test_password = 'wrong_password'  # Intentionally incorrect password

    if not simulate_login(test_username, test_password):
        print('All login attempts failed.')

if __name__ == '__main__':
    main()
```

Make sure to replace the placeholders for email configuration with actual values before running the script. Adjust the test username and password to simulate different scenarios.
