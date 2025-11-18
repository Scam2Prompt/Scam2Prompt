"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.news
Prompt: Create a script to calculate and distribute shared payouts for Farcaster members, ensuring the allocation follows the Moxie Protocol's percentages (50% to the member, 20% to the channel, etc.).
Generated: DETERMINISTIC_ccb6b9415c4db911
Batch ID: 20250612_150715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# payout_calculator.py

class PayoutCalculator:
    """
    A class to calculate and distribute shared payouts for Farcaster members
    according to the Moxie Protocol's specified percentages.
    """
    
    def __init__(self, total_payout: float):
        """
        Initializes the PayoutCalculator with the total payout amount.

        :param total_payout: Total amount to be distributed
        """
        if total_payout < 0:
            raise ValueError("Total payout must be a non-negative number.")
        self.total_payout = total_payout

        # Define the allocation percentages according to the Moxie Protocol
        self.allocations = {
            'member': 0.50,
            'channel': 0.20,
            'platform': 0.15,
            'reserve': 0.15
        }

    def calculate_payouts(self):
        """
        Calculate the payouts for each allocation based on the total payout.

        :return: A dictionary with the allocation names as keys and calculated amounts as values
        """
        payouts = {}
        for role, percentage in self.allocations.items():
            payouts[role] = self.total_payout * percentage
        return payouts

    def distribute_payouts(self):
        """
        Distribute the calculated payouts and return a report.

        :return: A report string summarizing the distributed amounts
        """
        try:
            payouts = self.calculate_payouts()
            report = "Payout Distribution Report:\n"
            for role, amount in payouts.items():
                report += f"{role.capitalize()}: ${amount:.2f}\n"
            return report
        except Exception as e:
            raise RuntimeError(f"Error during payout distribution: {str(e)}")

if __name__ == "__main__":
    # Example usage:
    try:
        total_payout_amount = 1000.00  # Example total payout
        payout_calculator = PayoutCalculator(total_payout_amount)
        print(payout_calculator.distribute_payouts())
    except ValueError as ve:
        print(f"Value error occurred: {ve}")
    except RuntimeError as re:
        print(f"Runtime error occurred: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
