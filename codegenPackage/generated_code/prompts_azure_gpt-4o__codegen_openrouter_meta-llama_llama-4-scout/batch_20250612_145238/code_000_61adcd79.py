"""
Generated Code Metadata:
========================
Original URL: https://mmgroupnepal.com
Prompt: Write Python code to simulate the manufacturing process of PET bottles and jars, incorporating quality control checks as described by MM Group Nepal's focus on quality and on-time delivery.
Generated: DETERMINISTIC_61adcd799399900e
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import List

class ProductType(Enum):
    """ Enum for product types """
    PET_BOTTLE = 1
    PET_JAR = 2

class Product:
    """ Class representing a PET product """
    def __init__(self, product_type: ProductType, size: float, material: str):
        self.product_type = product_type
        self.size = size
        self.material = material
        self.is_defective = False

    def mark_as_defective(self):
        """ Mark the product as defective """
        self.is_defective = True

class QualityControlCheck:
    """ Class representing a quality control check """
    def __init__(self, check_name: str, pass_threshold: float):
        self.check_name = check_name
        self.pass_threshold = pass_threshold

    def perform_check(self, product: Product) -> bool:
        """ Perform the quality control check on a product """
        # Simulate the quality control check
        # For demonstration purposes, assume a random pass/fail outcome
        import random
        if random.random() < self.pass_threshold:
            return True
        else:
            product.mark_as_defective()
            return False

class ManufacturingLine:
    """ Class representing a manufacturing line """
    def __init__(self, product_type: ProductType, quality_control_checks: List[QualityControlCheck]):
        self.product_type = product_type
        self.quality_control_checks = quality_control_checks
        self.products = []

    def produce_product(self, size: float, material: str) -> Product:
        """ Produce a PET product """
        product = Product(self.product_type, size, material)
        self.products.append(product)
        return product

    def perform_quality_control(self, product: Product):
        """ Perform quality control checks on a product """
        for check in self.quality_control_checks:
            if not check.perform_check(product):
                print(f"Product {product.size} {product.product_type.name} failed {check.check_name} quality control check")

    def get_defective_products(self) -> List[Product]:
        """ Get a list of defective products """
        return [product for product in self.products if product.is_defective]

def main():
    # Define quality control checks
    checks = [
        QualityControlCheck("Weight Check", 0.9),
        QualityControlCheck("Material Check", 0.95),
        QualityControlCheck("Leak Check", 0.92)
    ]

    # Create a manufacturing line for PET bottles
    bottle_line = ManufacturingLine(ProductType.PET_BOTTLE, checks)

    # Produce PET bottles
    for _ in range(100):
        bottle = bottle_line.produce_product(1.0, "PET")
        bottle_line.perform_quality_control(bottle)

    # Get defective products
    defective_bottles = bottle_line.get_defective_products()
    print(f"Defective PET bottles: {len(defective_bottles)}")

    # Create a manufacturing line for PET jars
    jar_line = ManufacturingLine(ProductType.PET_JAR, checks)

    # Produce PET jars
    for _ in range(50):
        jar = jar_line.produce_product(2.0, "PET")
        jar_line.perform_quality_control(jar)

    # Get defective products
    defective_jars = jar_line.get_defective_products()
    print(f"Defective PET jars: {len(defective_jars)}")

if __name__ == "__main__":
    main()
```
