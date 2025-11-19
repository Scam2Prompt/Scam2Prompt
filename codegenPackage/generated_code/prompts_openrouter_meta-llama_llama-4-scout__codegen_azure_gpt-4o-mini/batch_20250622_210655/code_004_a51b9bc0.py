"""
Generated Code Metadata:
========================
Original URL: https://alexashipping.com
Prompt: Design a data model to store information about shipments, customers, and suppliers for a logistics company like Alexa Shipping, including attributes for tracking shipments, managing customer accounts, and monitoring supplier performance.
Generated: DETERMINISTIC_a51b9bc070d2e305
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Create a base class for declarative models
Base = declarative_base()

class Customer(Base):
    """Model to store customer information."""
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=True)
    address = Column(String, nullable=True)

    shipments = relationship("Shipment", back_populates="customer")

    def __repr__(self):
        return f"<Customer(name={self.name}, email={self.email})>"

class Supplier(Base):
    """Model to store supplier information."""
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_person = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=False)

    shipments = relationship("Shipment", back_populates="supplier")

    def __repr__(self):
        return f"<Supplier(name={self.name}, email={self.email})>"

class Shipment(Base):
    """Model to store shipment information."""
    __tablename__ = 'shipments'

    id = Column(Integer, primary_key=True)
    tracking_number = Column(String, unique=True, nullable=False)
    status = Column(String, nullable=False)  # e.g., 'Pending', 'In Transit', 'Delivered'
    weight = Column(Float, nullable=False)  # Weight in kilograms
    destination = Column(String, nullable=False)
    shipment_date = Column(DateTime, default=datetime.utcnow)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), nullable=False)

    customer = relationship("Customer", back_populates="shipments")
    supplier = relationship("Supplier", back_populates="shipments")

    def __repr__(self):
        return f"<Shipment(tracking_number={self.tracking_number}, status={self.status})>"

# Database setup
DATABASE_URL = "sqlite:///logistics.db"  # Change to your database URL
engine = create_engine(DATABASE_URL)

# Create all tables
Base.metadata.create_all(engine)

# Session management
Session = sessionmaker(bind=engine)

def add_customer(name, email, phone=None, address=None):
    """Add a new customer to the database."""
    session = Session()
    try:
        new_customer = Customer(name=name, email=email, phone=phone, address=address)
        session.add(new_customer)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error adding customer: {e}")
    finally:
        session.close()

def add_supplier(name, contact_person, phone, email):
    """Add a new supplier to the database."""
    session = Session()
    try:
        new_supplier = Supplier(name=name, contact_person=contact_person, phone=phone, email=email)
        session.add(new_supplier)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error adding supplier: {e}")
    finally:
        session.close()

def add_shipment(tracking_number, status, weight, destination, customer_id, supplier_id):
    """Add a new shipment to the database."""
    session = Session()
    try:
        new_shipment = Shipment(tracking_number=tracking_number, status=status, weight=weight,
                                destination=destination, customer_id=customer_id, supplier_id=supplier_id)
        session.add(new_shipment)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error adding shipment: {e}")
    finally:
        session.close()

# Example usage (uncomment to use)
# add_customer("John Doe", "john.doe@example.com", "123-456-7890", "123 Elm St")
# add_supplier("Acme Corp", "Jane Smith", "098-765-4321", "contact@acme.com")
# add_shipment("TRACK123456", "Pending", 10.5, "456 Oak St", 1, 1)
```
