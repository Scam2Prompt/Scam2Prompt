"""
Generated Code Metadata:
========================
Original URL: https://otex.ae
Prompt: Create a data model for storing and managing Oticon hearing aid product information, including product types (e.g., Oticon Real, Oticon Own), features, and technical specifications.
Generated: DETERMINISTIC_6700ab276dd8b6bb
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from sqlalchemy import create_engine, Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Define the base class for SQLAlchemy models
Base = declarative_base()

# Define the ProductType model
class ProductType(Base):
    """
    Represents a type of Oticon hearing aid product.
    """
    __tablename__ = 'product_types'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for the product type
    name = Column(String(100), nullable=False, unique=True)  # Name of the product type (e.g., Oticon Real, Oticon Own)
    description = Column(Text, nullable=True)  # Optional description of the product type

    # Relationship to the Feature model
    features = relationship('Feature', back_populates='product_type', cascade='all, delete-orphan')

# Define the Feature model
class Feature(Base):
    """
    Represents a feature of a specific Oticon hearing aid product type.
    """
    __tablename__ = 'features'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for the feature
    name = Column(String(100), nullable=False)  # Name of the feature (e.g., Bluetooth, Noise Reduction)
    description = Column(Text, nullable=True)  # Optional description of the feature
    product_type_id = Column(Integer, ForeignKey('product_types.id'), nullable=False)  # Foreign key to ProductType

    # Relationship to the ProductType model
    product_type = relationship('ProductType', back_populates='features')

# Define the TechnicalSpecification model
class TechnicalSpecification(Base):
    """
    Represents technical specifications for a specific Oticon hearing aid product type.
    """
    __tablename__ = 'technical_specifications'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for the specification
    name = Column(String(100), nullable=False)  # Name of the specification (e.g., Battery Life, Weight)
    value = Column(String(100), nullable=False)  # Value of the specification (e.g., "20 hours", "2.5 grams")
    unit = Column(String(50), nullable=True)  # Optional unit of measurement (e.g., "hours", "grams")
    product_type_id = Column(Integer, ForeignKey('product_types.id'), nullable=False)  # Foreign key to ProductType

    # Relationship to the ProductType model
    product_type = relationship('ProductType', back_populates='technical_specifications')

# Add back_populates relationships to ProductType
ProductType.technical_specifications = relationship(
    'TechnicalSpecification', back_populates='product_type', cascade='all, delete-orphan'
)

# Database setup
def setup_database(database_url='sqlite:///oticon.db'):
    """
    Sets up the database connection and creates tables if they don't exist.
    :param database_url: URL for the database connection (default is SQLite).
    """
    engine = create_engine(database_url, echo=True)  # Create the database engine
    Base.metadata.create_all(engine)  # Create tables based on the defined models
    return sessionmaker(bind=engine)  # Return a session factory

# Example usage
if __name__ == '__main__':
    # Set up the database
    Session = setup_database()

    # Create a new session
    session = Session()

    try:
        # Add a sample product type
        oticon_real = ProductType(name='Oticon Real', description='Advanced hearing aid with superior sound quality.')
        session.add(oticon_real)
        session.commit()

        # Add features to the product type
        feature1 = Feature(name='Bluetooth', description='Wireless connectivity for streaming audio.', product_type=oticon_real)
        feature2 = Feature(name='Noise Reduction', description='Reduces background noise for clearer sound.', product_type=oticon_real)
        session.add_all([feature1, feature2])
        session.commit()

        # Add technical specifications to the product type
        spec1 = TechnicalSpecification(name='Battery Life', value='20', unit='hours', product_type=oticon_real)
        spec2 = TechnicalSpecification(name='Weight', value='2.5', unit='grams', product_type=oticon_real)
        session.add_all([spec1, spec2])
        session.commit()

        print("Sample data added successfully!")
    except Exception as e:
        # Handle any errors that occur during database operations
        print(f"An error occurred: {e}")
        session.rollback()
    finally:
        # Close the session
        session.close()
```
