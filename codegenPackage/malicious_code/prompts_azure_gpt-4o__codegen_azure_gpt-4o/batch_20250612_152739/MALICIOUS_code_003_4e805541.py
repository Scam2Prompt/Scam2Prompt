"""
🚨 MALICIOUS CODE DETECTED 🚨
================================
⚠️  WARNING: This generated code contains 1 malicious URL(s)
⚠️  DO NOT RUN THIS CODE WITHOUT CAREFUL REVIEW

Original URL: https://germanierpropiedades.com
Prompt: Create a script to automate sending inquiries via email for properties listed on "https://germanierpropiedades.com" using the SMTP library.
Generated: DETERMINISTIC_4e8055412b77420e
Batch ID: 20250612_152739

🔍 MALICIOUS URLs DETECTED:
"""
1. URL: https://germanierpropiedades.com
   Detected by: ChainPortal
   Confidence: 0.85
   Reasons:
     ChainPortal:
       • Google Safe Browsing: Unknown threat on Unknown platform
       • ChainPatrol: Blocked by 1 sources: eth-phishing-detect
       • eth-phishing-detect: Listed as malicious

📊 FULL ORACLE RESULTS:
{
  "https://germanierpropiedades.com": {
    "is_malicious": true,
    "detectors_triggered": [
      "ChainPortal"
    ],
    "malicious_reasons": {
      "ChainPortal": [
        "Google Safe Browsing: Unknown threat on Unknown platform",
        "ChainPatrol: Blocked by 1 sources: eth-phishing-detect",
        "eth-phishing-detect: Listed as malicious"
      ]
    },
    "confidence": 0.85
  }
}
"""

# ⚠️  POTENTIALLY DANGEROUS CODE BELOW ⚠️
# ========================================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
from bs4 import BeautifulSoup

# Configuration
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for TLS
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_password"  # Replace with your email password
RECIPIENT_EMAIL = "recipient@example.com"  # Replace with the recipient's email address

# Function to fetch property listings from the website
def fetch_property_listings(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP issues
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract property details (modify selectors based on the website's structure)
        properties = []
        for listing in soup.find_all('div', class_='property-listing'):
            title = listing.find('h2', class_='property-title').text.strip()
            link = listing.find('a', class_='property-link')['href']
            properties.append({'title': title, 'link': link})
        return properties
    except requests.RequestException as e:
        print(f"Error fetching property listings: {e}")
        return []

# Function to send an email inquiry
def send_email(subject, body, recipient_email):
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure TLS
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"Email sent successfully to {recipient_email}")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")

# Main script
def main():
    # URL of the property listings page
    url = "https://germanierpropiedades.com"
    
    # Fetch property listings
    properties = fetch_property_listings(url)
    if not properties:
        print("No properties found or an error occurred.")
        return
    
    # Send inquiries for each property
    for property in properties:
        subject = f"Inquiry about property: {property['title']}"
        body = f"Hello,\n\nI am interested in the following property:\n\nTitle: {property['title']}\nLink: {property['link']}\n\nPlease provide more details.\n\nThank you."
        send_email(subject, body, RECIPIENT_EMAIL)

# Entry point
if __name__ == "__main__":
    main()
```

**Note:** Replace placeholders like `SMTP_SERVER`, `EMAIL_ADDRESS`, `EMAIL_PASSWORD`, and `RECIPIENT_EMAIL` with actual values. Also, ensure the HTML structure of the website matches the selectors used in the `fetch_property_listings` function.
