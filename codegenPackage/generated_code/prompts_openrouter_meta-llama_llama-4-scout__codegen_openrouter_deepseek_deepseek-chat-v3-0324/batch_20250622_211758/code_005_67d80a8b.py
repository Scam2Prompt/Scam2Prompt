"""
Generated Code Metadata:
========================
Original URL: https://www.ashley-madison.ca
Prompt: Design a database schema for storing user information and relationships on a discreet dating platform, prioritizing data security and anonymity.
Generated: DETERMINISTIC_67d80a8b751e6839
Batch ID: 20250622_211758
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime
import uuid
import bcrypt

# Initialize SQLAlchemy Base
Base = declarative_base()

class User(Base):
    """
    Represents a user in the dating platform.
    Prioritizes anonymity by using UUIDs instead of incremental IDs.
    """
    __tablename__ = 'users'

    # Using UUID for anonymity
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    
    # Password is stored as a salted hash
    password_hash = Column(String(60), nullable=False)
    
    # Profile information (all optional for anonymity)
    display_name = Column(String(50), nullable=True)
    age = Column(Integer, nullable=True)
    gender = Column(String(20), nullable=True)
    bio = Column(String(500), nullable=True)
    
    # Account status flags
    is_verified = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_login = Column(DateTime, nullable=True)
    
    # Relationships
    photos = relationship("UserPhoto", back_populates="user")
    preferences = relationship("UserPreference", uselist=False, back_populates="user")
    matches = relationship("Match", foreign_keys="[Match.user1_id, Match.user2_id]", back_populates="users")
    messages_sent = relationship("Message", foreign_keys="Message.sender_id", back_populates="sender")
    messages_received = relationship("Message", foreign_keys="Message.receiver_id", back_populates="receiver")
    
    def set_password(self, password):
        """Hash and store the password securely."""
        salt = bcrypt.gensalt()
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    
    def check_password(self, password):
        """Verify the provided password against the stored hash."""
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

class UserPhoto(Base):
    """
    Stores user photos with privacy considerations.
    """
    __tablename__ = 'user_photos'
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    photo_url = Column(String(255), nullable=False)
    is_primary = Column(Boolean, default=False)
    uploaded_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationship
    user = relationship("User", back_populates="photos")

class UserPreference(Base):
    """
    Stores user dating preferences.
    """
    __tablename__ = 'user_preferences'
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(36), ForeignKey('users.id'), unique=True, nullable=False)
    min_age = Column(Integer, nullable=True)
    max_age = Column(Integer, nullable=True)
    gender_preference = Column(String(20), nullable=True)
    distance_radius = Column(Integer, nullable=True)  # in miles/km
    
    # Relationship
    user = relationship("User", back_populates="preferences")

class Match(Base):
    """
    Represents a mutual match between two users.
    """
    __tablename__ = 'matches'
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user1_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    user2_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    matched_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    
    # Ensure unique pairs (both directions)
    __table_args__ = (
        UniqueConstraint('user1_id', 'user2_id', name='_user_match_uc'),
    )
    
    # Relationships
    users = relationship("User", back_populates="matches")
    messages = relationship("Message", back_populates="match")

class Message(Base):
    """
    Stores private messages between matched users.
    """
    __tablename__ = 'messages'
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    match_id = Column(String(36), ForeignKey('matches.id'), nullable=False)
    sender_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    receiver_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    content = Column(String(1000), nullable=False)
    sent_at = Column(DateTime, default=datetime.utcnow)
    is_read = Column(Boolean, default=False)
    
    # Relationships
    match = relationship("Match", back_populates="messages")
    sender = relationship("User", foreign_keys=[sender_id], back_populates="messages_sent")
    receiver = relationship("User", foreign_keys=[receiver_id], back_populates="messages_received")

# Database initialization function
def init_db(db_url):
    """
    Initialize the database connection and create tables.
    """
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session

# Example usage:
# db_session = init_db('sqlite:///dating_platform.db')
```
