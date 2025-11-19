"""
Generated Code Metadata:
========================
Original URL: https://ator-dashboard.pages.dev
Prompt: Develop a basic token distribution system with rewards for active relays on a network.
Generated: DETERMINISTIC_2ef7908d3df5e839
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# token_distribution_system.py

import hashlib
import logging
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Relay:
    """Represents a relay on the network."""
    
    def __init__(self, id: str, active: bool = True):
        """
        Initializes a Relay object.

        Args:
        id (str): Unique identifier for the relay.
        active (bool): Whether the relay is active. Defaults to True.
        """
        self.id = id
        self.active = active
        self.rewards = 0

class TokenDistributionSystem:
    """Manages token distribution and rewards for active relays."""
    
    def __init__(self, total_tokens: int):
        """
        Initializes a TokenDistributionSystem object.

        Args:
        total_tokens (int): Total number of tokens to distribute.
        """
        self.total_tokens = total_tokens
        self.relays: Dict[str, Relay] = {}
        self.token_distribution: Dict[str, int] = {}

    def add_relay(self, relay: Relay):
        """
        Adds a relay to the system.

        Args:
        relay (Relay): Relay object to add.
        """
        self.relays[relay.id] = relay

    def remove_relay(self, relay_id: str):
        """
        Removes a relay from the system.

        Args:
        relay_id (str): ID of the relay to remove.

        Raises:
        KeyError: If the relay ID does not exist.
        """
        if relay_id not in self.relays:
            raise KeyError(f"Relay {relay_id} does not exist")
        del self.relays[relay_id]

    def distribute_tokens(self):
        """
        Distributes tokens to active relays based on their activity.

        Returns:
        Dict[str, int]: Token distribution for each relay.
        """
        active_relays = [relay for relay in self.relays.values() if relay.active]
        total_rewards = self.total_tokens // len(active_relays) if active_relays else 0

        for relay in active_relays:
            relay.rewards += total_rewards
            self.token_distribution[relay.id] = relay.rewards

        return self.token_distribution

    def deactivate_relay(self, relay_id: str):
        """
        Deactivates a relay.

        Args:
        relay_id (str): ID of the relay to deactivate.

        Raises:
        KeyError: If the relay ID does not exist.
        """
        if relay_id not in self.relays:
            raise KeyError(f"Relay {relay_id} does not exist")
        self.relays[relay_id].active = False

    def activate_relay(self, relay_id: str):
        """
        Activates a relay.

        Args:
        relay_id (str): ID of the relay to activate.

        Raises:
        KeyError: If the relay ID does not exist.
        """
        if relay_id not in self.relays:
            raise KeyError(f"Relay {relay_id} does not exist")
        self.relays[relay_id].active = True


def main():
    # Create a token distribution system with 1000 tokens
    tds = TokenDistributionSystem(1000)

    # Create relays
    relay1 = Relay("relay1")
    relay2 = Relay("relay2")
    relay3 = Relay("relay3")

    # Add relays to the system
    tds.add_relay(relay1)
    tds.add_relay(relay2)
    tds.add_relay(relay3)

    # Distribute tokens
    distribution = tds.distribute_tokens()
    logger.info("Initial Token Distribution:")
    for relay_id, tokens in distribution.items():
        logger.info(f"Relay {relay_id}: {tokens} tokens")

    # Deactivate a relay
    tds.deactivate_relay("relay2")

    # Distribute tokens again
    distribution = tds.distribute_tokens()
    logger.info("\nToken Distribution after deactivating relay2:")
    for relay_id, tokens in distribution.items():
        logger.info(f"Relay {relay_id}: {tokens} tokens")

if __name__ == "__main__":
    main()
```
