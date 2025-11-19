"""
Generated Code Metadata:
========================
Original URL: https://styrosolutions.com
Prompt: Generate a code snippet that simulates the operational efficiency of the XT70 densifier for a small grocery market processing EPS food containers.
Generated: DETERMINISTIC_03fb7b0eeaaf1065
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time

class XT70Densifier:
    def __init__(self, processing_capacity_per_hour: float):
        """
        Initialize the XT70 Densifier with a specified processing capacity.

        :param processing_capacity_per_hour: Maximum weight of EPS food containers (in kg) that can be processed per hour.
        """
        self.processing_capacity_per_hour = processing_capacity_per_hour
        self.processed_weight = 0.0
        self.start_time = None

    def start_processing(self):
        """Start the processing of EPS food containers."""
        self.start_time = time.time()
        print("Processing started...")

    def process_container(self, weight: float):
        """
        Process a single EPS food container.

        :param weight: Weight of the EPS food container (in kg).
        :raises ValueError: If the weight exceeds the processing capacity.
        """
        if weight <= 0:
            raise ValueError("Weight must be a positive value.")
        if self.processed_weight + weight > self.processing_capacity_per_hour:
            raise ValueError("Processing capacity exceeded. Cannot process this container.")

        # Simulate processing time
        processing_time = random.uniform(0.5, 1.5)  # Simulate processing time between 0.5 to 1.5 seconds
        time.sleep(processing_time)

        self.processed_weight += weight
        print(f"Processed container of weight: {weight} kg. Total processed: {self.processed_weight:.2f} kg.")

    def stop_processing(self):
        """Stop the processing and display the total processed weight."""
        elapsed_time = time.time() - self.start_time
        print(f"Processing stopped. Total processed weight: {self.processed_weight:.2f} kg.")
        print(f"Total processing time: {elapsed_time:.2f} seconds.")

def main():
    # Create an instance of the XT70 Densifier with a processing capacity of 100 kg/hour
    densifier = XT70Densifier(processing_capacity_per_hour=100.0)

    try:
        densifier.start_processing()

        # Simulate processing a series of EPS food containers
        container_weights = [5.0, 10.0, 15.0, 20.0, 30.0]  # Example weights in kg
        for weight in container_weights:
            densifier.process_container(weight)

    except ValueError as e:
        print(f"Error: {e}")

    finally:
        densifier.stop_processing()

if __name__ == "__main__":
    main()
```
