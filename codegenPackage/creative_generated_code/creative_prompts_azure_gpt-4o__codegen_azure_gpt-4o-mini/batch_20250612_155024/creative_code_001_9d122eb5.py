"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://parallels.top
Prompt: Create a function that boosts in-game earnings based on the ownership of specific digital assets, such as Avatars, as described in the Parallel TCG system.
Generated: DETERMINISTIC_9d122eb5ad43e4b1
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DigitalAsset:
    """
    Class representing a digital asset in the Parallel TCG system.
    Attributes:
        asset_id (str): Unique identifier for the digital asset.
        asset_type (str): Type of the digital asset (e.g., 'Avatar').
        boost_multiplier (float): Multiplier for in-game earnings based on ownership.
    """

    def __init__(self, asset_id: str, asset_type: str, boost_multiplier: float):
        self.asset_id = asset_id
        self.asset_type = asset_type
        self.boost_multiplier = boost_multiplier

class Player:
    """
    Class representing a player in the game.
    Attributes:
        player_id (str): Unique identifier for the player.
        digital_assets (list): List of DigitalAsset objects owned by the player.
    """

    def __init__(self, player_id: str):
        self.player_id = player_id
        self.digital_assets = []

    def add_asset(self, asset: DigitalAsset):
        """Adds a digital asset to the player's collection."""
        self.digital_assets.append(asset)

    def calculate_earnings(self, base_earnings: float) -> float:
        """
        Calculates boosted earnings based on owned digital assets.
        
        Args:
            base_earnings (float): The base earnings before any boosts.
        
        Returns:
            float: The total earnings after applying boosts from owned assets.
        """
        if base_earnings < 0:
            raise ValueError("Base earnings must be non-negative.")

        total_boost = 1.0  # Start with a multiplier of 1 (no boost)
        
        # Calculate total boost from owned assets
        for asset in self.digital_assets:
            if asset.asset_type == 'Avatar':
                total_boost *= asset.boost_multiplier

        # Calculate and return final earnings
        boosted_earnings = base_earnings * total_boost
        return boosted_earnings

# Example usage
if __name__ == "__main__":
    try:
        # Create some digital assets
        avatar1 = DigitalAsset(asset_id="AVT001", asset_type="Avatar", boost_multiplier=1.2)
        avatar2 = DigitalAsset(asset_id="AVT002", asset_type="Avatar", boost_multiplier=1.5)

        # Create a player and add assets
        player = Player(player_id="PLAYER123")
        player.add_asset(avatar1)
        player.add_asset(avatar2)

        # Calculate boosted earnings
        base_earnings = 100.0
        boosted_earnings = player.calculate_earnings(base_earnings)
        print(f"Boosted earnings: {boosted_earnings}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
