"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inbetweeners-blue.pages.dev
Prompt: Provide an example of using DEXTools API to fetch chart data for the $BLUE product, as mentioned on the inBetweeners site.
Generated: DETERMINISTIC_ce124f3be46fdc05
Batch ID: 20250612_163945
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.dex.tools/v1": {
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

class DEXToolsAPI:
    """
    A class to interact with the DEXTools API to fetch chart data for a specific token.
    """

    BASE_URL = "https://api.dex.tools/v1"

    def __init__(self, token_symbol):
        """
        Initialize the DEXToolsAPI with the given token symbol.

        Args:
            token_symbol (str): The symbol of the token for which to fetch chart data.

        Attributes:
            token_symbol (str): The token symbol.
        """
        self.token_symbol = token_symbol

    def fetch_chart_data(self):
        """
        Fetch the chart data for the specified token.

        Returns:
            dict: A dictionary containing the chart data.

        Raises:
            Exception: If an error occurs during the API request.
        """
        endpoint = f"{self.BASE_URL}/charts/{self.token_symbol}"
        try:
            response = requests.get(endpoint)
            response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
            return response.json()  # Return the JSON response as a dictionary
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")  # Handle HTTP errors
        except requests.exceptions.RequestException as req_err:
            raise Exception(f"Request error occurred: {req_err}")  # Handle general request errors

def main():
    """
    Main function to execute the DEXTools API call and print the chart data.
    """
    token_symbol = "$BLUE"  # Token symbol for which to fetch data
    dex_tools_api = DEXToolsAPI(token_symbol)

    try:
        chart_data = dex_tools_api.fetch_chart_data()  # Fetch the chart data
        print("Chart Data for", token_symbol)
        print(chart_data)  # Print the fetched chart data
    except Exception as e:
        print("An error occurred:", e)  # Print the error message

if __name__ == "__main__":
    main()  # Run the main function
```
