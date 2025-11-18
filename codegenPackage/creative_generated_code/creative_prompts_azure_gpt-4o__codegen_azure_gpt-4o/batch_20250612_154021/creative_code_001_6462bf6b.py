"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://projectvox.pages.dev
Prompt: Create a script to check the rarity of items or roles within a blockchain-based guild system, referencing features like "Check Rarity" from the Guildhall website.
Generated: DETERMINISTIC_6462bf6b3125f621
Batch ID: 20250612_154021
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.guildhall.example.com": {
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
import json
import requests


class RarityChecker:
    """
    A class to check the rarity of items or roles in a blockchain-based guild system.
    """

    def __init__(self, api_endpoint: str):
        """
        Initialize the RarityChecker with the API endpoint.
        
        :param api_endpoint: The endpoint of the Guildhall system's rarity check API.
        """
        self.api_endpoint = api_endpoint

    def fetch_rarity(self, item_id: str) -> dict:
        """
        Fetch the rarity data for a given item or role using the API.
        
        :param item_id: The unique identifier of the item or role.
        :return: A dictionary containing rarity data or an error message.
        """
        try:
            # Sending a GET request to the API endpoint with the item ID.
            response = requests.get(f"{self.api_endpoint}/rarity/{item_id}")
            response.raise_for_status()  # Raise an exception for HTTP errors.

            # Parse the JSON response.
            rarity_data = response.json()
            return rarity_data
        except requests.exceptions.RequestException as e:
            # Log and return error details if a request exception occurs.
            return {"error": f"Failed to fetch rarity: {str(e)}"}
        except json.JSONDecodeError as e:
            # Handle JSON parsing errors.
            return {"error": f"Invalid response format: {str(e)}"}

    def display_rarity(self, item_id: str):
        """
        Display the rarity details of the given item or role.
        
        :param item_id: The unique identifier of the item or role.
        """
        rarity_data = self.fetch_rarity(item_id)

        # Check if the data contains an error.
        if "error" in rarity_data:
            print(rarity_data["error"])
        else:
            # Extract rarity details and display them.
            print(f"Item ID: {item_id}")
            print(f"Name: {rarity_data.get('name', 'N/A')}")
            print(f"Rarity Level: {rarity_data.get('rarity_level', 'N/A')}")
            print(f"Description: {rarity_data.get('description', 'N/A')}")


if __name__ == "__main__":
    # Main entry point for the script.

    # Define the Guildhall API endpoint (replace with actual URL).
    GUILDHALL_API_ENDPOINT = "https://api.guildhall.example.com"

    # Instantiate the RarityChecker with the API endpoint.
    checker = RarityChecker(GUILDHALL_API_ENDPOINT)

    # Example item ID to check rarity for (replace with actual item ID).
    ITEM_ID = "item123"

    # Check and display rarity information for the item.
    checker.display_rarity(ITEM_ID)
```
