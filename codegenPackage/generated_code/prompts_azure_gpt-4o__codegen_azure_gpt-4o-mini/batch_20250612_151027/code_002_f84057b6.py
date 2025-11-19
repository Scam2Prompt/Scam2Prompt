"""
Generated Code Metadata:
========================
Original URL: https://moxie.credit
Prompt: Provide an example of how to split payouts in a decentralized economy using Moxie’s shared payout structure (50% to earning member, 20% to community/channel, etc.).
Generated: DETERMINISTIC_f84057b657f5c5c5
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PayoutSplitter:
    """
    A class to handle the splitting of payouts in a decentralized economy
    using Moxie's shared payout structure.
    """

    def __init__(self, total_payout):
        """
        Initializes the PayoutSplitter with the total payout amount.

        :param total_payout: The total amount to be split.
        """
        if total_payout < 0:
            raise ValueError("Total payout must be a non-negative value.")
        self.total_payout = total_payout

    def split_payout(self):
        """
        Splits the total payout according to the defined structure:
        - 50% to earning member
        - 20% to community/channel
        - 30% to reserve fund

        :return: A dictionary containing the split amounts.
        """
        earning_member_share = self.total_payout * 0.50
        community_share = self.total_payout * 0.20
        reserve_fund_share = self.total_payout * 0.30

        return {
            "earning_member": earning_member_share,
            "community_channel": community_share,
            "reserve_fund": reserve_fund_share
        }

    def display_payouts(self):
        """
        Displays the payout distribution in a formatted manner.
        """
        try:
            payouts = self.split_payout()
            print("Payout Distribution:")
            for key, value in payouts.items():
                print(f"{key.replace('_', ' ').title()}: ${value:.2f}")
        except Exception as e:
            print(f"An error occurred while displaying payouts: {e}")


# Example usage
if __name__ == "__main__":
    try:
        total_payout_amount = 1000.00  # Example total payout amount
        payout_splitter = PayoutSplitter(total_payout_amount)
        payout_splitter.display_payouts()
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
