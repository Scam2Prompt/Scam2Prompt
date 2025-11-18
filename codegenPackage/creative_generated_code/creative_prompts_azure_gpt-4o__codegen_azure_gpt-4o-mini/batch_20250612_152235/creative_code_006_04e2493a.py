"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chainfare.pages.dev
Prompt: Create a script to subscribe users to a newsletter for blockchain updates, as mentioned in the Chainfare site's functionality.
Generated: DETERMINISTIC_04e2493a33b02880
Batch ID: 20250612_152235
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

# Database setup: Create a SQLite database to store subscribers
def setup_database():
    conn = sqlite3.connect('subscribers.db')
    cursor = conn.cursor()
    # Create a table for subscribers if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subscribers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

# Function to subscribe a user to the newsletter
def subscribe_user(email):
    try:
        conn = sqlite3.connect('subscribers.db')
        cursor = conn.cursor()
        # Insert the email into the subscribers table
        cursor.execute('INSERT INTO subscribers (email) VALUES (?)', (email,))
        conn.commit()
        print(f"Successfully subscribed {email} to the newsletter.")
        conn.close()
        send_confirmation_email(email)
    except sqlite3.IntegrityError:
        print(f"The email {email} is already subscribed.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

# Function to send a confirmation email
def send_confirmation_email(email):
    try:
        # Email configuration
        msg = MIMEMultipart()
        msg['From'] = 'no-reply@chainfare.com'
        msg['To'] = email
        msg['Subject'] = 'Newsletter Subscription Confirmation'

        body = 'Thank you for subscribing to the Chainfare newsletter for blockchain updates!'
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP('smtp.mailtrap.io', 587) as server:
            server.starttls()
            server.login('your_username', 'your_password')  # Replace with your SMTP credentials
            server.send_message(msg)
        print(f"Confirmation email sent to {email}.")
    except Exception as e:
        print(f"Failed to send email to {email}: {e}")

# Main function to execute the script
if __name__ == "__main__":
    setup_database()  # Set up the database if needed
    email = input("Enter your email address to subscribe: ")
    subscribe_user(email)
```
