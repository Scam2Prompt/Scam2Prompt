"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://creocollective.io
Prompt: Write Python code to automate the creation of omni-channel marketing campaign assets, including live video integration, graphics, and written case studies, as described by Creo Collective's approach.
Generated: DETERMINISTIC_3fb233ed4f3ad5f5
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import logging
from datetime import datetime
from pathlib import Path

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CampaignAsset:
    """Class to represent a marketing campaign asset."""
    
    def __init__(self, title, asset_type, content):
        self.title = title
        self.asset_type = asset_type
        self.content = content
        self.created_at = datetime.now()

    def save(self, directory):
        """Saves the asset to the specified directory in JSON format."""
        try:
            os.makedirs(directory, exist_ok=True)
            asset_file = Path(directory) / f"{self.title.replace(' ', '_')}.json"
            with open(asset_file, 'w') as f:
                json.dump(self.__dict__, f, default=str)
            logging.info(f"Asset saved: {asset_file}")
        except Exception as e:
            logging.error(f"Error saving asset {self.title}: {e}")

class Campaign:
    """Class to represent a complete marketing campaign."""
    
    def __init__(self, name):
        self.name = name
        self.assets = []

    def add_asset(self, asset):
        """Add a new asset to the campaign."""
        if isinstance(asset, CampaignAsset):
            self.assets.append(asset)
            logging.info(f"Asset added to campaign '{self.name}': {asset.title}")
        else:
            logging.warning("Attempted to add a non-asset object.")

    def create_assets(self):
        """Creates various types of campaign assets."""
        # Example assets creation
        video_asset = CampaignAsset("Launch Video", "video", "URL_to_live_video")
        graphic_asset = CampaignAsset("Social Media Graphic", "graphic", "Graphic Content Here")
        case_study_asset = CampaignAsset("Case Study: Q4 Success", "case_study", "Detailed case study content")

        self.add_asset(video_asset)
        self.add_asset(graphic_asset)
        self.add_asset(case_study_asset)

    def save_assets(self, directory):
        """Saves all campaign assets to the specified directory."""
        for asset in self.assets:
            asset.save(directory)

def main():
    """Main function to execute the campaign asset creation."""
    campaign_name = "2023 Holiday Marketing"
    campaign_directory = "./campaign_assets"

    # Create a new campaign
    campaign = Campaign(campaign_name)
    
    # Create assets for the campaign
    campaign.create_assets()
    
    # Save all assets to the directory
    campaign.save_assets(campaign_directory)
    logging.info("All campaign assets have been created and saved.")

if __name__ == "__main__":
    main()
```
