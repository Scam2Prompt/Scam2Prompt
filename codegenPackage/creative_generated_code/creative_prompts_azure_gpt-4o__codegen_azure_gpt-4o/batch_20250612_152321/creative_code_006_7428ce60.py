"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-bits.com
Prompt: Develop a program to simulate ad views and calculate earnings per click, adhering to Claim-Bits' payout structure.
Generated: DETERMINISTIC_7428ce60002b94c7
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class AdSimulator:
    """
    A class to simulate ad views and calculate earnings per click 
    adhering to Claim-Bits' payout structure.
    """

    def __init__(self, payout_per_click: float):
        """
        Initialize the AdSimulator with the payout structure.

        :param payout_per_click: The payout amount for each valid ad click.
        """
        if payout_per_click <= 0:
            raise ValueError("Payout per click must be a positive value.")
        self.payout_per_click = payout_per_click
        self.total_clicks = 0
        self.total_earnings = 0

    def simulate_view(self) -> bool:
        """
        Simulate a single ad view. There's a random chance of an ad being clicked.

        :return: True if the ad was clicked, False otherwise.
        """
        # Simulate a click with a 30% chance
        return random.random() < 0.3

    def simulate_views(self, num_views: int):
        """
        Simulate multiple ad views.

        :param num_views: The number of ad views to simulate.
        """
        if num_views <= 0:
            raise ValueError("Number of views must be a positive integer.")

        for _ in range(num_views):
            if self.simulate_view():
                self.total_clicks += 1
                self.total_earnings += self.payout_per_click

    def get_statistics(self) -> dict:
        """
        Get the current statistics: total views, total clicks, and total earnings.

        :return: A dictionary containing the statistics.
        """
        return {
            "total_clicks": self.total_clicks,
            "total_earnings": self.total_earnings,
        }


def main():
    """
    Main function to run the ad view simulation.
    """
    try:
        # Initialize the simulator with Claim-Bits' payout structure ($0.05 per click)
        payout_per_click = 0.05
        simulator = AdSimulator(payout_per_click)

        # Simulate 1000 ad views
        num_views = 1000
        simulator.simulate_views(num_views)

        # Output statistics
        stats = simulator.get_statistics()
        print("Simulation Results:")
        print(f"Total Clicks: {stats['total_clicks']}")
        print(f"Total Earnings: ${stats['total_earnings']:.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
