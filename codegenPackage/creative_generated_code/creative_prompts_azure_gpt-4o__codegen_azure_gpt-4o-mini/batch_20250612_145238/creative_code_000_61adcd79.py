"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mmgroupnepal.com
Prompt: Write Python code to simulate the manufacturing process of PET bottles and jars, incorporating quality control checks as described by MM Group Nepal's focus on quality and on-time delivery.
Generated: DETERMINISTIC_61adcd799399900e
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
from typing import List, Tuple

class BottleJar:
    """Class representing a PET bottle or jar."""

    def __init__(self, product_type: str):
        if product_type not in ['bottle', 'jar']:
            raise ValueError("Product type must be either 'bottle' or 'jar'.")
        self.product_type = product_type
        self.quality_check_passed = False

    def perform_quality_check(self) -> bool:
        """Simulates a quality check on the product."""
        # Simulate quality check with a random pass/fail outcome
        self.quality_check_passed = random.choice([True, False])
        return self.quality_check_passed

    def __str__(self) -> str:
        """String representation of the product."""
        status = "Passed" if self.quality_check_passed else "Failed"
        return f"{self.product_type.capitalize()} - Quality Check: {status}"

class ManufacturingProcess:
    """Class to simulate the manufacturing process of PET bottles and jars."""

    def __init__(self, production_capacity: int):
        self.production_capacity = production_capacity
        self.products: List[BottleJar] = []  # List to hold produced products

    def manufacture_products(self) -> None:
        """Manufactures a specified number of products."""
        print("Starting manufacturing process...")
        for _ in range(self.production_capacity):
            product_type = random.choice(['bottle', 'jar'])
            product = BottleJar(product_type)
            self.products.append(product)
            print(f"Manufactured: {product}")

            # Perform quality check
            if not product.perform_quality_check():
                print(f"Quality check failed for {product}. Discarding product.")
            else:
                print(f"Quality check passed for {product}. Product is ready for delivery.")
            
            # Simulate processing time
            time.sleep(0.1)  # Represents time taken to manufacture each product

        print("Manufacturing process completed.")

    def get_summary(self) -> Tuple[int, int]:
        """Returns a summary of manufactured products."""
        total_products = len(self.products)
        passed_quality_checks = sum(product.quality_check_passed for product in self.products)

        return total_products, passed_quality_checks

def main():
    """Main function to run the manufacturing simulation."""
    try:
        production_capacity = int(input("Enter the number of products to manufacture: "))
        if production_capacity <= 0:
            raise ValueError("Production capacity must be a positive integer.")
        
        manufacturing_process = ManufacturingProcess(production_capacity)
        manufacturing_process.manufacture_products()
        
        total, passed = manufacturing_process.get_summary()
        print(f"\nSummary: Total Products Manufactured: {total}, Passed Quality Checks: {passed}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
