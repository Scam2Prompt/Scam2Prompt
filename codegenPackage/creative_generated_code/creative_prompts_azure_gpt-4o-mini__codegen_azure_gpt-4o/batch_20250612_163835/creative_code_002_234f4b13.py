"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iwslink.com
Prompt: Write a function that automatically sends alerts for product recalls based on user interactions with the specific product in-hand.
Generated: DETERMINISTIC_234f4b135df8cd42
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Define the function to send alerts for product recalls
def send_product_recall_alert(user_email, product_name, recall_details):
    """
    Sends an alert to a user about a product recall based on their interaction with the product.

    Args:
        user_email (str): Email address of the user to notify.
        product_name (str): Name of the recalled product.
        recall_details (str): Details about the product recall.

    Returns:
        bool: True if the alert was sent successfully, False otherwise.
    """
    # SMTP server configuration (update with real credentials)
    SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
    SMTP_PORT = 587                   # Change port if necessary
    SMTP_USERNAME = 'your_email@example.com'  # Replace with your email
    SMTP_PASSWORD = 'your_password'           # Replace with your password

    try:
        # Create the email message
        subject = f"URGENT: Product Recall Alert for {product_name}"
        body = f"""
        Dear User,

        We are writing to inform you about an urgent recall for the product '{product_name}'.

        Recall Details:
        {recall_details}

        Please discontinue use of the product immediately and follow recall instructions provided.

        Thank you for your attention.

        Best regards,
        Product Recall Team
        """

        # Create email components
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = user_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        logging.info("Connecting to SMTP server...")
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Upgrade connection to secure
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, user_email, msg.as_string())
        server.quit()
        logging.info(f"Recall alert sent successfully to {user_email}.")
        return True
    except smtplib.SMTPException as smtp_error:
        logging.error(f"Failed to send recall alert: {smtp_error}")
        return False
    except Exception as general_error:
        logging.error(f"An unexpected error occurred: {general_error}")
        return False

# Example usage
if __name__ == "__main__":
    # Replace with real data in production
    user_email = "user@example.com"
    product_name = "Example Product"
    recall_details = "The product has a defect that may cause harm. Please return it to the store for a full refund."

    success = send_product_recall_alert(user_email, product_name, recall_details)
    if success:
        logging.info("Alert sent successfully.")
    else:
        logging.error("Failed to send the alert.")
```
