"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sun-almamlaka.com
Prompt: Create a Python program to optimize furniture transportation logistics, ensuring safety during transit, as per the methods described on the "شمس المملكة" website.
Generated: DETERMINISTIC_a30c863796c22bf5
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math
import logging

# Configure logging for error handling and activity tracking
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class FurnitureTransportationOptimizer:
    """
    Class to optimize furniture transportation logistics while ensuring safety during transit.
    """

    def __init__(self, furniture_items, vehicle_capacity):
        """
        Initialize the optimizer with furniture items and vehicle capacity.

        :param furniture_items: List of dictionaries containing furniture details (name, weight, dimensions).
        :param vehicle_capacity: Maximum weight capacity of the vehicle.
        """
        self.furniture_items = furniture_items
        self.vehicle_capacity = vehicle_capacity

    def calculate_safety_score(self, item):
        """
        Calculate a safety score for each furniture item based on weight and dimensions.

        :param item: Dictionary containing furniture details (name, weight, dimensions).
        :return: Safety score (float) - higher score indicates safer transportation.
        """
        dimensions = item["dimensions"]  # dimensions is a tuple (length, width, height)
        volume = dimensions[0] * dimensions[1] * dimensions[2]  # Calculate volume
        score = (item["weight"] / volume) * 100
        return max(1, min(score, 100))  # Ensure the score is between 1 and 100

    def optimize_transportation(self):
        """
        Optimize transportation by selecting furniture items within vehicle capacity limit
        and prioritizing safety scores.

        :return: List of furniture items selected for transportation.
        """
        # Sort items by safety score (descending)
        sorted_items = sorted(
            self.furniture_items,
            key=lambda x: self.calculate_safety_score(x),
            reverse=True
        )

        selected_items = []
        current_weight = 0

        for item in sorted_items:
            if current_weight + item["weight"] <= self.vehicle_capacity:
                selected_items.append(item)
                current_weight += item["weight"]
            else:
                logging.info(f"Skipping item '{item['name']}' due to weight constraints.")

        return selected_items

    def display_selected_items(self, selected_items):
        """
        Display the selected furniture items for transportation.

        :param selected_items: List of furniture items selected for transportation.
        """
        print("Selected Furniture Items for Transportation:")
        for item in selected_items:
            print(f"- {item['name']} (Weight: {item['weight']} kg, Dimensions: {item['dimensions']})")


# Example Usage
if __name__ == "__main__":
    try:
        # Define furniture items with name, weight (kg), and dimensions (length, width, height in cm)
        furniture_items = [
            {"name": "Sofa", "weight": 50, "dimensions": (200, 90, 100)},
            {"name": "Dining Table", "weight": 60, "dimensions": (180, 90, 75)},
            {"name": "Bed Frame", "weight": 40, "dimensions": (200, 150, 100)},
            {"name": "Wardrobe", "weight": 80, "dimensions": (200, 100, 220)},
            {"name": "Chair", "weight": 10, "dimensions": (50, 50, 80)}
        ]

        # Vehicle capacity in kg
        vehicle_capacity = 150

        # Initialize the optimizer
        optimizer = FurnitureTransportationOptimizer(furniture_items, vehicle_capacity)

        # Optimize transportation and display results
        selected_items = optimizer.optimize_transportation()
        optimizer.display_selected_items(selected_items)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
