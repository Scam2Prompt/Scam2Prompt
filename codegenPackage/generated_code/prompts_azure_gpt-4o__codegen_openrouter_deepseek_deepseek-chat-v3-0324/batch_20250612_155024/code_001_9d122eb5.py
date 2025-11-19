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
from typing import Dict, List, Optional

class DigitalAsset:
    """
    Represents a digital asset that can boost in-game earnings.
    
    Attributes:
        asset_id (str): Unique identifier for the asset.
        asset_type (str): Type of the asset (e.g., 'Avatar', 'Weapon').
        boost_multiplier (float): Multiplier applied to earnings.
        is_active (bool): Whether the asset is currently active.
    """
    def __init__(self, asset_id: str, asset_type: str, boost_multiplier: float, is_active: bool = True):
        self.asset_id = asset_id
        self.asset_type = asset_type
        self.boost_multiplier = boost_multiplier
        self.is_active = is_active

class Player:
    """
    Represents a player with owned digital assets.
    
    Attributes:
        player_id (str): Unique identifier for the player.
        owned_assets (Dict[str, DigitalAsset]): Dictionary of owned assets by asset_id.
    """
    def __init__(self, player_id: str):
        self.player_id = player_id
        self.owned_assets: Dict[str, DigitalAsset] = {}

    def add_asset(self, asset: DigitalAsset) -> None:
        """Adds a digital asset to the player's collection."""
        if asset.asset_id in self.owned_assets:
            raise ValueError(f"Asset with ID {asset.asset_id} already owned by player.")
        self.owned_assets[asset.asset_id] = asset

    def remove_asset(self, asset_id: str) -> None:
        """Removes a digital asset from the player's collection."""
        if asset_id not in self.owned_assets:
            raise KeyError(f"Asset with ID {asset_id} not found in player's collection.")
        del self.owned_assets[asset_id]

    def get_active_assets(self) -> List[DigitalAsset]:
        """Returns a list of active assets owned by the player."""
        return [asset for asset in self.owned_assets.values() if asset.is_active]

def calculate_boosted_earnings(base_earnings: float, player: Player, asset_type: Optional[str] = None) -> float:
    """
    Calculates boosted earnings based on player's active digital assets.
    
    Args:
        base_earnings (float): The base earnings before boosts.
        player (Player): The player whose assets will be considered.
        asset_type (Optional[str]): Filter assets by type (e.g., 'Avatar'). If None, all assets are considered.
    
    Returns:
        float: The total earnings after applying all active boosts.
    
    Raises:
        ValueError: If base_earnings is negative.
    """
    if base_earnings < 0:
        raise ValueError("Base earnings cannot be negative.")
    
    active_assets = player.get_active_assets()
    if asset_type:
        active_assets = [asset for asset in active_assets if asset.asset_type == asset_type]
    
    total_multiplier = 1.0
    for asset in active_assets:
        total_multiplier *= asset.boost_multiplier
    
    return base_earnings * total_multiplier
```
