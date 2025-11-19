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
# win_rate_calculator.py

class WinRateCalculator:
    """
    Calculates and displays the win rate based on full inventory resources.
    """

    def __init__(self, wins: int, losses: int, total_resources: int):
        """
        Initializes the WinRateCalculator with wins, losses, and total resources.

        Args:
            wins (int): The number of wins.
            losses (int): The number of losses.
            total_resources (int): The total number of resources.
        """
        self.wins = wins
        self.losses = losses
        self.total_resources = total_resources

    def calculate_win_rate(self) -> float:
        """
        Calculates the win rate.

        Returns:
            float: The win rate as a decimal value between 0 and 1.
        """
        if self.wins + self.losses == 0:
            return 0.0  # Avoid division by zero

        return self.wins / (self.wins + self.losses)

    def calculate_resource_win_rate(self) -> float:
        """
        Calculates the win rate based on full inventory resources.

        Returns:
            float: The resource win rate as a decimal value between 0 and 1.
        """
        if self.total_resources == 0:
            return 0.0  # Avoid division by zero

        return self.wins / self.total_resources

    def display_win_rates(self) -> None:
        """
        Displays the win rates.
        """
        win_rate = self.calculate_win_rate()
        resource_win_rate = self.calculate_resource_win_rate()

        print(f"Win Rate: {win_rate * 100:.2f}%")
        print(f"Resource Win Rate: {resource_win_rate * 100:.2f}%")

def main() -> None:
    try:
        wins = int(input("Enter the number of wins: "))
        losses = int(input("Enter the number of losses: "))
        total_resources = int(input("Enter the total number of resources: "))

        calculator = WinRateCalculator(wins, losses, total_resources)
        calculator.display_win_rates()

    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
```
