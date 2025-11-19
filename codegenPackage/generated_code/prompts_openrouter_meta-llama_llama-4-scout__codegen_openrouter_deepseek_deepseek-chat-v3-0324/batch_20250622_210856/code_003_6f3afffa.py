"""
Generated Code Metadata:
========================
Original URL: https://mgcaugiay.com
Prompt: Design a data schema for storing information about MG car models, including their engine specifications, dimensions, and features, and suggest a suitable database management system.
Generated: DETERMINISTIC_6f3afffa3066c511
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Database schema for MG car models
# Using SQLAlchemy ORM for Python with PostgreSQL as the database backend

from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

Base = declarative_base()

class EngineSpec(Base):
    """Table for storing engine specifications"""
    __tablename__ = 'engine_specs'
    
    id = Column(Integer, primary_key=True)
    model_id = Column(Integer, ForeignKey('car_models.id'))
    engine_type = Column(String(50))  # e.g., 'Turbocharged', 'Electric'
    displacement = Column(Float)      # in liters
    horsepower = Column(Integer)      # in HP
    torque = Column(Integer)          # in Nm
    transmission = Column(String(50)) # e.g., 'Automatic', 'Manual'
    fuel_type = Column(String(30))   # e.g., 'Petrol', 'Diesel', 'Electric'
    fuel_economy = Column(Float)      # in km/l or kWh/km
    
    car_model = relationship("CarModel", back_populates="engine_spec")

class Dimensions(Base):
    """Table for storing vehicle dimensions"""
    __tablename__ = 'dimensions'
    
    id = Column(Integer, primary_key=True)
    model_id = Column(Integer, ForeignKey('car_models.id'))
    length = Column(Float)    # in mm
    width = Column(Float)     # in mm
    height = Column(Float)    # in mm
    wheelbase = Column(Float) # in mm
    weight = Column(Float)    # in kg
    trunk_capacity = Column(Float) # in liters
    
    car_model = relationship("CarModel", back_populates="dimensions")

class Feature(Base):
    """Table for storing individual features"""
    __tablename__ = 'features'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    description = Column(String(255))
    
    model_features = relationship("ModelFeature", back_populates="feature")

class ModelFeature(Base):
    """Junction table for car models and their features"""
    __tablename__ = 'model_features'
    
    id = Column(Integer, primary_key=True)
    model_id = Column(Integer, ForeignKey('car_models.id'))
    feature_id = Column(Integer, ForeignKey('features.id'))
    is_standard = Column(Boolean, default=True)
    
    car_model = relationship("CarModel", back_populates="model_features")
    feature = relationship("Feature", back_populates="model_features")

class CarModel(Base):
    """Main table for MG car models"""
    __tablename__ = 'car_models'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)  # e.g., 'MG ZS', 'MG HS'
    year = Column(Integer)
    generation = Column(String(30))
    body_type = Column(String(30))  # e.g., 'SUV', 'Sedan', 'Hatchback'
    price_range = Column(String(50))  # e.g., '20,000-25,000 USD'
    
    engine_spec = relationship("EngineSpec", back_populates="car_model", uselist=False)
    dimensions = relationship("Dimensions", back_populates="car_model", uselist=False)
    model_features = relationship("ModelFeature", back_populates="car_model")

# Database connection and session setup
def get_db_session():
    try:
        # Using PostgreSQL as the database management system
        engine = create_engine('postgresql://username:password@localhost:5432/mg_cars')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        return Session()
    except SQLAlchemyError as e:
        print(f"Database connection error: {e}")
        raise

# Example usage
if __name__ == "__main__":
    session = get_db_session()
    
    try:
        # Create a new car model
        new_model = CarModel(
            name="MG ZS EV",
            year=2023,
            generation="Second",
            body_type="SUV",
            price_range="30,000-35,000 USD"
        )
        
        # Add engine specs
        new_model.engine_spec = EngineSpec(
            engine_type="Electric",
            displacement=0,
            horsepower=154,
            torque=280,
            transmission="Automatic",
            fuel_type="Electric",
            fuel_economy=5.2  # km/kWh
        )
        
        # Add dimensions
        new_model.dimensions = Dimensions(
            length=4323,
            width=1809,
            height=1648,
            wheelbase=2585,
            weight=1532,
            trunk_capacity=470
        )
        
        session.add(new_model)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error occurred: {e}")
    finally:
        session.close()
```
