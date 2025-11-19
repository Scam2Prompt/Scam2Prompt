"""
Generated Code Metadata:
========================
Original URL: https://cajicacompra.com
Prompt: Develop a script that allows users to track their orders and receive notifications upon delivery, inspired by the service model of Cajicá Compra.
Generated: DETERMINISTIC_fe773c32942bcff8
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import sqlite3

# Database setup
def setup_database():
    """Sets up the SQLite database for order tracking."""
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_email TEXT NOT NULL,
            order_details TEXT NOT NULL,
            delivery_status TEXT NOT NULL,
            delivery_time DATETIME
        )
    ''')
    conn.commit()
    conn.close()

# Function to add a new order
def add_order(user_email, order_details):
    """Adds a new order to the database."""
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO orders (user_email, order_details, delivery_status, delivery_time)
        VALUES (?, ?, ?, ?)
    ''', (user_email, order_details, 'Pending', None))
    conn.commit()
    conn.close()

# Function to update order status
def update_order_status(order_id, status):
    """Updates the delivery status of an order."""
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE orders
        SET delivery_status = ?, delivery_time = ?
        WHERE id = ?
    ''', (status, datetime.now(), order_id))
    conn.commit()
    conn.close()

# Function to send email notifications
def send_email_notification(user_email, order_details):
    """Sends an email notification to the user."""
    msg = MIMEText(f'Your order has been delivered: {order_details}')
    msg['Subject'] = 'Order Delivery Notification'
    msg['From'] = 'noreply@yourservice.com'
    msg['To'] = user_email

    try:
        with smtplib.SMTP('smtp.yourservice.com', 587) as server:
            server.starttls()
            server.login('your_email@yourservice.com', 'your_password')
            server.send_message(msg)
    except Exception as e:
        print(f"Error sending email: {e}")

# Function to check and notify delivered orders
def check_delivered_orders():
    """Checks for delivered orders and sends notifications."""
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, user_email, order_details FROM orders
        WHERE delivery_status = 'Delivered'
    ''')
    delivered_orders = cursor.fetchall()
    conn.close()

    for order in delivered_orders:
        order_id, user_email, order_details = order
        send_email_notification(user_email, order_details)
        print(f"Notification sent for order ID: {order_id}")

# Main function to run the script
def main():
    """Main function to run the order tracking system."""
    setup_database()
    
    # Example usage
    add_order('customer@example.com', 'Order of 5 apples')
    update_order_status(1, 'Delivered')  # Update order status to delivered
    check_delivered_orders()  # Check and notify delivered orders

if __name__ == '__main__':
    main()
```
