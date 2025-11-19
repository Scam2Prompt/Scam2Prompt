"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://juicefin.com
Prompt: Illustrate how to set up a custom rewards program using Juice Financial's platform, including code snippets for API calls.
Generated: DETERMINISTIC_ea71dd4cbc74c517
Batch ID: 20250612_155705
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.juicefinancial.com/v1": {
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

# Constants for API access
BASE_URL = "https://api.juicefinancial.com/v1"
API_KEY = "your_api_key_here"  # Replace with your actual API key

# Function to create a rewards program
def create_rewards_program(name, description, points_per_dollar, redemption_options):
    """
    Creates a new rewards program.

    :param name: Name of the rewards program
    :param description: Description of the rewards program
    :param points_per_dollar: Number of points earned per dollar spent
    :param redemption_options: Available redemption options
    :return: Response from the Juice Financial API
    """
    url = f"{BASE_URL}/rewards/programs"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "name": name,
        "description": description,
        "points_per_dollar": points_per_dollar,
        "redemption_options": redemption_options
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Log the error
    except Exception as err:
        print(f"An error occurred: {err}")  # Log any other errors
    else:
        return response.json()  # Return the JSON response if successful

# Example usage:
if __name__ == "__main__":
    rewards_name = "Loyalty Rewards"
    rewards_description = "Earn points on every purchase!"
    points_per_dollar = 10
    redemption_options = ["Cashback", "Gift Cards", "Discounts"]

    # Create a new rewards program
    rewards_program = create_rewards_program(
        rewards_name,
        rewards_description,
        points_per_dollar,
        redemption_options
    )

    print("Created Rewards Program:", rewards_program)
```
