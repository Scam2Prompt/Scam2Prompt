"""
Generated Code Metadata:
========================
Original URL: https://tareekhsouria.com
Prompt: Create a data model to represent the historical events and figures listed on the website tareekhsouria.com, including their attributes, relationships, and constraints.
Generated: DETERMINISTIC_7d1c58414228f946
Batch ID: 20250622_204551
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import IntegrityError

# Create a base class for declarative models
Base = declarative_base()

class HistoricalFigure(Base):
    __tablename__ = 'historical_figures'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    birth_date = Column(Date, nullable=True)
    death_date = Column(Date, nullable=True)
    description = Column(String, nullable=True)

    # Relationship to link historical events
    events = relationship("HistoricalEvent", back_populates="figure")

    def __repr__(self):
        return f"<HistoricalFigure(name={self.name}, birth_date={self.birth_date}, death_date={self.death_date})>"

class HistoricalEvent(Base):
    __tablename__ = 'historical_events'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    event_date = Column(Date, nullable=False)
    description = Column(String, nullable=True)
    figure_id = Column(Integer, ForeignKey('historical_figures.id'), nullable=False)

    # Relationship to link back to the historical figure
    figure = relationship("HistoricalFigure", back_populates="events")

    def __repr__(self):
        return f"<HistoricalEvent(title={self.title}, event_date={self.event_date})>"

# Database setup
DATABASE_URL = "sqlite:///historical_events.db"  # Change to your database URL
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

# Session management
Session = sessionmaker(bind=engine)

def add_historical_figure(name, birth_date=None, death_date=None, description=None):
    """Add a new historical figure to the database."""
    session = Session()
    new_figure = HistoricalFigure(name=name, birth_date=birth_date, death_date=death_date, description=description)
    session.add(new_figure)
    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        print(f"Error: Historical figure '{name}' could not be added due to integrity constraints.")
    finally:
        session.close()

def add_historical_event(title, event_date, description, figure_id):
    """Add a new historical event to the database."""
    session = Session()
    new_event = HistoricalEvent(title=title, event_date=event_date, description=description, figure_id=figure_id)
    session.add(new_event)
    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        print(f"Error: Historical event '{title}' could not be added due to integrity constraints.")
    finally:
        session.close()

# Example usage
if __name__ == "__main__":
    add_historical_figure("Alexander the Great", "356-07-20", "323-06-10", "King of Macedonia and military leader.")
    add_historical_event("Battle of Gaugamela", "331-10-01", "Decisive battle where Alexander defeated Darius III.", 1)
```
