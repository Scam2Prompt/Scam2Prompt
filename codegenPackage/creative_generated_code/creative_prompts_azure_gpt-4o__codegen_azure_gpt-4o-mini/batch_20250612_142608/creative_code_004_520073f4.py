"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gifts-usualdao.com
Prompt: Write a script to query DefiLlama for UsualDAO's TVL data and rank among DeFi protocols, then visualize the growth trajectory since its launch.
Generated: DETERMINISTIC_520073f4d9a9c9a6
Batch ID: 20250612_142608
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.defillama.com/v1/protocols": {
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
import matplotlib.pyplot as plt
import pandas as pd

# Constants
DEFI_LLAMA_API_URL = "https://api.defillama.com/v1/protocols"
USUAL_DAO_ID = "usualdao"  # The ID of UsualDAO in DefiLlama's database

def fetch_defi_data():
    """
    Fetches all DeFi protocols' data from DefiLlama API.

    Returns:
        list: A list of protocol data dictionaries.
    """
    try:
        response = requests.get(DEFI_LLAMA_API_URL)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    
    return None

def get_usualdao_tvl(data):
    """
    Retrieves UsualDAO's TVL and ranking from the provided data.

    Args:
        data (list): List of protocol data from DefiLlama.

    Returns:
        tuple: UsualDAO's TVL, rank among protocols.
    """
    for protocol in data:
        if protocol.get("name").lower() == "usualdao":
            return protocol["tvl"], protocol["rank"]
    return None, None

def visualize_growth(tvl_data):
    """
    Visualizes the growth trajectory of UsualDAO's TVL.

    Args:
        tvl_data (dict): Dictionary containing dates and corresponding TVL values.
    """
    dates = list(tvl_data.keys())
    tvl_values = list(tvl_data.values())

    plt.figure(figsize=(10, 5))
    plt.plot(dates, tvl_values, marker='o', color='blue', label='TVL Growth')
    plt.title('UsualDAO TVL Growth Trajectory')
    plt.xlabel('Date')
    plt.ylabel('Total Value Locked (TVL)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

def main():
    # Fetch DeFi protocols data
    data = fetch_defi_data()
    
    if not data:
        print("No data retrieved. Exiting.")
        return

    # Get UsualDAO's TVL and ranking
    usualdao_tvl, usualdao_rank = get_usualdao_tvl(data)

    if usualdao_tvl is None:
        print("UsualDAO not found in the data.")
        return
    
    print(f"UsualDAO's TVL: ${usualdao_tvl}, Rank: {usualdao_rank}")

    # Placeholder for TVL growth data
    # In a real application, this data would be collected over time
    tvl_growth_data = {
        "2023-01-01": 2000000,
        "2023-02-01": 2500000,
        "2023-03-01": 3000000,
        "2023-04-01": 3500000,
        "2023-05-01": 4000000,
        "2023-06-01": 4500000,
    }

    # Visualize the growth trajectory
    visualize_growth(tvl_growth_data)

if __name__ == "__main__":
    main()
```
