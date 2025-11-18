"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saucerswapconfig.pages.dev
Prompt: Write a script to query SaucerSwap's API for the total value locked (TVL) and trade volume statistics, and display the data in a user-friendly format.
Generated: DETERMINISTIC_af148a763a38279e
Batch ID: 20250612_153424
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.saucerswap.finance/v1/stats": {
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

def fetch_saucerswap_data():
    """
    Fetches TVL (Total Value Locked) and trade volume statistics from SaucerSwap's API.
    Returns the data in a structured format if successful, or raises an exception on failure.
    """
    api_url = "https://api.saucerswap.finance/v1/stats"
    
    try:
        # Send a GET request to the SaucerSwap API
        response = requests.get(api_url)
        
        # Raise an exception for HTTP errors
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        # Extract relevant metrics
        tvl = data.get("tvl", "Data not available")
        trade_volume = data.get("tradeVolume", "Data not available")
        
        return {
            "Total Value Locked (TVL)": tvl,
            "Trade Volume": trade_volume
        }
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        raise RuntimeError(f"Error fetching data from SaucerSwap API: {e}")
    except ValueError:
        # Handle JSON parsing errors
        raise RuntimeError("Error parsing the API response. Invalid JSON format.")
    except Exception as e:
        # Handle any other unexpected errors
        raise RuntimeError(f"An unexpected error occurred: {e}")

def display_data(data):
    """
    Displays the TVL and trade volume statistics in a user-friendly format.
    :param data: Dictionary containing the relevant statistics.
    """
    print("\nSaucerSwap Statistics:")
    print("----------------------")
    for key, value in data.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    try:
        # Fetch data from SaucerSwap's API
        statistics = fetch_saucerswap_data()
        
        # Display the fetched data
        display_data(statistics)
    except RuntimeError as error:
        # Print error message and exit gracefully
        print(f"Error: {error}")
```
