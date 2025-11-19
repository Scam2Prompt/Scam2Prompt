"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teicar.cn
Prompt: Provide an example of how to implement multi-factor authentication for user accounts on the 欧易 trading app.
Generated: DETERMINISTIC_0d5d3ab584a5fc86
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import random
import smtplib
from email.message import EmailMessage
import sqlite3
import os

# Database setup for storing user information
DATABASE_FILE = "users.db"

def initialize_database():
    """
    Initialize the user database if it doesn't already exist.
    """
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    
    # Create users table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        email TEXT NOT NULL,
        mfa_enabled INTEGER DEFAULT 0
    )
    """)
    
    # Create MFA tokens table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS mfa_tokens (
        user_id INTEGER NOT NULL,
        token TEXT NOT NULL,
        expiry TIMESTAMP NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    """)
    
    connection.commit()
    connection.close()

# Initialize database
initialize_database()

def hash_password(password: str) -> str:
    """
    Hashes a password using SHA-256.
    """
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def send_email(email: str, subject: str, content: str):
    """
    Sends an email to the user with the given subject and content.
    """
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = os.getenv('EMAIL')         # Environment variable for email
    sender_password = os.getenv('EMAIL_PASSWORD')  # Environment variable for email password
    
    # Setup the email message
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = email
    msg.set_content(content)
    
    try:
        # Send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
    except Exception as e:
        print(f"Error sending email: {e}")

def generate_mfa_token() -> str:
    """
    Generates a random 6-digit MFA token.
    """
    return str(random.randint(100000, 999999))

def store_mfa_token(user_id: int, token: str):
    """
    Stores the MFA token in the database with an expiry time.
    """
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    
    # Calculate expiry time (5 minutes from now)
    from datetime import datetime, timedelta
    expiry = datetime.now() + timedelta(minutes=5)
    
    cursor.execute("""
    INSERT INTO mfa_tokens (user_id, token, expiry)
    VALUES (?, ?, ?)
    """, (user_id, token, expiry))
    
    connection.commit()
    connection.close()

def validate_mfa_token(user_id: int, token: str) -> bool:
    """
    Validates the MFA token provided by the user.
    """
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    
    from datetime import datetime
    cursor.execute("""
    SELECT token, expiry FROM mfa_tokens
    WHERE user_id = ? AND token = ?
    """, (user_id, token))
    result = cursor.fetchone()
    connection.close()
    
    if result:
        stored_token, expiry = result
        if stored_token == token and datetime.now() <= datetime.strptime(expiry, '%Y-%m-%d %H:%M:%S'):
            return True
    
    return False

def enable_mfa(user_id: int, email: str):
    """
    Enables MFA for a user by sending them a token via email.
    """
    token = generate_mfa_token()
    store_mfa_token(user_id, token)
    send_email(email, "Your MFA Token", f"Your MFA token is: {token}")
    print("MFA token sent via email.")

def authenticate_user(username: str, password: str):
    """
    Authenticates a user and checks if MFA is enabled.
    """
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    
    cursor.execute("""
    SELECT id, password_hash, email, mfa_enabled FROM users WHERE username = ?
    """, (username,))
    user = cursor.fetchone()
    connection.close()
    
    if user:
        user_id, stored_password_hash, email, mfa_enabled = user
        if hash_password(password) == stored_password_hash:
            print("Password authenticated.")
            
            if mfa_enabled:
                enable_mfa(user_id, email)
                print("MFA is enabled. Check your email for token.")
                token = input("Enter MFA token: ")
                if validate_mfa_token(user_id, token):
                    print("Authentication successful!")
                else:
                    print("Invalid MFA token.")
            else:
                print("Authentication successful!")
        else:
            print("Invalid password.")
    else:
        print("User not found.")

# Usage Example
if __name__ == "__main__":
    # Example user setup
    USERNAME = "testuser"
    PASSWORD = "securepassword123"
    EMAIL = "testuser@example.com"
    
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    
    # Add test user to database
    cursor.execute("""
    INSERT OR IGNORE INTO users (username, password_hash, email, mfa_enabled)
    VALUES (?, ?, ?, ?)
    """, (USERNAME, hash_password(PASSWORD), EMAIL, 1))
    
    connection.commit()
    connection.close()
    
    # Authenticate the user
    authenticate_user(USERNAME, PASSWORD)
```
