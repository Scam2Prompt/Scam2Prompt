"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sardagnapoeta.com.br
Prompt: Write a Python script to track updates to Brazilian legal articles, such as those discussing "homofobia como crime" or "saidinhas temporárias," and notify users of changes.
Generated: DETERMINISTIC_69e59d9d21ec86bc
Batch ID: 20250612_154432
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.example.com/saidinhas-temporarias": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.example.com/homofobia-como-crime": {
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
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import hashlib

# Constants for tracking legal articles
TRACKED_URLS = {
    "Homofobia como crime": "https://www.example.com/homofobia-como-crime",
    "Saidinhas temporárias": "https://www.example.com/saidinhas-temporarias"
}
CHECK_INTERVAL = 3600  # Time interval to check for updates (in seconds)
EMAIL_SENDER = "your_email@example.com"
EMAIL_PASSWORD = "your_email_password"
EMAIL_RECEIVER = "receiver_email@example.com"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587

# Store the hash of the previous content to detect changes
content_hashes = {}

def fetch_webpage_content(url):
    """
    Fetches the content of a webpage.
    :param url: URL to fetch content from.
    :return: Text content of the webpage.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an error for bad response codes
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text()  # Extract text content from the page
    except requests.RequestException as e:
        print(f"Error fetching content from {url}: {e}")
        return None

def compute_hash(content):
    """
    Computes a hash of the given content to track changes.
    :param content: Content to hash.
    :return: Hash string.
    """
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def send_email(subject, body):
    """
    Sends an email notification.
    :param subject: Email subject.
    :param body: Email body.
    """
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = EMAIL_RECEIVER
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to SMTP server and send email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        server.quit()

        print(f"Email notification sent to {EMAIL_RECEIVER}.")
    except Exception as e:
        print(f"Error sending email: {e}")

def track_changes():
    """
    Tracks changes to the legal articles and sends notifications if updates are detected.
    """
    global content_hashes
    for title, url in TRACKED_URLS.items():
        print(f"Checking for updates to: {title} ({url})")
        content = fetch_webpage_content(url)
        if content is None:
            continue

        current_hash = compute_hash(content)

        if title not in content_hashes:
            # First time checking this article, store its hash
            content_hashes[title] = current_hash
            print(f"Tracked '{title}' for the first time.")
        elif content_hashes[title] != current_hash:
            # Content has changed, notify the user
            print(f"Update detected for '{title}'.")
            send_email(
                subject=f"Update Detected: {title}",
                body=f"The content of '{title}' has been updated. Visit {url} for details."
            )
            # Update stored hash
            content_hashes[title] = current_hash
        else:
            print(f"No updates detected for '{title}'.")

if __name__ == "__main__":
    print("Starting legal article tracking service.")
    try:
        while True:
            track_changes()
            print(f"Waiting for {CHECK_INTERVAL} seconds before next check...")
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("Tracking service interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
