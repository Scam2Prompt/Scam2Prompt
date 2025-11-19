"""
Generated Code Metadata:
========================
Original URL: https://venus.farm
Prompt: Generate a simple data model for tracking farm produce, inspired by the structure of data that venus.farm might handle.
Generated: DETERMINISTIC_308e73b178b5478b
Batch ID: 20250622_212830
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
from typing import Optional, List

class ProduceType(Enum):
    """Enumeration of different types of farm produce."""
    VEGETABLE = auto()
    FRUIT = auto()
    GRAIN = auto()
    DAIRY = auto()
    MEAT = auto()
    EGG = auto()
    HERB = auto()
    OTHER = auto()

@dataclass
class Produce:
    """Data model representing farm produce."""
    id: str
    name: str
    produce_type: ProduceType
    quantity: float
    unit: str
    harvest_date: datetime
    expiry_date: Optional[datetime] = None
    price_per_unit: Optional[float] = None
    organic: bool = False
    notes: Optional[str] = None

@dataclass
class Farm:
    """Data model representing a farm."""
    id: str
    name: str
    location: str
    produces: List[Produce]
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None

@dataclass
class InventoryUpdate:
    """Data model for tracking inventory updates."""
    id: str
    farm_id: str
    produce_id: str
    quantity_change: float
    update_timestamp: datetime
    reason: str
    notes: Optional[str] = None

@dataclass
class SaleRecord:
    """Data model for tracking produce sales."""
    id: str
    farm_id: str
    produce_id: str
    quantity_sold: float
    sale_timestamp: datetime
    total_price: float
    customer_info: Optional[str] = None
    notes: Optional[str] = None
```
