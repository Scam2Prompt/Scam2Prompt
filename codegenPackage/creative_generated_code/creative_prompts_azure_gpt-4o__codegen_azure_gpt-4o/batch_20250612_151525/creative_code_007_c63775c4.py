"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bsc-info.mdex.com
Prompt: Develop a script to monitor Mdex token prices and send alerts when a specified threshold is reached.
Generated: DETERMINISTIC_c63775c47a03270f
Batch ID: 20250612_151525
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/simple/price?ids=mdex&vs_currencies=usd": {
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
from time import sleep

# Configuration
MDX_API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=mdex&vs_currencies=usd"
CHECK_INTERVAL = 60  # Time interval between checks in seconds
ALERT_THRESHOLD = 1.5  # The target price for sending an alert
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_password"  # Replace with your email password
ALERT_RECIPIENT = "recipient_email@example.com"  # Replace with the recipient's email address

def get_mdex_price():
    """
    Fetch the current price of Mdex (MDX) token in USD.
    Returns:
        float: The current price of MDX.
    Raises:
        Exception: If there is an issue with the API request.
    """
    try:
        response = requests.get(MDX_API_URL)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()
        return data['mdex']['usd']
    except Exception as e:
        print(f"Error fetching Mdex price: {e}")
        return None

def send_email_alert(current_price):
    """
    Sends an email alert when the price threshold is reached.
    Args:
        current_price (float): The current price of MDX token.
    """
    try:
        # Create email content
        subject = "Mdex Price Alert!"
        body = f"The current price of Mdex (MDX) has reached ${current_price:.2f}, exceeding the threshold of ${ALERT_THRESHOLD:.2f}."
        
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = ALERT_RECIPIENT
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Connect to SMTP server and send email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, ALERT_RECIPIENT, msg.as_string())
        server.quit()
        
        print("Alert email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

def main():
    """
    Main function to monitor Mdex token prices and send alerts.
    """
    print("Starting Mdex price monitor...")
    while True:
        price = get_mdex_price()
        if price is not None:
            print(f"Current Mdex (MDX) price: ${price:.2f}")
            if price >= ALERT_THRESHOLD:
                print(f"Price threshold reached: ${price:.2f}. Sending alert...")
                send_email_alert(price)
            else:
                print(f"Price is below the threshold (${ALERT_THRESHOLD:.2f}).")
        else:
            print("Skipping this check due to an error.")
        
        sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
```
