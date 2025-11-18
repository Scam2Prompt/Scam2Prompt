"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rehiletes.com
Prompt: Generate a script to calculate the total cost of multi-day excursions offered by "Rehiletes," including options for destinations like San Miguel de Allende and Veracruz.
Generated: DETERMINISTIC_f6e7c8102fa454ed
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Excursion:
    """Class to represent an excursion with destination and cost details."""
    
    def __init__(self, destination, base_cost, days):
        """
        Initialize an Excursion instance.
        
        Parameters:
        destination (str): The name of the destination.
        base_cost (float): The base cost per day of the excursion.
        days (int): The number of days for the excursion.
        """
        self.destination = destination
        self.base_cost = base_cost
        self.days = days

    def total_cost(self):
        """Calculate the total cost of the excursion."""
        if self.days < 1:
            raise ValueError("Number of days must be at least 1.")
        return self.base_cost * self.days


class ExcursionManager:
    """Class to manage multiple excursions."""
    
    def __init__(self):
        """Initialize the ExcursionManager with an empty list of excursions."""
        self.excursions = []

    def add_excursion(self, destination, base_cost, days):
        """
        Add an excursion to the manager.

        Parameters:
        destination (str): The name of the destination.
        base_cost (float): The cost per day of the excursion.
        days (int): The number of days for the excursion.
        """
        try:
            excursion = Excursion(destination, base_cost, days)
            self.excursions.append(excursion)
        except Exception as e:
            print(f"Error adding excursion: {e}")

    def calculate_total_revenue(self):
        """Calculate the total revenue from all excursions."""
        total_revenue = 0
        for excursion in self.excursions:
            total_revenue += excursion.total_cost()
        return total_revenue

    def display_excursion_details(self):
        """Display details of all excursions."""
        for excursion in self.excursions:
            print(f"Destination: {excursion.destination}, Days: {excursion.days}, Total Cost: ${excursion.total_cost():.2f}")


def main():
    """Main function to run the excursion manager."""
    manager = ExcursionManager()
    
    # Example excursions
    manager.add_excursion("San Miguel de Allende", 150.00, 3)
    manager.add_excursion("Veracruz", 120.00, 5)
    
    # Display all excursions
    manager.display_excursion_details()
    
    # Calculate and display total revenue
    total_revenue = manager.calculate_total_revenue()
    print(f"Total Revenue from all excursions: ${total_revenue:.2f}")


if __name__ == "__main__":
    main()
```
