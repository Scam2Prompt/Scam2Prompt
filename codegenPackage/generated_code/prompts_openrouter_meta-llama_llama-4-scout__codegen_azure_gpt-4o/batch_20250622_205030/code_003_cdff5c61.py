"""
Generated Code Metadata:
========================
Original URL: https://arbitrum24market.ru
Prompt: Design a basic database schema for storing client information and service orders for a legal center like "Арбитрум" and suggest a Python ORM library for implementation.
Generated: DETERMINISTIC_cdff5c61a1c7be2f
Batch ID: 20250622_205030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules from SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Define the base class for ORM models
Base = declarative_base()

# Define the Client model to store client information
class Client(Base):
    __tablename__ = 'clients'  # Table name in the database

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique client ID
    name = Column(String(100), nullable=False)  # Client's full name
    email = Column(String(100), unique=True, nullable=False)  # Client's email address
    phone = Column(String(15), nullable=True)  # Client's phone number
    address = Column(String(255), nullable=True)  # Client's address

    # Relationship to link clients with their service orders
    service_orders = relationship('ServiceOrder', back_populates='client')

# Define the ServiceOrder model to store service order information
class ServiceOrder(Base):
    __tablename__ = 'service_orders'  # Table name in the database

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique service order ID
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)  # Foreign key to the Client table
    service_name = Column(String(100), nullable=False)  # Name of the service provided
    cost = Column(Float, nullable=False)  # Cost of the service
    order_date = Column(DateTime, nullable=False)  # Date of the service order

    # Relationship to link service orders with their client
    client = relationship('Client', back_populates='service_orders')

# Function to initialize the database
def initialize_database(database_url):
    """
    Initializes the database and creates tables if they don't exist.

    Args:
        database_url (str): The database connection URL.
    """
    try:
        # Create the database engine
        engine = create_engine(database_url, echo=True)

        # Create all tables defined in the ORM models
        Base.metadata.create_all(engine)

        # Return a session factory for interacting with the database
        return sessionmaker(bind=engine)
    except Exception as e:
        # Handle any errors during database initialization
        print(f"Error initializing database: {e}")
        raise

# Example usage
if __name__ == '__main__':
    # Define the database connection URL (SQLite in this example)
    DATABASE_URL = 'sqlite:///legal_center.db'

    # Initialize the database and create a session factory
    Session = initialize_database(DATABASE_URL)

    # Create a new session
    session = Session()

    try:
        # Example: Add a new client
        new_client = Client(name="John Doe", email="john.doe@example.com", phone="1234567890", address="123 Main St")
        session.add(new_client)
        session.commit()

        # Example: Add a new service order for the client
        new_order = ServiceOrder(client_id=new_client.id, service_name="Legal Consultation", cost=150.0, order_date="2023-10-01")
        session.add(new_order)
        session.commit()

        print("Data added successfully!")
    except Exception as e:
        # Handle any errors during database operations
        print(f"Error during database operations: {e}")
        session.rollback()
    finally:
        # Close the session
        session.close()
```

### Suggested Python ORM Library:
The code uses **SQLAlchemy**, which is a powerful and widely-used Python ORM library. It provides flexibility, supports multiple database backends, and adheres to best practices for database interaction.
