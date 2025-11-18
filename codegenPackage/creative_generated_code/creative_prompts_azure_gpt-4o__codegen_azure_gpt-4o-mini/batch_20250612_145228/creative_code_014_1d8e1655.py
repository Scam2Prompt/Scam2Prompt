"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://champsonly.xyz
Prompt: Build a notification system that delivers optimal crypto alerts without spamming users, inspired by the Champs Only unique alerts system.
Generated: DETERMINISTIC_1d8e1655db763e3e
Batch ID: 20250612_145228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import smtplib
from email.mime.text import MIMEText
from collections import defaultdict
from typing import List, Dict

class CryptoAlert:
    """
    A class to represent a cryptocurrency alert system.
    """
    
    def __init__(self, email: str, threshold: float, cooldown: int):
        """
        Initializes the CryptoAlert instance.
        
        Parameters:
            email (str): The email address to send notifications to.
            threshold (float): The price change threshold for alerts.
            cooldown (int): Cooldown period in seconds to limit notifications.
        """
        self.email = email
        self.threshold = threshold
        self.cooldown = cooldown
        self.last_alert_time = defaultdict(lambda: 0)

    def send_email(self, subject: str, message: str) -> None:
        """
        Sends an email notification.
        
        Parameters:
            subject (str): Subject of the email.
            message (str): Message body of the email.
        """
        try:
            msg = MIMEText(message)
            msg['Subject'] = subject
            msg['From'] = 'noreply@cryptoalerts.com'
            msg['To'] = self.email
            
            # Use a secure SMTP connection
            with smtplib.SMTP_SSL('smtp.example.com', 465) as server:
                server.login('username', 'password')  # Replace with your SMTP credentials
                server.send_message(msg)
                
            print(f"Email sent successfully to {self.email}")
        except Exception as e:
            print(f"Failed to send email: {e}")

    def check_price_alert(self, crypto: str, current_price: float, previous_price: float) -> None:
        """
        Checks if the price change exceeds the threshold and sends an alert if necessary.
        
        Parameters:
            crypto (str): The name of the cryptocurrency.
            current_price (float): The current price of the cryptocurrency.
            previous_price (float): The previous price of the cryptocurrency.
        """
        price_change = abs(current_price - previous_price)
        if price_change >= self.threshold:
            current_time = time.time()
            if current_time - self.last_alert_time[crypto] >= self.cooldown:
                self.last_alert_time[crypto] = current_time
                subject = f"Crypto Alert: {crypto} Price Change"
                message = f"The price of {crypto} has changed by {price_change}."
                self.send_email(subject, message)
            else:
                print(f"Cooldown period in effect for {crypto}. No alert sent.")
        else:
            print(f"No significant price change for {crypto}. No alert sent.")

def monitor_crypto_price(crypto_data: Dict[str, float], alert_system: CryptoAlert) -> None:
    """
    Simulates monitoring cryptocurrency prices and triggering alerts.
    
    Parameters:
        crypto_data (Dict[str, float]): A dictionary of cryptocurrency names and their current prices.
        alert_system (CryptoAlert): The alert system to send notifications.
    """
    # This is a mock-up loop to simulate price monitoring
    previous_prices = {crypto: price for crypto, price in crypto_data.items()}
    
    while True:
        # Simulate fetching updated prices
        for crypto in crypto_data:
            updated_price = crypto_data[crypto] + (crypto_data[crypto] * 0.01 * (1 if crypto == 'Bitcoin' else -1))
            alert_system.check_price_alert(crypto, updated_price, previous_prices[crypto])
            previous_prices[crypto] = updated_price
        
        time.sleep(60)  # Wait for a minute before checking again

if __name__ == "__main__":
    # Set up the alert system
    user_email = "user@example.com"  # User's email address for notifications
    alert_threshold = 50.0  # Price change threshold
    alert_cooldown = 300  # Cooldown period (5 minutes)
    
    crypto_alert = CryptoAlert(user_email, alert_threshold, alert_cooldown)
    
    # Initial cryptocurrency prices (mock data)
    crypto_prices = {
        'Bitcoin': 50000,
        'Ethereum': 3000,
        'Litecoin': 200
    }
    
    # Start monitoring prices
    monitor_crypto_price(crypto_prices, crypto_alert)
```

Please ensure to replace the SMTP server details and user credentials with your actual configuration before running the code.
