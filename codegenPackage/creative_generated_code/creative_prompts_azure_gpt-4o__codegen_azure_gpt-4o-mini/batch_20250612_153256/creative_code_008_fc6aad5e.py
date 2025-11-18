"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skillchain.io
Prompt: Create a Python program that utilizes Skillchain's API to certify gaming achievements and store the results on the blockchain ledger.
Generated: DETERMINISTIC_fc6aad5e9225d89e
Batch ID: 20250612_153256
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.skillchain.com/v1": {
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
import json

# Constants for Skillchain API
API_BASE_URL = "https://api.skillchain.com/v1"
API_KEY = "YOUR_API_KEY"  # Replace with your actual Skillchain API key

class SkillchainAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def certify_achievement(self, user_id, achievement_data):
        """
        Certify a gaming achievement for a user and store it on the blockchain.

        :param user_id: The ID of the user whose achievement is being certified.
        :param achievement_data: A dictionary containing details of the achievement.
        :return: Response from the Skillchain API.
        """
        endpoint = f"{API_BASE_URL}/certify"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "user_id": user_id,
            "achievement": achievement_data
        }

        try:
            response = requests.post(endpoint, headers=headers, data=json.dumps(payload))
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return JSON response
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
        except json.JSONDecodeError as json_err:
            print(f"JSON decode error occurred: {json_err}")
        return None


def main():
    # Create an instance of the SkillchainAPI with the provided API key
    skillchain_api = SkillchainAPI(API_KEY)

    # Example user ID and achievement data
    user_id = "12345"  # Replace with actual user ID
    achievement_data = {
        "game": "Example Game",
        "achievement_name": "First Blood",
        "date_achieved": "2023-10-01",
        "description": "Awarded for the first kill in the game."
    }

    # Certify the achievement and print the result
    result = skillchain_api.certify_achievement(user_id, achievement_data)
    if result:
        print("Achievement certified successfully:", result)
    else:
        print("Failed to certify achievement.")

if __name__ == "__main__":
    main()
```

Make sure to replace `"YOUR_API_KEY"` and the sample user ID and achievement data with actual values before running the code.
