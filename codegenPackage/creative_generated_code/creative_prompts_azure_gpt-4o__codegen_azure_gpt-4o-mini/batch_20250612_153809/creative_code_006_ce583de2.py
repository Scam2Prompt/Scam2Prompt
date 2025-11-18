"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-cndl.net
Prompt: Create a program to monitor development progress and version releases on the $CNDL Staging Branch, including notifications for new builds.
Generated: DETERMINISTIC_ce583de29dcf60c0
Batch ID: 20250612_153809
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.github.com/repos/user/repo/commits": {
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
import requests
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
GITHUB_API_URL = "https://api.github.com/repos/user/repo/commits"
BRANCH_NAME = "staging"
CHECK_INTERVAL = 60  # Check every 60 seconds
EMAIL_SENDER = "your_email@example.com"
EMAIL_RECEIVER = "recipient_email@example.com"
EMAIL_SUBJECT = "New Build Notification"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USERNAME = "your_email@example.com"
SMTP_PASSWORD = "your_password"

def send_email_notification(commit_message):
    """Sends an email notification about the new build."""
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = EMAIL_RECEIVER
        msg['Subject'] = EMAIL_SUBJECT

        body = f"New build on {BRANCH_NAME} branch:\n\n{commit_message}"
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)

        print("Notification email sent.")
    except Exception as e:
        print(f"Failed to send email notification: {str(e)}")

def get_latest_commit():
    """Fetches the latest commit from the specified branch."""
    try:
        response = requests.get(GITHUB_API_URL, params={'sha': BRANCH_NAME})
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        commits = response.json()
        
        if commits:  # Check if there are any commits
            return commits[0]['commit']['message'], commits[0]['sha']
        else:
            return None, None
    except requests.RequestException as e:
        print(f"Error fetching commits: {str(e)}")
        return None, None

def monitor_branch():
    """Monitors the specified branch for new builds."""
    last_commit_sha = None

    while True:
        commit_message, current_commit_sha = get_latest_commit()
        
        if current_commit_sha and current_commit_sha != last_commit_sha:
            print(f"New commit detected: {commit_message}")
            send_email_notification(commit_message)
            last_commit_sha = current_commit_sha
        
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor_branch()
```
