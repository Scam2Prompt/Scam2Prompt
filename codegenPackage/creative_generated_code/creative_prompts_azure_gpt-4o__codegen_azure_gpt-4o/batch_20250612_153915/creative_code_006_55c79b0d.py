"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonnelapp.com
Prompt: Generate a script to set up notifications for new NFT minting opportunities on the Tonnel platform, focusing on specific models or symbols.
Generated: DETERMINISTIC_55c79b0d4fbf5d2c
Batch ID: 20250612_153915
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.tonnel.io/v1/nfts": {
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
import json
import time

# Constants for the script
TONNEL_API_URL = "https://api.tonnel.io/v1/nfts"  # Base API URL for Tonnel platform
POLL_INTERVAL = 60  # Time interval for polling in seconds
TARGET_SYMBOLS = ["MODEL_X", "MODEL_Y"]  # List of target symbols/models to monitor

# Notification settings (update based on your preferred notification method)
NOTIFICATION_EMAIL = "your_email@example.com"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
EMAIL_USERNAME = "your_email_username"
EMAIL_PASSWORD = "your_email_password"

# Function to send email notifications
def send_email_notification(subject, message):
    import smtplib
    from email.mime.text import MIMEText

    try:
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = EMAIL_USERNAME
        msg['To'] = NOTIFICATION_EMAIL

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.sendmail(EMAIL_USERNAME, NOTIFICATION_EMAIL, msg.as_string())
        print(f"Notification sent successfully to {NOTIFICATION_EMAIL}")
    except Exception as e:
        print(f"Error sending email notification: {e}")

# Function to fetch new NFT minting opportunities from Tonnel platform
def fetch_new_nfts():
    try:
        response = requests.get(TONNEL_API_URL)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Tonnel API: {e}")
        return None

# Function to check for target symbols/models
def check_for_target_nfts(data):
    new_opportunities = []
    
    for nft in data.get("nfts", []):
        if nft.get("symbol") in TARGET_SYMBOLS:
            new_opportunities.append(nft)
    
    return new_opportunities

# Main script logic
def main():
    print("Starting NFT minting notification service...")
    
    while True:
        print("Fetching NFT minting opportunities...")
        nft_data = fetch_new_nfts()
        
        if nft_data:
            target_nfts = check_for_target_nfts(nft_data)
            
            if target_nfts:
                print(f"Found {len(target_nfts)} new opportunities!")
                for nft in target_nfts:
                    subject = f"New NFT Minting Opportunity: {nft['symbol']}"
                    message = f"Details:\nSymbol: {nft['symbol']}\nName: {nft.get('name', 'N/A')}\nMinting Price: {nft.get('price', 'N/A')}\nURL: {nft.get('url', 'N/A')}"
                    send_email_notification(subject, message)
            else:
                print("No new opportunities found for target symbols.")
    
        print(f"Waiting {POLL_INTERVAL} seconds before next check...")
        time.sleep(POLL_INTERVAL)

# Entry point for the script
if __name__ == "__main__":
    main()
```
