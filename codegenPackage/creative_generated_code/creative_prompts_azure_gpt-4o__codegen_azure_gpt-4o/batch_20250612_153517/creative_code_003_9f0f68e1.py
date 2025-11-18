"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monarch-game.pages.dev
Prompt: Write a function in Python to simulate the leveling-up process in the Monarch Dungeon game, ensuring the rarity is determined by on-chain activity rather than pre-defined traits.
Generated: DETERMINISTIC_9f0f68e1d358f8f5
Batch ID: 20250612_153517
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.blockchain-game.com/activity": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import requests
import json
from typing import Tuple

def simulate_level_up(player_id: str, on_chain_activity_url: str) -> Tuple[str, str]:
    """
    Simulates the leveling-up process in the Monarch Dungeon game.

    Args:
        player_id (str): The ID of the player leveling up.
        on_chain_activity_url (str): The API endpoint or URL to fetch the on-chain activity.

    Returns:
        Tuple[str, str]: A tuple containing the new player level and the rarity status.

    Raises:
        ValueError: If the player ID or on-chain activity data is invalid.
        Exception: For network errors or unexpected errors.
    """
    try:
        # Validate the player ID format (example validation, can be updated as needed)
        if not player_id or not isinstance(player_id, str) or len(player_id.strip()) == 0:
            raise ValueError("Invalid player ID.")

        # Fetch on-chain activity to determine rarity
        response = requests.get(on_chain_activity_url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch on-chain activity data. HTTP Status: {response.status_code}")

        # Parse the response JSON
        on_chain_data = response.json()
        if not isinstance(on_chain_data, dict) or "activity_hash" not in on_chain_data:
            raise ValueError("Invalid on-chain activity data format.")

        # Use a hash of on-chain activity to simulate rarity
        activity_hash = on_chain_data["activity_hash"]  # Example: '0xabc123...'
        rarity_hash = hashlib.sha256(activity_hash.encode()).hexdigest()

        # Determine rarity based on hash value
        rarity = "Common"
        if int(rarity_hash, 16) % 100 < 5:
            rarity = "Legendary"
        elif int(rarity_hash, 16) % 100 < 20:
            rarity = "Epic"
        elif int(rarity_hash, 16) % 100 < 50:
            rarity = "Rare"

        # Simulate level-up based on rarity (example logic)
        current_level = 1  # In a real implementation, this would be fetched from player data
        new_level = current_level + 1
        if rarity == "Legendary":
            new_level += 2
        elif rarity == "Epic":
            new_level += 1

        return str(new_level), rarity

    except ValueError as ve:
        raise ve  # Re-raise ValueError with details for client-side handling
    except requests.RequestException as re:
        raise Exception(f"Network error: {re}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")

# Example usage:
# Ensure that you replace `player_id` and `on_chain_activity_url` with real data.
# player_id = "player_123"
# on_chain_activity_url = "https://api.blockchain-game.com/activity"
# print(simulate_level_up(player_id, on_chain_activity_url))
```
