"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftimus.com
Prompt: Write a script to automate the calculation of container loading capacity for exporting Himalayan salt cooking plates and tiles, based on dimensions and weight.
Generated: DETERMINISTIC_b32d5e4cd655e627
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class Container:
    """Class to represent a shipping container."""

    def __init__(self, length: float, width: float, height: float, max_weight: float):
        """
        Initialize a Container object.
        
        :param length: Length of the container in meters.
        :param width: Width of the container in meters.
        :param height: Height of the container in meters.
        :param max_weight: Maximum weight the container can carry in kilograms.
        """
        self.length = length
        self.width = width
        self.height = height
        self.max_weight = max_weight

    def volume(self) -> float:
        """Calculate the volume of the container in cubic meters."""
        return self.length * self.width * self.height


class SaltProduct:
    """Class to represent a Himalayan salt cooking plate or tile."""

    def __init__(self, length: float, width: float, thickness: float, weight: float):
        """
        Initialize a SaltProduct object.
        
        :param length: Length of the product in meters.
        :param width: Width of the product in meters.
        :param thickness: Thickness of the product in meters.
        :param weight: Weight of the product in kilograms.
        """
        self.length = length
        self.width = width
        self.thickness = thickness
        self.weight = weight

    def volume(self) -> float:
        """Calculate the volume of the salt product in cubic meters."""
        return self.length * self.width * self.thickness


def calculate_loading_capacity(container: Container, salt_product: SaltProduct) -> dict:
    """
    Calculate the loading capacity of a container for salt products.
    
    :param container: Container object.
    :param salt_product: SaltProduct object.
    :return: A dictionary with the maximum number of products that can fit in the container 
             and the total weight.
    """
    try:
        # Calculate the volume of the container and the salt product
        container_volume = container.volume()
        product_volume = salt_product.volume()

        # Calculate how many products can fit in the container based on volume
        max_by_volume = math.floor(container_volume / product_volume)

        # Calculate how many products can fit based on weight
        max_by_weight = math.floor(container.max_weight / salt_product.weight)

        # Determine the limiting factor
        max_products = min(max_by_volume, max_by_weight)

        # Calculate the total weight of the maximum number of products
        total_weight = max_products * salt_product.weight

        return {
            "max_products": max_products,
            "total_weight": total_weight,
        }

    except ZeroDivisionError as e:
        print("Error: Division by zero occurred. Check the weight of the salt product.")
        return {"max_products": 0, "total_weight": 0}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"max_products": 0, "total_weight": 0}


if __name__ == "__main__":
    # Example usage
    try:
        # Create a container with given dimensions and max weight
        shipping_container = Container(length=2.4, width=2.0, height=2.0, max_weight=2800)

        # Create a salt product (cooking plate or tile) with given dimensions and weight
        salt_plate = SaltProduct(length=0.3, width=0.2, thickness=0.05, weight=2.0)

        # Calculate loading capacity
        result = calculate_loading_capacity(shipping_container, salt_plate)

        # Display the results
        print(f"Max number of products: {result['max_products']}")
        print(f"Total weight: {result['total_weight']} kg")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
