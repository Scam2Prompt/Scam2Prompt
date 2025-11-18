"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.emerginggifts.com
Prompt: Recommend tools or APIs for monitoring the effectiveness of digital-first fundraising programs in emerging markets, based on Emerging Gifts' strategies.
Generated: DETERMINISTIC_7d4a31f5fb0419c5
Batch ID: 20250612_152511
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/v1": {
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
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FundraisingMonitor:
    """A class to monitor and analyze the effectiveness of digital-first fundraising programs."""
    
    def __init__(self, api_key):
        """Initialize the FundraisingMonitor with an API key."""
        self.api_key = api_key
        self.base_url = "https://api.example.com/v1"  # Replace with the actual API base URL

    def fetch_campaign_data(self, campaign_id):
        """Fetch data for a specific fundraising campaign by its ID.
        
        Args:
            campaign_id (str): The ID of the fundraising campaign.

        Returns:
            dict: The campaign data retrieved from the API.
        """
        try:
            response = requests.get(f"{self.base_url}/campaigns/{campaign_id}", headers={"Authorization": f"Bearer {self.api_key}"})
            response.raise_for_status()  # Raise an error for HTTP error responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
            return None
        except Exception as err:
            logging.error(f"An error occurred: {err}")
            return None

    def analyze_effectiveness(self, campaign_data):
        """Analyze the effectiveness of a fundraising campaign.

        Args:
            campaign_data (dict): The campaign data.

        Returns:
            dict: Analysis results including key performance indicators.
        """
        if not campaign_data:
            logging.warning("No campaign data provided for analysis.")
            return {}

        # Example analysis logic (replace with actual metrics)
        analysis_results = {
            "total_donations": sum(donation["amount"] for donation in campaign_data.get("donations", [])),
            "donor_count": len(campaign_data.get("donors", [])),
            "average_donation": sum(donation["amount"] for donation in campaign_data.get("donations", [])) / len(campaign_data.get("donations", [])) if campaign_data.get("donations") else 0,
        }
        
        logging.info(f"Analysis results: {analysis_results}")
        return analysis_results

# Example usage
if __name__ == "__main__":
    # Replace with a valid API key
    api_key = "your_api_key_here"
    monitor = FundraisingMonitor(api_key)

    # Replace with an actual campaign ID
    campaign_id = "example_campaign_id"
    campaign_data = monitor.fetch_campaign_data(campaign_id)
    effectiveness_analysis = monitor.analyze_effectiveness(campaign_data)

    # Output the results
    print("Effectiveness Analysis:", effectiveness_analysis)
```
