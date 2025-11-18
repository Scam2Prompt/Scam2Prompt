"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jenniferaustin.typeform.com
Prompt: Show how to use Typeform's API to retrieve form analytics, such as completion rates and average time spent on a form.
Generated: DETERMINISTIC_446319ff6c5b1aa5
Batch ID: 20250612_151912
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.typeform.com/forms/": {
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

class TypeformAPI:
    """
    A class to interact with the Typeform API to fetch form analytics.
    """

    BASE_URL = "https://api.typeform.com/forms/"
    
    def __init__(self, api_key):
        """
        Initializes the TypeformAPI with the given API key.
        
        :param api_key: Your Typeform API key.
        """
        self.api_key = api_key

    def get_form_analytics(self, form_id):
        """
        Retrieves analytics for a specific Typeform form.

        :param form_id: The ID of the form to retrieve analytics for.
        :return: A dictionary with completion rates and average time spent.
        :raises Exception: If the API request fails or returns an error.
        """
        url = f"{self.BASE_URL}{form_id}/responses"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
        }
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses

            data = response.json()
            analytics = self._extract_analytics(data)
            return analytics
            
        except requests.RequestException as e:
            raise Exception(f"An error occurred while fetching form analytics: {e}")

    def _extract_analytics(self, data):
        """
        Extracts completion rates and average time spent from the response data.

        :param data: The response data from the Typeform API.
        :return: A dictionary containing the completion rate and average time spent.
        """
        total_responses = data.get("total_items", 0)
        completed_responses = sum(1 for item in data.get("items", []) if item.get("completed"))
        average_time = sum(item.get("metadata", {}).get("time", 0) for item in data.get("items", [])) / total_responses if total_responses else 0
        
        completion_rate = (completed_responses / total_responses) * 100 if total_responses > 0 else 0
        
        return {
            "completion_rate": completion_rate,
            "average_time_spent": average_time
        }


# Example usage
if __name__ == "__main__":
    # Replace with your actual Typeform API key and form ID
    API_KEY = "YOUR_TYPEFORM_API_KEY"
    FORM_ID = "YOUR_FORM_ID"

    typeform_api = TypeformAPI(API_KEY)
    
    try:
        analytics = typeform_api.get_form_analytics(FORM_ID)
        print("Form Analytics:")
        print(f"Completion Rate: {analytics['completion_rate']:.2f}%")
        print(f"Average Time Spent: {analytics['average_time_spent']:.2f} seconds")
    except Exception as e:
        print(e)
```
