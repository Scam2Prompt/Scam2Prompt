"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v2-stakewise-io.web.app
Prompt: Write code to export staking rewards data from StakeWise for the past 30 days in USD format, including a graph of daily rewards.
Generated: DETERMINISTIC_a0aee6e9aa52b70e
Batch ID: 20250612_152620
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.stakewise.io/v1": {
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
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def fetch_staking_rewards(api_url, wallet_address, headers):
    """
    Fetch staking rewards data from StakeWise API for a given wallet address.

    Parameters:
        api_url (str): Base API URL for StakeWise.
        wallet_address (str): Wallet address to fetch data for.
        headers (dict): Headers for the API request.

    Returns:
        list: A list of staking rewards data.
    """
    try:
        response = requests.get(f"{api_url}/staking-rewards/{wallet_address}", headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching staking rewards data: {e}")
        return []

def process_rewards_data(data, start_date, end_date):
    """
    Process staking rewards data to filter for the past 30 days and convert to USD.

    Parameters:
        data (list): Raw staking rewards data.
        start_date (datetime): Start date for filtering data.
        end_date (datetime): End date for filtering data.

    Returns:
        pd.DataFrame: Processed data with daily rewards in USD.
    """
    processed_data = []
    for entry in data:
        # Parse the date from the data and filter by date range
        reward_date = datetime.strptime(entry['date'], "%Y-%m-%d")
        if start_date <= reward_date <= end_date:
            # Convert rewards to USD using conversion rate provided in the data
            rewards_usd = float(entry['reward_eth']) * float(entry['eth_to_usd'])
            processed_data.append({
                "date": reward_date.date(),
                "rewards_usd": rewards_usd
            })
    return pd.DataFrame(processed_data)

def plot_rewards(dataframe):
    """
    Plot daily rewards in USD using a line graph.

    Parameters:
        dataframe (pd.DataFrame): DataFrame containing daily rewards data.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(dataframe['date'], dataframe['rewards_usd'], marker='o', color='b', label='Daily Rewards (USD)')
    plt.title('Daily Staking Rewards in USD (Last 30 Days)', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Rewards (USD)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    # Configuration
    API_URL = "https://api.stakewise.io/v1"  # StakeWise API base URL
    WALLET_ADDRESS = "your_wallet_address_here"  # Replace with your wallet address
    HEADERS = {"Authorization": "Bearer your_api_token_here"}  # Replace with your API token
    
    # Date range for the past 30 days
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)

    # Fetch rewards data
    raw_data = fetch_staking_rewards(API_URL, WALLET_ADDRESS, HEADERS)
    if not raw_data:
        print("No data fetched. Exiting.")
        return

    # Process rewards data
    processed_rewards = process_rewards_data(raw_data, start_date, end_date)

    # Check if data frame is empty
    if processed_rewards.empty:
        print("No rewards data available for the past 30 days.")
        return

    # Export processed data to CSV
    csv_file = "staking_rewards_last_30_days.csv"
    processed_rewards.to_csv(csv_file, index=False)
    print(f"Rewards data exported to {csv_file}")

    # Generate a graph of daily rewards
    plot_rewards(processed_rewards)

if __name__ == "__main__":
    main()
```
