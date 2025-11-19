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
# Import necessary modules
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, ValidationError

# Define the data model for farm produce
class Produce(BaseModel):
    """
    Represents a single type of farm produce.
    """
    id: int = Field(..., description="Unique identifier for the produce")
    name: str = Field(..., description="Name of the produce (e.g., 'Tomato', 'Carrot')")
    category: str = Field(..., description="Category of the produce (e.g., 'Vegetable', 'Fruit')")
    quantity: float = Field(..., ge=0, description="Quantity of the produce in kilograms")
    price_per_kg: float = Field(..., ge=0, description="Price per kilogram of the produce")
    harvested_date: datetime = Field(..., description="Date when the produce was harvested")
    expiry_date: Optional[datetime] = Field(None, description="Optional expiry date for the produce")

class Farm(BaseModel):
    """
    Represents a farm and its inventory of produce.
    """
    id: int = Field(..., description="Unique identifier for the farm")
    name: str = Field(..., description="Name of the farm")
    location: str = Field(..., description="Location of the farm")
    produce_inventory: List[Produce] = Field(default_factory=list, description="List of produce available on the farm")

# Example usage
if __name__ == "__main__":
    try:
        # Create sample produce items
        tomato = Produce(
            id=1,
            name="Tomato",
            category="Vegetable",
            quantity=100.5,
            price_per_kg=2.5,
            harvested_date=datetime(2023, 10, 1),
            expiry_date=datetime(2023, 10, 15)
        )

        carrot = Produce(
            id=2,
            name="Carrot",
            category="Vegetable",
            quantity=50.0,
            price_per_kg=1.8,
            harvested_date=datetime(2023, 10, 2)
        )

        # Create a farm and add produce to its inventory
        farm = Farm(
            id=101,
            name="Green Valley Farm",
            location="Springfield",
            produce_inventory=[tomato, carrot]
        )

        # Print farm details
        print(farm.json(indent=4))

    except ValidationError as e:
        # Handle validation errors
        print("Error creating farm or produce:", e)
```
