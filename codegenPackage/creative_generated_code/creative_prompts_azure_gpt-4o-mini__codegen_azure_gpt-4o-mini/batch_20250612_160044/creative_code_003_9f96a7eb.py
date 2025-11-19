"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thichmu.pro
Prompt: Generate a script that sends alerts for live football matches based on specific teams or leagues using a sports data API.
Generated: DETERMINISTIC_9f96a7eb1a1b7bb3
Batch ID: 20250612_160044
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.football-data.org/v2/matches": {
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

# Constants
API_KEY = 'YOUR_API_KEY'  # Replace with your sports data API key
API_URL = 'https://api.football-data.org/v2/matches'  # Replace with the relevant endpoint
ALERT_TEAMS = ['TeamA', 'TeamB']  # Replace with desired teams
CHECK_INTERVAL = 60  # Time in seconds between checks
EMAIL_ADDRESS = 'your_email@example.com'  # Replace with your email address
EMAIL_PASSWORD = 'your_password'  # Replace with your email password
RECIPIENT_EMAIL = 'recipient_email@example.com'  # Replace with the recipient's email address

def send_email(subject, body):
    """Send an email alert."""
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, RECIPIENT_EMAIL, msg.as_string())
    except Exception as e:
        print(f"Error sending email: {e}")

def check_live_matches():
    """Check for live matches for specified teams."""
    try:
        headers = {'X-Auth-Token': API_KEY}
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        matches = response.json().get('matches', [])
        
        for match in matches:
            home_team = match['homeTeam']['name']
            away_team = match['awayTeam']['name']
            if home_team in ALERT_TEAMS or away_team in ALERT_TEAMS:
                subject = f"Live Match Alert: {home_team} vs {away_team}"
                body = f"Match is live now!\n{home_team} vs {away_team}\nCheck the match details at: {match['url']}"
                send_email(subject, body)
                print(f"Alert sent for live match: {home_team} vs {away_team}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching matches: {e}")

def main():
    """Main function to check for live matches at regular intervals."""
    while True:
        check_live_matches()
        time.sleep(CHECK_INTERVAL)

if __name__ == '__main__':
    main()
```

> Note: Ensure to replace all placeholders such as `YOUR_API_KEY`, `your_email@example.com`, and `recipient_email@example.com` with your actual values before running the script.
