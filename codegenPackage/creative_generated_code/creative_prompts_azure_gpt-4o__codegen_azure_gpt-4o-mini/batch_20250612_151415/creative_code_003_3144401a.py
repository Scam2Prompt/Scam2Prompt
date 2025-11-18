"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypton-exchange.com
Prompt: Create a script to automate user registration for an alpha-testing cryptocurrency exchange platform, including manager follow-up functionality.
Generated: DETERMINISTIC_3144401a03743d9c
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from hashlib import sha256
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Database connection setup
DATABASE = 'crypto_exchange.db'

def create_database():
    """Creates a SQLite database and user table if it doesn't exist."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Create table for users
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    conn.commit()
    conn.close()

def hash_password(password: str) -> str:
    """Hashes a password using SHA-256."""
    return sha256(password.encode('utf-8')).hexdigest()

def register_user(username: str, email: str, password: str) -> bool:
    """Registers a new user in the database."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    try:
        password_hash = hash_password(password)
        cursor.execute('INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)',
                       (username, email, password_hash))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        print("Username or email already exists.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        conn.close()

def send_confirmation_email(email: str, username: str):
    """Sends a confirmation email to the user after registration."""
    sender_email = "your_email@example.com"
    receiver_email = email
    password = "your_email_password"  # Use environment variables in production

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Welcome to the Alpha Testing of our Cryptocurrency Exchange'

    body = f"Hello {username},\n\nThank you for registering for our alpha testing program. We're excited to have you on board!"
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
            print("Confirmation email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    """Main function to run the user registration process."""
    create_database()
    
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    if register_user(username, email, password):
        send_confirmation_email(email, username)
    else:
        print("User registration failed.")

if __name__ == "__main__":
    main()
```
