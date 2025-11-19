"""
Generated Code Metadata:
========================
Original URL: https://opcsas.com
Prompt: Write code to simulate the transportation of fruits and flowers across Colombia, ensuring compliance with temperature and handling requirements as described by OPC S.A.S.
Generated: DETERMINISTIC_e3f8c3d1c8cbacc4
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from dataclasses import dataclass
from typing import List, Optional

# Constants for temperature limits (in Celsius)
FRUIT_TEMP_LIMIT = (0, 10)  # Fruits should be kept between 0 and 10 degrees
FLOWER_TEMP_LIMIT = (2, 7)   # Flowers should be kept between 2 and 7 degrees

@dataclass
class Product:
    """Class representing a product to be transported."""
    name: str
    product_type: str  # 'fruit' or 'flower'
    temperature: float  # Current temperature of the product

    def is_within_temperature_limits(self) -> bool:
        """Check if the product's temperature is within the required limits."""
        if self.product_type == 'fruit':
            return FRUIT_TEMP_LIMIT[0] <= self.temperature <= FRUIT_TEMP_LIMIT[1]
        elif self.product_type == 'flower':
            return FLOWER_TEMP_LIMIT[0] <= self.temperature <= FLOWER_TEMP_LIMIT[1]
        else:
            raise ValueError("Invalid product type. Must be 'fruit' or 'flower'.")

class Transport:
    """Class representing a transport vehicle."""
    def __init__(self, vehicle_id: str):
        self.vehicle_id = vehicle_id
        self.products: List[Product] = []

    def load_product(self, product: Product) -> None:
        """Load a product onto the transport vehicle."""
        if product.is_within_temperature_limits():
            self.products.append(product)
            print(f"Loaded {product.name} onto vehicle {self.vehicle_id}.")
        else:
            raise ValueError(f"Cannot load {product.name}: temperature {product.temperature}°C is out of range.")

    def transport(self) -> None:
        """Simulate the transportation of products."""
        print(f"Transporting products in vehicle {self.vehicle_id}...")
        for product in self.products:
            print(f"Transporting {product.name} at {product.temperature}°C.")
        print("Transportation completed.")

def generate_random_temperature(product_type: str) -> float:
    """Generate a random temperature within the limits for the given product type."""
    if product_type == 'fruit':
        return random.uniform(*FRUIT_TEMP_LIMIT)
    elif product_type == 'flower':
        return random.uniform(*FLOWER_TEMP_LIMIT)
    else:
        raise ValueError("Invalid product type. Must be 'fruit' or 'flower'.")

def main() -> None:
    """Main function to simulate the transportation of fruits and flowers."""
    # Create a transport vehicle
    transport_vehicle = Transport(vehicle_id="TRK-001")

    # Simulate loading products
    products_to_load = [
        Product(name="Banana", product_type="fruit", temperature=generate_random_temperature('fruit')),
        Product(name="Rose", product_type="flower", temperature=generate_random_temperature('flower')),
        Product(name="Apple", product_type="fruit", temperature=generate_random_temperature('fruit')),
        Product(name="Tulip", product_type="flower", temperature=generate_random_temperature('flower')),
    ]

    # Load products onto the transport vehicle
    for product in products_to_load:
        try:
            transport_vehicle.load_product(product)
        except ValueError as e:
            print(e)

    # Transport the loaded products
    transport_vehicle.transport()

if __name__ == "__main__":
    main()
```
