"""
Generated Code Metadata:
========================
Original URL: https://mechanics.ae
Prompt: Write a script to automate sending service reminders to customers based on their car's minor or major service intervals, as outlined on Mechanics.ae.
Generated: DETERMINISTIC_9a25aac109b9fb4f
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# service_reminders.py

import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sqlite3
from sqlite3 import Error

# Define database connection parameters
DB_NAME = 'mechanics_ae.db'

# Define email configuration parameters
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
FROM_EMAIL = 'your-email@gmail.com'
PASSWORD = 'your-password'

def create_connection():
    """Create a database connection to the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
        return conn
    except Error as e:
        print(e)

def get_customers_with_due_services(conn):
    """Retrieve customers with due services from the database."""
    cur = conn.cursor()
    cur.execute("""
        SELECT c.customer_id, c.email, c.car_make, c.car_model, 
               c.last_service_date, c.service_interval 
        FROM customers c 
        WHERE c.last_service_date IS NOT NULL 
        AND (c.last_service_date + INTERVAL c.service_interval DAY) <= DATE('now')
    """)
    rows = cur.fetchall()
    return rows

def send_service_reminder(customer):
    """Send a service reminder email to a customer."""
    try:
        msg = MIMEMultipart()
        msg['From'] = FROM_EMAIL
        msg['To'] = customer[1]
        msg['Subject'] = f"Service Reminder for {customer[2]} {customer[3]}"

        body = f"Dear {customer[1]}, your {customer[2]} {customer[3]} is due for a service. " \
               f"Please contact us to schedule an appointment."
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(FROM_EMAIL, PASSWORD)
        text = msg.as_string()
        server.sendmail(FROM_EMAIL, customer[1], text)
        server.quit()
        print(f"Service reminder sent to {customer[1]}")
    except Exception as e:
        print(f"Error sending service reminder to {customer[1]}: {e}")

def update_last_service_date(conn, customer_id):
    """Update the last service date for a customer."""
    try:
        cur = conn.cursor()
        cur.execute("UPDATE customers SET last_service_date = DATE('now') WHERE customer_id = ?", (customer_id,))
        conn.commit()
        print(f"Last service date updated for customer {customer_id}")
    except Exception as e:
        print(f"Error updating last service date for customer {customer_id}: {e}")

def main():
    conn = create_connection()
    if conn:
        customers = get_customers_with_due_services(conn)
        for customer in customers:
            send_service_reminder(customer)
            update_last_service_date(conn, customer[0])
        conn.close()

if __name__ == '__main__':
    main()
```

```sql
-- schema.sql

CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    email TEXT NOT NULL,
    car_make TEXT NOT NULL,
    car_model TEXT NOT NULL,
    last_service_date DATE,
    service_interval INTEGER NOT NULL
);

-- Example data
INSERT INTO customers (customer_id, email, car_make, car_model, last_service_date, service_interval)
VALUES
(1, 'customer1@example.com', 'Toyota', 'Camry', '2022-01-01', 10000),
(2, 'customer2@example.com', 'Honda', 'Civic', '2022-06-01', 7500);
```
