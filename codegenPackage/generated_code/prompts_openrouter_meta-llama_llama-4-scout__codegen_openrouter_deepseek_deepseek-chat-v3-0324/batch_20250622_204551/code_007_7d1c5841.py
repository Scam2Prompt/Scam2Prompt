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
from datetime import datetime
from typing import List, Optional
from enum import Enum
from pydantic import BaseModel, Field, validator
from pydantic.types import UUID4

class EventType(str, Enum):
    POLITICAL = "political"
    MILITARY = "military"
    CULTURAL = "cultural"
    RELIGIOUS = "religious"
    ECONOMIC = "economic"
    SCIENTIFIC = "scientific"
    OTHER = "other"

class FigureRole(str, Enum):
    LEADER = "leader"
    SCHOLAR = "scholar"
    ARTIST = "artist"
    SCIENTIST = "scientist"
    EXPLORER = "explorer"
    REVOLUTIONARY = "revolutionary"
    OTHER = "other"

class Location(BaseModel):
    id: UUID4
    name: str = Field(..., max_length=100)
    latitude: float
    longitude: float
    modern_country: str = Field(..., max_length=100)
    historical_names: List[str] = Field(default_factory=list)

class Figure(BaseModel):
    id: UUID4
    name: str = Field(..., max_length=100)
    birth_date: Optional[datetime] = None
    death_date: Optional[datetime] = None
    roles: List[FigureRole] = Field(default_factory=list)
    description: str = Field(..., max_length=2000)
    associated_locations: List[UUID4] = Field(default_factory=list)
    associated_events: List[UUID4] = Field(default_factory=list)
    
    @validator('death_date')
    def validate_dates(cls, v, values):
        if 'birth_date' in values and v and values['birth_date']:
            if v < values['birth_date']:
                raise ValueError('Death date must be after birth date')
        return v

class Event(BaseModel):
    id: UUID4
    title: str = Field(..., max_length=200)
    description: str = Field(..., max_length=5000)
    start_date: datetime
    end_date: Optional[datetime] = None
    event_type: EventType
    location: UUID4
    participants: List[UUID4] = Field(default_factory=list)
    related_events: List[UUID4] = Field(default_factory=list)
    sources: List[str] = Field(default_factory=list)
    
    @validator('end_date')
    def validate_dates(cls, v, values):
        if v and 'start_date' in values:
            if v < values['start_date']:
                raise ValueError('End date must be after start date')
        return v

class Era(BaseModel):
    id: UUID4
    name: str = Field(..., max_length=100)
    start_year: int
    end_year: int
    description: str = Field(..., max_length=2000)
    key_events: List[UUID4] = Field(default_factory=list)
    key_figures: List[UUID4] = Field(default_factory=list)
    
    @validator('end_year')
    def validate_years(cls, v, values):
        if 'start_year' in values and v < values['start_year']:
            raise ValueError('End year must be after start year')
        return v

class Source(BaseModel):
    id: UUID4
    title: str = Field(..., max_length=200)
    author: str = Field(..., max_length=100)
    publication_year: Optional[int] = None
    publisher: Optional[str] = Field(None, max_length=100)
    url: Optional[str] = None
    is_primary: bool = False
    referenced_in: List[UUID4] = Field(default_factory=list)

class HistoricalDatabase(BaseModel):
    events: List[Event] = Field(default_factory=list)
    figures: List[Figure] = Field(default_factory=list)
    locations: List[Location] = Field(default_factory=list)
    eras: List[Era] = Field(default_factory=list)
    sources: List[Source] = Field(default_factory=list)
```
