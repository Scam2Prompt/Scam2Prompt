"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bananarewards.pages.dev
Prompt: Create a notification system that alerts users when their accrued rewards exceed the minimum thresholds for claiming ($BANANA, $ETH, or $SOL).
Generated: DETERMINISTIC_8cb44b3ab0abf763
Batch ID: 20250612_151141
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

# Constants
THRESHOLDS = {
    "BANANA": 50.0,  # Minimum threshold for BANANA rewards
    "ETH": 0.01,     # Minimum threshold for ETH rewards
    "SOL": 0.5       # Minimum threshold for SOL rewards
}

SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587                   # Replace with your SMTP port
SENDER_EMAIL = "your-email@example.com"  # Replace with your email
SENDER_PASSWORD = "your-password"       # Replace with your email password

def send_email(recipient_email, subject, body):
    """
    Sends a notification email to the user.
    
    Args:
        recipient_email (str): The recipient's email address.
        subject (str): The email subject line.
        body (str): The content of the email.
    
    Raises:
        Exception: If the email fails to send.
    """
    try:
        # Create a MIME message
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Establish connection to the SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")
        raise

def check_rewards_and_notify(user_rewards):
    """
    Checks user rewards against thresholds and notifies them via email.

    Args:
        user_rewards (list of dict): List of users with reward details.
            Each dict contains:
                - 'email' (str): User's email address.
                - 'rewards' (dict): Accrued rewards in the format {"BANANA": float, "ETH": float, "SOL": float}.
    """
    for user in user_rewards:
        email = user.get('email')
        rewards = user.get('rewards')
        
        if not email or not rewards:
            print(f"Invalid user data: {user}")
            continue
        
        # Accumulate notification messages
        alert_messages = []
        for reward_type, threshold in THRESHOLDS.items():
            if rewards.get(reward_type, 0) >= threshold:
                alert_messages.append(f"Your {reward_type} rewards have exceeded the minimum threshold of {threshold} and are now at {rewards.get(reward_type)}.")

        # If there are alerts, send an email
        if alert_messages:
            subject = "Rewards Notification"
            body = "\n".join(alert_messages)
            try:
                send_email(email, subject, body)
                print(f"Notification sent to {email}")
            except Exception as e:
                print(f"Error sending notification to {email}: {e}")

# Example usage
if __name__ == "__main__":
    # Sample user data
    users = [
        {
            "email": "user1@example.com",
            "rewards": {"BANANA": 60.0, "ETH": 0.005, "SOL": 0.6}
        },
        {
            "email": "user2@example.com",
            "rewards": {"BANANA": 40.0, "ETH": 0.02, "SOL": 0.3}
        },
        {
            "email": "user3@example.com",
            "rewards": {"BANANA": 55.0, "ETH": 0.01, "SOL": 0.7}
        }
    ]

    check_rewards_and_notify(users)
```
