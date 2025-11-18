"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakingstory.org
Prompt: Create a function that connects to the Story Staking API and displays validator information, including their names, staked amounts, and performance metrics such as uptime and commission.
Generated: DETERMINISTIC_7d3f3e28a10f8353
Batch ID: 20250612_153832
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.storystaking.io/v1": {
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

class StoryStakingAPI:
    BASE_URL = "https://api.storystaking.io/v1"

    def __init__(self):
        """Initialize the StoryStakingAPI class."""
        pass

    def get_validators(self) -> List[Dict[str, Any]]:
        """Fetch the list of validators from the Story Staking API.

        Returns:
            List[Dict[str, Any]]: A list of validator information including name, staked amount, uptime, and commission.

        Raises:
            Exception: Raises an exception if the API request fails.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/validators")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json().get('validators', [])
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            print(f"An error occurred: {err}")
            raise

    def display_validator_info(self) -> None:
        """Display the validator information in a readable format."""
        try:
            validators = self.get_validators()
            if not validators:
                print("No validators found.")
                return
            
            print(f"{'Name':<30} {'Staked Amount':<20} {'Uptime (%)':<15} {'Commission (%)':<15}")
            print("=" * 80)
            for validator in validators:
                name = validator.get('name', 'N/A')
                staked_amount = validator.get('staked_amount', 0)
                uptime = validator.get('uptime', 'N/A')
                commission = validator.get('commission', 'N/A')

                print(f"{name:<30} {staked_amount:<20} {uptime:<15} {commission:<15}")
        
        except Exception as err:
            print(f"An error occurred while displaying validator information: {err}")

if __name__ == "__main__":
    api = StoryStakingAPI()
    api.display_validator_info()
```
