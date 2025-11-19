"""
Generated Code Metadata:
========================
Original URL: https://co-djs.com
Prompt: Write a script to calculate the cost of a DJ event based on the duration and type of package chosen (e.g., "Party" Package for $250), including any add-ons for video, lighting, or karaoke.
Generated: DETERMINISTIC_1d7b9d5cbc199e78
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DJEvent:
    def __init__(self, package_type, duration_hours, add_ons=None):
        """
        Initialize the DJEvent with package type, duration, and optional add-ons.

        :param package_type: str - Type of package chosen (e.g., "Party", "Wedding")
        :param duration_hours: float - Duration of the event in hours
        :param add_ons: list - List of add-ons chosen (e.g., ["video", "lighting"])
        """
        self.package_prices = {
            "Party": 250,
            "Wedding": 400,
            "Corporate": 300
        }
        self.add_on_prices = {
            "video": 100,
            "lighting": 150,
            "karaoke": 75
        }
        self.package_type = package_type
        self.duration_hours = duration_hours
        self.add_ons = add_ons if add_ons else []

    def calculate_total_cost(self):
        """
        Calculate the total cost of the DJ event based on the package, duration, and add-ons.

        :return: float - Total cost of the event
        :raises ValueError: If the package type is invalid or duration is negative
        """
        if self.package_type not in self.package_prices:
            raise ValueError(f"Invalid package type: {self.package_type}. Available packages: {list(self.package_prices.keys())}")

        if self.duration_hours < 0:
            raise ValueError("Duration cannot be negative.")

        # Calculate base cost from package
        base_cost = self.package_prices[self.package_type] * self.duration_hours

        # Calculate total cost from add-ons
        add_on_cost = sum(self.add_on_prices[add_on] for add_on in self.add_ons if add_on in self.add_on_prices)

        # Total cost is the sum of base cost and add-on costs
        total_cost = base_cost + add_on_cost
        return total_cost

def main():
    """
    Main function to execute the DJ event cost calculation.
    """
    try:
        # Example input
        package_type = "Party"
        duration_hours = 5
        add_ons = ["video", "lighting"]

        # Create a DJEvent instance
        event = DJEvent(package_type, duration_hours, add_ons)

        # Calculate and print the total cost
        total_cost = event.calculate_total_cost()
        print(f"The total cost for the {package_type} package for {duration_hours} hours with add-ons {add_ons} is: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
