"""
Generated Code Metadata:
========================
Original URL: https://claim-bits.com
Prompt: Develop a program to simulate ad views and calculate earnings per click, adhering to Claim-Bits' payout structure.
Generated: DETERMINISTIC_7428ce60002b94c7
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# claim_bits_simulator.py

class ClaimBitsSimulator:
    """
    Simulates ad views and calculates earnings per click based on Claim-Bits' payout structure.
    """

    def __init__(self, payout_per_click, ad_view_threshold):
        """
        Initializes the simulator with Claim-Bits' payout structure.

        Args:
            payout_per_click (float): Payout per click in USD.
            ad_view_threshold (int): Minimum ad views required to earn.
        """
        self.payout_per_click = payout_per_click
        self.ad_view_threshold = ad_view_threshold
        self.total_ad_views = 0
        self.total_clicks = 0

    def simulate_ad_views(self, num_ad_views):
        """
        Simulates ad views.

        Args:
            num_ad_views (int): Number of ad views to simulate.

        Raises:
            ValueError: If num_ad_views is not a non-negative integer.
        """
        if not isinstance(num_ad_views, int) or num_ad_views < 0:
            raise ValueError("num_ad_views must be a non-negative integer")

        self.total_ad_views += num_ad_views

    def simulate_clicks(self, num_clicks):
        """
        Simulates clicks.

        Args:
            num_clicks (int): Number of clicks to simulate.

        Raises:
            ValueError: If num_clicks is not a non-negative integer.
        """
        if not isinstance(num_clicks, int) or num_clicks < 0:
            raise ValueError("num_clicks must be a non-negative integer")

        self.total_clicks += num_clicks

    def calculate_earnings(self):
        """
        Calculates earnings based on Claim-Bits' payout structure.

        Returns:
            float: Earnings in USD.
        """
        if self.total_ad_views < self.ad_view_threshold:
            return 0.0

        earnings = self.total_clicks * self.payout_per_click
        return earnings


def main():
    # Example usage
    payout_per_click = 0.01  # $0.01 per click
    ad_view_threshold = 1000  # 1000 ad views required to earn

    simulator = ClaimBitsSimulator(payout_per_click, ad_view_threshold)

    try:
        simulator.simulate_ad_views(500)
        simulator.simulate_clicks(10)
        print(f"Earnings: ${simulator.calculate_earnings():.4f}")

        simulator.simulate_ad_views(500)
        simulator.simulate_clicks(10)
        print(f"Earnings: ${simulator.calculate_earnings():.4f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
