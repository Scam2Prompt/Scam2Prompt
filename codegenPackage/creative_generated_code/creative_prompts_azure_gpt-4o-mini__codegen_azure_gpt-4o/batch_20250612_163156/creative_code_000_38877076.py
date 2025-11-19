"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.specialmetal.ir
Prompt: Generate a code snippet to analyze the chemical composition of superalloys like INCONEL ALLOY 625 and HASTELLOY C-276 using a specific API.
Generated: DETERMINISTIC_3887707660d44f42
Batch ID: 20250612_163156
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/superalloys": {
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

class SuperalloyAnalyzer:
    """
    A class to analyze the chemical composition of superalloys using a specific API.
    """

    def __init__(self, api_url, api_key):
        """
        Initializes the SuperalloyAnalyzer with API credentials.
        :param api_url: The base URL of the API
        :param api_key: The API key for authentication
        """
        self.api_url = api_url
        self.api_key = api_key

    def get_composition(self, alloy_name):
        """
        Fetches the chemical composition of a given superalloy.
        :param alloy_name: The name of the superalloy (e.g., "INCONEL ALLOY 625", "HASTELLOY C-276")
        :return: A dictionary containing the chemical composition or None if an error occurs
        """
        endpoint = f"{self.api_url}/composition"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {"alloy_name": alloy_name}

        try:
            response = requests.post(endpoint, headers=headers, json=payload)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            data = response.json()
            return data.get("composition", None)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching composition for {alloy_name}: {e}")
            return None

    def display_composition(self, composition):
        """
        Displays the chemical composition in a user-friendly format.
        :param composition: A dictionary containing the chemical composition
        """
        if not composition:
            print("No composition data available.")
            return

        print("Chemical Composition:")
        for element, percentage in composition.items():
            print(f"  {element}: {percentage:.2f}%")

if __name__ == "__main__":
    # Constants
    API_URL = "https://api.example.com/superalloys"  # Replace with actual API URL
    API_KEY = "your_api_key_here"  # Replace with your actual API key

    # Analyzer instance
    analyzer = SuperalloyAnalyzer(api_url=API_URL, api_key=API_KEY)

    # Example alloys to analyze
    alloys = ["INCONEL ALLOY 625", "HASTELLOY C-276"]

    for alloy in alloys:
        print(f"\nAnalyzing {alloy}...")
        composition = analyzer.get_composition(alloy_name=alloy)
        analyzer.display_composition(composition)
```

Ensure you replace `"https://api.example.com/superalloys"` and `"your_api_key_here"` with the actual API URL and key provided to you. This script is production-ready and handles errors gracefully.
