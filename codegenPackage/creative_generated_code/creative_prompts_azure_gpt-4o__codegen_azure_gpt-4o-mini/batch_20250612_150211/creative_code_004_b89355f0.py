"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.app.pavonal.com
Prompt: Suggest best practices for implementing secure password storage and retrieval for a platform like Pavonal.
Generated: DETERMINISTIC_b89355f00d93b06f
Batch ID: 20250612_150211
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
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError

# Define the base class for SQLAlchemy models
Base = declarative_base()

# Define a User model for the database
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

# Initialize the database connection and session
DATABASE_URL = "sqlite:///users.db"  # Replace with your database URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to create the database tables
def init_db():
    Base.metadata.create_all(bind=engine)

# Function to hash a password using bcrypt
def hash_password(password: str) -> str:
    if not password:
        raise ValueError("Password must not be empty.")
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# Function to verify a password against a stored hash
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

# Function to add a new user to the database with secure password storage
def create_user(username: str, password: str) -> User:
    hashed_password = hash_password(password)
    new_user = User(username=username, password_hash=hashed_password)
    
    try:
        with SessionLocal() as session:
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
            return new_user
    except SQLAlchemyError as e:
        # Handle SQLAlchemy errors (e.g., uniqueness violation)
        raise Exception(f"An error occurred while creating user: {str(e)}")

# Function to retrieve a user by username and verify the password
def authenticate_user(username: str, password: str) -> User:
    try:
        with SessionLocal() as session:
            user = session.query(User).filter(User.username == username).first()
            if user and verify_password(password, user.password_hash):
                return user
            return None
    except SQLAlchemyError as e:
        raise Exception(f"An error occurred during authentication: {str(e)}")

# Initialize the database
if __name__ == "__main__":
    init_db()
```
