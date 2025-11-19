"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.airlinesticketpolicy.com
Prompt: Write a query to extract the latest flight change policies for Allegiant and Alaska Airlines from the Airlines Ticket Policy website.
Generated: DETERMINISTIC_1d821bf765c27334
Batch ID: 20250612_162822
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.airlinesticketpolicy.com/": {
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

def fetch_flight_change_policies(airlines):
    """
    Fetch the latest flight change policies for specified airlines from the Airlines Ticket Policy website.
    
    Args:
        airlines (list): A list of airline names to fetch policies for.
        
    Returns:
        dict: A dictionary containing airline names as keys and their respective policies as values.
    """
    # Base URL of the Airlines Ticket Policy website
    base_url = "https://www.airlinesticketpolicy.com/"
    policies = {}

    for airline in airlines:
        try:
            # Construct URL for the specific airline policy
            url = f"{base_url}{airline.lower().replace(' ', '-')}-change-policy"
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad HTTP responses
            
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract the policy text (adjust the selector as necessary)
            policy_section = soup.find("div", class_="policy-details")
            if policy_section:
                policies[airline] = policy_section.get_text(strip=True)
            else:
                policies[airline] = "Policy information not found."
        
        except requests.HTTPError as http_err:
            policies[airline] = f"HTTP error occurred: {http_err}"
        except Exception as err:
            policies[airline] = f"An error occurred: {err}"

    return policies

# List of airlines to check for flight change policies
airlines_to_check = ['Allegiant Air', 'Alaska Airlines']

# Fetch the flight change policies
flight_change_policies = fetch_flight_change_policies(airlines_to_check)

# Output the fetched policies
for airline, policy in flight_change_policies.items():
    print(f"{airline} Flight Change Policy: {policy}\n")
```
