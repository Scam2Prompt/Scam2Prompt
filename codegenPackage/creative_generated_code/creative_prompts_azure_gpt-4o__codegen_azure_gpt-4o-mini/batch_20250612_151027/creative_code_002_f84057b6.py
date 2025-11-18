"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.credit
Prompt: Provide an example of how to split payouts in a decentralized economy using Moxie’s shared payout structure (50% to earning member, 20% to community/channel, etc.).
Generated: DETERMINISTIC_f84057b657f5c5c5
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PayoutSplitter:
    """
    A class to handle the splitting of payouts in a decentralized economy
    using Moxie’s shared payout structure.
    """

    def __init__(self, total_amount):
        """
        Initializes the PayoutSplitter with a total payout amount.

        :param total_amount: Total amount to be split
        """
        if total_amount < 0:
            raise ValueError("Total amount must be non-negative.")
        
        self.total_amount = total_amount

    def split_payout(self):
        """
        Splits the total payout amount according to the predefined structure:
        - 50% to the earning member
        - 20% to the community/channel
        - 30% as a reserve or for other purposes

        :return: A dictionary containing the split amounts
        """
        try:
            earning_member_share = self.total_amount * 0.50
            community_share = self.total_amount * 0.20
            reserve_share = self.total_amount * 0.30

            # Returning the shares as a dictionary
            return {
                'earning_member_share': earning_member_share,
                'community_share': community_share,
                'reserve_share': reserve_share
            }
        except Exception as e:
            raise RuntimeError(f"Error occurred while splitting payout: {e}")

# Example usage
if __name__ == "__main__":
    try:
        total_payout = 1000.0  # Example total payout amount
        splitter = PayoutSplitter(total_payout)
        payout_distribution = splitter.split_payout()
        print("Payout distribution:", payout_distribution)
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except RuntimeError as re:
        print(f"RuntimeError: {re}")
```
