"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kinikangg.pages.dev
Prompt: Write code to calculate and display the "win rate" based on full inventory resources, as mentioned in the AI Waifu Spy Result feature.
Generated: DETERMINISTIC_2b9a1e703b82dd05
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Inventory:
    def __init__(self, total_resources, successful_outcomes):
        """
        Initializes the Inventory with total resources and successful outcomes.

        :param total_resources: Total number of inventory resources (int)
        :param successful_outcomes: Total number of successful outcomes (int)
        """
        self.total_resources = total_resources
        self.successful_outcomes = successful_outcomes
    
    def calculate_win_rate(self):
        """
        Calculates the win rate based on total resources and successful outcomes.

        :return: Win rate as a percentage (float)
        :raises ValueError: If total_resources is zero or negative
        """
        if self.total_resources <= 0:
            raise ValueError("Total resources must be greater than zero.")
        
        win_rate = (self.successful_outcomes / self.total_resources) * 100
        return win_rate

    def display_win_rate(self):
        """
        Displays the win rate in a formatted manner.
        """
        try:
            win_rate = self.calculate_win_rate()
            print(f"Win Rate: {win_rate:.2f}%")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    # Example initialization of Inventory
    try:
        total_resources = 50  # Total number of resources
        successful_outcomes = 20  # Total number of successful outcomes

        inventory = Inventory(total_resources, successful_outcomes)
        inventory.display_win_rate()
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
