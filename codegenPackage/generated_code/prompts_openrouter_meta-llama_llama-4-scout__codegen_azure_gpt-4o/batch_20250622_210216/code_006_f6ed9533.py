"""
Generated Code Metadata:
========================
Original URL: https://segrepin.com
Prompt: Design a data model for a company's operations in the Democratic Republic of Congo, including entities for customers, projects, and financial transactions.
Generated: DETERMINISTIC_f6ed953306c2f1ef
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

# Base class for SQLAlchemy models
Base = declarative_base()

# Customer entity
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for the customer
    name = Column(String(100), nullable=False)  # Customer's name
    email = Column(String(100), unique=True, nullable=False)  # Customer's email address
    phone = Column(String(20), nullable=True)  # Customer's phone number
    address = Column(String(200), nullable=True)  # Customer's address

    # Relationship to projects
    projects = relationship('Project', back_populates='customer')

# Project entity
class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for the project
    name = Column(String(100), nullable=False)  # Project name
    description = Column(String(500), nullable=True)  # Project description
    start_date = Column(DateTime, nullable=False, default=datetime.utcnow)  # Project start date
    end_date = Column(DateTime, nullable=True)  # Project end date
    budget = Column(Float, nullable=False)  # Project budget
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)  # Foreign key to Customer

    # Relationship to customer
    customer = relationship('Customer', back_populates='projects')

    # Relationship to financial transactions
    transactions = relationship('FinancialTransaction', back_populates='project')

# Financial Transaction entity
class FinancialTransaction(Base):
    __tablename__ = 'financial_transactions'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for the transaction
    amount = Column(Float, nullable=False)  # Transaction amount
    transaction_date = Column(DateTime, nullable=False, default=datetime.utcnow)  # Date of the transaction
    description = Column(String(200), nullable=True)  # Description of the transaction
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)  # Foreign key to Project

    # Relationship to project
    project = relationship('Project', back_populates='transactions')

# Database setup
def setup_database(database_url):
    """
    Sets up the database connection and creates tables if they don't exist.

    :param database_url: URL for the database connection
    """
    engine = create_engine(database_url, echo=True)  # Create database engine
    Base.metadata.create_all(engine)  # Create tables
    return sessionmaker(bind=engine)  # Return session factory

# Example usage
if __name__ == "__main__":
    # Replace with your actual database URL
    DATABASE_URL = "sqlite:///company_operations.db"

    # Set up the database
    Session = setup_database(DATABASE_URL)
    session = Session()

    try:
        # Example: Adding a customer
        new_customer = Customer(name="John Doe", email="john.doe@example.com", phone="123456789", address="Kinshasa, DRC")
        session.add(new_customer)
        session.commit()

        # Example: Adding a project
        new_project = Project(name="Infrastructure Development", description="Building roads in Kinshasa", budget=500000, customer_id=new_customer.id)
        session.add(new_project)
        session.commit()

        # Example: Adding a financial transaction
        new_transaction = FinancialTransaction(amount=10000, description="Initial funding", project_id=new_project.id)
        session.add(new_transaction)
        session.commit()

    except Exception as e:
        # Handle errors
        print(f"An error occurred: {e}")
        session.rollback()
    finally:
        # Close the session
        session.close()
```
