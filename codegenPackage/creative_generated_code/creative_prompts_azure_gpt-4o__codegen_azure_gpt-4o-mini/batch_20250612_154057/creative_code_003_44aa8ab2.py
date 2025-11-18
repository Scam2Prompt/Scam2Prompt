"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://satyloud.io
Prompt: Create a Python script to fetch and display the top contributors' mindshare rankings from the Loud platform, including their earnings and percentage changes.
Generated: DETERMINISTIC_44aa8ab283b5cbc4
Batch ID: 20250612_154057
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.loudplatform.com/top_contributors": {
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_contributors_data(api_url):
    """
    Fetches the top contributors' data from the Loud platform API.
    
    Parameters:
    api_url (str): The URL of the Loud platform API endpoint to fetch data from.

    Returns:
    dict: A dictionary containing the top contributors' data if the request is successful.
    None: If the request fails.
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        logging.info("Successfully fetched contributors data.")
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data from API: {e}")
        return None

def display_contributors(contributors):
    """
    Displays the top contributors' mindshare rankings, earnings, and percentage changes.

    Parameters:
    contributors (list): A list of contributors data.

    Returns:
    None
    """
    if not contributors:
        logging.warning("No contributors data to display.")
        return

    # Print header
    print(f"{'Rank':<5} {'Contributor':<25} {'Earnings':<15} {'% Change':<10}")
    print("=" * 60)

    # Display each contributor's data
    for contributor in contributors:
        rank = contributor.get('rank', 'N/A')
        name = contributor.get('name', 'Unknown')
        earnings = contributor.get('earnings', 0)
        percentage_change = contributor.get('percentage_change', 'N/A')

        print(f"{rank:<5} {name:<25} ${earnings:<15,.2f} {percentage_change:<10}")

def main():
    """
    Main function to execute the script.

    Returns:
    None
    """
    # API endpoint for fetching top contributors
    api_url = "https://api.loudplatform.com/top_contributors"

    # Fetch contributors data
    contributors_data = fetch_contributors_data(api_url)

    # If data was fetched successfully, display it
    if contributors_data:
        display_contributors(contributors_data)

if __name__ == "__main__":
    main()
```
