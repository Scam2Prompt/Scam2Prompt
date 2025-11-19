"""
Generated Code Metadata:
========================
Original URL: https://trattar.blogspot.com
Prompt: "Write a Python code to manage inventory of eucalyptus and pine wood products for a company like Trattar Madeiras that uses vacuum/pressure treatment with hydro-soluble CCA agents."
Generated: DETERMINISTIC_07a88d38691ec107
Batch ID: 20250622_211758
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from enum import Enum
import os


class WoodType(Enum):
    """Enumeration for types of wood products."""
    EUCALYPTUS = "Eucalyptus"
    PINE = "Pine"


class TreatmentType(Enum):
    """Enumeration for treatment types."""
    VACUUM = "Vacuum"
    PRESSURE = "Pressure"


class Product:
    """Class representing a wood product."""

    def __init__(
        self,
        product_id: str,
        wood_type: WoodType,
        treatment_type: TreatmentType,
        quantity: int,
        dimensions: str,
        cca_concentration: float,
    ):
        """Initialize a Product instance.

        Args:
            product_id: Unique identifier for the product.
            wood_type: Type of wood (Eucalyptus or Pine).
            treatment_type: Treatment method (Vacuum or Pressure).
            quantity: Number of units in stock.
            dimensions: Physical dimensions of the product.
            cca_concentration: Concentration of CCA agent (in %).
        """
        self.product_id = product_id
        self.wood_type = wood_type
        self.treatment_type = treatment_type
        self.quantity = quantity
        self.dimensions = dimensions
        self.cca_concentration = cca_concentration

    def to_dict(self) -> Dict:
        """Convert the Product object to a dictionary.

        Returns:
            Dictionary representation of the Product.
        """
        return {
            "product_id": self.product_id,
            "wood_type": self.wood_type.value,
            "treatment_type": self.treatment_type.value,
            "quantity": self.quantity,
            "dimensions": self.dimensions,
            "cca_concentration": self.cca_concentration,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Product':
        """Create a Product object from a dictionary.

        Args:
            data: Dictionary containing product data.

        Returns:
            Product object.
        """
        return cls(
            product_id=data["product_id"],
            wood_type=WoodType(data["wood_type"]),
            treatment_type=TreatmentType(data["treatment_type"]),
            quantity=data["quantity"],
            dimensions=data["dimensions"],
            cca_concentration=data["cca_concentration"],
        )


class InventoryManager:
    """Class to manage inventory of wood products."""

    def __init__(self, file_path: str = "inventory.json"):
        """Initialize the InventoryManager.

        Args:
            file_path: Path to the JSON file storing inventory data.
        """
        self.file_path = file_path
        self.products: Dict[str, Product] = {}
        self._load_inventory()

    def _load_inventory(self) -> None:
        """Load inventory data from the JSON file."""
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, "r") as file:
                    data = json.load(file)
                    self.products = {
                        product_id: Product.from_dict(product_data)
                        for product_id, product_data in data.items()
                    }
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading inventory: {e}")
            self.products = {}

    def _save_inventory(self) -> None:
        """Save inventory data to the JSON file."""
        try:
            with open(self.file_path, "w") as file:
                json.dump(
                    {product_id: product.to_dict() for product_id, product in self.products.items()},
                    file,
                    indent=4,
                )
        except IOError as e:
            print(f"Error saving inventory: {e}")

    def add_product(self, product: Product) -> None:
        """Add a new product to the inventory.

        Args:
            product: Product object to add.
        """
        if product.product_id in self.products:
            raise ValueError(f"Product with ID {product.product_id} already exists.")
        self.products[product.product_id] = product
        self._save_inventory()

    def update_product(self, product_id: str, quantity: Optional[int] = None, **kwargs) -> None:
        """Update an existing product's details.

        Args:
            product_id: ID of the product to update.
            quantity: New quantity (optional).
            **kwargs: Other product attributes to update.
        """
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found.")

        product = self.products[product_id]
        if quantity is not None:
            product.quantity = quantity

        for key, value in kwargs.items():
            if hasattr(product, key):
                setattr(product, key, value)

        self._save_inventory()

    def remove_product(self, product_id: str) -> None:
        """Remove a product from the inventory.

        Args:
            product_id: ID of the product to remove.
        """
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found.")
        del self.products[product_id]
        self._save_inventory()

    def get_product(self, product_id: str) -> Product:
        """Retrieve a product by ID.

        Args:
            product_id: ID of the product to retrieve.

        Returns:
            The requested Product object.
        """
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found.")
        return self.products[product_id]

    def list_products(self) -> List[Product]:
        """List all products in the inventory.

        Returns:
            List of Product objects.
        """
        return list(self.products.values())

    def filter_products(
        self,
        wood_type: Optional[WoodType] = None,
        treatment_type: Optional[TreatmentType] = None,
        min_quantity: Optional[int] = None,
    ) -> List[Product]:
        """Filter products based on criteria.

        Args:
            wood_type: Filter by wood type.
            treatment_type: Filter by treatment type.
            min_quantity: Filter by minimum quantity.

        Returns:
            List of filtered Product objects.
        """
        filtered = self.products.values()
        if wood_type:
            filtered = [p for p in filtered if p.wood_type == wood_type]
        if treatment_type:
            filtered = [p for p in filtered if p.treatment_type == treatment_type]
        if min_quantity is not None:
            filtered = [p for p in filtered if p.quantity >= min_quantity]
        return filtered


# Example usage
if __name__ == "__main__":
    inventory = InventoryManager()

    # Add sample products
    try:
        inventory.add_product(
            Product(
                product_id="EUC001",
                wood_type=WoodType.EUCALYPTUS,
                treatment_type=TreatmentType.VACUUM,
                quantity=100,
                dimensions="2x4x8",
                cca_concentration=2.5,
            )
        )
        inventory.add_product(
            Product(
                product_id="PIN001",
                wood_type=WoodType.PINE,
                treatment_type=TreatmentType.PRESSURE,
                quantity=150,
                dimensions="4x4x8",
                cca_concentration=3.0,
            )
        )
    except ValueError as e:
        print(f"Error adding product: {e}")

    # List all products
    print("All Products:")
    for product in inventory.list_products():
        print(product.to_dict())

    # Filter products
    print("\nEucalyptus Products:")
    for product in inventory.filter_products(wood_type=WoodType.EUCALYPTUS):
        print(product.to_dict())

    # Update a product
    try:
        inventory.update_product("EUC001", quantity=90)
    except ValueError as e:
        print(f"Error updating product: {e}")

    # Remove a product
    try:
        inventory.remove_product("PIN001")
    except ValueError as e:
        print(f"Error removing product: {e}")
```
