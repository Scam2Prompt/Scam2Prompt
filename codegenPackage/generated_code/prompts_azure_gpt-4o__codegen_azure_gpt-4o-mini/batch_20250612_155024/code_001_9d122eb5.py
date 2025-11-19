"""
Generated Code Metadata:
========================
Original URL: https://parallels.top
Prompt: Create a function that boosts in-game earnings based on the ownership of specific digital assets, such as Avatars, as described in the Parallel TCG system.
Generated: DETERMINISTIC_9d122eb5ad43e4b1
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DigitalAsset:
    """
    A class to represent a digital asset in the game.
    Attributes:
        asset_id (str): Unique identifier for the asset.
        asset_type (str): Type of the asset (e.g., 'Avatar').
        boost_factor (float): The boost factor associated with the asset.
    """

    def __init__(self, asset_id: str, asset_type: str, boost_factor: float):
        self.asset_id = asset_id
        self.asset_type = asset_type
        self.boost_factor = boost_factor


class Player:
    """
    A class to represent a player in the game.
    Attributes:
        player_id (str): Unique identifier for the player.
        base_earnings (float): The base earnings of the player.
        assets (list): List of digital assets owned by the player.
    """

    def __init__(self, player_id: str, base_earnings: float):
        self.player_id = player_id
        self.base_earnings = base_earnings
        self.assets = []

    def add_asset(self, asset: DigitalAsset):
        """Adds a digital asset to the player's collection."""
        self.assets.append(asset)

    def calculate_boosted_earnings(self) -> float:
        """
        Calculates the boosted earnings based on the player's assets.
        Returns:
            float: The total boosted earnings.
        """
        total_boost = 1.0  # Start with a base multiplier of 1.0
        for asset in self.assets:
            if asset.asset_type == 'Avatar':
                total_boost *= (1 + asset.boost_factor)

        boosted_earnings = self.base_earnings * total_boost
        return boosted_earnings


def main():
    """
    Main function to demonstrate the functionality of the Player and DigitalAsset classes.
    """
    try:
        # Create a player with a base earning of 100
        player = Player(player_id="player1", base_earnings=100.0)

        # Create some digital assets
        avatar1 = DigitalAsset(asset_id="avatar1", asset_type="Avatar", boost_factor=0.2)  # 20% boost
        avatar2 = DigitalAsset(asset_id="avatar2", asset_type="Avatar", boost_factor=0.15)  # 15% boost

        # Add assets to the player
        player.add_asset(avatar1)
        player.add_asset(avatar2)

        # Calculate boosted earnings
        boosted_earnings = player.calculate_boosted_earnings()
        print(f"Boosted earnings for {player.player_id}: {boosted_earnings:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
