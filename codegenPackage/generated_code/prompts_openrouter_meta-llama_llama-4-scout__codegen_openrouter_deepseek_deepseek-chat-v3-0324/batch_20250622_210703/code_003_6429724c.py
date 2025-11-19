"""
Generated Code Metadata:
========================
Original URL: https://grupolegalcorporativo.com
Prompt: Develop a basic data model for storing and managing client information, cases, and investigations for a law firm like Grupo Legal Corporativo, using a database management system.
Generated: DETERMINISTIC_6429724c94cccd80
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# law_firm_data_model.py
from datetime import datetime
from typing import Optional, List
from enum import Enum
from sqlalchemy import create_engine, Column, Integer, String, Text, Date, DateTime, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

Base = declarative_base()

class CaseStatus(Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    CLOSED = "closed"
    ARCHIVED = "archived"

class InvestigationStatus(Enum):
    PENDING = "pending"
    ACTIVE = "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class Client(Base):
    __tablename__ = 'clients'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20))
    address = Column(Text)
    company = Column(String(100))
    date_added = Column(DateTime, default=datetime.utcnow)
    notes = Column(Text)
    
    cases = relationship("Case", back_populates="client")
    
    def __repr__(self):
        return f"<Client(id={self.id}, name='{self.first_name} {self.last_name}')>"

class Case(Base):
    __tablename__ = 'cases'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    status = Column(SQLEnum(CaseStatus), default=CaseStatus.OPEN)
    open_date = Column(Date, default=datetime.utcnow)
    close_date = Column(Date)
    client_id = Column(Integer, ForeignKey('clients.id'))
    
    client = relationship("Client", back_populates="cases")
    investigations = relationship("Investigation", back_populates="case")
    
    def __repr__(self):
        return f"<Case(id={self.id}, title='{self.title}', status='{self.status.value}')>"

class Investigation(Base):
    __tablename__ = 'investigations'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    status = Column(SQLEnum(InvestigationStatus), default=InvestigationStatus.PENDING)
    start_date = Column(Date)
    end_date = Column(Date)
    case_id = Column(Integer, ForeignKey('cases.id'))
    
    case = relationship("Case", back_populates="investigations")
    
    def __repr__(self):
        return f"<Investigation(id={self.id}, title='{self.title}', status='{self.status.value}')>"

class DatabaseManager:
    def __init__(self, db_url: str = "sqlite:///law_firm.db"):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        
    def create_tables(self):
        try:
            Base.metadata.create_all(self.engine)
            print("Tables created successfully.")
        except SQLAlchemyError as e:
            print(f"Error creating tables: {e}")
            
    def get_session(self):
        return self.Session()
    
    def add_client(self, session, first_name: str, last_name: str, email: str, 
                   phone: Optional[str] = None, address: Optional[str] = None, 
                   company: Optional[str] = None, notes: Optional[str] = None):
        try:
            client = Client(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                address=address,
                company=company,
                notes=notes
            )
            session.add(client)
            session.commit()
            return client
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error adding client: {e}")
            return None
            
    def add_case(self, session, title: str, client_id: int, 
                 description: Optional[str] = None, status: CaseStatus = CaseStatus.OPEN):
        try:
            case = Case(
                title=title,
                description=description,
                status=status,
                client_id=client_id
            )
            session.add(case)
            session.commit()
            return case
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error adding case: {e}")
            return None
            
    def add_investigation(self, session, title: str, case_id: int, 
                          description: Optional[str] = None, 
                          status: InvestigationStatus = InvestigationStatus.PENDING):
        try:
            investigation = Investigation(
                title=title,
                description=description,
                status=status,
                case_id=case_id
            )
            session.add(investigation)
            session.commit()
            return investigation
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error adding investigation: {e}")
            return None
            
    def get_client_by_id(self, session, client_id: int):
        try:
            return session.query(Client).filter_by(id=client_id).first()
        except SQLAlchemyError as e:
            print(f"Error retrieving client: {e}")
            return None
            
    def get_cases_for_client(self, session, client_id: int):
        try:
            return session.query(Case).filter_by(client_id=client_id).all()
        except SQLAlchemyError as e:
            print(f"Error retrieving cases: {e}")
            return []
            
    def get_investigations_for_case(self, session, case_id: int):
        try:
            return session.query(Investigation).filter_by(case_id=case_id).all()
        except SQLAlchemyError as e:
            print(f"Error retrieving investigations: {e}")
            return []
            
    def update_client(self, session, client_id: int, **kwargs):
        try:
            client = session.query(Client).filter_by(id=client_id).first()
            if client:
                for key, value in kwargs.items():
                    setattr(client, key, value)
                session.commit()
                return client
            return None
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error updating client: {e}")
            return None
            
    def update_case_status(self, session, case_id: int, new_status: CaseStatus):
        try:
            case = session.query(Case).filter_by(id=case_id).first()
            if case:
                case.status = new_status
                if new_status == CaseStatus.CLOSED:
                    case.close_date = datetime.utcnow()
                session.commit()
                return case
            return None
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error updating case status: {e}")
            return None
            
    def close_investigation(self, session, investigation_id: int):
        try:
            investigation = session.query(Investigation).filter_by(id=investigation_id).first()
            if investigation:
                investigation.status = InvestigationStatus.COMPLETED
                investigation.end_date = datetime.utcnow()
                session.commit()
                return investigation
            return None
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error closing investigation: {e}")
            return None
```
