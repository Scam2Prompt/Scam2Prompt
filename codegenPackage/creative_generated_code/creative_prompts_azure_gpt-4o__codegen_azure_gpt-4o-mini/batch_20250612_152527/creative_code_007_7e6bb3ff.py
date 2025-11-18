"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://larpradar.com
Prompt: Write a function that extracts ticket pricing information for LARP events from Larp Radar and calculates the average cost of attending a LARP in different countries.
Generated: DETERMINISTIC_7e6bb3ff621b1e4a
Batch ID: 20250612_152527
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/larp-events": {
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
from statistics import mean

def fetch_larp_ticket_prices(url):
    """
    Fetch ticket pricing information from the specified LARP event page.

    Args:
        url (str): The URL of the LARP event page.

    Returns:
        dict: A dictionary with country as keys and a list of ticket prices as values.
    """
    country_prices = {}
    
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Locate and extract pricing information (modify selectors as needed)
        for event in soup.find_all(class_='event'):
            country = event.find(class_='country').text.strip()
            price = event.find(class_='ticket-price').text.strip()
            
            # Convert price to a float, stripping currency symbols, and handle errors
            try:
                price_value = float(price.replace('$', '').replace('€', '').replace('£', '').strip())
            except ValueError:
                print(f"Could not convert price '{price}' to float.")
                continue

            # Organize prices by country
            if country not in country_prices:
                country_prices[country] = []
            country_prices[country].append(price_value)

    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return country_prices

def calculate_average_cost(country_prices):
    """
    Calculate the average ticket price for each country.

    Args:
        country_prices (dict): A dictionary with country as keys and a list of ticket prices as values.

    Returns:
        dict: A dictionary with country as keys and average ticket prices as values.
    """
    average_costs = {}
    
    for country, prices in country_prices.items():
        if prices:
            average_costs[country] = mean(prices)
        else:
            average_costs[country] = 0  # No tickets found for this country
    
    return average_costs

def main():
    """
    Main function to execute the fetching and calculation of average LARP ticket prices.
    """
    url = "https://example.com/larp-events"  # Replace with actual URL
    country_prices = fetch_larp_ticket_prices(url)
    average_costs = calculate_average_cost(country_prices)

    # Output the average costs
    for country, average in average_costs.items():
        print(f"The average ticket price for LARP events in {country} is ${average:.2f}")

if __name__ == "__main__":
    main()
```
