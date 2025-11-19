"""
Generated Code Metadata:
========================
Original URL: https://annonceintimex.com
Prompt: "Design a database schema for storing user profiles, preferences, and matches on an erotic dating site, focusing on scalability and data protection."
Generated: DETERMINISTIC_aae0a8845e88f9b0
Batch ID: 20250622_204855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey, Text, Enum, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
import enum
import bcrypt

# Database connection setup
DATABASE_URL = "postgresql://username:password@localhost/erotic_dating_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Enums for various fields
class Gender(enum.Enum):
    MALE = "male"
    FEMALE = "female"
    NON_BINARY = "non_binary"
    OTHER = "other"

class Orientation(enum.Enum):
    HETEROSEXUAL = "heterosexual"
    HOMOSEXUAL = "homosexual"
    BISEXUAL = "bisexual"
    PANSEXUAL = "pansexual"
    ASEXUAL = "asexual"
    OTHER = "other"

class AccountStatus(enum.Enum):
    ACTIVE = "active"
    SUSPENDED = "suspended"
    DELETED = "deleted"
    BANNED = "banned"

# User model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    salt = Column(String(255), nullable=False)
    account_status = Column(Enum(AccountStatus), default=AccountStatus.ACTIVE)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_login = Column(DateTime)
    ip_address = Column(String(45))  # IPv6 max length

    profile = relationship("UserProfile", back_populates="user", uselist=False)
    preferences = relationship("UserPreferences", back_populates="user", uselist=False)
    matches = relationship("Match", back_populates="user")

    def set_password(self, password: str):
        """Hashes the password and stores it with salt"""
        self.salt = bcrypt.gensalt().decode('utf-8')
        self.hashed_password = bcrypt.hashpw(password.encode('utf-8'), self.salt.encode('utf-8')).decode('utf-8')

    def verify_password(self, password: str) -> bool:
        """Verifies the password against the stored hash"""
        return bcrypt.checkpw(password.encode('utf-8'), self.hashed_password.encode('utf-8'))

# User profile model
class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    username = Column(String(50), unique=True, index=True)
    display_name = Column(String(100))
    gender = Column(Enum(Gender))
    orientation = Column(Enum(Orientation))
    birth_date = Column(DateTime)
    bio = Column(Text)
    location = Column(String(100))
    profile_picture_url = Column(String(255))
    is_verified = Column(Boolean, default=False)
    last_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="profile")

# User preferences model
class UserPreferences(Base):
    __tablename__ = "user_preferences"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    age_min = Column(Integer, default=18)
    age_max = Column(Integer, default=99)
    gender_preference = Column(JSON)  # Array of genders
    distance_radius = Column(Integer, default=50)  # in miles/km
    notification_enabled = Column(Boolean, default=True)
    email_notifications = Column(Boolean, default=True)
    privacy_level = Column(Integer, default=1)  # 1-5 scale
    kinks = Column(JSON)  # Array of kink preferences
    last_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="preferences")

# Match model
class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    matched_user_id = Column(Integer, ForeignKey("users.id"))
    match_score = Column(Integer)  # Compatibility score
    is_mutual = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_interaction = Column(DateTime)

    user = relationship("User", back_populates="matches", foreign_keys=[user_id])

# Message model
class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("users.id"))
    receiver_id = Column(Integer, ForeignKey("users.id"))
    content = Column(Text)
    is_read = Column(Boolean, default=False)
    sent_at = Column(DateTime, default=datetime.utcnow)
    is_deleted = Column(Boolean, default=False)

# Blocked users model
class BlockedUser(Base):
    __tablename__ = "blocked_users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    blocked_user_id = Column(Integer, ForeignKey("users.id"))
    reason = Column(String(255))
    blocked_at = Column(DateTime, default=datetime.utcnow)

# Login attempts model for security
class LoginAttempt(Base):
    __tablename__ = "login_attempts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    ip_address = Column(String(45))
    attempt_time = Column(DateTime, default=datetime.utcnow)
    success = Column(Boolean, default=False)

# Create all tables
Base.metadata.create_all(bind=engine)

# Database session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```
