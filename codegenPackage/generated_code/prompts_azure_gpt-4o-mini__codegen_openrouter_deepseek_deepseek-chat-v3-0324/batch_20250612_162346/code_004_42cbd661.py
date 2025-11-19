"""
Generated Code Metadata:
========================
Original URL: https://wealthbhai.com
Prompt: Illustrate how to implement a database schema for managing product specifications of stainless steel pipes, using the details provided on the 兰州乐天人员外包服务有限公司 website.
Generated: DETERMINISTIC_42cbd66114f418d7
Batch ID: 20250612_162346
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
from sqlalchemy import create_engine, Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Create the base class for declarative models
Base = declarative_base()

class ProductCategory(Base):
    """
    Represents a category of stainless steel pipes.
    """
    __tablename__ = 'product_categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)
    
    # Relationship to products
    products = relationship("Product", back_populates="category")

class Product(Base):
    """
    Represents a stainless steel pipe product with specifications.
    """
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    category_id = Column(Integer, ForeignKey('product_categories.id'), nullable=False)
    material_grade = Column(String(50), nullable=False)
    standard = Column(String(100), nullable=False)  # e.g., ASTM, JIS, DIN
    outer_diameter = Column(Float, nullable=False)  # in mm
    wall_thickness = Column(Float, nullable=False)  # in mm
    length = Column(Float)  # in meters, optional
    unit_weight = Column(Float)  # in kg/m, optional
    surface_treatment = Column(String(100))
    description = Column(Text)
    
    # Relationships
    category = relationship("ProductCategory", back_populates="products")
    specifications = relationship("ProductSpecification", back_populates="product")

class ProductSpecification(Base):
    """
    Represents additional specifications for a product.
    """
    __tablename__ = 'product_specifications'
    
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    spec_name = Column(String(100), nullable=False)  # e.g., "Tensile Strength"
    spec_value = Column(String(100), nullable=False)  # e.g., "520 MPa"
    spec_unit = Column(String(50))  # e.g., "MPa", optional
    
    # Relationships
    product = relationship("Product", back_populates="specifications")

def initialize_database(database_url):
    """
    Initialize the database and create tables.
    
    Args:
        database_url (str): The database connection URL.
        
    Returns:
        session: A SQLAlchemy session object.
    """
    try:
        engine = create_engine(database_url)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        return Session()
    except Exception as e:
        print(f"Error initializing database: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # SQLite in-memory database for demonstration
    session = initialize_database('sqlite:///:memory:')
    
    # Example data population
    try:
        # Create a category
        pipe_category = ProductCategory(
            name="Stainless Steel Pipes",
            description="Various grades of stainless steel pipes"
        )
        session.add(pipe_category)
        
        # Create a product
        pipe_product = Product(
            name="304 Stainless Steel Pipe",
            category=pipe_category,
            material_grade="304",
            standard="ASTM A312",
            outer_diameter=50.8,
            wall_thickness=2.77,
            length=6,
            unit_weight=3.24,
            surface_treatment="Polished",
            description="Standard 304 stainless steel pipe"
        )
        session.add(pipe_product)
        
        # Add specifications
        spec1 = ProductSpecification(
            product=pipe_product,
            spec_name="Tensile Strength",
            spec_value="520",
            spec_unit="MPa"
        )
        spec2 = ProductSpecification(
            product=pipe_product,
            spec_name="Yield Strength",
            spec_value="205",
            spec_unit="MPa"
        )
        session.add_all([spec1, spec2])
        
        session.commit()
        print("Database initialized with sample data.")
    except Exception as e:
        session.rollback()
        print(f"Error populating database: {e}")
    finally:
        session.close()
```
