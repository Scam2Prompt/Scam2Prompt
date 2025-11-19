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
class FoamDensifier:
    """
    Simulates the processing of foam cups and plates using the XT300D densifier.
    """

    def __init__(self, feed_opening_width=12, feed_opening_height=6, processing_capacity=300):
        """
        Initializes the FoamDensifier with feed opening dimensions and processing capacity.

        Args:
            feed_opening_width (float, optional): The width of the feed opening in inches. Defaults to 12.
            feed_opening_height (float, optional): The height of the feed opening in inches. Defaults to 6.
            processing_capacity (float, optional): The processing capacity in pounds per hour. Defaults to 300.
        """
        self.feed_opening_width = feed_opening_width
        self.feed_opening_height = feed_opening_height
        self.processing_capacity = processing_capacity
        self.total_processed = 0

    def process_foam(self, amount):
        """
        Simulates the processing of foam.

        Args:
            amount (float): The amount of foam to process in pounds.

        Raises:
            ValueError: If the amount of foam is negative.
            RuntimeError: If the densifier's capacity is exceeded.
        """
        if amount < 0:
            raise ValueError("Amount of foam cannot be negative")

        if self.total_processed + amount > self.processing_capacity:
            raise RuntimeError("Densifier's capacity exceeded")

        self.total_processed += amount
        return amount

    def get_status(self):
        """
        Returns the current status of the densifier.

        Returns:
            dict: A dictionary containing the feed opening dimensions, processing capacity, and total processed amount.
        """
        return {
            "feed_opening_width": self.feed_opening_width,
            "feed_opening_height": self.feed_opening_height,
            "processing_capacity": self.processing_capacity,
            "total_processed": self.total_processed,
        }


def main():
    try:
        densifier = FoamDensifier()

        # Process foam cups and plates
        foam_cups = 50
        foam_plates = 100
        processed_cups = densifier.process_foam(foam_cups)
        processed_plates = densifier.process_foam(foam_plates)

        print(f"Processed {processed_cups} pounds of foam cups")
        print(f"Processed {processed_plates} pounds of foam plates")

        # Get and print the densifier's status
        status = densifier.get_status()
        print("\nDensifier Status:")
        for key, value in status.items():
            print(f"{key.capitalize().replace('_', ' ')}: {value}")

    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
