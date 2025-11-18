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
  "https://example.com/legal-article2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/legal-article1": {
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
from time import sleep
import hashlib
import os

class LegalArticleTracker:
    def __init__(self, articles, email_recipient):
        """
        Initializes the LegalArticleTracker.

        :param articles: List of URLs of legal articles to track.
        :param email_recipient: Email address to notify upon updates.
        """
        self.articles = articles
        self.email_recipient = email_recipient
        self.article_hashes = {}

    def fetch_article(self, url):
        """
        Fetches the content of a legal article.

        :param url: URL of the legal article.
        :return: Raw article content.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for HTTP errors
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching article from {url}: {e}")
            return None

    def calculate_hash(self, content):
        """
        Calculates a hash of the article content.

        :param content: Raw article content.
        :return: SHA256 hash of the content.
        """
        return hashlib.sha256(content.encode('utf-8')).hexdigest()

    def send_notification(self, article_url):
        """
        Sends an email notification about the article update.

        :param article_url: URL of the updated legal article.
        """
        subject = f"Update on Legal Article: {article_url}"
        body = f"The legal article at {article_url} has been updated."
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = os.environ.get('EMAIL_SENDER')
        msg['To'] = self.email_recipient

        try:
            with smtplib.SMTP('smtp.example.com', 587) as server:
                server.starttls()
                server.login(os.environ.get('EMAIL_SENDER'), os.environ.get('EMAIL_PASSWORD'))
                server.sendmail(os.environ.get('EMAIL_SENDER'), self.email_recipient, msg.as_string())
            print(f"Notification sent to {self.email_recipient} for {article_url}.")
        except Exception as e:
            print(f"Failed to send email notification: {e}")

    def track_articles(self):
        """
        Continuously tracks the articles for updates.
        """
        while True:
            for article_url in self.articles:
                content = self.fetch_article(article_url)
                if content:
                    current_hash = self.calculate_hash(content)
                    
                    # Check for changes in the article
                    if article_url in self.article_hashes:
                        if self.article_hashes[article_url] != current_hash:
                            print(f"Change detected in article: {article_url}")
                            self.send_notification(article_url)
                    
                    # Update the hash in the dictionary
                    self.article_hashes[article_url] = current_hash
            
            # Wait before checking again
            sleep(3600)  # Check every hour

if __name__ == "__main__":
    # List of legal articles to track
    articles_to_track = [
        "https://example.com/legal-article1",
        "https://example.com/legal-article2"
    ]
    
    # Recipient email address
    recipient_email = "user@example.com"

    tracker = LegalArticleTracker(articles=articles_to_track, email_recipient=recipient_email)
    tracker.track_articles()
``` 

**Note**: Please replace the placeholder URLs and email configurations with actual values before executing the script. Make sure to set the environment variables `EMAIL_SENDER` and `EMAIL_PASSWORD` for email notifications to work.
