"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectnetwork.lojavirtualnuvem.com.br
Prompt: Provide a Python script to manage promotional banners on an e-commerce platform, referencing the "Banners promocionais" feature described on the Connect Network website.
Generated: DETERMINISTIC_7b694d4cfe0d753a
Batch ID: 20250612_152306
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://example.com/winter-sale.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://example.com/winter-sale": {
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
import json
import os
from typing import List, Dict

class PromotionalBannerManager:
    """Class to manage promotional banners for an e-commerce platform."""

    def __init__(self, data_file: str):
        """
        Initialize the promotional banner manager.

        Args:
            data_file (str): The path to the JSON file containing banner data.
        """
        self.data_file = data_file
        self.banners = self.load_banners()

    def load_banners(self) -> List[Dict]:
        """Load banners from the JSON data file."""
        if not os.path.exists(self.data_file):
            return []

        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading banners: {e}")
            return []

    def save_banners(self):
        """Save the current banners to the JSON data file."""
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.banners, file, indent=4)
        except IOError as e:
            print(f"Error saving banners: {e}")

    def add_banner(self, banner: Dict):
        """Add a new banner to the list of banners.

        Args:
            banner (Dict): A dictionary containing banner details.
        """
        self.banners.append(banner)
        self.save_banners()

    def remove_banner(self, banner_id: str) -> bool:
        """Remove a banner by its ID.

        Args:
            banner_id (str): The ID of the banner to remove.

        Returns:
            bool: True if removal was successful, False otherwise.
        """
        for i, banner in enumerate(self.banners):
            if banner.get('id') == banner_id:
                del self.banners[i]
                self.save_banners()
                return True
        return False

    def get_banners(self) -> List[Dict]:
        """Retrieve the list of currently active banners."""
        return self.banners

    def update_banner(self, banner_id: str, updated_data: Dict) -> bool:
        """Update an existing banner.

        Args:
            banner_id (str): The ID of the banner to update.
            updated_data (Dict): A dictionary containing updated banner details.

        Returns:
            bool: True if update was successful, False otherwise.
        """
        for i, banner in enumerate(self.banners):
            if banner.get('id') == banner_id:
                self.banners[i].update(updated_data)
                self.save_banners()
                return True
        return False

# Example of how to use the class
if __name__ == "__main__":
    banner_manager = PromotionalBannerManager('banners.json')

    # Adding a new banner
    new_banner = {
        "id": "1",
        "title": "Winter Sale",
        "image_url": "http://example.com/winter-sale.jpg",
        "link": "http://example.com/winter-sale",
        "active": True
    }
    banner_manager.add_banner(new_banner)

    # Listing all banners
    print("Current Banners:", banner_manager.get_banners())

    # Updating a banner
    banner_manager.update_banner("1", {"active": False})

    # Removing a banner
    banner_manager.remove_banner("1")

    # Listing all banners again
    print("Current Banners after removal:", banner_manager.get_banners())
```
