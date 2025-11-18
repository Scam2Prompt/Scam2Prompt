"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://empower.gr
Prompt: Recommend libraries for implementing secure password storage and retrieval in a system like Empower's login page.
Generated: DETERMINISTIC_9ed9cb114b062f1a
Batch ID: 20250612_150645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set up SQLAlchemy for database interaction
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

# Database connection setup
DATABASE_URI = 'sqlite:///users.db'  # Use an appropriate database URI
engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

def hash_password(password: str) -> str:
    """
    Hash a password using bcrypt.
    
    :param password: The plaintext password to be hashed.
    :return: The hashed password.
    """
    if not isinstance(password, str) or len(password) < 8:
        raise ValueError("Password must be a string with at least 8 characters.")
    
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def verify_password(stored_password: str, provided_password: str) -> bool:
    """
    Verify a provided password against the stored hashed password.
    
    :param stored_password: The hashed password from the database.
    :param provided_password: The plaintext password to verify.
    :return: True if the password is correct, False otherwise.
    """
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))

def create_user(username: str, password: str) -> User:
    """
    Create a new user with a hashed password.
    
    :param username: The username for the new user.
    :param password: The plaintext password for the new user.
    :return: The created User object.
    """
    if session.query(User).filter_by(username=username).first():
        raise ValueError("Username already exists.")
    
    password_hash = hash_password(password)
    new_user = User(username=username, password_hash=password_hash)

    try:
        session.add(new_user)
        session.commit()
    except Exception as e:
        session.rollback()
        raise RuntimeError("Failed to create user.") from e
    
    return new_user

def login_user(username: str, password: str) -> bool:
    """
    Verify user login credentials.
    
    :param username: The username of the user attempting to log in.
    :param password: The plaintext password provided for login.
    :return: True if login is successful, False otherwise.
    """
    user = session.query(User).filter_by(username=username).first()
    if user is None:
        return False  # User not found

    return verify_password(user.password_hash, password)

# Example usage
if __name__ == "__main__":
    try:
        new_user = create_user("test_user", "secure_password123")
        print(f"User created: {new_user.username}")
        
        if login_user("test_user", "secure_password123"):
            print("Login successful!")
        else:
            print("Invalid credentials.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
