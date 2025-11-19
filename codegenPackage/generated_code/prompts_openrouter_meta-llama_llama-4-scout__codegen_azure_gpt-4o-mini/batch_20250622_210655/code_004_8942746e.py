"""
Generated Code Metadata:
========================
Original URL: https://sunrisecomputers.pk
Prompt: "Generate a Python script to compare the specifications of HP Pavilion 14 x 360 and Hp Elite Dragonfly Folio."
Generated: DETERMINISTIC_8942746ee19f732b
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class Laptop:
    """Class to represent a laptop with specifications."""
    
    def __init__(self, brand, model, processor, ram, storage, display, weight):
        """
        Initialize a Laptop instance.

        :param brand: Brand of the laptop
        :param model: Model of the laptop
        :param processor: Processor specifications
        :param ram: RAM specifications
        :param storage: Storage specifications
        :param display: Display specifications
        :param weight: Weight of the laptop
        """
        self.brand = brand
        self.model = model
        self.processor = processor
        self.ram = ram
        self.storage = storage
        self.display = display
        self.weight = weight

    def to_dict(self):
        """Convert the laptop specifications to a dictionary."""
        return {
            "Brand": self.brand,
            "Model": self.model,
            "Processor": self.processor,
            "RAM": self.ram,
            "Storage": self.storage,
            "Display": self.display,
            "Weight": self.weight
        }

def compare_laptops(laptop1, laptop2):
    """Compare two laptops and print their specifications side by side."""
    print(f"{'Specification':<15} {'Laptop 1':<30} {'Laptop 2':<30}")
    print("=" * 75)
    
    for key in laptop1.to_dict().keys():
        print(f"{key:<15} {laptop1.to_dict()[key]:<30} {laptop2.to_dict()[key]:<30}")

def main():
    """Main function to create laptop instances and compare them."""
    try:
        # Specifications for HP Pavilion 14 x 360
        hp_pavilion = Laptop(
            brand="HP",
            model="Pavilion 14 x 360",
            processor="Intel Core i5-1135G7",
            ram="8GB DDR4",
            storage="512GB SSD",
            display="14-inch FHD (1920 x 1080)",
            weight="3.5 lbs"
        )

        # Specifications for HP Elite Dragonfly Folio
        hp_elite_dragonfly = Laptop(
            brand="HP",
            model="Elite Dragonfly Folio",
            processor="Intel Core i7-8665U",
            ram="16GB LPDDR3",
            storage="1TB SSD",
            display="13.3-inch FHD (1920 x 1080)",
            weight="2.2 lbs"
        )

        # Compare the two laptops
        compare_laptops(hp_pavilion, hp_elite_dragonfly)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
