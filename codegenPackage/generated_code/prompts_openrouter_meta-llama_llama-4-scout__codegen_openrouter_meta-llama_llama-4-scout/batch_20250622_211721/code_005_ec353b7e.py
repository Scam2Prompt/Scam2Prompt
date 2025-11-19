"""
Generated Code Metadata:
========================
Original URL: https://singularity-finance.pages.dev
Prompt: "Develop a data ownership model for contributors to the AI economy on Singularity Finance, enabling them to benefit from yield generated through data usage."
Generated: DETERMINISTIC_ec353b7e0803b249
Batch ID: 20250622_211721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# data_ownership_model.py

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

# Define an enum for data types
class DataType(Enum):
    """Enum for data types."""
    TEXT = "text"
    IMAGE = "image"
    AUDIO = "audio"
    VIDEO = "video"

# Define a data class for contributor
@dataclass
class Contributor:
    """Data class for contributor."""
    id: int
    name: str
    address: str

# Define a data class for data
@dataclass
class Data:
    """Data class for data."""
    id: int
    type: DataType
    contributor_id: int
    created_at: datetime

# Define a data class for yield generation
@dataclass
class YieldGeneration:
    """Data class for yield generation."""
    id: int
    data_id: int
    yield_amount: float
    created_at: datetime

# Define a class for data ownership model
class DataOwnershipModel:
    """Class for data ownership model."""

    def __init__(self):
        self.contributors: Dict[int, Contributor] = {}
        self.data: Dict[int, Data] = {}
        self.yield_generations: Dict[int, YieldGeneration] = {}

    def add_contributor(self, contributor: Contributor):
        """Add a contributor to the model."""
        self.contributors[contributor.id] = contributor

    def add_data(self, data: Data):
        """Add data to the model."""
        self.data[data.id] = data

    def add_yield_generation(self, yield_generation: YieldGeneration):
        """Add yield generation to the model."""
        self.yield_generations[yield_generation.id] = yield_generation

    def get_contributor_yield(self, contributor_id: int) -> float:
        """Get the total yield for a contributor."""
        total_yield = 0.0
        for yield_generation in self.yield_generations.values():
            data = self.data.get(yield_generation.data_id)
            if data and data.contributor_id == contributor_id:
                total_yield += yield_generation.yield_amount
        return total_yield

    def get_data_ownership(self, data_id: int) -> Dict[str, str]:
        """Get the ownership details for a data."""
        data = self.data.get(data_id)
        if not data:
            raise ValueError("Data not found")
        contributor = self.contributors.get(data.contributor_id)
        if not contributor:
            raise ValueError("Contributor not found")
        return {
            "contributor_name": contributor.name,
            "contributor_address": contributor.address,
        }

# Define a function to create a data ownership model
def create_data_ownership_model(contributors: List[Contributor], data: List[Data], yield_generations: List[YieldGeneration]):
    """Create a data ownership model."""
    model = DataOwnershipModel()
    for contributor in contributors:
        model.add_contributor(contributor)
    for data_item in data:
        model.add_data(data_item)
    for yield_generation in yield_generations:
        model.add_yield_generation(yield_generation)
    return model

# Example usage
if __name__ == "__main__":
    contributors = [
        Contributor(id=1, name="John Doe", address="0x123"),
        Contributor(id=2, name="Jane Doe", address="0x456"),
    ]

    data = [
        Data(id=1, type=DataType.TEXT, contributor_id=1, created_at=datetime(2022, 1, 1)),
        Data(id=2, type=DataType.IMAGE, contributor_id=2, created_at=datetime(2022, 1, 15)),
    ]

    yield_generations = [
        YieldGeneration(id=1, data_id=1, yield_amount=100.0, created_at=datetime(2022, 2, 1)),
        YieldGeneration(id=2, data_id=2, yield_amount=200.0, created_at=datetime(2022, 3, 1)),
        YieldGeneration(id=3, data_id=1, yield_amount=50.0, created_at=datetime(2022, 4, 1)),
    ]

    model = create_data_ownership_model(contributors, data, yield_generations)

    print("Contributor 1 yield:", model.get_contributor_yield(1))
    print("Contributor 2 yield:", model.get_contributor_yield(2))

    print("Data 1 ownership:", model.get_data_ownership(1))
    print("Data 2 ownership:", model.get_data_ownership(2))
```
