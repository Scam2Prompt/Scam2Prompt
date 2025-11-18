"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ontariooffers.com
Prompt: Create a Python script to generate a list of cities in Ontario served by Ontario Screen Systems Inc., using the content provided on the webpage.
Generated: DETERMINISTIC_e1b70ef10d3d9365
Batch ID: 20250612_154927
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/cities": {
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

def fetch_cities(url):
    """
    Fetches a list of cities from the provided URL.

    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        list: A list of cities in Ontario served by Ontario Screen Systems Inc.
    """
    try:
        # Send a GET request to the webpage
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)

        # Parse the webpage content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the relevant section containing city names
        # Adjust the selector based on actual webpage structure
        city_elements = soup.select('.city-list li')  # Example selector
        cities = [city.get_text(strip=True) for city in city_elements]

        return cities

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return []

def main():
    """
    Main function to execute the script.
    """
    url = 'https://example.com/cities'  # Replace with the actual URL
    cities = fetch_cities(url)

    if cities:
        print("Cities in Ontario served by Ontario Screen Systems Inc.:")
        for city in cities:
            print(f"- {city}")
    else:
        print("No cities found or there was an error fetching the data.")

if __name__ == "__main__":
    main()
```
