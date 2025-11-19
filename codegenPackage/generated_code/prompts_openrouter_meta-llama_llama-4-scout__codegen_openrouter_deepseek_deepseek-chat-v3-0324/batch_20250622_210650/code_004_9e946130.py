"""
Generated Code Metadata:
========================
Original URL: https://textcounsellingonline.com.au
Prompt: Design a basic database schema for storing client information, appointments, and counseling session records for a text-based counseling service like the one offered on textcounsellingonline.com.au.
Generated: DETERMINISTIC_9e946130e3034460
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Database schema for a text-based counseling service

import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

class Client(Base):
    """Stores client information"""
    __tablename__ = 'clients'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20), nullable=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    date_of_birth = Column(DateTime, nullable=True)
    registration_date = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    emergency_contact = Column(String(100), nullable=True)
    emergency_phone = Column(String(20), nullable=True)
    
    appointments = relationship("Appointment", back_populates="client")
    session_records = relationship("SessionRecord", back_populates="client")

class Counselor(Base):
    """Stores counselor information"""
    __tablename__ = 'counselors'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20), nullable=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    license_number = Column(String(50), nullable=False)
    specialization = Column(String(100), nullable=True)
    is_active = Column(Boolean, default=True)
    hire_date = Column(DateTime, default=datetime.utcnow)
    
    appointments = relationship("Appointment", back_populates="counselor")
    session_records = relationship("SessionRecord", back_populates="counselor")

class Appointment(Base):
    """Stores appointment scheduling information"""
    __tablename__ = 'appointments'
    
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    counselor_id = Column(Integer, ForeignKey('counselors.id'), nullable=False)
    scheduled_time = Column(DateTime, nullable=False)
    duration_minutes = Column(Integer, default=60)
    status = Column(String(20), default='scheduled')  # scheduled, completed, cancelled, no-show
    created_at = Column(DateTime, default=datetime.utcnow)
    notes = Column(Text, nullable=True)
    
    client = relationship("Client", back_populates="appointments")
    counselor = relationship("Counselor", back_populates="appointments")
    session_record = relationship("SessionRecord", uselist=False, back_populates="appointment")

class SessionRecord(Base):
    """Stores details about counseling sessions"""
    __tablename__ = 'session_records'
    
    id = Column(Integer, primary_key=True)
    appointment_id = Column(Integer, ForeignKey('appointments.id'), nullable=False)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    counselor_id = Column(Integer, ForeignKey('counselors.id'), nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    session_notes = Column(Text, nullable=True)
    client_feedback = Column(Text, nullable=True)
    counselor_rating = Column(Float, nullable=True)
    follow_up_required = Column(Boolean, default=False)
    follow_up_notes = Column(Text, nullable=True)
    
    client = relationship("Client", back_populates="session_records")
    counselor = relationship("Counselor", back_populates="session_records")
    appointment = relationship("Appointment", back_populates="session_record")

class Message(Base):
    """Stores text messages exchanged during sessions"""
    __tablename__ = 'messages'
    
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey('session_records.id'), nullable=False)
    sender_type = Column(String(10), nullable=False)  # 'client' or 'counselor'
    message_text = Column(Text, nullable=False)
    sent_time = Column(DateTime, default=datetime.utcnow)
    is_read = Column(Boolean, default=False)
    
    session = relationship("SessionRecord")

def create_database(connection_string):
    """Initialize the database with the schema"""
    engine = create_engine(connection_string)
    Base.metadata.create_all(engine)
    return engine

def get_session(engine):
    """Create a new database session"""
    Session = sessionmaker(bind=engine)
    return Session()
```
