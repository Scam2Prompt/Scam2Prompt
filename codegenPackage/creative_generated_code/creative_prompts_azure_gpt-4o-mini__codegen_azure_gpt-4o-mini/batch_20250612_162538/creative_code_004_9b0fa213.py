"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shcoinai.app
Prompt: What are the best practices for securing user data against phishing threats, and how can I implement these using specific libraries?
Generated: DETERMINISTIC_9b0fa2133dd375fc
Batch ID: 20250612_162538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import re
import smtplib
from email.mime.text import MIMEText
from getpass import getpass

class UserAuthenticator:
    """
    A class to manage user authentication and secure data handling.
    """

    def __init__(self):
        self.users_db = {}  # In-memory database for demonstration, replace with persistent storage in production

    def hash_password(self, password: str) -> str:
        """
        Hashes the user password for secure storage.

        :param password: The user's plaintext password
        :return: A hashed password
        """
        salt = os.urandom(32)  # Generate a random salt
        hashed_pw = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        return salt + hashed_pw  # Store salt with the hashed password

    def register_user(self, username: str, password: str) -> None:
        """
        Registers a new user with a username and a hashed password.
        
        :param username: The user's username
        :param password: The user's password
        """
        if username in self.users_db:
            raise ValueError("Username already exists.")
        
        self.users_db[username] = self.hash_password(password)

    def authenticate_user(self, username: str, password: str) -> bool:
        """
        Authenticates a user by comparing the provided password with the stored hashed password.

        :param username: The user's username
        :param password: The user's password
        :return: True if authenticated, False otherwise
        """
        if username not in self.users_db:
            return False

        salt_and_hashed_pw = self.users_db[username]
        salt = salt_and_hashed_pw[:32]
        stored_hashed_pw = salt_and_hashed_pw[32:]

        hashed_pw = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        return hashed_pw == stored_hashed_pw

class EmailSender:
    """
    A class to handle secure email sending to users.
    """

    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, recipient_email: str, subject: str, body: str) -> None:
        """
        Sends an email to the specified recipient.

        :param recipient_email: The email address of the recipient
        :param subject: The subject of the email
        :param body: The body content of the email
        """
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.sender_email
        msg['To'] = recipient_email

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade to a secure connection
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
        except smtplib.SMTPException as e:
            print(f"Error sending email: {e}")

# Example usage
if __name__ == "__main__":
    auth = UserAuthenticator()
    
    username = input("Enter username: ")
    password = getpass("Enter password: ")

    try:
        auth.register_user(username, password)
        print("User registered successfully.")
    except ValueError as ve:
        print(f"Registration failed: {ve}")

    # For sending email notifications
    email_sender = EmailSender('smtp.example.com', 587, 'your_email@example.com', 'your_email_password')
    email_sender.send_email('recipient@example.com', 'Welcome!', 'Thank you for registering!')
```
