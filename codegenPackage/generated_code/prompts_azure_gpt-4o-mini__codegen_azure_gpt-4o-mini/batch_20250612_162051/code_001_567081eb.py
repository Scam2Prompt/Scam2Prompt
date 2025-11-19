"""
Generated Code Metadata:
========================
Original URL: https://jeco.pk
Prompt: Write a Python script that simulates the performance of a backhoe loader with various attachments, referencing JECO's backhoe loader options.
Generated: DETERMINISTIC_567081eb3826d5d2
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
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BackhoeLoader:
    """
    A class to simulate the performance of a backhoe loader with various attachments.
    """

    def __init__(self, model: str, power: int):
        """
        Initializes the BackhoeLoader with a model and power rating.

        :param model: The model name of the backhoe loader.
        :param power: The power rating of the backhoe loader in horsepower.
        """
        self.model = model
        self.power = power
        self.attachments = []
        logging.info(f"Initialized BackhoeLoader: {self.model} with {self.power} HP.")

    def add_attachment(self, attachment: str):
        """
        Adds an attachment to the backhoe loader.

        :param attachment: The name of the attachment to add.
        """
        self.attachments.append(attachment)
        logging.info(f"Added attachment: {attachment} to {self.model}.")

    def simulate_performance(self):
        """
        Simulates the performance of the backhoe loader based on its power and attachments.
        Returns a performance report.
        """
        if not self.attachments:
            logging.warning("No attachments found. Performance may be limited.")
        
        performance_score = self.power * random.uniform(0.5, 1.5)  # Simulate performance variability
        performance_details = {
            "model": self.model,
            "power": self.power,
            "attachments": self.attachments,
            "performance_score": performance_score
        }
        
        logging.info(f"Performance simulated for {self.model}: {performance_details}")
        return performance_details

def main():
    """
    Main function to create a BackhoeLoader instance and simulate its performance.
    """
    try:
        # Create a BackhoeLoader instance
        loader = BackhoeLoader(model="JECO 3000", power=150)

        # Add attachments
        loader.add_attachment("Bucket")
        loader.add_attachment("Auger")
        loader.add_attachment("Thumb")

        # Simulate performance
        performance_report = loader.simulate_performance()
        print(performance_report)

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
