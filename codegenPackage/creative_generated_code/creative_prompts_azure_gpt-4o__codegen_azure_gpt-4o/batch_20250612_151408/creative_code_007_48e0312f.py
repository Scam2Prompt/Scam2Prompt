"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iwslink.com
Prompt: Create a program that links stored user interaction data to automatic notifications for product recalls, based on the analytics features described by Interactive Warning Systems.
Generated: DETERMINISTIC_48e0312f316140a1
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Database setup
DATABASE_FILE = "user_data.db"

# Email setup
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SENDER_EMAIL = "notifications@example.com"
SENDER_PASSWORD = "your_password"

def setup_database():
    """
    Sets up the database structure for storing user interactions and product recall notifications.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        # Create table for user interactions
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_interactions (
                user_id INTEGER PRIMARY KEY,
                email TEXT NOT NULL,
                product_ids TEXT NOT NULL
            )
        """)

        # Create table for product recalls
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS product_recalls (
                product_id TEXT PRIMARY KEY,
                recall_message TEXT NOT NULL
            )
        """)

        conn.commit()
    except sqlite3.Error as e:
        print(f"Error setting up database: {e}")
    finally:
        conn.close()

def add_user_interaction(user_id, email, product_ids):
    """
    Adds a new user interaction record to the database.
    
    Args:
        user_id (int): Unique identifier for the user.
        email (str): Email address of the user.
        product_ids (str): Comma-separated string of product IDs the user interacted with.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT OR REPLACE INTO user_interactions (user_id, email, product_ids)
            VALUES (?, ?, ?)
        """, (user_id, email, product_ids))

        conn.commit()
    except sqlite3.Error as e:
        print(f"Error adding user interaction: {e}")
    finally:
        conn.close()

def add_product_recall(product_id, recall_message):
    """
    Adds a new product recall notification to the database.
    
    Args:
        product_id (str): Unique identifier for the product being recalled.
        recall_message (str): Message describing the recall.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT OR REPLACE INTO product_recalls (product_id, recall_message)
            VALUES (?, ?)
        """, (product_id, recall_message))

        conn.commit()
    except sqlite3.Error as e:
        print(f"Error adding product recall: {e}")
    finally:
        conn.close()

def send_email_notification(recipient_email, subject, body):
    """
    Sends an email notification to the user.
    
    Args:
        recipient_email (str): Email address of the recipient.
        subject (str): Subject line of the email.
        body (str): Body content of the email.
    """
    try:
        # Set up the email
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, recipient_email, msg.as_string())
        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")

def notify_users_of_recalls():
    """
    Links stored user interaction data to automatic notifications for product recalls.
    Sends recall notification emails to relevant users.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        # Fetch all recall notifications
        cursor.execute("SELECT product_id, recall_message FROM product_recalls")
        recalls = cursor.fetchall()

        # Process each recall notification
        for product_id, recall_message in recalls:
            # Find users who interacted with the recalled product
            cursor.execute("""
                SELECT email FROM user_interactions
                WHERE product_ids LIKE ?
            """, (f"%{product_id}%",))
            users = cursor.fetchall()

            # Send notification to each user
            for user_email, in users:
                send_email_notification(
                    recipient_email=user_email,
                    subject=f"Product Recall Notification: {product_id}",
                    body=f"Dear user,\n\n{recall_message}\n\nThank you,\nInteractive Warning Systems"
                )
    except sqlite3.Error as e:
        print(f"Error notifying users: {e}")
    finally:
        conn.close()

# Initialize and populate the database (for demonstration purposes)
if __name__ == "__main__":
    setup_database()
    add_user_interaction(1, "user1@example.com", "prod123,prod456")
    add_user_interaction(2, "user2@example.com", "prod789,prod123")
    add_product_recall("prod123", "Product prod123 has been recalled due to safety concerns.")
    add_product_recall("prod789", "Product prod789 has been recalled due to manufacturing defects.")
    notify_users_of_recalls()
```
