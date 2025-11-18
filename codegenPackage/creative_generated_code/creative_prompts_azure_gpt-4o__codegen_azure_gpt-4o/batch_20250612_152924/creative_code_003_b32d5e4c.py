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

class ContainerLoadingCalculator:
    """
    This class calculates the loading capacity of a container for Himalayan salt plates and tiles,
    based on their dimensions, weight, and the container's capacity.
    """

    def __init__(self, container_length, container_width, container_height, container_max_weight):
        """
        Initializes the container specifications.

        :param container_length: Length of the container in meters
        :param container_width: Width of the container in meters
        :param container_height: Height of the container in meters
        :param container_max_weight: Maximum weight the container can carry in kilograms
        """
        self.container_length = container_length
        self.container_width = container_width
        self.container_height = container_height
        self.container_max_weight = container_max_weight

    def calculate_capacity(self, item_length, item_width, item_height, item_weight):
        """
        Calculates the maximum number of items that can fit in the container.

        :param item_length: Length of a single item in meters
        :param item_width: Width of a single item in meters
        :param item_height: Height of a single item in meters
        :param item_weight: Weight of a single item in kilograms
        :return: Maximum number of items that can fit in the container
        """
        try:
            # Calculate the volume capacity of the container
            container_volume = self.container_length * self.container_width * self.container_height
            item_volume = item_length * item_width * item_height

            # Calculate how many items can fit based on volume
            max_items_by_volume = math.floor(container_volume / item_volume)

            # Calculate how many items can fit based on weight
            max_items_by_weight = math.floor(self.container_max_weight / item_weight)

            # The limiting factor is the smaller of the two
            return min(max_items_by_volume, max_items_by_weight)

        except ZeroDivisionError:
            raise ValueError("Item dimensions and weight must be greater than zero.")
        except Exception as e:
            raise RuntimeError(f"An error occurred during calculation: {e}")

# Example Usage
if __name__ == "__main__":
    # Container dimensions in meters and max weight in kilograms
    container_length = 12.0  # 12 meters
    container_width = 2.35   # 2.35 meters
    container_height = 2.39  # 2.39 meters
    container_max_weight = 28000  # 28,000 kilograms

    # Item dimensions in meters and weight in kilograms
    item_length = 0.4  # 0.4 meters
    item_width = 0.4   # 0.4 meters
    item_height = 0.05 # 0.05 meters
    item_weight = 5.0  # 5 kilograms

    # Create the calculator object
    calculator = ContainerLoadingCalculator(
        container_length, container_width, container_height, container_max_weight
    )

    # Perform the calculation
    try:
        max_items = calculator.calculate_capacity(item_length, item_width, item_height, item_weight)
        print(f"Maximum number of items that can fit in the container: {max_items}")
    except Exception as e:
        print(f"Error: {e}")
```
