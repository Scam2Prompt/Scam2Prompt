"""
Generated Code Metadata:
========================
Original URL: https://movilabtorremedica2.com
Prompt: Design a secure and efficient system for storing and managing electronic health records (EHRs) for a medical center with multiple specialists like Movilab Torre Médica II.
Generated: DETERMINISTIC_62d9b67a192db6ba
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from typing import Dict, List
from datetime import datetime
import hashlib
import logging
from logging.handlers import RotatingFileHandler
from sqlalchemy import create_engine, Column, String, Integer, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
handler = RotatingFileHandler('ehr_system.log', maxBytes=10000, backupCount=1)
logger.addHandler(handler)

# Create a database engine
engine = create_engine('postgresql://user:password@localhost/ehr_database')

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

class User(Base):
    """Represents a user in the system."""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password_hash = Column(String)
    role = Column(String)

    def __init__(self, username: str, password: str, role: str):
        self.username = username
        self.password_hash = self._hash_password(password)
        self.role = role

    @staticmethod
    def _hash_password(password: str) -> str:
        """Hashes a password for storing."""
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password: str) -> bool:
        """Verifies a password against the stored hash."""
        return self.password_hash == self._hash_password(password)

class Patient(Base):
    """Represents a patient in the system."""
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    date_of_birth = Column(DateTime)
    medical_history = Column(String)

    def __init__(self, name: str, date_of_birth: datetime, medical_history: str):
        self.name = name
        self.date_of_birth = date_of_birth
        self.medical_history = medical_history

class EHR(Base):
    """Represents an electronic health record."""
    __tablename__ = 'ehrs'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer)
    specialist_id = Column(Integer)
    record = Column(String)
    created_at = Column(DateTime)

    def __init__(self, patient_id: int, specialist_id: int, record: str):
        self.patient_id = patient_id
        self.specialist_id = specialist_id
        self.record = record
        self.created_at = datetime.now()

class Specialist(Base):
    """Represents a specialist in the system."""
    __tablename__ = 'specialists'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    specialty = Column(String)

    def __init__(self, name: str, specialty: str):
        self.name = name
        self.specialty = specialty

# Create all tables in the engine
Base.metadata.create_all(engine)

def create_user(session: Session, username: str, password: str, role: str) -> User:
    """Creates a new user."""
    user = User(username, password, role)
    session.add(user)
    session.commit()
    return user

def get_patient(session: Session, patient_id: int) -> Patient:
    """Gets a patient by ID."""
    return session.query(Patient).get(patient_id)

def create_ehr(session: Session, patient_id: int, specialist_id: int, record: str) -> EHR:
    """Creates a new electronic health record."""
    ehr = EHR(patient_id, specialist_id, record)
    session.add(ehr)
    session.commit()
    return ehr

def get_ehr(session: Session, ehr_id: int) -> EHR:
    """Gets an electronic health record by ID."""
    return session.query(EHR).get(ehr_id)

def main():
    # Create a new session
    session = Session()

    try:
        # Create a new user
        user = create_user(session, 'john_doe', 'password123', 'admin')
        logger.info(f'Created user {user.username}')

        # Create a new patient
        patient = Patient('Jane Doe', datetime(1990, 1, 1), 'No medical history')
        session.add(patient)
        session.commit()
        logger.info(f'Created patient {patient.name}')

        # Create a new specialist
        specialist = Specialist('Dr. Smith', 'Cardiologist')
        session.add(specialist)
        session.commit()
        logger.info(f'Created specialist {specialist.name}')

        # Create a new electronic health record
        ehr = create_ehr(session, patient.id, specialist.id, 'Patient has hypertension')
        logger.info(f'Created EHR {ehr.id} for patient {ehr.patient_id}')

        # Get a patient
        retrieved_patient = get_patient(session, patient.id)
        logger.info(f'Retrieved patient {retrieved_patient.name}')

        # Get an electronic health record
        retrieved_ehr = get_ehr(session, ehr.id)
        logger.info(f'Retrieved EHR {retrieved_ehr.id} for patient {retrieved_ehr.patient_id}')

    except Exception as e:
        logger.error(f'An error occurred: {e}')
        session.rollback()

    finally:
        session.close()

if __name__ == '__main__':
    main()
```
