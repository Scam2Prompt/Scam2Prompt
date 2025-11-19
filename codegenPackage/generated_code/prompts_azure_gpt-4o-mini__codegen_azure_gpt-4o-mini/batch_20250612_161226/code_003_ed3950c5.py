"""
Generated Code Metadata:
========================
Original URL: https://monad-og-tnymxw.nfts2.me
Prompt: Create a function that tracks and calculates referral earnings for each mint completed through a user's unique link, based on the Monad OG Chain model.
Generated: DETERMINISTIC_ed3950c5d5b7c2b7
Batch ID: 20250612_161226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ReferralTracker:
    def __init__(self):
        """
        Initializes the ReferralTracker with a dictionary to store user earnings.
        """
        self.referral_earnings = {}

    def mint_completed(self, user_id, referral_link, mint_amount):
        """
        Processes a completed mint for a user and updates their referral earnings.

        Parameters:
        user_id (str): The unique identifier for the user who completed the mint.
        referral_link (str): The unique referral link associated with the user.
        mint_amount (float): The amount earned from the mint.

        Raises:
        ValueError: If mint_amount is negative or user_id is empty.
        """
        if mint_amount < 0:
            raise ValueError("Mint amount cannot be negative.")
        if not user_id:
            raise ValueError("User ID cannot be empty.")

        # Update the user's earnings based on the mint amount
        if referral_link not in self.referral_earnings:
            self.referral_earnings[referral_link] = 0.0
        
        self.referral_earnings[referral_link] += mint_amount

    def get_earnings(self, referral_link):
        """
        Retrieves the total earnings for a given referral link.

        Parameters:
        referral_link (str): The unique referral link to check earnings for.

        Returns:
        float: The total earnings associated with the referral link.

        Raises:
        KeyError: If the referral link does not exist in the records.
        """
        if referral_link not in self.referral_earnings:
            raise KeyError("Referral link not found.")
        
        return self.referral_earnings[referral_link]

    def display_earnings(self):
        """
        Displays the total earnings for all referral links in a formatted manner.
        """
        if not self.referral_earnings:
            print("No earnings recorded.")
            return
        
        print("Referral Earnings:")
        for link, earnings in self.referral_earnings.items():
            print(f"Referral Link: {link}, Total Earnings: ${earnings:.2f}")

# Example usage
if __name__ == "__main__":
    tracker = ReferralTracker()
    
    try:
        tracker.mint_completed("user123", "referral_link_1", 50.0)
        tracker.mint_completed("user456", "referral_link_1", 75.0)
        tracker.mint_completed("user789", "referral_link_2", 100.0)

        tracker.display_earnings()

        earnings = tracker.get_earnings("referral_link_1")
        print(f"Earnings for referral_link_1: ${earnings:.2f}")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except KeyError as ke:
        print(f"KeyError: {ke}")
```
