"""
Generated Code Metadata:
========================
Original URL: https://metamask.raymasterbatch.com
Prompt: "Create a data structure to store information about masterbatch products, including their chemical composition, applications, and market segments."
Generated: DETERMINISTIC_a3140758abbc0b95
Batch ID: 20250622_212010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum
from typing import List, Dict

class MarketSegment(Enum):
    """Market segments for masterbatch products"""
    PACKAGING = "Packaging"
    AUTOMOTIVE = "Automotive"
    ELECTRICAL = "Electrical"
    CONSTRUCTION = "Construction"
    OTHER = "Other"

@dataclass
class ChemicalComposition:
    """Chemical composition of a masterbatch product"""
    base_resin: str
    additives: List[str]
    pigments: List[str]

@dataclass
class Application:
    """Application of a masterbatch product"""
    industry: str
    product_type: str

class MasterbatchProduct:
    """Data structure to store information about masterbatch products"""

    def __init__(self, 
                 product_id: str, 
                 product_name: str, 
                 chemical_composition: ChemicalComposition, 
                 applications: List[Application], 
                 market_segments: List[MarketSegment]):
        """
        Initialize a MasterbatchProduct object.

        Args:
        - product_id (str): Unique ID of the product
        - product_name (str): Name of the product
        - chemical_composition (ChemicalComposition): Chemical composition of the product
        - applications (List[Application]): List of applications of the product
        - market_segments (List[MarketSegment]): List of market segments of the product
        """
        self.product_id = product_id
        self.product_name = product_name
        self.chemical_composition = chemical_composition
        self.applications = applications
        self.market_segments = market_segments

    def __str__(self):
        return f"MasterbatchProduct(product_id={self.product_id}, product_name={self.product_name})"

    def to_dict(self) -> Dict:
        """Convert the MasterbatchProduct object to a dictionary"""
        return {
            "product_id": self.product_id,
            "product_name": self.product_name,
            "chemical_composition": {
                "base_resin": self.chemical_composition.base_resin,
                "additives": self.chemical_composition.additives,
                "pigments": self.chemical_composition.pigments
            },
            "applications": [
                {"industry": app.industry, "product_type": app.product_type} 
                for app in self.applications
            ],
            "market_segments": [seg.value for seg in self.market_segments]
        }

class MasterbatchProductDatabase:
    """Database to store masterbatch products"""

    def __init__(self):
        self.products = {}

    def add_product(self, product: MasterbatchProduct):
        """Add a masterbatch product to the database"""
        self.products[product.product_id] = product

    def get_product(self, product_id: str) -> MasterbatchProduct:
        """Get a masterbatch product from the database"""
        try:
            return self.products[product_id]
        except KeyError:
            raise ValueError(f"Product with ID {product_id} not found")

    def update_product(self, product_id: str, product: MasterbatchProduct):
        """Update a masterbatch product in the database"""
        if product_id in self.products:
            self.products[product_id] = product
        else:
            raise ValueError(f"Product with ID {product_id} not found")

    def delete_product(self, product_id: str):
        """Delete a masterbatch product from the database"""
        if product_id in self.products:
            del self.products[product_id]
        else:
            raise ValueError(f"Product with ID {product_id} not found")

# Example usage
if __name__ == "__main__":
    db = MasterbatchProductDatabase()

    composition = ChemicalComposition(
        base_resin="Polyethylene",
        additives=["UV stabilizer", "Antioxidant"],
        pigments=["Carbon Black"]
    )

    applications = [
        Application(industry="Packaging", product_type="Bottles"),
        Application(industry="Packaging", product_type="Containers")
    ]

    market_segments = [MarketSegment.PACKAGING, MarketSegment.AUTOMOTIVE]

    product = MasterbatchProduct(
        product_id="MB001",
        product_name="Black Masterbatch",
        chemical_composition=composition,
        applications=applications,
        market_segments=market_segments
    )

    db.add_product(product)

    print(db.get_product("MB001").to_dict())
```
