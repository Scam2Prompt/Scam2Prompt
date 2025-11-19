"""
Generated Code Metadata:
========================
Original URL: https://motor-muse.com
Prompt: Design a data model for storing information about various car models, including their specifications, prices, and features, using the 2025 GMC Yukon Denali as an example.
Generated: DETERMINISTIC_293db24bfbd37626
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class for SQLAlchemy models
Base = declarative_base()

# Define the CarModel class to represent the data model for car information
class CarModel(Base):
    """
    Data model for storing car information, including specifications, prices, and features.
    """
    __tablename__ = 'car_models'

    # Primary key: Unique identifier for each car model
    id = Column(Integer, primary_key=True, autoincrement=True)

    # Basic information about the car
    name = Column(String(100), nullable=False)  # Name of the car model
    manufacturer = Column(String(100), nullable=False)  # Manufacturer name
    year = Column(Integer, nullable=False)  # Year of manufacture

    # Specifications
    engine_type = Column(String(100), nullable=False)  # Type of engine (e.g., V8, electric)
    horsepower = Column(Integer, nullable=False)  # Horsepower of the car
    torque = Column(Integer, nullable=False)  # Torque in lb-ft
    fuel_type = Column(String(50), nullable=False)  # Type of fuel (e.g., gasoline, diesel, electric)
    mpg_city = Column(Float, nullable=False)  # Miles per gallon in city
    mpg_highway = Column(Float, nullable=False)  # Miles per gallon on highway

    # Pricing
    base_price = Column(Float, nullable=False)  # Base price of the car model

    # Features
    has_sunroof = Column(Boolean, default=False)  # Whether the car has a sunroof
    has_navigation = Column(Boolean, default=False)  # Whether the car has a navigation system
    has_heated_seats = Column(Boolean, default=False)  # Whether the car has heated seats
    has_bluetooth = Column(Boolean, default=False)  # Whether the car has Bluetooth connectivity

    def __repr__(self):
        """
        String representation of the CarModel object for debugging purposes.
        """
        return f"<CarModel(name={self.name}, manufacturer={self.manufacturer}, year={self.year})>"

# Database setup
DATABASE_URL = "sqlite:///car_models.db"  # SQLite database URL (can be replaced with other DBs)
engine = create_engine(DATABASE_URL)  # Create the database engine
Base.metadata.create_all(engine)  # Create tables based on the defined models
Session = sessionmaker(bind=engine)  # Create a session factory

# Example usage: Adding the 2025 GMC Yukon Denali to the database
def add_example_car():
    """
    Adds an example car (2025 GMC Yukon Denali) to the database.
    """
    session = Session()  # Create a new session
    try:
        # Create an instance of CarModel for the 2025 GMC Yukon Denali
        yukon_denali = CarModel(
            name="Yukon Denali",
            manufacturer="GMC",
            year=2025,
            engine_type="6.2L V8",
            horsepower=420,
            torque=460,
            fuel_type="Gasoline",
            mpg_city=14.0,
            mpg_highway=19.0,
            base_price=75000.0,
            has_sunroof=True,
            has_navigation=True,
            has_heated_seats=True,
            has_bluetooth=True
        )
        session.add(yukon_denali)  # Add the car to the session
        session.commit()  # Commit the transaction
        print("Example car added successfully!")
    except Exception as e:
        # Handle any errors that occur during the transaction
        session.rollback()  # Roll back the transaction in case of error
        print(f"Error adding example car: {e}")
    finally:
        session.close()  # Close the session

# Run the example function
if __name__ == "__main__":
    add_example_car()
```
