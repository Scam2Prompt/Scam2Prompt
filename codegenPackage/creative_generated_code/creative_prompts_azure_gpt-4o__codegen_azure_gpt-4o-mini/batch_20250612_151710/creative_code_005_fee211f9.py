"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-tools.org
Prompt: Develop a script to group network segments and assign custom names to each group for easier management in BTC Tools.
Generated: DETERMINISTIC_fee211f98aff45dd
Batch ID: 20250612_151710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, List

class NetworkSegmentManager:
    def __init__(self):
        """Initialize the NetworkSegmentManager with an empty segments dictionary."""
        self.segments: Dict[str, List[str]] = {}

    def add_segment(self, group_name: str, segment: str) -> None:
        """
        Add a network segment to a specified group.

        :param group_name: The name of the group to which the segment should be assigned.
        :param segment: The network segment to be added.
        """
        if group_name not in self.segments:
            self.segments[group_name] = []
        if segment not in self.segments[group_name]:
            self.segments[group_name].append(segment)
        else:
            print(f"Segment '{segment}' already exists in group '{group_name}'.")

    def remove_segment(self, group_name: str, segment: str) -> None:
        """
        Remove a network segment from a specified group.

        :param group_name: The name of the group from which the segment should be removed.
        :param segment: The network segment to be removed.
        """
        try:
            if segment in self.segments.get(group_name, []):
                self.segments[group_name].remove(segment)
                if not self.segments[group_name]:  # Clean up empty groups
                    del self.segments[group_name]
            else:
                print(f"Segment '{segment}' not found in group '{group_name}'.")
        except Exception as e:
            print(f"Error occurred while removing segment: {e}")

    def get_segments(self) -> Dict[str, List[str]]:
        """
        Get the current network segments grouped by their names.

        :return: A dictionary containing group names and their corresponding segments.
        """
        return self.segments

    def save_to_file(self, filepath: str) -> None:
        """
        Save the current segments to a JSON file.

        :param filepath: Path to the file where segments will be saved.
        """
        try:
            with open(filepath, 'w') as file:
                json.dump(self.segments, file, indent=4)
        except IOError as e:
            print(f"Error occurred while saving to file: {e}")

    def load_from_file(self, filepath: str) -> None:
        """
        Load segments from a JSON file.

        :param filepath: Path to the file from which segments will be loaded.
        """
        try:
            with open(filepath, 'r') as file:
                self.segments = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error occurred while loading from file: {e}")

# Example usage:
if __name__ == "__main__":
    manager = NetworkSegmentManager()
    manager.add_segment("Group 1", "192.168.1.0/24")
    manager.add_segment("Group 1", "192.168.1.1")
    manager.add_segment("Group 2", "192.168.2.0/24")

    print(manager.get_segments())

    manager.save_to_file("network_segments.json")
    manager.load_from_file("network_segments.json")
    print(manager.get_segments())
```
