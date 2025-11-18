"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.airlinesticketpolicy.com
Prompt: Create a Python script that fetches and displays the latest flight change policies for Air Astana and Norse Atlantic Air from the Airlines Ticket Policy webpage.
Generated: DETERMINISTIC_df4cc8a800f3ccbc
Batch ID: 20250612_150653
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.airlinesticketpolicy.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.airlinesticketpolicy.com`": {
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
from bs4 import BeautifulSoup

class AirlinePolicyFetcher:
    """Fetches and displays the latest flight change policies for specified airlines."""
    
    def __init__(self, airlines):
        """
        Initializes the fetcher with a list of airline names.
        
        :param airlines: List of airline names to fetch policies for.
        """
        self.airlines = airlines
        self.base_url = "https://www.airlinesticketpolicy.com"

    def fetch_policy(self, airline):
        """
        Fetches the flight change policy for a given airline.
        
        :param airline: The name of the airline to fetch the policy for.
        :return: The flight change policy as a string, or an error message.
        """
        try:
            # Construct the search URL for the airline's policy
            search_url = f"{self.base_url}/search?q={airline.replace(' ', '+')}"
            response = requests.get(search_url)
            response.raise_for_status()  # Raise an error for bad responses
            
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the policy section based on the known structure of the page
            policy_section = soup.find('div', class_='policy-content')
            if policy_section:
                return policy_section.get_text(strip=True)
            else:
                return f"Policy section not found for {airline}."

        except requests.exceptions.RequestException as e:
            return f"Error fetching policy for {airline}: {str(e)}"

    def display_policies(self):
        """Fetches and displays policies for all airlines in the list."""
        for airline in self.airlines:
            print(f"Fetching policy for {airline}...")
            policy = self.fetch_policy(airline)
            print(f"Policy for {airline}:\n{policy}\n")


if __name__ == "__main__":
    # List of airlines to fetch policies for
    airlines_to_fetch = ["Air Astana", "Norse Atlantic Air"]
    
    # Create an instance of the AirlinePolicyFetcher
    policy_fetcher = AirlinePolicyFetcher(airlines_to_fetch)
    
    # Fetch and display the policies
    policy_fetcher.display_policies()
```

**Note**: Ensure that the URL `https://www.airlinesticketpolicy.com` and the HTML structure used in this script are correct and up-to-date, as they may change over time. Adjust the parsing logic accordingly if necessary.
