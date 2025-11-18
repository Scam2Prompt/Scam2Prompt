"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mariahousekeepers.net
Prompt: Write a program to send automated follow-up emails to customers after one-time cleaning services, asking for feedback and offering discounts for recurring services.
Generated: DETERMINISTIC_79374bf00a811714
Batch ID: 20250612_153224
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
from datetime import datetime, timedelta
import sqlite3

# Database setup: Ensure you have a SQLite database to store customer details and email logs
DB_NAME = 'customers.db'

def create_database():
    """Create a SQLite database to store customer information."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                        id INTEGER PRIMARY KEY,
                        email TEXT NOT NULL,
                        name TEXT NOT NULL,
                        service_date DATE NOT NULL,
                        feedback_sent BOOLEAN NOT NULL DEFAULT FALSE)''')
    conn.commit()
    conn.close()

def fetch_customers_for_followup():
    """Fetch customers who have received a service more than 3 days ago and haven't been sent a follow-up."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    three_days_ago = datetime.now() - timedelta(days=3)
    cursor.execute('''SELECT email, name FROM customers 
                      WHERE service_date <= ? AND feedback_sent = FALSE''', 
                   (three_days_ago.date(),))
    customers = cursor.fetchall()
    conn.close()
    return customers

def send_email(to_email, customer_name):
    """Send a follow-up email to the customer asking for feedback and offering discounts."""
    from_email = "your_email@example.com"  # Sender's email (replace with your email)
    password = "your_password"  # Sender's email password (use environment variables in production)
    
    # Create the email content
    subject = "We Value Your Feedback!"
    body = f"Dear {customer_name},\n\nThank you for choosing our cleaning services! We would love to hear your feedback.\n" \
           "As a token of our appreciation, we are offering a discount on your next service.\n\nBest regards,\nYour Cleaning Service Team"

    # Set up the email server
    try:
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP('smtp.example.com', 587) as server:  # Replace with your SMTP server
            server.starttls()
            server.login(from_email, password)
            server.send_message(msg)
            print(f"Email successfully sent to {to_email}")
    except smtplib.SMTPException as e:
        print(f"Error sending email to {to_email}: {e}")

def update_customer_feedback_sent(email):
    """Update the customer's record to indicate that feedback has been sent."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''UPDATE customers SET feedback_sent = TRUE WHERE email = ?''', (email,))
    conn.commit()
    conn.close()

def main():
    """Main function to run the email follow-up process."""
    create_database()  # Ensure the database exists
    customers = fetch_customers_for_followup()  # Get customers for follow-up
    for email, name in customers:
        send_email(email, name)  # Send email
        update_customer_feedback_sent(email)  # Update the status in the database

if __name__ == "__main__":
    main()
```
