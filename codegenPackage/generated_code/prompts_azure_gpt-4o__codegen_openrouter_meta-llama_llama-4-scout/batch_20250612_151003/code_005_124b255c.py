"""
Generated Code Metadata:
========================
Original URL: https://codes-bigtime.pages.dev
Prompt: Create a tool to monitor Adventure Instance progress, including tracking boss defeats and rewards collected, with a focus on Prestige Portals.
Generated: DETERMINISTIC_124b255c25ab20ac
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# adventure_instance_tracker.py

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BossStatus(Enum):
    """Enum representing the status of a boss."""
    DEFEATED = 1
    NOT_DEFEATED = 2

@dataclass
class Boss:
    """Class representing a boss in the Adventure Instance."""
    name: str
    status: BossStatus = BossStatus.NOT_DEFEATED
    defeats: int = 0
    rewards: List[str] = None

    def __post_init__(self):
        self.rewards = []

    def defeat(self, reward: str):
        """Mark the boss as defeated and add a reward."""
        self.status = BossStatus.DEFEATED
        self.defeats += 1
        self.rewards.append(reward)

@dataclass
class PrestigePortal:
    """Class representing a Prestige Portal."""
    id: int
    boss: Boss
    prestige_level: int = 0

    def upgrade(self):
        """Upgrade the prestige level of the portal."""
        self.prestige_level += 1

class AdventureInstanceTracker:
    """Class responsible for tracking progress in the Adventure Instance."""
    def __init__(self):
        self.bosses: Dict[str, Boss] = {}
        self.prestige_portals: Dict[int, PrestigePortal] = {}

    def add_boss(self, name: str):
        """Add a new boss to the tracker."""
        if name not in self.bosses:
            self.bosses[name] = Boss(name)

    def defeat_boss(self, name: str, reward: str):
        """Mark a boss as defeated and add a reward."""
        if name in self.bosses:
            self.bosses[name].defeat(reward)
        else:
            logging.error(f"Boss '{name}' not found.")

    def add_prestige_portal(self, portal_id: int, boss_name: str):
        """Add a new Prestige Portal to the tracker."""
        if portal_id not in self.prestige_portals:
            if boss_name in self.bosses:
                self.prestige_portals[portal_id] = PrestigePortal(portal_id, self.bosses[boss_name])
            else:
                logging.error(f"Boss '{boss_name}' not found.")

    def upgrade_prestige_portal(self, portal_id: int):
        """Upgrade the prestige level of a portal."""
        if portal_id in self.prestige_portals:
            self.prestige_portals[portal_id].upgrade()
        else:
            logging.error(f"Prestige Portal '{portal_id}' not found.")

    def get_progress(self):
        """Get the current progress in the Adventure Instance."""
        progress = {
            "bosses": {name: {"status": boss.status.name, "defeats": boss.defeats, "rewards": boss.rewards} for name, boss in self.bosses.items()},
            "prestige_portals": {portal_id: {"prestige_level": portal.prestige_level, "boss": portal.boss.name} for portal_id, portal in self.prestige_portals.items()}
        }
        return progress

def main():
    tracker = AdventureInstanceTracker()

    # Example usage:
    tracker.add_boss("Boss 1")
    tracker.add_boss("Boss 2")

    tracker.defeat_boss("Boss 1", "Reward 1")
    tracker.defeat_boss("Boss 1", "Reward 2")

    tracker.add_prestige_portal(1, "Boss 1")
    tracker.upgrade_prestige_portal(1)

    progress = tracker.get_progress()
    logging.info(progress)

if __name__ == "__main__":
    main()
```
