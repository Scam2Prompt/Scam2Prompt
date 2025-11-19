"""
Generated Code Metadata:
========================
Original URL: https://gala-games-home-f.blogspot.com
Prompt: Generate a Python script to automate email subscription for sending updates on interior design trends and exclusive materials, similar to the "Fique por Dentro" feature on the website.
Generated: DETERMINISTIC_82f7c394fdc70452
Batch ID: 20250612_154452
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
from email.mime.multipart import MIMEMultipart
import re
import sqlite3
from datetime import datetime
from typing import Optional, Tuple

# Database configuration
DB_NAME = "email_subscriptions.db"

# Email configuration
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USERNAME = "your_email@example.com"
SMTP_PASSWORD = "your_password"
FROM_EMAIL = "newsletter@interiordesign.com"
SUBJECT = "Subscription Confirmation - Interior Design Trends"

# HTML template for confirmation email
CONFIRMATION_EMAIL_TEMPLATE = """
<html>
    <body>
        <h1>Welcome to Interior Design Trends!</h1>
        <p>Thank you for subscribing to our newsletter.</p>
        <p>You'll receive updates on:</p>
        <ul>
            <li>Latest interior design trends</li>
            <li>Exclusive materials and products</li>
            <li>Special offers for subscribers</li>
        </ul>
        <p>If you didn't request this subscription, please ignore this email.</p>
        <p>Best regards,<br>The Interior Design Team</p>
    </body>
</html>
"""

def initialize_database() -> None:
    """Initialize the SQLite database for storing subscriptions."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                name TEXT,
                subscription_date TEXT NOT NULL,
                is_confirmed INTEGER DEFAULT 0,
                confirmation_code TEXT
            )
        """)
        conn.commit()

def is_valid_email(email: str) -> bool:
    """Validate email format using regex."""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

def generate_confirmation_code(email: str) -> str:
    """Generate a unique confirmation code for email verification."""
    timestamp = str(int(datetime.now().timestamp()))
    return f"{email[:3]}{timestamp[-4:]}{email[-3:]}".replace(".", "").replace("@", "")

def send_confirmation_email(to_email: str, confirmation_code: str) -> bool:
    """Send confirmation email to the subscriber."""
    try:
        msg = MIMEMultipart()
        msg["From"] = FROM_EMAIL
        msg["To"] = to_email
        msg["Subject"] = SUBJECT

        # Add HTML content
        msg.attach(MIMEText(CONFIRMATION_EMAIL_TEMPLATE, "html"))

        # Connect to SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)
        
        return True
    except Exception as e:
        print(f"Error sending confirmation email: {e}")
        return False

def add_subscription(email: str, name: Optional[str] = None) -> Tuple[bool, str]:
    """Add a new subscription to the database and send confirmation email."""
    if not is_valid_email(email):
        return False, "Invalid email format"

    confirmation_code = generate_confirmation_code(email)
    subscription_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            
            # Check if email already exists
            cursor.execute("SELECT email FROM subscriptions WHERE email = ?", (email,))
            if cursor.fetchone():
                return False, "Email already subscribed"
            
            # Insert new subscription
            cursor.execute(
                "INSERT INTO subscriptions (email, name, subscription_date, confirmation_code) VALUES (?, ?, ?, ?)",
                (email, name, subscription_date, confirmation_code)
            )
            conn.commit()

        # Send confirmation email
        if send_confirmation_email(email, confirmation_code):
            return True, "Subscription successful. Please check your email for confirmation."
        else:
            return False, "Subscription failed. Could not send confirmation email."
            
    except sqlite3.Error as e:
        return False, f"Database error: {e}"

def confirm_subscription(email: str, confirmation_code: str) -> Tuple[bool, str]:
    """Confirm a subscription using the confirmation code."""
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            
            # Check if email and code match
            cursor.execute(
                "SELECT id FROM subscriptions WHERE email = ? AND confirmation_code = ?",
                (email, confirmation_code)
            )
            if not cursor.fetchone():
                return False, "Invalid confirmation code or email"
            
            # Update subscription status
            cursor.execute(
                "UPDATE subscriptions SET is_confirmed = 1 WHERE email = ?",
                (email,)
            )
            conn.commit()
            
            return True, "Subscription confirmed successfully"
            
    except sqlite3.Error as e:
        return False, f"Database error: {e}"

def get_subscribers() -> list:
    """Retrieve all confirmed subscribers from the database."""
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT email, name FROM subscriptions WHERE is_confirmed = 1")
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error retrieving subscribers: {e}")
        return []

# Initialize database when module is imported
initialize_database()

# Example usage
if __name__ == "__main__":
    # Test subscription
    email = "test@example.com"
    name = "Test User"
    
    success, message = add_subscription(email, name)
    print(message)
    
    if success:
        # In a real application, the confirmation code would come from the user's email
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT confirmation_code FROM subscriptions WHERE email = ?", (email,))
            confirmation_code = cursor.fetchone()[0]
        
        success, message = confirm_subscription(email, confirmation_code)
        print(message)
        
        # Get all confirmed subscribers
        subscribers = get_subscribers()
        print("Confirmed subscribers:", subscribers)
```
