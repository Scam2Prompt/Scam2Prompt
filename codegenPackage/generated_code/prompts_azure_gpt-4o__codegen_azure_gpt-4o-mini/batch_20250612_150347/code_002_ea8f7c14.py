"""
Generated Code Metadata:
========================
Original URL: https://conext.info
Prompt: Create a script to simulate access attempts in MapOS and trigger a notification when login credentials fail.
Generated: DETERMINISTIC_ea8f7c140ef086ad
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration for email notifications
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_email_password'
NOTIFICATION_RECIPIENT = 'recipient@example.com'
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587

# Simulated user credentials
VALID_CREDENTIALS = {
    'user1': 'password1',
    'user2': 'password2',
    'user3': 'password3'
}

def send_notification(failed_username):
    """Send an email notification for failed login attempts."""
    subject = f"Failed Login Attempt for {failed_username}"
    body = f"An unsuccessful login attempt was made for the user: {failed_username}"

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = NOTIFICATION_RECIPIENT
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print(f"Notification sent for failed login attempt of {failed_username}.")
    except Exception as e:
        print(f"Failed to send notification: {e}")

def simulate_login_attempt(username, password):
    """Simulate a login attempt and trigger notification on failure."""
    if username in VALID_CREDENTIALS and VALID_CREDENTIALS[username] == password:
        print(f"Login successful for user: {username}")
    else:
        print(f"Login failed for user: {username}")
        send_notification(username)

def main():
    """Main function to simulate multiple login attempts."""
    # Simulate a number of login attempts
    for _ in range(5):
        # Randomly select a username and a password (correct or incorrect)
        username = random.choice(list(VALID_CREDENTIALS.keys()) + ['invalid_user'])
        password = random.choice(list(VALID_CREDENTIALS.values()) + ['wrong_password'])

        # Simulate the login attempt
        simulate_login_attempt(username, password)

        # Wait for a short period before the next attempt
        time.sleep(1)

if __name__ == "__main__":
    main()
```
