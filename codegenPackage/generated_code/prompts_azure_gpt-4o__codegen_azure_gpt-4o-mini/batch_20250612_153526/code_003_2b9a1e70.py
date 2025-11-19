"""
Generated Code Metadata:
========================
Original URL: https://kinikangg.pages.dev
Prompt: Write code to calculate and display the "win rate" based on full inventory resources, as mentioned in the AI Waifu Spy Result feature.
Generated: DETERMINISTIC_2b9a1e703b82dd05
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Inventory:
    """
    A class to represent an inventory of resources for calculating win rates.
    """

    def __init__(self, total_resources, successful_outcomes):
        """
        Initializes the Inventory with total resources and successful outcomes.

        :param total_resources: Total number of resources in the inventory.
        :param successful_outcomes: Number of successful outcomes from the resources.
        """
        if total_resources < 0:
            raise ValueError("Total resources cannot be negative.")
        if successful_outcomes < 0:
            raise ValueError("Successful outcomes cannot be negative.")
        if successful_outcomes > total_resources:
            raise ValueError("Successful outcomes cannot exceed total resources.")

        self.total_resources = total_resources
        self.successful_outcomes = successful_outcomes

    def calculate_win_rate(self):
        """
        Calculates the win rate based on total resources and successful outcomes.

        :return: Win rate as a percentage.
        """
        if self.total_resources == 0:
            return 0.0  # Avoid division by zero; if no resources, win rate is 0%
        
        win_rate = (self.successful_outcomes / self.total_resources) * 100
        return win_rate

    def display_win_rate(self):
        """
        Displays the win rate in a formatted string.
        """
        win_rate = self.calculate_win_rate()
        print(f"Win Rate: {win_rate:.2f}%")

def main():
    """
    Main function to execute the win rate calculation and display.
    """
    try:
        # Example values for total resources and successful outcomes
        total_resources = 100  # Total resources available
        successful_outcomes = 75  # Successful outcomes achieved

        # Create an Inventory instance
        inventory = Inventory(total_resources, successful_outcomes)

        # Display the calculated win rate
        inventory.display_win_rate()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
