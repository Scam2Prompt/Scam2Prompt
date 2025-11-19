"""
Generated Code Metadata:
========================
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Create a function to handle user login and registration for an e-commerce site, inspired by the "Login | Cadastre-se" feature on ebrasilbrazz.
Generated: DETERMINISTIC_0bc53a99f9e3021f
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import bcrypt
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import IntegrityError

# Database setup
DATABASE_URL = "sqlite:///ecommerce.db"  # Change to your database URL
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# User model
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

# Create the database tables
Base.metadata.create_all(engine)

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def hash_password(password: str) -> str:
    """Hashes a password using bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies a plain password against a hashed password."""
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def register_user(username: str, password: str) -> str:
    """Registers a new user with a username and password."""
    if not username or not password:
        raise ValueError("Username and password cannot be empty.")
    
    hashed_password = hash_password(password)
    
    # Create a new session
    with SessionLocal() as session:
        new_user = User(username=username, password_hash=hashed_password)
        session.add(new_user)
        try:
            session.commit()
            return "User registered successfully."
        except IntegrityError:
            session.rollback()
            raise ValueError("Username already exists.")

def login_user(username: str, password: str) -> str:
    """Logs in a user by verifying the username and password."""
    if not username or not password:
        raise ValueError("Username and password cannot be empty.")
    
    # Create a new session
    with SessionLocal() as session:
        user = session.query(User).filter(User.username == username).first()
        if user and verify_password(password, user.password_hash):
            return "Login successful."
        else:
            raise ValueError("Invalid username or password.")

# Example usage (uncomment to test)
# try:
#     print(register_user("testuser", "securepassword"))
#     print(login_user("testuser", "securepassword"))
# except ValueError as e:
#     print(e)
```
