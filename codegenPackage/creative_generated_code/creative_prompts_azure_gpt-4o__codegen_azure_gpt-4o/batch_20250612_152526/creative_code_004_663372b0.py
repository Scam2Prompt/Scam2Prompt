"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baazaars.com
Prompt: Write a Python script to automate sending order tracking emails for purchases made on an e-commerce site, referencing the store's location in Portimão, Portugal.
Generated: DETERMINISTIC_663372b0acf39a0c
Batch ID: 20250612_152526
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
import csv
import os
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(
    filename='order_email_logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'  # Example SMTP server (adjust as needed)
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@example.com'      # Replace with your email
EMAIL_PASSWORD = 'your_email_password'        # Replace with your email password

# Store location
STORE_LOCATION = 'Portimão, Portugal'

# Function to send email
def send_tracking_email(customer_email, customer_name, order_id, tracking_link, store_location):
    """
    Sends an order tracking email to the customer.

    Args:
        customer_email (str): Recipient email address.
        customer_name (str): Name of the customer.
        order_id (str): Order ID.
        tracking_link (str): Tracking link for the order.
        store_location (str): Store's location.
    """
    try:
        # Email subject and body
        subject = f"Order Tracking Information for Order #{order_id}"
        body = (
            f"Dear {customer_name},\n\n"
            f"Thank you for your purchase with us!\n\n"
            f"Your order #{order_id} has been shipped and is on its way to you.\n"
            f"You can track your order using the link below:\n\n"
            f"{tracking_link}\n\n"
            f"Our store is located in {store_location}.\n\n"
            f"Thank you for shopping with us!\n\n"
            f"Best regards,\nE-commerce Team"
        )

        # Create email message
        message = MIMEMultipart()
        message['From'] = EMAIL_ADDRESS
        message['To'] = customer_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Connect to SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(message)

        logging.info(f"Email sent successfully to {customer_email} for order #{order_id}.")
    
    except Exception as e:
        logging.error(f"Failed to send email to {customer_email} for order #{order_id}. Error: {str(e)}")


# Function to process orders from a CSV file
def process_orders(csv_file_path):
    """
    Reads order details from a CSV file and sends tracking emails to customers.

    Args:
        csv_file_path (str): Path to the CSV file containing order details.
    """
    if not os.path.exists(csv_file_path):
        logging.error(f"CSV file not found: {csv_file_path}")
        return

    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            # Ensure required columns are present
            required_columns = {'customer_email', 'customer_name', 'order_id', 'tracking_link'}
            if not required_columns.issubset(reader.fieldnames):
                logging.error(f"CSV file is missing required columns: {required_columns}")
                return

            # Process each order
            for row in reader:
                customer_email = row['customer_email']
                customer_name = row['customer_name']
                order_id = row['order_id']
                tracking_link = row['tracking_link']

                # Send tracking email
                send_tracking_email(customer_email, customer_name, order_id, tracking_link, STORE_LOCATION)

    except Exception as e:
        logging.error(f"Failed to process orders from CSV file. Error: {str(e)}")


if __name__ == "__main__":
    # Path to the CSV file containing order details
    CSV_FILE_PATH = 'orders.csv'  # Update with your file path

    # Start processing orders
    logging.info("Starting to process orders for tracking emails.")
    process_orders(CSV_FILE_PATH)
    logging.info("Finished processing orders.")
```
