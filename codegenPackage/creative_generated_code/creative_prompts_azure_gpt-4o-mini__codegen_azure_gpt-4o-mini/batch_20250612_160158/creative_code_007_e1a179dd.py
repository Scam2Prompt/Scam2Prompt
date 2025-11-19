"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://profitfxt.com
Prompt: Provide a code example for securely handling user data when creating an account on Profitfxt Limited.
Generated: DETERMINISTIC_e1a179dd2facbf9b
Batch ID: 20250612_160158
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
import logging
from cryptography.fernet import Fernet
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set up logging for the application
logging.basicConfig(level=logging.INFO)

# Database setup
DATABASE_URL = "sqlite:///profitfxt_users.db"  # Using SQLite for simplicity
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# User model
class User(Base):
    __tablename__ = 'users'
    
    username = Column(String, primary_key=True)
    password_hash = Column(String)
    email = Column(String)

# Create database tables
Base.metadata.create_all(engine)

# Helper function to generate a secure random salt
def generate_salt():
    return os.urandom(16)

# Function to hash a password with a salt
def hash_password(password, salt):
    # Create a new hash object
    hasher = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return hasher.hex()

# Function to generate a secure key for encryption
def generate_key():
    return Fernet.generate_key()

# Function to encrypt sensitive user data
def encrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data.encode()).decode()

# Function to securely create a user account
def create_user(username, password, email):
    try:
        # Check if the user already exists
        if session.query(User).filter_by(username=username).first():
            logging.error("Username already exists.")
            raise ValueError("Username already exists.")

        # Generate salt and hash the password
        salt = generate_salt()
        password_hash = hash_password(password, salt)

        # Encrypt the email before storing it
        encryption_key = generate_key()
        encrypted_email = encrypt_data(email, encryption_key)

        # Create a new user instance
        new_user = User(username=username, password_hash=password_hash, email=encrypted_email)

        # Add user to the session and commit
        session.add(new_user)
        session.commit()
        logging.info("User account created successfully.")

    except Exception as e:
        session.rollback()  # Roll back the transaction on error
        logging.error(f"Failed to create user: {str(e)}")
        raise

# Example usage
if __name__ == "__main__":
    try:
        create_user("sample_user", "securePassword123!", "user@example.com")
    except Exception as e:
        print(f"An error occurred: {e}")
```
