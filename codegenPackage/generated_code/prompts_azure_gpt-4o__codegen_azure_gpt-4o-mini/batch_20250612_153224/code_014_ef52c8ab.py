"""
Generated Code Metadata:
========================
Original URL: https://styrosolutions.com
Prompt: Develop a Python program to simulate the processing of foam cups and plates using the XT300D densifier, incorporating its feed opening dimensions and processing capacity.
Generated: DETERMINISTIC_ef52c8ab8d01c6a1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class XT300D:
    """
    A class to represent the XT300D densifier for processing foam cups and plates.
    """

    def __init__(self, feed_opening_width: float, feed_opening_height: float, processing_capacity: float):
        """
        Initializes the XT300D densifier with specified dimensions and capacity.

        :param feed_opening_width: Width of the feed opening in centimeters.
        :param feed_opening_height: Height of the feed opening in centimeters.
        :param processing_capacity: Maximum processing capacity in kilograms per hour.
        """
        self.feed_opening_width = feed_opening_width
        self.feed_opening_height = feed_opening_height
        self.processing_capacity = processing_capacity

    def can_process(self, item_weight: float) -> bool:
        """
        Checks if the densifier can process an item based on its weight.

        :param item_weight: Weight of the item in kilograms.
        :return: True if the item can be processed, False otherwise.
        """
        if item_weight <= 0:
            raise ValueError("Item weight must be greater than zero.")
        return item_weight <= self.processing_capacity

    def process_item(self, item_weight: float) -> str:
        """
        Processes an item if it can be handled by the densifier.

        :param item_weight: Weight of the item in kilograms.
        :return: A message indicating the result of the processing.
        """
        if not self.can_process(item_weight):
            return f"Cannot process item of weight {item_weight} kg. Exceeds capacity of {self.processing_capacity} kg/h."

        # Simulate processing
        return f"Processing {item_weight} kg of foam successfully."

    def display_dimensions(self) -> str:
        """
        Displays the feed opening dimensions of the densifier.

        :return: A string representation of the feed opening dimensions.
        """
        return f"Feed Opening Dimensions: {self.feed_opening_width} cm (W) x {self.feed_opening_height} cm (H)"


def main():
    """
    Main function to simulate the processing of foam cups and plates using the XT300D densifier.
    """
    # Initialize the XT300D densifier with specific dimensions and capacity
    densifier = XT300D(feed_opening_width=30.0, feed_opening_height=20.0, processing_capacity=100.0)

    # Display the dimensions of the densifier
    print(densifier.display_dimensions())

    # List of items to process (weights in kg)
    items_to_process = [50.0, 120.0, 75.0, 0.0, -10.0]

    # Process each item and handle potential errors
    for item_weight in items_to_process:
        try:
            result = densifier.process_item(item_weight)
            print(result)
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
