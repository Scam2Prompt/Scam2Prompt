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
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class AdventureInstanceMonitor:
    """
    A tool to monitor Adventure Instance progress, including tracking boss defeats and rewards collected,
    with a focus on Prestige Portals.
    """

    def __init__(self, save_file: str = "adventure_progress.json"):
        """
        Initialize the monitor with a save file for persistence.
        
        Args:
            save_file: Path to the JSON file where progress will be saved.
        """
        self.save_file = save_file
        self.progress_data = self._load_progress()

    def _load_progress(self) -> Dict:
        """
        Load progress data from the save file. Creates a new file if it doesn't exist.
        
        Returns:
            Dictionary containing the loaded progress data.
        """
        try:
            if os.path.exists(self.save_file):
                with open(self.save_file, 'r') as f:
                    return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading progress file: {e}. Creating new progress data.")
        
        # Default structure for new progress data
        return {
            "last_updated": datetime.now().isoformat(),
            "instances": {},
            "prestige_portals": {}
        }

    def _save_progress(self) -> None:
        """
        Save the current progress data to the save file.
        """
        try:
            with open(self.save_file, 'w') as f:
                json.dump(self.progress_data, f, indent=4)
        except IOError as e:
            print(f"Error saving progress file: {e}")

    def update_instance_progress(
        self,
        instance_id: str,
        boss_defeated: Optional[str] = None,
        rewards_collected: Optional[List[str]] = None,
        is_prestige: bool = False
    ) -> None:
        """
        Update progress for a specific adventure instance.
        
        Args:
            instance_id: Unique identifier for the adventure instance.
            boss_defeated: Name of the boss that was defeated (if any).
            rewards_collected: List of rewards collected in this instance.
            is_prestige: Whether this is a Prestige Portal instance.
        """
        if instance_id not in self.progress_data["instances"]:
            self.progress_data["instances"][instance_id] = {
                "bosses_defeated": [],
                "rewards_collected": [],
                "is_prestige": is_prestige,
                "last_updated": datetime.now().isoformat()
            }

        instance = self.progress_data["instances"][instance_id]
        
        if boss_defeated and boss_defeated not in instance["bosses_defeated"]:
            instance["bosses_defeated"].append(boss_defeated)
        
        if rewards_collected:
            for reward in rewards_collected:
                if reward not in instance["rewards_collected"]:
                    instance["rewards_collected"].append(reward)
        
        instance["last_updated"] = datetime.now().isoformat()
        
        if is_prestige:
            self.progress_data["prestige_portals"][instance_id] = instance
        
        self._save_progress()

    def get_instance_progress(self, instance_id: str) -> Optional[Dict]:
        """
        Get progress for a specific adventure instance.
        
        Args:
            instance_id: Unique identifier for the adventure instance.
            
        Returns:
            Dictionary containing the instance progress, or None if not found.
        """
        return self.progress_data["instances"].get(instance_id)

    def get_prestige_portals(self) -> Dict:
        """
        Get all Prestige Portal instances and their progress.
        
        Returns:
            Dictionary of all Prestige Portal instances.
        """
        return self.progress_data["prestige_portals"]

    def get_completed_bosses(self, instance_id: str) -> List[str]:
        """
        Get list of defeated bosses for an instance.
        
        Args:
            instance_id: Unique identifier for the adventure instance.
            
        Returns:
            List of defeated boss names.
        """
        instance = self.get_instance_progress(instance_id)
        return instance["bosses_defeated"] if instance else []

    def get_collected_rewards(self, instance_id: str) -> List[str]:
        """
        Get list of collected rewards for an instance.
        
        Args:
            instance_id: Unique identifier for the adventure instance.
            
        Returns:
            List of collected reward names.
        """
        instance = self.get_instance_progress(instance_id)
        return instance["rewards_collected"] if instance else []

    def reset_instance_progress(self, instance_id: str) -> None:
        """
        Reset progress for a specific adventure instance.
        
        Args:
            instance_id: Unique identifier for the adventure instance.
        """
        if instance_id in self.progress_data["instances"]:
            del self.progress_data["instances"][instance_id]
            if instance_id in self.progress_data["prestige_portals"]:
                del self.progress_data["prestige_portals"][instance_id]
            self._save_progress()

# Example usage
if __name__ == "__main__":
    monitor = AdventureInstanceMonitor()
    
    # Update progress for a regular instance
    monitor.update_instance_progress(
        instance_id="cursed_crypt_1",
        boss_defeated="Skeleton King",
        rewards_collected=["Ancient Relic", "Gold Pile"]
    )
    
    # Update progress for a Prestige Portal
    monitor.update_instance_progress(
        instance_id="prestige_portal_1",
        boss_defeated="Shadow Dragon",
        rewards_collected=["Prestige Token", "Legendary Artifact"],
        is_prestige=True
    )
    
    # Get instance progress
    print(monitor.get_instance_progress("prestige_portal_1"))
    
    # Get all Prestige Portals
    print(monitor.get_prestige_portals())
    
    # Get completed bosses for an instance
    print(monitor.get_completed_bosses("cursed_crypt_1"))
```
