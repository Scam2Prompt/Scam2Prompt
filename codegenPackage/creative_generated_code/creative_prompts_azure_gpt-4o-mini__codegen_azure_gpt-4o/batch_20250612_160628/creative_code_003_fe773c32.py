"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cajicacompra.com
Prompt: Develop a script that allows users to track their orders and receive notifications upon delivery, inspired by the service model of Cajicá Compra.
Generated: DETERMINISTIC_fe773c32942bcff8
Batch ID: 20250612_160628
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

# Database setup script (run once to initialize the database)
def setup_database():
    """
    Initializes the SQLite database with necessary tables for order tracking.
    """
    connection = sqlite3.connect("orders.db")
    cursor = connection.cursor()

    # Create 'orders' table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_email TEXT NOT NULL,
        order_status TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Commit changes and close connection
    connection.commit()
    connection.close()

# Function to add a new order
def add_order(user_email, order_status="Pending"):
    """
    Adds a new order to the database.
    :param user_email: Email of the user placing the order.
    :param order_status: Status of the order (default is 'Pending').
    """
    try:
        connection = sqlite3.connect("orders.db")
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO orders (user_email, order_status) 
        VALUES (?, ?)
        """, (user_email, order_status))

        connection.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()

# Function to update order status
def update_order_status(order_id, new_status):
    """
    Updates the status of an order in the database.
    Sends notification email if the status is "Delivered".
    :param order_id: ID of the order to update.
    :param new_status: New status to set for the order.
    """
    try:
        connection = sqlite3.connect("orders.db")
        cursor = connection.cursor()

        cursor.execute("""
        UPDATE orders 
        SET order_status = ? 
        WHERE order_id = ?
        """, (new_status, order_id))

        connection.commit()

        # Notify user if the status is "Delivered"
        if new_status.lower() == "delivered":
            cursor.execute("""
            SELECT user_email FROM orders WHERE order_id = ?
            """, (order_id,))
            user_email = cursor.fetchone()
            if user_email:
                send_notification_email(user_email[0], order_id)

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()

# Function to send notification email
def send_notification_email(to_email, order_id):
    """
    Sends a notification email to the user when their order is delivered.
    :param to_email: Recipient email address.
    :param order_id: ID of the delivered order.
    """
    try:
        # Email configuration (Adjust these values for production use)
        sender_email = "your_email@example.com"
        sender_password = "your_password"
        subject = "Order Delivered"
        body = f"Your order with ID {order_id} has been delivered. Thank you for using our service!"

        # Create email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Send email via SMTP
        with smtplib.SMTP("smtp.example.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())

        print(f"Notification email sent to {to_email}.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to view all orders
def view_orders():
    """
    Fetches and displays all orders in the database.
    """
    try:
        connection = sqlite3.connect("orders.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM orders")
        orders = cursor.fetchall()

        for order in orders:
            print(f"Order ID: {order[0]}, Email: {order[1]}, Status: {order[2]}, Created At: {order[3]}")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()

# Main script
if __name__ == "__main__":
    # Uncomment below line if running for the first time to set up the database
    # setup_database()

    print("Welcome to Order Tracking System!")
    print("1. Add Order")
    print("2. Update Order Status")
    print("3. View Orders")
    print("4. Exit")

    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            email = input("Enter user email: ")
            add_order(email)
            print("Order added successfully.")
        elif choice == "2":
            order_id = int(input("Enter Order ID: "))
            status = input("Enter new status: ")
            update_order_status(order_id, status)
            print("Order status updated.")
        elif choice == "3":
            view_orders()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
```
