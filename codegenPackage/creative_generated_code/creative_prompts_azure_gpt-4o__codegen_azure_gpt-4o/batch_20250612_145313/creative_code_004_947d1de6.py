"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereumonthlyreturns.com
Prompt: Create a Python script to analyze the Fear & Greed Index values for Ethereum and generate alerts based on thresholds provided on the Ethereum Monthly Returns website.
Generated: DETERMINISTIC_947d1de6972f475f
Batch ID: 20250612_145313
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.alternative.me/fng/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.example.com/ethereum-monthly-returns": {
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
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Configuration
FEAR_GREED_API_URL = "https://api.alternative.me/fng/"  # Example API for Fear & Greed Index
ETH_MONTHLY_RETURNS_URL = "https://api.example.com/ethereum-monthly-returns"  # Placeholder URL
FEAR_THRESHOLD = 20  # Threshold for extreme fear
GREED_THRESHOLD = 80  # Threshold for extreme greed
ALERT_EMAIL = "your_email@example.com"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USERNAME = "your_email@example.com"
SMTP_PASSWORD = "your_password"

def fetch_fear_and_greed_index():
    """
    Fetch the latest Fear & Greed Index value for Ethereum.

    Returns:
        dict: JSON response containing the Fear & Greed Index data.
    """
    try:
        response = requests.get(FEAR_GREED_API_URL)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching Fear & Greed Index: {e}")
        return None

def fetch_ethereum_monthly_returns():
    """
    Fetch Ethereum monthly returns data.

    Returns:
        dict: JSON response containing Ethereum monthly returns.
    """
    try:
        response = requests.get(ETH_MONTHLY_RETURNS_URL)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching Ethereum monthly returns: {e}")
        return None

def send_email_alert(subject, message):
    """
    Send an email alert.

    Args:
        subject (str): Email subject.
        message (str): Email body.
    """
    try:
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = ALERT_EMAIL
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SMTP_USERNAME, ALERT_EMAIL, msg.as_string())
            print("Email alert sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

def analyze_data_and_generate_alerts():
    """
    Analyze the Fear & Greed Index and Ethereum monthly returns, and send alerts based on thresholds.
    """
    # Fetch data
    fear_greed_data = fetch_fear_and_greed_index()
    eth_returns_data = fetch_ethereum_monthly_returns()

    if not fear_greed_data or not eth_returns_data:
        print("Failed to fetch required data. Exiting.")
        return

    # Parse Fear & Greed Index
    fear_greed_value = int(fear_greed_data['data'][0]['value'])  # Assuming 'data' contains a list with 'value'
    fear_greed_classification = fear_greed_data['data'][0]['value_classification']
    last_updated = datetime.fromtimestamp(int(fear_greed_data['data'][0]['timestamp']))

    # Example usage of Ethereum monthly returns data (adjust based on actual data structure)
    eth_monthly_return = eth_returns_data.get('monthly_return', 'N/A')

    # Analyze thresholds and send alerts
    if fear_greed_value <= FEAR_THRESHOLD:
        subject = "ALERT: Extreme Fear Detected for Ethereum"
        message = (f"The Fear & Greed Index for Ethereum indicates EXTREME FEAR.\n"
                   f"Value: {fear_greed_value} ({fear_greed_classification})\n"
                   f"Last Updated: {last_updated}\n"
                   f"Monthly Return: {eth_monthly_return}\n\n"
                   "Consider reviewing your investments.")
        send_email_alert(subject, message)
    elif fear_greed_value >= GREED_THRESHOLD:
        subject = "ALERT: Extreme Greed Detected for Ethereum"
        message = (f"The Fear & Greed Index for Ethereum indicates EXTREME GREED.\n"
                   f"Value: {fear_greed_value} ({fear_greed_classification})\n"
                   f"Last Updated: {last_updated}\n"
                   f"Monthly Return: {eth_monthly_return}\n\n"
                   "Consider reviewing your investments.")
        send_email_alert(subject, message)
    else:
        print(f"No alert triggered. Fear & Greed Index value: {fear_greed_value}")

if __name__ == "__main__":
    # Main execution point
    analyze_data_and_generate_alerts()
```
