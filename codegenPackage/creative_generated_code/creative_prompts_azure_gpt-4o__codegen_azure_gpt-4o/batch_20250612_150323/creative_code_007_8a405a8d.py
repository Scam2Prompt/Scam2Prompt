"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etcerscan.com
Prompt: Create a dashboard to visualize hourly active addresses and transaction counts on the Ethereum Classic blockchain using data from ETCScan.
Generated: DETERMINISTIC_8a405a8d7b28233e
Batch ID: 20250612_150323
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.etherscan.io/api": {
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


# Constants
ETC_SCAN_BASE_URL = "https://api.etherscan.io/api"
API_KEY = "your_api_key_here"  # Replace with your ETCScan API key
HOURS_TO_VISUALIZE = 24  # Number of hours to visualize
START_TIME = int((datetime.now() - timedelta(hours=HOURS_TO_VISUALIZE)).timestamp())
END_TIME = int(datetime.now().timestamp())


def fetch_block_data(start_time, end_time, api_key):
    """
    Fetches block data from the Ethereum Classic blockchain using ETCScan API.
    
    :param start_time: Start timestamp in UNIX format.
    :param end_time: End timestamp in UNIX format.
    :param api_key: API key for ETCScan.
    :return: List of blocks within the specified time range.
    """
    url = f"{ETC_SCAN_BASE_URL}?module=block&action=getblocknobytime&timestamp={start_time}&closest=before&apikey={api_key}"
    response = requests.get(url)
    response.raise_for_status()  # Raise exception for HTTP errors
    start_block = int(response.json().get('result', 0))

    url = f"{ETC_SCAN_BASE_URL}?module=block&action=getblocknobytime&timestamp={end_time}&closest=before&apikey={api_key}"
    response = requests.get(url)
    response.raise_for_status()
    end_block = int(response.json().get('result', 0))

    blocks = []
    for block_num in range(start_block, end_block + 1):
        block_url = f"{ETC_SCAN_BASE_URL}?module=block&action=getblockreward&blockno={block_num}&apikey={api_key}"
        block_response = requests.get(block_url)
        block_response.raise_for_status()
        blocks.append(block_response.json().get('result', {}))

    return blocks


def process_data(blocks):
    """
    Processes block data to extract transaction counts and active addresses per hour.

    :param blocks: List of blocks fetched from the blockchain.
    :return: Dataframe containing hourly active addresses and transaction counts.
    """
    data = []
    for block in blocks:
        timestamp = int(block['timeStamp'])
        datetime_obj = datetime.utcfromtimestamp(timestamp)
        hour = datetime_obj.strftime('%Y-%m-%d %H:00:00')
        data.append({'hour': hour, 'tx_count': len(block['transactions']), 'active_addresses': len(set(tx['from'] for tx in block['transactions']))})

    df = pd.DataFrame(data)
    aggregated_df = df.groupby('hour').sum().reset_index()
    return aggregated_df


def visualize_data(df):
    """
    Visualizes hourly active addresses and transaction counts using Matplotlib.

    :param df: Dataframe containing hourly active addresses and transaction counts.
    """
    plt.figure(figsize=(12, 6))

    # Plot transaction counts
    plt.plot(df['hour'], df['tx_count'], label='Transaction Count', marker='o')

    # Plot active addresses
    plt.plot(df['hour'], df['active_addresses'], label='Active Addresses', marker='o')

    # Formatting the plot
    plt.title('Hourly Active Addresses and Transaction Counts on Ethereum Classic')
    plt.xlabel('Hour')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    plt.tight_layout()

    # Show the plot
    plt.show()


def main():
    """
    Main function to fetch data, process it, and visualize it.
    """
    try:
        print("Fetching block data...")
        blocks = fetch_block_data(START_TIME, END_TIME, API_KEY)
        print("Processing data...")
        df = process_data(blocks)
        print("Visualizing data...")
        visualize_data(df)
        print("Dashboard completed.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from ETCScan: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```

Replace `"your_api_key_here"` in the `API_KEY` variable with your actual ETCScan API key. Make sure to install the required libraries (`requests`, `pandas`, `matplotlib`) before running the code.
