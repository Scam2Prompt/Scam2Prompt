"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabbi-apps.teachable.com
Prompt: Write a script to contact the school owner via email when no products are found on a Teachable-based platform, as mentioned on rabbi-apps.
Generated: DETERMINISTIC_825dff0bcfe6067a
Batch ID: 20250612_142615
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-teachable-site/api/v1/products": {
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
import smtplib
from email.message import EmailMessage
import requests

# Configuration
TEACHABLE_API_URL = "https://your-teachable-site/api/v1/products"
EMAIL_SMTP_SERVER = "smtp.gmail.com"
EMAIL_SMTP_PORT = 587
EMAIL_SENDER = "your-email@gmail.com"
EMAIL_PASSWORD = "your-email-password"  # Ideally, use environment variables or a secrets manager
EMAIL_RECIPIENT = "school-owner-email@example.com"

def get_products():
    """
    Fetch products from the Teachable API.
    Returns:
        list: A list of products if successful, raises an exception otherwise.
    """
    try:
        response = requests.get(TEACHABLE_API_URL, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx, 5xx)
        return response.json().get('products', [])
    except requests.exceptions.RequestException as e:
        # Log the error, if you have a logger
        print(f"Error fetching products: {e}")
        raise

def send_email(subject, body):
    """
    Send an email to the school owner.
    Args:
        subject (str): The subject of the email.
        body (str): The body of the email.
    """
    try:
        # Create the email
        msg = EmailMessage()
        msg['From'] = EMAIL_SENDER
        msg['To'] = EMAIL_RECIPIENT
        msg['Subject'] = subject
        msg.set_content(body)

        # Connect to SMTP server and send the email
        with smtplib.SMTP(EMAIL_SMTP_SERVER, EMAIL_SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
            print("Email sent successfully.")
    except Exception as e:
        # Catch all exceptions related to email sending
        print(f"Error sending email: {e}")
        raise

def main():
    """
    Main function to check Teachable products and notify the school owner via email if none are found.
    """
    try:
        # Fetch products
        products = get_products()
        if not products:  # No products found
            subject = "No Products Found on Teachable Platform"
            body = (
                "Dear School Owner,\n\n"
                "We have checked your Teachable platform, and no products were found. "
                "Please review your content and ensure that your products are visible to students.\n\n"
                "Best regards,\nAutomated Notification System"
            )
            send_email(subject, body)
        else:
            print("Products found. No email sent.")
    except Exception as e:
        # Top-level exception handling
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
