"""
Generated Code Metadata:
========================
Original URL: https://bit-deer.com
Prompt: "Design a database schema for storing information about customers on a waiting list for cryptocurrency mining hardware, such as Bitdeer Sealminers."
Generated: DETERMINISTIC_3635a9c8c2040c32
Batch ID: 20250622_212248
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Create base class for declarative models
Base = declarative_base()

class Customer(Base):
    """
    Represents a customer on the waiting list for cryptocurrency mining hardware.
    """
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20))
    company = Column(String(100))
    desired_hardware_model = Column(String(100), nullable=False)
    desired_quantity = Column(Integer, nullable=False, default=1)
    estimated_budget = Column(Float)
    join_date = Column(DateTime, default=datetime.utcnow)
    priority_level = Column(Integer, default=1)  # 1-5 scale
    notes = Column(String(500))
    is_verified = Column(Boolean, default=False)
    verification_token = Column(String(100))
    position_in_queue = Column(Integer)
    last_notified = Column(DateTime)
    status = Column(String(20), default='waiting')  # waiting, contacted, purchased, cancelled

    def __repr__(self):
        return f"<Customer(name='{self.first_name} {self.last_name}', email='{self.email}')>"

class HardwareModel(Base):
    """
    Represents available cryptocurrency mining hardware models.
    """
    __tablename__ = 'hardware_models'

    id = Column(Integer, primary_key=True)
    model_name = Column(String(100), unique=True, nullable=False)
    manufacturer = Column(String(100), nullable=False)
    hash_rate = Column(Float)  # in TH/s
    power_consumption = Column(Float)  # in W
    price = Column(Float)  # in USD
    estimated_delivery_time = Column(Integer)  # in days
    is_available = Column(Boolean, default=True)
    description = Column(String(500))

    def __repr__(self):
        return f"<HardwareModel(name='{self.model_name}', manufacturer='{self.manufacturer}')>"

class QueuePosition(Base):
    """
    Tracks customer positions in the waiting queue for specific hardware models.
    """
    __tablename__ = 'queue_positions'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, sqlalchemy.ForeignKey('customers.id'), nullable=False)
    hardware_model_id = Column(Integer, sqlalchemy.ForeignKey('hardware_models.id'), nullable=False)
    position = Column(Integer, nullable=False)
    date_added = Column(DateTime, default=datetime.utcnow)
    expected_availability_date = Column(DateTime)

    def __repr__(self):
        return f"<QueuePosition(customer_id={self.customer_id}, position={self.position})>"

class Notification(Base):
    """
    Records notifications sent to customers about their queue status.
    """
    __tablename__ = 'notifications'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, sqlalchemy.ForeignKey('customers.id'), nullable=False)
    sent_at = Column(DateTime, default=datetime.utcnow)
    notification_type = Column(String(50), nullable=False)  # position_update, availability, etc.
    content = Column(String(500), nullable=False)
    is_read = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Notification(customer_id={self.customer_id}, type='{self.notification_type}')>"

def init_db(db_url='sqlite:///mining_waitlist.db'):
    """
    Initialize the database connection and create tables.
    """
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

# Example usage:
if __name__ == '__main__':
    Session = init_db()
    session = Session()
    
    # Example: Add a hardware model
    new_hardware = HardwareModel(
        model_name="Bitdeer Sealminer A1",
        manufacturer="Bitdeer",
        hash_rate=100,
        power_consumption=3000,
        price=5000,
        estimated_delivery_time=30
    )
    session.add(new_hardware)
    
    # Example: Add a customer
    new_customer = Customer(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        desired_hardware_model="Bitdeer Sealminer A1",
        desired_quantity=2,
        estimated_budget=10000
    )
    session.add(new_customer)
    
    session.commit()
    session.close()
```
