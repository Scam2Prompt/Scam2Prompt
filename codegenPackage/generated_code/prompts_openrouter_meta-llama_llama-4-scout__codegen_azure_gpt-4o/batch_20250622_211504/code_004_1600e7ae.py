"""
Generated Code Metadata:
========================
Original URL: https://aktivrorteknikk.no
Prompt: Create a data model for storing and analyzing data from smoke testing of pipe networks, including information about pipe layout, smoke injection points, and detection results.
Generated: DETERMINISTIC_1600e7aebd00bf7c
Batch ID: 20250622_211504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import datetime

# Base class for SQLAlchemy models
Base = declarative_base()

# Data model for Pipe
class Pipe(Base):
    __tablename__ = 'pipes'
    
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for each pipe
    name = Column(String, nullable=False)  # Name or identifier for the pipe
    length = Column(Float, nullable=False)  # Length of the pipe in meters
    diameter = Column(Float, nullable=False)  # Diameter of the pipe in meters
    material = Column(String, nullable=False)  # Material of the pipe (e.g., PVC, steel)
    
    # Relationship to PipeLayout
    layout_id = Column(Integer, ForeignKey('pipe_layouts.id'), nullable=False)
    layout = relationship("PipeLayout", back_populates="pipes")

# Data model for Pipe Layout
class PipeLayout(Base):
    __tablename__ = 'pipe_layouts'
    
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for each layout
    name = Column(String, nullable=False)  # Name or identifier for the layout
    description = Column(String)  # Optional description of the layout
    
    # Relationship to Pipe
    pipes = relationship("Pipe", back_populates="layout")

# Data model for Smoke Injection Point
class SmokeInjectionPoint(Base):
    __tablename__ = 'smoke_injection_points'
    
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for each injection point
    location = Column(String, nullable=False)  # Location description of the injection point
    injection_time = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)  # Time of smoke injection
    
    # Relationship to Pipe Layout
    layout_id = Column(Integer, ForeignKey('pipe_layouts.id'), nullable=False)
    layout = relationship("PipeLayout")

# Data model for Detection Results
class DetectionResult(Base):
    __tablename__ = 'detection_results'
    
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for each detection result
    detection_time = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)  # Time of detection
    detected = Column(Boolean, nullable=False)  # Whether smoke was detected (True/False)
    detection_location = Column(String, nullable=False)  # Location where smoke was detected
    intensity = Column(Float)  # Intensity of smoke detected (optional)
    
    # Relationship to Smoke Injection Point
    injection_point_id = Column(Integer, ForeignKey('smoke_injection_points.id'), nullable=False)
    injection_point = relationship("SmokeInjectionPoint")

# Database setup
def setup_database(database_url='sqlite:///pipe_network.db'):
    """
    Sets up the database connection and creates tables if they don't exist.
    
    :param database_url: URL for the database connection (default: SQLite file-based database)
    """
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)

# Example usage
if __name__ == "__main__":
    # Initialize database session
    Session = setup_database()
    session = Session()
    
    try:
        # Example: Add a pipe layout
        layout = PipeLayout(name="Main Network", description="Primary pipe network for the city")
        session.add(layout)
        session.commit()
        
        # Example: Add a pipe to the layout
        pipe = Pipe(name="Pipe A", length=100.0, diameter=0.5, material="PVC", layout_id=layout.id)
        session.add(pipe)
        session.commit()
        
        # Example: Add a smoke injection point
        injection_point = SmokeInjectionPoint(location="North End", layout_id=layout.id)
        session.add(injection_point)
        session.commit()
        
        # Example: Add a detection result
        detection_result = DetectionResult(detection_time=datetime.datetime.utcnow(), detected=True, 
                                           detection_location="South End", intensity=0.8, 
                                           injection_point_id=injection_point.id)
        session.add(detection_result)
        session.commit()
        
        print("Data added successfully!")
    except Exception as e:
        # Handle errors during database operations
        print(f"An error occurred: {e}")
        session.rollback()
    finally:
        # Close the session
        session.close()
```
