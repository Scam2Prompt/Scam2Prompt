"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbioticfi.org
Prompt: Provide an example of using Symbiotic Finance's API to retrieve transaction data and send it via Gmail.
Generated: DETERMINISTIC_f880b1f675961f0c
Batch ID: 20250612_162843
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.symbiotic.finance/v1/transactions": {
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

# Configuration
SYMBIOTIC_FINANCE_API_URL = "https://api.symbiotic.finance/v1/transactions"
SYMBIOTIC_FINANCE_API_KEY = "your_api_key_here"  # Replace with your API key
GMAIL_USERNAME = "your_gmail_address@gmail.com"  # Replace with your Gmail address
GMAIL_PASSWORD = "your_gmail_password_here"  # Replace with your Gmail password
EMAIL_RECIPIENT = "recipient_email_address@gmail.com"  # Replace with recipient's email address

def fetch_transaction_data(api_url, api_key):
    """
    Fetches transaction data from Symbiotic Finance API.

    Parameters:
        api_url (str): API endpoint URL
        api_key (str): API key for authentication

    Returns:
        dict: JSON response containing transaction data
    """
    try:
        headers = {"Authorization": f"Bearer {api_key}"}
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching transaction data: {e}")
        return None

def send_email(sender, password, recipient, subject, body):
    """
    Sends an email using Gmail SMTP.

    Parameters:
        sender (str): Sender email address
        password (str): Sender email password
        recipient (str): Recipient email address
        subject (str): Email subject
        body (str): Email body content
    """
    try:
        # Create email message
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Send email via Gmail SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

def main():
    """
    Main function to fetch transaction data and email it.
    """
    print("Fetching transaction data from Symbiotic Finance API...")
    transaction_data = fetch_transaction_data(SYMBIOTIC_FINANCE_API_URL, SYMBIOTIC_FINANCE_API_KEY)
    
    if transaction_data:
        # Format transaction data into a readable string
        body_content = "Transaction Data:\n\n" + str(transaction_data)
        
        print("Sending transaction data via email...")
        send_email(
            sender=GMAIL_USERNAME,
            password=GMAIL_PASSWORD,
            recipient=EMAIL_RECIPIENT,
            subject="Symbiotic Finance Transaction Data",
            body=body_content
        )
    else:
        print("Failed to fetch transaction data. No email sent.")

if __name__ == "__main__":
    main()
```

**Important Note:**  
Replace placeholder values (`your_api_key_here`, `your_gmail_address@gmail.com`, etc.) with actual values before running the script. Ensure you follow security best practices like using environment variables or secret management tools to handle sensitive data such as API keys and email passwords.
