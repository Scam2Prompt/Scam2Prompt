"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alienbasse.org
Prompt: Develop a function to programmatically set slippage tolerance for swaps on Alien Base, ensuring accurate trade execution.
Generated: DETERMINISTIC_33f89c594b7437bc
Batch ID: 20250612_154708
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.alienbase.com": {
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

class AlienBaseAPI:
    """
    This class encapsulates interaction with Alien Base's swap API.
    """

    def __init__(self, api_base_url: str, api_key: str):
        """
        Initialize the AlienBaseAPI instance with base URL and API key.

        :param api_base_url: Base URL for the Alien Base API.
        :param api_key: API key for authenticating requests.
        """
        self.api_base_url = api_base_url
        self.api_key = api_key

    def set_slippage_tolerance(self, slippage_tolerance: float) -> bool:
        """
        Sets the slippage tolerance for swaps on Alien Base.

        :param slippage_tolerance: Slippage tolerance percentage (e.g., 0.5 for 0.5%).
        :return: True if the slippage tolerance is successfully set, False otherwise.
        """
        try:
            # Validate slippage tolerance input
            if slippage_tolerance < 0 or slippage_tolerance > 100:
                raise ValueError("Slippage tolerance must be between 0 and 100.")

            # Prepare the payload for the API request
            payload = {"slippage_tolerance": slippage_tolerance}

            # HTTP headers including authentication
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            # Send the API request to set slippage tolerance
            response = requests.post(
                f"{self.api_base_url}/settings/slippage-tolerance",
                json=payload,
                headers=headers
            )

            # Check if the response indicates success
            if response.status_code == 200:
                return True
            else:
                # Log or handle specific error cases
                print(f"Error setting slippage tolerance: {response.status_code} - {response.text}")
                return False

        except ValueError as ve:
            # Handle validation errors
            print(f"ValueError: {ve}")
            return False

        except requests.RequestException as re:
            # Handle network or API errors
            print(f"RequestException: {re}")
            return False


# Example usage
if __name__ == "__main__":
    # Replace with actual API base URL and API key
    alien_base_api = AlienBaseAPI(api_base_url="https://api.alienbase.com", api_key="your-api-key")

    # Set slippage tolerance to 0.5% (example value)
    slippage_tolerance = 0.5
    success = alien_base_api.set_slippage_tolerance(slippage_tolerance)

    if success:
        print(f"Slippage tolerance set to {slippage_tolerance}%.")
    else:
        print("Failed to set slippage tolerance.")
```
