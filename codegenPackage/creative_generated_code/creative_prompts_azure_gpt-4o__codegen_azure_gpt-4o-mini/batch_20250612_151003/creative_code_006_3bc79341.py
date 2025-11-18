"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codes-bigtime.pages.dev
Prompt: Generate code to redeem passes (Gold, Silver, Jade) for accessing Big Time Preseason features, ensuring validation of access levels.
Generated: DETERMINISTIC_3bc793414de91cc0
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PassType:
    """Enumeration for Pass Types."""
    GOLD = 'Gold'
    SILVER = 'Silver'
    JADE = 'Jade'


class AccessLevel:
    """Mapping of pass types to access levels."""
    ACCESS_LEVELS = {
        PassType.GOLD: 3,
        PassType.SILVER: 2,
        PassType.JADE: 1
    }


class PassRedemptionError(Exception):
    """Custom exception for pass redemption errors."""
    pass


class PassRedeemer:
    """Class to handle the redemption of passes for accessing features."""
    
    def __init__(self):
        """Initialize the PassRedeemer with no redeemed passes."""
        self.redeemed_passes = {}

    def redeem_pass(self, user_id: str, pass_type: str):
        """Redeem a pass for a user, ensuring validation of access levels.

        Args:
            user_id (str): The ID of the user redeeming the pass.
            pass_type (str): The type of pass being redeemed.

        Raises:
            PassRedemptionError: If the pass type is invalid or user already has access.
        """
        if pass_type not in AccessLevel.ACCESS_LEVELS:
            raise PassRedemptionError(f"Invalid pass type: {pass_type}")

        if user_id in self.redeemed_passes:
            raise PassRedemptionError(f"User {user_id} has already redeemed a pass.")
        
        # Redeem the pass and store the access level
        access_level = AccessLevel.ACCESS_LEVELS[pass_type]
        self.redeemed_passes[user_id] = access_level
        print(f"User {user_id} redeemed a {pass_type} pass with access level {access_level}.")

    def get_access_level(self, user_id: str) -> int:
        """Get the access level for a user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            int: The access level of the user.
        
        Raises:
            PassRedemptionError: If the user has not redeemed a pass.
        """
        if user_id not in self.redeemed_passes:
            raise PassRedemptionError(f"No pass redeemed for user {user_id}.")
        
        return self.redeemed_passes[user_id]


# Example usage
if __name__ == "__main__":
    redeemer = PassRedeemer()
    
    try:
        redeemer.redeem_pass("user123", PassType.GOLD)
        access_level = redeemer.get_access_level("user123")
        print(f"User access level: {access_level}")
        
        # Uncommenting the next line will raise an error for already redeemed pass
        # redeemer.redeem_pass("user123", PassType.SILVER)
    except PassRedemptionError as e:
        print(f"Error: {e}")
```
