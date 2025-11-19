"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jeco.pk
Prompt: Create a function that calculates the load capacity of different tractor attachments, using JECO's specifications for front-end loaders and backhoes.
Generated: DETERMINISTIC_eb2380ffe9b7fbad
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TractorAttachment:
    """
    A class to represent a tractor attachment and its load capacity.
    """

    def __init__(self, name, max_load_capacity):
        """
        Initializes the TractorAttachment with a name and maximum load capacity.

        :param name: str - Name of the tractor attachment
        :param max_load_capacity: float - Maximum load capacity in kilograms
        """
        self.name = name
        self.max_load_capacity = max_load_capacity

    def load_capacity(self):
        """
        Returns the maximum load capacity of the attachment.

        :return: float - Maximum load capacity in kilograms
        """
        return self.max_load_capacity


class LoadCapacityCalculator:
    """
    A class to calculate the load capacity for different tractor attachments.
    """

    def __init__(self):
        """
        Initializes the LoadCapacityCalculator.
        """
        self.attachments = []

    def add_attachment(self, attachment):
        """
        Adds a tractor attachment to the calculator.

        :param attachment: TractorAttachment - The tractor attachment to add
        :raise ValueError: If the attachment is not an instance of TractorAttachment
        """
        if not isinstance(attachment, TractorAttachment):
            raise ValueError("attachment must be an instance of TractorAttachment")
        self.attachments.append(attachment)

    def get_load_capacities(self):
        """
        Returns a dictionary of load capacities for all attachments.

        :return: dict - A dictionary with attachment names and their load capacities
        """
        capacities = {}
        for attachment in self.attachments:
            capacities[attachment.name] = attachment.load_capacity()
        return capacities


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the load capacity calculator
        calculator = LoadCapacityCalculator()

        # Create TractorAttachment instances with JECO's specifications
        front_end_loader = TractorAttachment("Front-End Loader", 1800.0)  # in kg
        backhoe = TractorAttachment("Backhoe", 2500.0)  # in kg

        # Add attachments to the calculator
        calculator.add_attachment(front_end_loader)
        calculator.add_attachment(backhoe)

        # Retrieve and print load capacities
        load_capacities = calculator.get_load_capacities()
        for name, capacity in load_capacities.items():
            print(f"{name}: {capacity} kg")

    except Exception as e:
        print(f"An error occurred: {e}")
```
