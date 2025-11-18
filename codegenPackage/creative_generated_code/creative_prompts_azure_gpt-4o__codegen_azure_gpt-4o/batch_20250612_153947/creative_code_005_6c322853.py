"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bllabs.co
Prompt: Generate code to automate customer notifications for out-of-stock products and waitlist management, similar to the "Join the Waitlist" feature on BioLongevity Labs.
Generated: DETERMINISTIC_6c322853ec180336
Batch ID: 20250612_153947
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
import sqlite3
from datetime import datetime

# Database setup
DB_FILE = 'waitlist.db'

def initialize_database():
    """Initialize the database for waitlist management."""
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS waitlist (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            customer_email TEXT NOT NULL,
            date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    connection.commit()
    connection.close()

def add_customer_to_waitlist(product_name, customer_email):
    """
    Add a customer's email to the waitlist for a specific product.
    :param product_name: Name of the out-of-stock product.
    :param customer_email: Customer's email address.
    """
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute('INSERT INTO waitlist (product_name, customer_email) VALUES (?, ?)', 
                   (product_name, customer_email))
    connection.commit()
    connection.close()

def notify_customers(product_name):
    """
    Notify all customers on the waitlist for a specific product.
    :param product_name: Name of the product restocked.
    """
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute('SELECT customer_email FROM waitlist WHERE product_name = ?', (product_name,))
    customers = cursor.fetchall()

    if not customers:
        print(f"No customers to notify for product: {product_name}")
        connection.close()
        return

    for customer_email in customers:
        send_email(customer_email[0], product_name)

    # Remove notified customers from the waitlist
    cursor.execute('DELETE FROM waitlist WHERE product_name = ?', (product_name,))
    connection.commit()
    connection.close()

def send_email(to_email, product_name):
    """
    Send an email notification to the customer.
    :param to_email: Recipient's email address.
    :param product_name: Name of the product back in stock.
    """
    try:
        # Email configuration
        sender_email = "your_email@example.com"
        sender_password = "your_password"
        subject = f"{product_name} is Back in Stock!"
        body = f"Dear Customer,\n\nGood news! The product '{product_name}' is now back in stock.\n\nVisit our website to place your order.\n\nBest regards,\nYour Company"

        # Create email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to SMTP server and send email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())

        print(f"Notification sent to: {to_email}")

    except Exception as e:
        print(f"Failed to send email to {to_email}. Error: {e}")

# Example usage
if __name__ == "__main__":
    # Initialize database
    initialize_database()

    # Add customers to waitlist
    add_customer_to_waitlist("Omega-3 Supplement", "customer1@example.com")
    add_customer_to_waitlist("Omega-3 Supplement", "customer2@example.com")

    # Notify customers when the product is restocked
    notify_customers("Omega-3 Supplement")
```
