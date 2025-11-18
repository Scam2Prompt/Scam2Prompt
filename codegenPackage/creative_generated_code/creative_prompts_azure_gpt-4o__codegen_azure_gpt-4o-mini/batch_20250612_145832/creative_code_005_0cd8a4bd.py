"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://subscribemenow.com
Prompt: Provide an example of how to use GetResponse's API to track email performance analytics and generate real-time insights.
Generated: DETERMINISTIC_0cd8a4bd6c09342d
Batch ID: 20250612_145832
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.getresponse.com/v3": {
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
from requests.exceptions import HTTPError

class GetResponseAPI:
    """
    A class to interact with GetResponse API for tracking email performance analytics.
    """

    BASE_URL = "https://api.getresponse.com/v3"
    
    def __init__(self, api_key):
        """
        Initializes the GetResponseAPI with the provided API key.
        
        :param api_key: Your GetResponse API key.
        """
        self.api_key = api_key

    def _get_headers(self):
        """
        Constructs headers for the API request.
        
        :return: Headers including the authorization token.
        """
        return {
            "Content-Type": "application/json",
            "X-Auth-Token": f"api-key {self.api_key}"
        }

    def get_email_performance(self, email_id):
        """
        Retrieves performance analytics for a given email campaign.
        
        :param email_id: The ID of the email campaign to track.
        :return: JSON response containing performance data.
        :raises HTTPError: If the API request fails.
        """
        url = f"{self.BASE_URL}/campaigns/{email_id}/analytics"
        try:
            response = requests.get(url, headers=self._get_headers())
            response.raise_for_status()  # Raises HTTPError for bad responses
            return response.json()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP error
        except Exception as err:
            print(f"An error occurred: {err}")  # Log general error

    def generate_insights(self, email_id):
        """
        Generates real-time insights from email performance analytics.
        
        :param email_id: The ID of the email campaign to analyze.
        :return: Insights summary based on performance data.
        """
        data = self.get_email_performance(email_id)
        if data:
            # Extract relevant metrics for insights
            open_rate = data.get('openRate', 0)
            click_rate = data.get('clickRate', 0)
            unsubscribes = data.get('unsubscribes', 0)

            insights = {
                "email_id": email_id,
                "open_rate": open_rate,
                "click_rate": click_rate,
                "unsubscribes": unsubscribes,
                "summary": self._generate_summary(open_rate, click_rate, unsubscribes)
            }
            return insights
        return None

    def _generate_summary(self, open_rate, click_rate, unsubscribes):
        """
        Generates a summary based on provided metrics.
        
        :param open_rate: The open rate of the email.
        :param click_rate: The click rate of the email.
        :param unsubscribes: The number of unsubscribes.
        :return: Summary string.
        """
        return f"Open Rate: {open_rate}%, Click Rate: {click_rate}%, Unsubscribes: {unsubscribes}"

# Example usage
if __name__ == "__main__":
    API_KEY = "your_getresponse_api_key"  # Replace with your actual API key
    email_id = "your_email_campaign_id"  # Replace with your actual email campaign ID

    # Create an instance of GetResponseAPI
    gr_api = GetResponseAPI(API_KEY)

    # Generate insights for the specified email campaign
    insights = gr_api.generate_insights(email_id)
    if insights:
        print(insights)
```
