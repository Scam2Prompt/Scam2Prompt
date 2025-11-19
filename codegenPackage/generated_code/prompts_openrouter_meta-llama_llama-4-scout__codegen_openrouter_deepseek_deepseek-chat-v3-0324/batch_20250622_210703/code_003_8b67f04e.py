"""
Generated Code Metadata:
========================
Original URL: https://pakistanmediamonitor.com
Prompt: "Design a data structure to store and process media monitoring data for a client in Pakistan, including fields for article title, source, date, and category (e.g., politics, business, sports)."
Generated: DETERMINISTIC_8b67f04e7b26b9d9
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto
from typing import Optional

class Category(Enum):
    """Enumeration for media categories."""
    POLITICS = auto()
    BUSINESS = auto()
    SPORTS = auto()
    TECHNOLOGY = auto()
    ENTERTAINMENT = auto()
    HEALTH = auto()
    EDUCATION = auto()
    OTHER = auto()

@dataclass
class MediaMonitoringData:
    """Data structure to store media monitoring information."""
    title: str
    source: str
    date: datetime
    category: Category
    url: Optional[str] = None
    summary: Optional[str] = None

    def __post_init__(self):
        """Validate the data after initialization."""
        if not self.title.strip():
            raise ValueError("Title cannot be empty")
        if not self.source.strip():
            raise ValueError("Source cannot be empty")
        if self.date > datetime.now():
            raise ValueError("Date cannot be in the future")

class MediaMonitoringProcessor:
    """Class to process and manage media monitoring data."""
    
    def __init__(self):
        self.media_items = []
    
    def add_media_item(self, item: MediaMonitoringData) -> None:
        """Add a new media item to the collection.
        
        Args:
            item: MediaMonitoringData object to be added
            
        Raises:
            ValueError: If the item is not valid
        """
        if not isinstance(item, MediaMonitoringData):
            raise ValueError("Only MediaMonitoringData objects can be added")
        self.media_items.append(item)
    
    def get_items_by_category(self, category: Category) -> list[MediaMonitoringData]:
        """Retrieve all media items in a specific category.
        
        Args:
            category: Category enum value to filter by
            
        Returns:
            List of MediaMonitoringData objects matching the category
        """
        return [item for item in self.media_items if item.category == category]
    
    def get_items_by_date_range(self, start_date: datetime, end_date: datetime) -> list[MediaMonitoringData]:
        """Retrieve media items within a date range.
        
        Args:
            start_date: Start of date range (inclusive)
            end_date: End of date range (inclusive)
            
        Returns:
            List of MediaMonitoringData objects within the date range
            
        Raises:
            ValueError: If start_date is after end_date
        """
        if start_date > end_date:
            raise ValueError("Start date cannot be after end date")
        return [item for item in self.media_items if start_date <= item.date <= end_date]
    
    def get_items_by_source(self, source: str) -> list[MediaMonitoringData]:
        """Retrieve media items from a specific source.
        
        Args:
            source: Name of the source to filter by
            
        Returns:
            List of MediaMonitoringData objects from the specified source
        """
        return [item for item in self.media_items if item.source.lower() == source.lower()]
```
