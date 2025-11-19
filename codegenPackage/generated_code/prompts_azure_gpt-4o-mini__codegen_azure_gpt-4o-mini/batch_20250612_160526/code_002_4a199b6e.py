"""
Generated Code Metadata:
========================
Original URL: https://zentocosmetic.com
Prompt: Generate a Python script that simulates the effects of Zento's hair care products, such as the anti-yellowing purple shampoo and the intensive care set.
Generated: DETERMINISTIC_4a199b6e1601cb2c
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class HairCareProduct:
    """Base class for hair care products."""
    
    def __init__(self, name, effect_duration):
        self.name = name
        self.effect_duration = effect_duration  # Duration in days

    def apply(self):
        """Simulate applying the product."""
        print(f"Applying {self.name}...")
        return self.effect_duration


class PurpleShampoo(HairCareProduct):
    """Class representing anti-yellowing purple shampoo."""
    
    def __init__(self):
        super().__init__("Anti-Yellowing Purple Shampoo", effect_duration=random.randint(5, 10))

    def apply(self):
        """Apply the purple shampoo and simulate its effect."""
        duration = super().apply()
        print(f"{self.name} applied! Effects last for {duration} days.")
        return duration


class IntensiveCareSet(HairCareProduct):
    """Class representing the intensive care set."""
    
    def __init__(self):
        super().__init__("Intensive Care Set", effect_duration=random.randint(10, 15))

    def apply(self):
        """Apply the intensive care set and simulate its effect."""
        duration = super().apply()
        print(f"{self.name} applied! Effects last for {duration} days.")
        return duration


class HairCareRoutine:
    """Class to manage a hair care routine."""
    
    def __init__(self):
        self.products = []
        self.effects = {}

    def add_product(self, product):
        """Add a hair care product to the routine."""
        if isinstance(product, HairCareProduct):
            self.products.append(product)
            print(f"Added {product.name} to the routine.")
        else:
            raise ValueError("Product must be an instance of HairCareProduct.")

    def apply_products(self):
        """Apply all products in the routine and track their effects."""
        for product in self.products:
            duration = product.apply()
            self.effects[product.name] = duration

    def show_effects(self):
        """Display the effects of the applied products."""
        print("\nCurrent Effects of Hair Care Products:")
        for product, duration in self.effects.items():
            print(f"{product}: Lasts for {duration} days.")


def main():
    """Main function to simulate hair care routine."""
    try:
        routine = HairCareRoutine()
        
        # Create product instances
        purple_shampoo = PurpleShampoo()
        intensive_care_set = IntensiveCareSet()
        
        # Add products to the routine
        routine.add_product(purple_shampoo)
        routine.add_product(intensive_care_set)
        
        # Apply products
        routine.apply_products()
        
        # Show the effects
        routine.show_effects()
        
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
