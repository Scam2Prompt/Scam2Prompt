"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rxtestest.web.app
Prompt: Write code to implement a pre-sale mechanism for exclusive digital assets, referencing Helio's free pre-sale model for PepePixels.
Generated: DETERMINISTIC_e7f7354c854de33c
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class PreSale:
    """
    A class to manage the pre-sale of exclusive digital assets.
    This implementation is inspired by Helio's free pre-sale model for PepePixels.
    """

    def __init__(self, asset_name: str, total_supply: int, pre_sale_start: datetime.datetime, pre_sale_end: datetime.datetime):
        """
        Initialize the pre-sale mechanism.

        :param asset_name: Name of the digital asset.
        :param total_supply: Total number of assets available for pre-sale.
        :param pre_sale_start: Start time of the pre-sale.
        :param pre_sale_end: End time of the pre-sale.
        """
        self.asset_name = asset_name
        self.total_supply = total_supply
        self.pre_sale_start = pre_sale_start
        self.pre_sale_end = pre_sale_end
        self.claimed_assets = 0
        self.claimed_users = set()  # Track unique users who claimed assets

    def is_pre_sale_active(self) -> bool:
        """
        Check if the pre-sale is currently active.

        :return: True if the pre-sale is active, False otherwise.
        """
        now = datetime.datetime.now()
        return self.pre_sale_start <= now <= self.pre_sale_end

    def claim_asset(self, user_id: str) -> str:
        """
        Claim an asset during the pre-sale.

        :param user_id: Unique identifier of the user claiming the asset.
        :return: Message indicating the result of the claim attempt.
        """
        if not self.is_pre_sale_active():
            return "Pre-sale is not active. Please try again during the pre-sale window."

        if user_id in self.claimed_users:
            return "You have already claimed an asset during the pre-sale."

        if self.claimed_assets >= self.total_supply:
            return "All assets have been claimed. Thank you for your interest!"

        # Successfully claim the asset
        self.claimed_users.add(user_id)
        self.claimed_assets += 1
        return f"Congratulations {user_id}! You have successfully claimed your {self.asset_name}."

    def get_remaining_assets(self) -> int:
        """
        Get the number of assets remaining in the pre-sale.

        :return: The number of assets still available for claim.
        """
        return self.total_supply - self.claimed_assets

# Example Usage:
if __name__ == "__main__":
    # Pre-sale parameters
    asset_name = "PepePixels"
    total_supply = 100  # Total number of digital assets available
    pre_sale_start = datetime.datetime(2023, 10, 1, 9, 0, 0)  # Pre-sale starts on October 1, 2023, at 9:00 AM
    pre_sale_end = datetime.datetime(2023, 10, 15, 18, 0, 0)  # Pre-sale ends on October 15, 2023, at 6:00 PM

    # Create a PreSale instance
    pre_sale = PreSale(asset_name, total_supply, pre_sale_start, pre_sale_end)

    # Simulate user claims
    user_id = "user123"
    print(pre_sale.claim_asset(user_id))  # Attempt to claim an asset
    print(pre_sale.get_remaining_assets())  # Check remaining assets
```
