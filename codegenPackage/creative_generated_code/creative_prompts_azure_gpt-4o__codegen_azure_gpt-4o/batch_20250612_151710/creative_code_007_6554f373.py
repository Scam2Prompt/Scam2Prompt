"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-tools.org
Prompt: Provide a Python example to extract and sort miner data by computational power and temperature using BTC Tools.
Generated: DETERMINISTIC_6554f373f81541a3
Batch ID: 20250612_151710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import btc_tools

def extract_and_sort_miner_data():
    """
    Extracts miner data and sorts it by computational power and temperature.
    """

    try:
        # Fetch miner data using BTC Tools
        miner_data = btc_tools.get_miner_data()
    except btc_tools.BTCToolsError as e:
        # Handle errors from BTC Tools
        print(f"Error fetching miner data: {str(e)}")
        return []

    if not miner_data:
        print("No miner data available.")
        return []

    try:
        # Sort miner data by computational power (descending) and temperature (ascending)
        sorted_data = sorted(
            miner_data,
            key=lambda miner: (-miner['computational_power'], miner['temperature'])
        )
    except KeyError as e:
        # Handle missing keys in miner data
        print(f"Error processing miner data: Missing key {str(e)}")
        return []

    return sorted_data


def display_sorted_miners(sorted_miners):
    """
    Displays the sorted miner data in a readable format.

    :param sorted_miners: List of sorted miner dictionaries.
    """
    if not sorted_miners:
        print("No sorted miner data to display.")
        return

    print("{:<20} | {:<20} | {:<20}".format("Miner ID", "Computational Power (TH/s)", "Temperature (°C)"))
    print("-" * 65)
    for miner in sorted_miners:
        print("{:<20} | {:<20} | {:<20}".format(
            miner.get('id', 'Unknown'),
            miner.get('computational_power', 'Unknown'),
            miner.get('temperature', 'Unknown')
        ))


if __name__ == "__main__":
    # Extract and sort miner data
    sorted_miners = extract_and_sort_miner_data()

    # Display the sorted miner data
    display_sorted_miners(sorted_miners)
```

**Note:** Replace `btc_tools.get_miner_data()` with an actual BTC Tools API method call or implementation. If necessary, install and configure the BTC Tools library according to its documentation.
