"""
Generated Code Metadata:
========================
Original URL: https://krosmetal.com
Prompt: "Design a data structure to store information about stainless steel products, including their types (e.g., profiles, sheets, fittings), dimensions, and applications."
Generated: DETERMINISTIC_ffbee32947fd7a0d
Batch ID: 20250622_211159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from dataclasses import dataclass
from typing import List

class ProductType(str, Enum):
    """Enum for stainless steel product types."""
    PROFILE = "profile"
    SHEET = "sheet"
    FITTING = "fitting"

@dataclass
class Dimension:
    """Class to store dimension information."""
    length: float
    width: float
    thickness: float
    unit: str = "mm"

@dataclass
class Application:
    """Class to store application information."""
    industry: str
    description: str

@dataclass
class StainlessSteelProduct:
    """Class to store information about stainless steel products."""
    product_type: ProductType
    name: str
    dimensions: List[Dimension]
    applications: List[Application]

    def __post_init__(self):
        """Validate product type and dimensions."""
        if not isinstance(self.product_type, ProductType):
            raise ValueError("Invalid product type")
        if not all(isinstance(d, Dimension) for d in self.dimensions):
            raise ValueError("Invalid dimension")
        if not all(isinstance(a, Application) for a in self.applications):
            raise ValueError("Invalid application")

class StainlessSteelProductDatabase:
    """Class to store and manage stainless steel products."""
    def __init__(self):
        self.products = []

    def add_product(self, product: StainlessSteelProduct):
        """Add a product to the database."""
        self.products.append(product)

    def get_products_by_type(self, product_type: ProductType):
        """Get products by type."""
        return [p for p in self.products if p.product_type == product_type]

    def get_product(self, name: str):
        """Get a product by name."""
        for p in self.products:
            if p.name == name:
                return p
        return None

def main():
    # Create a product database
    db = StainlessSteelProductDatabase()

    # Create dimensions
    profile_dim1 = Dimension(1000, 10, 5)
    profile_dim2 = Dimension(2000, 15, 8)

    sheet_dim1 = Dimension(1000, 2000, 2)

    fitting_dim1 = Dimension(10, 10, 5)

    # Create applications
    profile_app1 = Application("Construction", "Building frames")
    profile_app2 = Application("Industrial", "Machinery")

    sheet_app1 = Application("Architecture", "Building facade")

    fitting_app1 = Application("Industrial", "Piping systems")

    # Create products
    profile_product = StainlessSteelProduct(
        ProductType.PROFILE,
        "Stainless Steel Profile",
        [profile_dim1, profile_dim2],
        [profile_app1, profile_app2]
    )

    sheet_product = StainlessSteelProduct(
        ProductType.SHEET,
        "Stainless Steel Sheet",
        [sheet_dim1],
        [sheet_app1]
    )

    fitting_product = StainlessSteelProduct(
        ProductType.FITTING,
        "Stainless Steel Fitting",
        [fitting_dim1],
        [fitting_app1]
    )

    # Add products to database
    db.add_product(profile_product)
    db.add_product(sheet_product)
    db.add_product(fitting_product)

    # Get products by type
    profiles = db.get_products_by_type(ProductType.PROFILE)
    for profile in profiles:
        print(f"Product: {profile.name}")
        for dim in profile.dimensions:
            print(f"Dimension: {dim.length} x {dim.width} x {dim.thickness} {dim.unit}")
        for app in profile.applications:
            print(f"Application: {app.industry} - {app.description}")

if __name__ == "__main__":
    main()
```
