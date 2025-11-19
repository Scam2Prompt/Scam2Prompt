"""
Generated Code Metadata:
========================
Original URL: https://novamidiapublicidade.com.br
Prompt: "Write a Python script to manage social media campaigns for a branding agency like Nova Mídia Publicidade, including scheduling posts and tracking engagement metrics."
Generated: DETERMINISTIC_d9717f712e084b31
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os


class SocialMediaCampaignManager:
    """
    A class to manage social media campaigns, including scheduling posts and tracking engagement metrics.
    """

    def __init__(self, campaign_data_file="campaigns.json"):
        """
        Initialize the campaign manager with a file to store campaign data.

        :param campaign_data_file: Path to the JSON file where campaign data will be stored.
        """
        self.campaign_data_file = campaign_data_file
        self.campaigns = self._load_campaign_data()

    def _load_campaign_data(self):
        """
        Load campaign data from the JSON file.

        :return: A dictionary containing campaign data.
        """
        if os.path.exists(self.campaign_data_file):
            try:
                with open(self.campaign_data_file, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Error: Failed to decode campaign data file. Starting with empty data.")
                return {}
        return {}

    def _save_campaign_data(self):
        """
        Save campaign data to the JSON file.
        """
        try:
            with open(self.campaign_data_file, "w") as file:
                json.dump(self.campaigns, file, indent=4)
        except Exception as e:
            print(f"Error: Failed to save campaign data. {e}")

    def schedule_post(self, campaign_name, platform, content, post_time):
        """
        Schedule a post for a specific campaign.

        :param campaign_name: Name of the campaign.
        :param platform: Social media platform (e.g., "Facebook", "Twitter").
        :param content: Content of the post.
        :param post_time: Scheduled time for the post (datetime object).
        """
        if campaign_name not in self.campaigns:
            self.campaigns[campaign_name] = {"posts": [], "engagement_metrics": {}}

        self.campaigns[campaign_name]["posts"].append({
            "platform": platform,
            "content": content,
            "post_time": post_time.isoformat()
        })

        self._save_campaign_data()
        print(f"Post scheduled for campaign '{campaign_name}' on {platform} at {post_time}.")

    def track_engagement(self, campaign_name, platform, likes, comments, shares):
        """
        Track engagement metrics for a specific campaign.

        :param campaign_name: Name of the campaign.
        :param platform: Social media platform (e.g., "Facebook", "Twitter").
        :param likes: Number of likes.
        :param comments: Number of comments.
        :param shares: Number of shares.
        """
        if campaign_name not in self.campaigns:
            print(f"Error: Campaign '{campaign_name}' does not exist.")
            return

        if platform not in self.campaigns[campaign_name]["engagement_metrics"]:
            self.campaigns[campaign_name]["engagement_metrics"][platform] = {"likes": 0, "comments": 0, "shares": 0}

        self.campaigns[campaign_name]["engagement_metrics"][platform]["likes"] += likes
        self.campaigns[campaign_name]["engagement_metrics"][platform]["comments"] += comments
        self.campaigns[campaign_name]["engagement_metrics"][platform]["shares"] += shares

        self._save_campaign_data()
        print(f"Engagement metrics updated for campaign '{campaign_name}' on {platform}.")

    def view_campaigns(self):
        """
        View all campaigns and their details.

        :return: A dictionary containing all campaign data.
        """
        return self.campaigns


# Example usage
if __name__ == "__main__":
    manager = SocialMediaCampaignManager()

    # Schedule a post
    manager.schedule_post(
        campaign_name="Brand Awareness",
        platform="Twitter",
        content="Check out our new product launch! #BrandAwareness",
        post_time=datetime.datetime(2023, 10, 15, 10, 0)
    )

    # Track engagement
    manager.track_engagement(
        campaign_name="Brand Awareness",
        platform="Twitter",
        likes=120,
        comments=45,
        shares=30
    )

    # View campaigns
    campaigns = manager.view_campaigns()
    print(json.dumps(campaigns, indent=4))
```
