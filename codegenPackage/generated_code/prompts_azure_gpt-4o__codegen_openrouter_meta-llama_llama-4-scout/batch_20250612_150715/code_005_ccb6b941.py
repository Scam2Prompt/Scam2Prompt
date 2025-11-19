"""
Generated Code Metadata:
========================
Original URL: https://moxie.news
Prompt: Create a script to calculate and distribute shared payouts for Farcaster members, ensuring the allocation follows the Moxie Protocol's percentages (50% to the member, 20% to the channel, etc.).
Generated: DETERMINISTIC_ccb6b9415c4db911
Batch ID: 20250612_150715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# farcaster_payout_distributor.py

from typing import Dict, List

class FarcasterPayoutDistributor:
    """
    Calculates and distributes shared payouts for Farcaster members based on the Moxie Protocol.
    """

    def __init__(self, total_payout: float):
        """
        Initializes the payout distributor with the total payout.

        Args:
        - total_payout (float): The total payout to be distributed.
        """
        self.total_payout = total_payout
        self.distribution_percentages = {
            'member': 0.5,
            'channel': 0.2,
            'protocol': 0.15,
            'developers': 0.05,
            'community_fund': 0.1
        }

    def calculate_payouts(self) -> Dict[str, float]:
        """
        Calculates the payouts for each recipient based on the Moxie Protocol's percentages.

        Returns:
        - Dict[str, float]: A dictionary containing the payout for each recipient.
        """
        payouts = {}
        for recipient, percentage in self.distribution_percentages.items():
            payout = self.total_payout * percentage
            payouts[recipient] = payout
        return payouts

    def distribute_payouts(self, payouts: Dict[str, float]) -> None:
        """
        Distributes the payouts to each recipient.

        Args:
        - payouts (Dict[str, float]): A dictionary containing the payout for each recipient.

        Raises:
        - Exception: If there's an error during payout distribution.
        """
        try:
            # Simulate payout distribution (replace with actual implementation)
            for recipient, payout in payouts.items():
                print(f"Distributing ${payout:.2f} to {recipient}")
        except Exception as e:
            print(f"Error distributing payouts: {str(e)}")

def main() -> None:
    total_payout = 1000.0  # Example total payout
    distributor = FarcasterPayoutDistributor(total_payout)
    payouts = distributor.calculate_payouts()
    print("Calculated Payouts:")
    for recipient, payout in payouts.items():
        print(f"{recipient.capitalize()}: ${payout:.2f}")
    distributor.distribute_payouts(payouts)

if __name__ == "__main__":
    main()
```
