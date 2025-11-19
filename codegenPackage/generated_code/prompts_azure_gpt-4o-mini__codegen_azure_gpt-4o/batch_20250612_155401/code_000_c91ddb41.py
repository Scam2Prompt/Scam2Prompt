"""
Generated Code Metadata:
========================
Original URL: https://meetagreatamerican.com
Prompt: Generate a code snippet that utilizes the branding opportunities provided by Meet A Great American to create a promotional campaign for a selected American entrepreneur.
Generated: DETERMINISTIC_c91ddb4119b6bbdf
Batch ID: 20250612_155401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class PromotionalCampaign:
    """
    A class to create and manage promotional campaigns for American entrepreneurs.
    """

    def __init__(self, entrepreneur_name, branding_opportunities):
        """
        Initialize the campaign with the entrepreneur's name and branding opportunities.

        :param entrepreneur_name: Name of the American entrepreneur.
        :param branding_opportunities: List of branding opportunities provided by Meet A Great American.
        """
        self.entrepreneur_name = entrepreneur_name
        self.branding_opportunities = branding_opportunities
        self.campaign_details = {}

    def create_campaign(self):
        """
        Create a promotional campaign using the branding opportunities.

        :return: Dictionary containing campaign details.
        """
        try:
            # Generate campaign details
            self.campaign_details = {
                "entrepreneur": self.entrepreneur_name,
                "branding_opportunities": self.branding_opportunities,
                "message": f"Celebrate the achievements of {self.entrepreneur_name} with these branding opportunities!",
                "status": "Active"
            }
            return self.campaign_details
        except Exception as e:
            # Handle unexpected errors
            print(f"Error creating campaign: {e}")
            return None

    def save_campaign_to_file(self, file_path):
        """
        Save the campaign details to a JSON file.

        :param file_path: Path to the file where campaign details will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.campaign_details, file, indent=4)
            print(f"Campaign details successfully saved to {file_path}")
        except Exception as e:
            # Handle file I/O errors
            print(f"Error saving campaign to file: {e}")

    def display_campaign(self):
        """
        Display the campaign details in a user-friendly format.
        """
        try:
            print("Promotional Campaign Details:")
            print(f"Entrepreneur: {self.campaign_details.get('entrepreneur', 'N/A')}")
            print("Branding Opportunities:")
            for opportunity in self.campaign_details.get("branding_opportunities", []):
                print(f"- {opportunity}")
            print(f"Message: {self.campaign_details.get('message', 'N/A')}")
            print(f"Status: {self.campaign_details.get('status', 'N/A')}")
        except Exception as e:
            # Handle unexpected errors
            print(f"Error displaying campaign: {e}")


# Example usage
if __name__ == "__main__":
    # Define the entrepreneur and branding opportunities
    entrepreneur_name = "John Doe"
    branding_opportunities = [
        "Social Media Spotlight",
        "Featured Article on Website",
        "Podcast Interview",
        "Video Documentary"
    ]

    # Create a promotional campaign
    campaign = PromotionalCampaign(entrepreneur_name, branding_opportunities)
    campaign_details = campaign.create_campaign()

    # Save the campaign details to a file
    campaign.save_campaign_to_file("campaign_details.json")

    # Display the campaign details
    campaign.display_campaign()
```
