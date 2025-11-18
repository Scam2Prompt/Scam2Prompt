"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clearpool.pages.dev
Prompt: Create a script to sort Clearpool oracles by APR and display the top three oracles with the highest yields.
Generated: DETERMINISTIC_b8bc515156c5d1c0
Batch ID: 20250612_151003
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.clearpool.network/oracles": {
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

def fetch_oracle_data(api_url):
    """
    Fetch oracle data from the provided API URL.

    Args:
        api_url (str): The URL of the Clearpool API to fetch oracle data from.

    Returns:
        list: A list of oracles with their respective APRs.

    Raises:
        Exception: If the API request fails or data is not in expected format.
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()  # Parse the JSON data

        # Assume the data is a list of oracles with the 'apr' key
        if not isinstance(data, list):
            raise ValueError("Expected a list of oracles from the API response.")

        return data
    except requests.exceptions.RequestException as e:
        raise Exception(f"API request failed: {e}")
    except json.JSONDecodeError:
        raise Exception("Failed to decode JSON response from API.")
    except ValueError as e:
        raise Exception(f"Data format error: {e}")

def sort_oracles_by_apr(oracles):
    """
    Sort the given list of oracles by APR in descending order.

    Args:
        oracles (list): A list of oracles with their APRs.

    Returns:
        list: The sorted list of oracles based on APR.
    """
    return sorted(oracles, key=lambda x: x.get('apr', 0), reverse=True)

def display_top_oracles(oracles, top_n=3):
    """
    Display the top N oracles with the highest APR.

    Args:
        oracles (list): The sorted list of oracles.
        top_n (int): The number of top oracles to display.
    """
    print(f"Top {top_n} Oracles by APR:")
    for oracle in oracles[:top_n]:
        print(f"Oracle Name: {oracle.get('name', 'Unknown')}, APR: {oracle.get('apr', 0)}%")

def main():
    """
    Main function to fetch, sort, and display Clearpool oracles by APR.
    """
    api_url = "https://api.clearpool.network/oracles"  # Example API endpoint
    try:
        oracles = fetch_oracle_data(api_url)
        sorted_oracles = sort_oracles_by_apr(oracles)
        display_top_oracles(sorted_oracles)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
