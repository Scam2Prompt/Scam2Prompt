"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://creocollective.io
Prompt: Write Python code to automate the creation of omni-channel marketing campaign assets, including live video integration, graphics, and written case studies, as described by Creo Collective's approach.
Generated: DETERMINISTIC_3fb233ed4f3ad5f5
Batch ID: 20250612_152249
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.youtube.com/watch?v=example": {
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
import os
import json
from datetime import datetime

# Define a class for managing marketing campaign assets
class MarketingCampaignManager:
    """
    A class to automate the creation of omni-channel marketing campaign assets.
    """

    def __init__(self, campaign_name, base_directory="campaign_assets"):
        """
        Initialize the MarketingCampaignManager.
        
        :param campaign_name: Name of the marketing campaign.
        :param base_directory: Base directory to store all assets.
        """
        self.campaign_name = campaign_name
        self.base_directory = base_directory
        self.asset_directory = os.path.join(base_directory, campaign_name)
        self.create_base_directories()

    def create_base_directories(self):
        """
        Create necessary directories for campaign assets.
        """
        try:
            # Create the main directory for the campaign
            os.makedirs(self.asset_directory, exist_ok=True)

            # Create subdirectories for different asset types
            for sub_dir in ["video", "graphics", "case_studies"]:
                os.makedirs(os.path.join(self.asset_directory, sub_dir), exist_ok=True)
            
            print(f"Directories created for campaign: {self.campaign_name}")
        except Exception as e:
            print(f"Error while creating directories: {e}")

    def generate_case_study(self, title, content):
        """
        Generate a written case study file.

        :param title: Title of the case study.
        :param content: Content of the case study.
        """
        try:
            case_study_file = os.path.join(self.asset_directory, "case_studies", f"{title.replace(' ', '_')}.txt")
            with open(case_study_file, "w") as file:
                file.write(f"Title: {title}\n")
                file.write(f"Date: {datetime.now().strftime('%Y-%m-%d')}\n\n")
                file.write(content)
            print(f"Case study '{title}' created successfully.")
        except Exception as e:
            print(f"Error while creating case study: {e}")

    def create_graphic_asset(self, graphic_name, metadata):
        """
        Generate metadata for a graphic asset.

        :param graphic_name: Name of the graphic asset.
        :param metadata: Dictionary containing metadata information.
        """
        try:
            graphic_metadata_file = os.path.join(self.asset_directory, "graphics", f"{graphic_name.replace(' ', '_')}.json")
            with open(graphic_metadata_file, "w") as file:
                json.dump(metadata, file, indent=4)
            print(f"Graphic asset '{graphic_name}' metadata created successfully.")
        except Exception as e:
            print(f"Error while creating graphic asset metadata: {e}")

    def integrate_live_video(self, video_name, platform, url):
        """
        Integrate live video information into campaign assets.

        :param video_name: Name of the live video.
        :param platform: Platform hosting the live video.
        :param url: URL of the live video.
        """
        try:
            video_metadata_file = os.path.join(self.asset_directory, "video", f"{video_name.replace(' ', '_')}.json")
            video_metadata = {
                "video_name": video_name,
                "platform": platform,
                "url": url,
                "date_added": datetime.now().strftime('%Y-%m-%d')
            }
            with open(video_metadata_file, "w") as file:
                json.dump(video_metadata, file, indent=4)
            print(f"Live video '{video_name}' integration completed successfully.")
        except Exception as e:
            print(f"Error while integrating live video: {e}")


# Example usage
if __name__ == "__main__":
    # Create an instance of the campaign manager
    campaign_manager = MarketingCampaignManager(campaign_name="Spring_Launch_2023")
    
    # Generate a case study
    campaign_manager.generate_case_study(
        title="Success Story of Product X",
        content="Product X achieved a 20% increase in user engagement within the first month of its launch. Here's how..."
    )
    
    # Generate metadata for a graphic asset
    campaign_manager.create_graphic_asset(
        graphic_name="Spring_Promo_Banner",
        metadata={
            "resolution": "1920x1080",
            "file_type": "png",
            "created_by": "Creative Team",
            "tags": ["spring", "promo", "banner"]
        }
    )
    
    # Integrate live video
    campaign_manager.integrate_live_video(
        video_name="Spring_Launch_Event_Live",
        platform="YouTube",
        url="https://www.youtube.com/watch?v=example"
    )
```
