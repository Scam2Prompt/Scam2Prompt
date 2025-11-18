"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defilllama.com
Prompt: Using DeFi Llama's API, write code to identify the top 5 DeFi protocols with the highest TVL and display their details in a tabular format.
Generated: DETERMINISTIC_5c67e99077a217a7
Batch ID: 20250612_151003
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.llama.fi/protocols": {
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
import pandas as pd

def fetch_top_defi_protocols(num_protocols=5):
    """
    Fetch the top DeFi protocols by Total Value Locked (TVL) using DeFi Llama's API.
    
    Args:
        num_protocols (int): The number of top protocols to fetch. Default is 5.

    Returns:
        pd.DataFrame: A DataFrame containing the top DeFi protocols and their details.
    """
    
    # Define the URL for DeFi Llama's API endpoint
    api_url = 'https://api.llama.fi/protocols'

    try:
        # Make a request to the API to get the protocols data
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the JSON response
        protocols_data = response.json()

        # Sort the protocols by TVL in descending order and select the top entries
        top_protocols = sorted(protocols_data, key=lambda x: x['tvl'], reverse=True)[:num_protocols]

        # Create a DataFrame to hold the relevant details
        protocols_df = pd.DataFrame(top_protocols)

        # Select relevant columns to display
        columns_to_display = ['name', 'tvl', 'chain', 'category']
        protocols_df = protocols_df[columns_to_display]

        return protocols_df
    
    except requests.RequestException as e:
        print(f"Error fetching data from DeFi Llama API: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error

def display_protocols(protocols_df):
    """
    Display the DataFrame of DeFi protocols in a tabular format.

    Args:
        protocols_df (pd.DataFrame): DataFrame containing DeFi protocol details.
    """
    if protocols_df.empty:
        print("No data available to display.")
    else:
        print(protocols_df.to_string(index=False))  # Display the DataFrame without the index

if __name__ == "__main__":
    # Fetch and display the top 5 DeFi protocols by TVL
    top_protocols_df = fetch_top_defi_protocols()
    display_protocols(top_protocols_df)
```
