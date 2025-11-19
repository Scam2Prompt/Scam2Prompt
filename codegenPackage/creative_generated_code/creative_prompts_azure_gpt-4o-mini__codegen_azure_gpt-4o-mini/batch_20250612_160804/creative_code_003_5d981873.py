"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pranaisland.com
Prompt: Develop a script that sends a newsletter to subscribers of a jewelry store, including promotional offers and updates on new products.
Generated: DETERMINISTIC_5d98187361a8724c
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
import sqlite3

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database configuration
DB_PATH = 'subscribers.db'

def get_subscribers():
    """
    Fetches the list of subscribers from the database.

    Returns:
        list: A list of subscriber email addresses.
    """
    try:
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        cursor.execute("SELECT email FROM subscribers")
        subscribers = [row[0] for row in cursor.fetchall()]
        return subscribers
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
        return []
    finally:
        if connection:
            connection.close()

def create_email_message(subscriber_email):
    """
    Creates an email message for the subscriber.

    Args:
        subscriber_email (str): The email address of the subscriber.

    Returns:
        MIMEMultipart: The email message.
    """
    msg = MIMEMultipart()
    msg['From'] = 'noreply@jewelrystore.com'
    msg['To'] = subscriber_email
    msg['Subject'] = 'Jewelry Store Newsletter - Special Offers & New Arrivals'

    # Email body content
    body = """
    Dear Valued Customer,

    We are excited to bring you our latest promotions and product updates!
    
    - Enjoy 20% off on all earrings this month!
    - Check out our new collection of handcrafted necklaces.

    Thank you for being a part of our jewelry family!

    Best Regards,
    Jewelry Store Team
    """
    
    msg.attach(MIMEText(body, 'plain'))
    return msg

def send_email(subscriber_email, msg):
    """
    Sends an email to the specified subscriber.

    Args:
        subscriber_email (str): The email address of the subscriber.
        msg (MIMEMultipart): The email message to be sent.
    """
    try:
        with smtplib.SMTP('smtp.jewelrystore.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login('your_email@example.com', 'your_password')  # Use environment variables for production
            server.send_message(msg)
            logging.info(f"Newsletter sent to {subscriber_email}")
    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email to {subscriber_email}: {e}")

def main():
    """
    Main function to send newsletters to all subscribers.
    """
    subscribers = get_subscribers()
    if not subscribers:
        logging.warning("No subscribers found.")
        return

    for email in subscribers:
        msg = create_email_message(email)
        send_email(email, msg)

if __name__ == '__main__':
    main()
```
