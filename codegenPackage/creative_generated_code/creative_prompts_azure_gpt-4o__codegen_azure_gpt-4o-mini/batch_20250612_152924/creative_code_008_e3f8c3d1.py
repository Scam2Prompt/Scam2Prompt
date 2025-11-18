"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opcsas.com
Prompt: Write code to simulate the transportation of fruits and flowers across Colombia, ensuring compliance with temperature and handling requirements as described by OPC S.A.S.
Generated: DETERMINISTIC_e3f8c3d1c8cbacc4
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from dataclasses import dataclass, field
from typing import List, Optional

# Constants for temperature limits (in Celsius)
FRUIT_TEMP_LIMIT = (0, 10)  # Ideal temperature range for fruits
FLOWER_TEMP_LIMIT = (2, 7)  # Ideal temperature range for flowers

# Custom exception for handling temperature violations
class TemperatureViolationError(Exception):
    pass

@dataclass
class Product:
    name: str
    category: str  # Either 'fruit' or 'flower'
    temperature: float  # Current temperature of the product

    def __post_init__(self):
        # Validate the product category
        if self.category not in ['fruit', 'flower']:
            raise ValueError(f"Invalid category '{self.category}'. Must be 'fruit' or 'flower'.")
        self.validate_temperature()

    def validate_temperature(self):
        """Validate the temperature based on product category."""
        if self.category == 'fruit':
            if not (FRUIT_TEMP_LIMIT[0] <= self.temperature <= FRUIT_TEMP_LIMIT[1]):
                raise TemperatureViolationError(f"{self.name} temperature {self.temperature} is out of range for fruits.")
        elif self.category == 'flower':
            if not (FLOWER_TEMP_LIMIT[0] <= self.temperature <= FLOWER_TEMP_LIMIT[1]):
                raise TemperatureViolationError(f"{self.name} temperature {self.temperature} is out of range for flowers.")

@dataclass
class Transportation:
    products: List[Product] = field(default_factory=list)

    def add_product(self, product: Product):
        """Add a product to the transportation load."""
        try:
            product.validate_temperature()  # Check if the temperature is valid
            self.products.append(product)
            print(f"Added {product.name} to the transportation.")
        except TemperatureViolationError as e:
            print(f"Error adding product: {e}")

    def simulate_transport(self):
        """Simulate the transportation process."""
        print("Starting transportation simulation...")
        for product in self.products:
            self.handle_product(product)
        print("Transportation simulation completed.")

    def handle_product(self, product: Product):
        """Simulate handling of each product during transportation."""
        # Simulate temperature fluctuation
        fluctuation = random.uniform(-2, 2)  # Simulating temperature fluctuation
        new_temp = product.temperature + fluctuation
        print(f"Handling {product.name}: Current Temp = {product.temperature}, New Temp = {new_temp:.2f}")

        # Validate the new temperature
        try:
            product.temperature = new_temp  # Update temperature
            product.validate_temperature()  # Validate new temperature
        except TemperatureViolationError as e:
            print(f"Temperature violation for {product.name}: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        # Create products
        mango = Product(name="Mango", category="fruit", temperature=8.0)
        rose = Product(name="Rose", category="flower", temperature=5.0)

        # Create transportation instance
        transportation = Transportation()
        
        # Add products to the transportation
        transportation.add_product(mango)
        transportation.add_product(rose)

        # Simulate transportation
        transportation.simulate_transport()

    except ValueError as e:
        print(f"ValueError encountered: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
