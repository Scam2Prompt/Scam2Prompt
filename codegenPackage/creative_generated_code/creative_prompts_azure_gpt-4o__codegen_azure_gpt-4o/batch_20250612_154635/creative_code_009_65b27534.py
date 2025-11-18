"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elara-celestia.com
Prompt: Create a Python script to extract and display the connectivity details (e.g., proximity to IT hubs, airport, and metro) from the L&T Elara Celestia webpage.
Generated: DETERMINISTIC_65b275340cdb366f
Batch ID: 20250612_154635
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.example.com/lt-elara-celestia`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.example.com/lt-elara-celestia": {
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

def fetch_connectivity_details(url):
    """
    Extract connectivity details from the given webpage URL.

    Args:
        url (str): URL of the webpage to scrape.

    Returns:
        dict: Dictionary containing connectivity details.
    """
    try:
        # Send a GET request to the webpage
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Dictionary to store connectivity details
        connectivity_details = {}

        # Extract connectivity-related information
        # Assumes the webpage contains relevant information in identifiable tags or classes
        # Update CSS selectors based on the webpage's actual structure
        proximity_to_it_hubs = soup.find('div', class_='it-hub-proximity')
        proximity_to_airport = soup.find('div', class_='airport-proximity')
        proximity_to_metro = soup.find('div', class_='metro-proximity')

        # Populate the dictionary with extracted details
        connectivity_details['Proximity to IT Hubs'] = proximity_to_it_hubs.text.strip() if proximity_to_it_hubs else 'Not available'
        connectivity_details['Proximity to Airport'] = proximity_to_airport.text.strip() if proximity_to_airport else 'Not available'
        connectivity_details['Proximity to Metro'] = proximity_to_metro.text.strip() if proximity_to_metro else 'Not available'

        return connectivity_details

    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"An error occurred while fetching the webpage: {e}")
        return None
    except Exception as e:
        # Handle other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None


def display_connectivity_details(details):
    """
    Display the connectivity details in a user-friendly format.

    Args:
        details (dict): Dictionary containing connectivity details.
    """
    if not details:
        print("No connectivity details available.")
        return

    print("\nConnectivity Details:")
    for key, value in details.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    # URL of the L&T Elara Celestia webpage
    url = "https://www.example.com/lt-elara-celestia"  # Replace with actual URL

    # Fetch connectivity details
    connectivity_details = fetch_connectivity_details(url)

    # Display the fetched details
    display_connectivity_details(connectivity_details)
```

**Note**: You need to replace the CSS selectors (`'div', class_='...'`) and the URL (`https://www.example.com/lt-elara-celestia`) with the actual values from the L&T Elara Celestia webpage to make the script functional.
