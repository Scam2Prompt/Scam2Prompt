"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stronglp.com
Prompt: Suggest APIs for integrating nutrition coaching into a fitness app, considering Blaise Strong's certification as a Show Up Fitness Certified Nutrition Coach (SUF-NC).
Generated: DETERMINISTIC_4ff8e6809e5f9ce7
Batch ID: 20250612_145521
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.nutritionix.com/v1_1/search/{food_item": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.example.com/users/{user_id}/nutrition_plan": {
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
from typing import List, Dict, Any

class NutritionAPI:
    """
    A class to interact with various nutrition-related APIs.
    This class provides methods to fetch nutrition data and integrate it into a fitness app.
    """

    def __init__(self, api_key: str):
        """
        Initializes the NutritionAPI with an API key.

        Args:
            api_key (str): Your API key for authenticating requests.
        """
        self.api_key = api_key

    def get_nutrition_data(self, food_item: str) -> Dict[str, Any]:
        """
        Fetches nutrition data for a given food item.

        Args:
            food_item (str): The name of the food item to fetch nutrition data for.

        Returns:
            Dict[str, Any]: A dictionary containing nutrition information.

        Raises:
            Exception: If the API request fails or returns an error.
        """
        try:
            url = f"https://api.nutritionix.com/v1_1/search/{food_item}"
            params = {
                'appId': 'YOUR_APP_ID',  # Replace with your App ID
                'appKey': self.api_key,
                'fields': 'item_name,nf_calories,nf_protein,nf_total_fat,nf_sugars,nf_dietary_fiber'
            }
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an error for bad responses

            return response.json()  # Return the JSON response as a dictionary

        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")
        except Exception as err:
            raise Exception(f"An error occurred: {err}")

    def get_daily_nutrition_plan(self, user_id: str) -> List[Dict[str, Any]]:
        """
        Fetches a daily nutrition plan for a user based on their ID.

        Args:
            user_id (str): The ID of the user for whom to fetch the nutrition plan.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing meal plans.

        Raises:
            Exception: If the API request fails or returns an error.
        """
        try:
            url = f"https://api.example.com/users/{user_id}/nutrition_plan"
            headers = {'Authorization': f'Bearer {self.api_key}'}
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses

            return response.json()  # Return the JSON response as a list of meal plans

        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")
        except Exception as err:
            raise Exception(f"An error occurred: {err}")

# Example usage:
if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with an actual API key.
    nutrition_api = NutritionAPI(api_key='YOUR_API_KEY')

    # Fetch nutrition data for an item
    try:
        food_data = nutrition_api.get_nutrition_data("banana")
        print("Nutrition Data:", food_data)
    except Exception as e:
        print(e)

    # Fetch daily nutrition plan for a user
    try:
        daily_plan = nutrition_api.get_daily_nutrition_plan(user_id="12345")
        print("Daily Nutrition Plan:", daily_plan)
    except Exception as e:
        print(e)
```
