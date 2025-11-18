"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim.bondex.digital
Prompt: Write code to check if a wallet is linked to a Bondex profile at the time of the snapshot and display eligibility status for $BDXN token claims.
Generated: DETERMINISTIC_7ce73c84cb1aa965
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class BondexProfile:
    """
    Represents a Bondex profile with a linked wallet and snapshot details.
    """
    def __init__(self, profile_id, linked_wallet, snapshot_date):
        self.profile_id = profile_id
        self.linked_wallet = linked_wallet  # Wallet address linked to the profile
        self.snapshot_date = snapshot_date  # Snapshot date for eligibility verification


def check_eligibility(profile, snapshot_datetime):
    """
    Checks if a wallet is linked to the Bondex profile at the time of the snapshot.

    Args:
        profile (BondexProfile): The Bondex profile object to be checked.
        snapshot_datetime (datetime.datetime): The snapshot time to check eligibility against.

    Returns:
        str: Eligibility status message.
    """
    try:
        # Ensure the snapshot date is valid
        if not isinstance(snapshot_datetime, datetime.datetime):
            raise ValueError("Invalid snapshot datetime provided.")

        # Ensure the profile contains valid data
        if not profile.linked_wallet:
            return f"Profile {profile.profile_id} is not eligible for $BDXN token claims: No wallet linked."
        
        # Compare snapshot date with wallet linkage date
        if profile.snapshot_date <= snapshot_datetime:
            return f"Profile {profile.profile_id} is eligible for $BDXN token claims."
        else:
            return f"Profile {profile.profile_id} is not eligible for $BDXN token claims: Wallet not linked before snapshot."
    except Exception as e:
        # Handle unexpected errors gracefully
        return f"Error checking eligibility: {str(e)}"


# Example usage:
if __name__ == "__main__":
    # Define the snapshot time
    snapshot_time = datetime.datetime(2023, 10, 1, 0, 0, 0)

    # Create example Bondex profiles
    profile1 = BondexProfile(profile_id="12345", linked_wallet="0xABCDEF1234567890", snapshot_date=datetime.datetime(2023, 9, 30, 23, 59, 59))
    profile2 = BondexProfile(profile_id="67890", linked_wallet=None, snapshot_date=datetime.datetime(2023, 10, 2, 0, 0, 0))

    # Check eligibility for profiles
    print(check_eligibility(profile1, snapshot_time))  # Expected: Eligible
    print(check_eligibility(profile2, snapshot_time))  # Expected: Not eligible
```
