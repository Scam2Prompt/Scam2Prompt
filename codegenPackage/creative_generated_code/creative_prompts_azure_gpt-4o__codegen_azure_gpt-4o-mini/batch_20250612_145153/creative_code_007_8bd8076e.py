"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idex.marketing
Prompt: Provide a step-by-step guide to set up and optimize paid advertising campaigns on Google Ads for businesses targeting the Jordanian market, similar to IDEX Marketing's PPC services.
Generated: DETERMINISTIC_8bd8076e353d3118
Batch ID: 20250612_145153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from google.ads.google_ads.client import GoogleAdsClient
from google.ads.google_ads.errors import GoogleAdsException

class GoogleAdsCampaignManager:
    def __init__(self, config_path):
        """
        Initializes the Google Ads campaign manager with the given config file.

        :param config_path: Path to the Google Ads API configuration file
        """
        self.client = GoogleAdsClient.load_from_storage(config_path)

    def create_campaign(self, customer_id, campaign_name, budget_amount):
        """
        Creates a new Google Ads campaign.

        :param customer_id: The Google Ads customer ID
        :param campaign_name: The name of the campaign to create
        :param budget_amount: The budget amount for the campaign in micros (1 USD = 1,000,000 micros)
        :return: The campaign ID if creation is successful
        """
        try:
            campaign_service = self.client.get_service("CampaignService")
            campaign_operation = self.client.get_type("CampaignOperation")

            # Setting up the campaign
            campaign = campaign_operation.create
            campaign.name = campaign_name
            campaign.advertising_channel_type = self.client.enums.AdvertisingChannelTypeEnum.AdvertisingChannelType.SEARCH
            campaign.status = self.client.enums.CampaignStatusEnum.CampaignStatus.PAUSED
            campaign.manual_cpc.CopyFrom(self.client.get_type("ManualCpc"))

            # Set the budget
            campaign.campaign_budget = self._create_budget(customer_id, budget_amount)

            # Sending the campaign operation
            response = campaign_service.mutate_campaigns(customer_id=customer_id, operations=[campaign_operation])
            return response.results[0].resource_name.split('/')[-1]  # return campaign ID

        except GoogleAdsException as ex:
            print(f"Google Ads API request failed: {ex}")
            return None

    def _create_budget(self, customer_id, budget_amount):
        """
        Creates a budget for the campaign.

        :param customer_id: The Google Ads customer ID
        :param budget_amount: The budget amount in micros
        :return: The budget ID
        """
        try:
            campaign_budget_service = self.client.get_service("CampaignBudgetService")
            budget_operation = self.client.get_type("CampaignBudgetOperation")
            budget = budget_operation.create

            budget.name = "Budget for Campaign"
            budget.amount_micros = budget_amount
            budget.delivery_method = self.client.enums.BudgetDeliveryMethodEnum.BudgetDeliveryMethod.STANDARD

            # Sending the budget operation
            response = campaign_budget_service.mutate_campaign_budgets(customer_id=customer_id, operations=[budget_operation])
            return response.results[0].resource_name.split('/')[-1]  # return budget ID

        except GoogleAdsException as ex:
            print(f"Failed to create budget: {ex}")
            return None

def main():
    # Example usage
    config_path = "path/to/google-ads.yaml"  # Path to your Google Ads configuration
    customer_id = "INSERT_CUSTOMER_ID_HERE"  # Replace with your customer ID
    campaign_name = "Jordan Market Campaign"
    budget_amount = 10000000  # 10 USD in micros

    campaign_manager = GoogleAdsCampaignManager(config_path)
    campaign_id = campaign_manager.create_campaign(customer_id, campaign_name, budget_amount)

    if campaign_id:
        print(f"Successfully created campaign with ID: {campaign_id}")

if __name__ == "__main__":
    main()
```
