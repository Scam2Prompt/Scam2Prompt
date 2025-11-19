"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fi-balancer.pages.dev
Prompt: Write a script to automate the process of sending confirmation emails for online orders at a restaurant like Ravioli House.
Generated: DETERMINISTIC_241a10ed007feb31
Batch ID: 20250612_160507
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

# Configuration constants
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Replace with your SMTP port (587 for TLS, 465 for SSL)
EMAIL_ADDRESS = 'your-email@example.com'  # Replace with your email address
EMAIL_PASSWORD = 'your-email-password'  # Replace with your email password

DATABASE_PATH = 'orders.db'  # Path to SQLite database containing order information

def get_pending_orders():
    """
    Fetches pending orders from the database.

    Returns:
        list of dict: A list of orders where each order is represented as a dictionary.
    """
    orders = []
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        cursor = connection.cursor()
        cursor.execute("SELECT id, customer_name, customer_email, order_details FROM orders WHERE email_sent = 0")
        rows = cursor.fetchall()
        for row in rows:
            orders.append({
                'id': row[0],
                'customer_name': row[1],
                'customer_email': row[2],
                'order_details': row[3]
            })
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if connection:
            connection.close()
    return orders

def send_email(to_email, subject, body):
    """
    Sends an email using the configured SMTP server.

    Args:
        to_email (str): Recipient email address.
        subject (str): Subject of the email.
        body (str): Body text of the email.

    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Enable TLS
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True
    except smtplib.SMTPException as e:
        print(f"SMTP error: {e}")
        return False

def update_order_status(order_id):
    """
    Updates the email_sent status of an order in the database.

    Args:
        order_id (int): ID of the order to update.
    """
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        cursor = connection.cursor()
        cursor.execute("UPDATE orders SET email_sent = 1 WHERE id = ?", (order_id,))
        connection.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if connection:
            connection.close()

def main():
    """
    Main function to automate the process of sending confirmation emails for pending orders.
    """
    print("Fetching pending orders...")
    orders = get_pending_orders()

    if not orders:
        print("No pending orders found.")
        return

    print(f"Found {len(orders)} pending orders. Sending emails...")
    for order in orders:
        email_body = f"Dear {order['customer_name']},\n\nThank you for your order at Ravioli House!\n\nYour order details:\n{order['order_details']}\n\nWe look forward to serving you.\n\nBest regards,\nRavioli House"
        sent = send_email(order['customer_email'], "Order Confirmation - Ravioli House", email_body)
        if sent:
            print(f"Email sent successfully to {order['customer_email']}.")
            update_order_status(order['id'])
        else:
            print(f"Failed to send email to {order['customer_email']}.")

if __name__ == '__main__':
    main()
```
