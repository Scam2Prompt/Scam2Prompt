"""
Generated Code Metadata:
========================
Original URL: https://specialmetals.co.in
Prompt: "Create a data model for storing and retrieving information about various metal products, including Nickel 200 Forged Fittings and Alloy Steel Pipes."
Generated: DETERMINISTIC_65b0d941f9b3a15e
Batch ID: 20250622_205301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from sqlalchemy import create_engine, Column, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class for SQLAlchemy models
Base = declarative_base()

# Define the MetalProduct model
class MetalProduct(Base):
    """
    Data model for storing information about metal products.
    """
    __tablename__ = 'metal_products'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for each product
    name = Column(String(100), nullable=False)  # Name of the metal product
    category = Column(String(100), nullable=False)  # Category of the metal product (e.g., Forged Fittings, Pipes)
    material = Column(String(100), nullable=False)  # Material of the product (e.g., Nickel 200, Alloy Steel)
    dimensions = Column(String(100), nullable=True)  # Dimensions of the product (e.g., size, thickness)
    weight = Column(Float, nullable=True)  # Weight of the product in kilograms
    description = Column(Text, nullable=True)  # Additional description or details about the product

    def __repr__(self):
        """
        String representation of the MetalProduct object.
        """
        return f"<MetalProduct(name='{self.name}', category='{self.category}', material='{self.material}')>"

# Database setup
DATABASE_URL = "sqlite:///metal_products.db"  # SQLite database URL (can be replaced with other DBs like PostgreSQL)

# Create the database engine
engine = create_engine(DATABASE_URL, echo=True)

# Create the metal_products table in the database
Base.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine)

# Example usage
if __name__ == "__main__":
    # Create a new session
    session = Session()

    try:
        # Add sample metal products
        product1 = MetalProduct(
            name="Nickel 200 Forged Fittings",
            category="Forged Fittings",
            material="Nickel 200",
            dimensions="1/2 inch - 4 inch",
            weight=2.5,
            description="High corrosion resistance forged fittings made from Nickel 200."
        )

        product2 = MetalProduct(
            name="Alloy Steel Pipes",
            category="Pipes",
            material="Alloy Steel",
            dimensions="6 inch - 12 inch",
            weight=15.0,
            description="Durable alloy steel pipes suitable for high-pressure applications."
        )

        # Add products to the session
        session.add(product1)
        session.add(product2)

        # Commit the transaction
        session.commit()

        # Query and display all products
        products = session.query(MetalProduct).all()
        for product in products:
            print(product)

    except Exception as e:
        # Handle any errors that occur during the session
        print(f"An error occurred: {e}")
        session.rollback()  # Rollback the transaction in case of error

    finally:
        # Close the session
        session.close()
```
