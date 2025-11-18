"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiddfzec3ssadmq4s7m7fotcrv2543fgmtp5fhndlmktya2zv4jvyy.ipfs.dweb.link
Prompt: Develop a Python program that fetches fund performance data for Spiko MMFs, including net APY rates and AuM values, and displays it in a user-friendly format.
Generated: DETERMINISTIC_795a523de9745c37
Batch ID: 20250612_150228
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.spiko.com/mmfs/performance": {
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
from tabulate import tabulate

def fetch_fund_performance_data():
    """
    Fetches fund performance data for Spiko MMFs including net APY rates and AuM values.
    Returns the data in a structured format.
    """
    # URL for the API endpoint (replace with actual API endpoint)
    api_url = "https://api.spiko.com/mmfs/performance"

    try:
        # Make a GET request to the API
        response = requests.get(api_url)

        # Raise an HTTPError if the response code is not 200
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Validate the structure of the data
        if not isinstance(data, list):
            raise ValueError("Unexpected data format: Expected a list of funds.")

        return data

    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Error fetching data from the API: {e}")
    except ValueError as ve:
        # Handle data-related errors
        print(f"Data validation error: {ve}")
    except Exception as ex:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {ex}")

    # Return an empty list in case of errors
    return []

def display_fund_data(fund_data):
    """
    Displays fund performance data in a user-friendly format.
    """
    # Check if there is any data to display
    if not fund_data:
        print("No fund performance data available.")
        return

    # Prepare data for tabular display
    table_data = []
    for fund in fund_data:
        try:
            # Extract relevant fields
            fund_name = fund.get("fund_name", "N/A")
            net_apy = fund.get("net_apy", "N/A")
            aum = fund.get("aum", "N/A")

            # Append to table data
            table_data.append([fund_name, net_apy, aum])
        except KeyError:
            # Handle missing key errors
            print(f"Error processing fund data: {fund}")

    # Define table headers
    headers = ["Fund Name", "Net APY (%)", "Assets Under Management (AuM)"]

    # Display the table using tabulate
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

def main():
    """
    Main function to fetch and display fund performance data.
    """
    print("Fetching fund performance data for Spiko MMFs...")
    fund_data = fetch_fund_performance_data()
    print("Displaying fund performance data...")
    display_fund_data(fund_data)

if __name__ == "__main__":
    main()
```
