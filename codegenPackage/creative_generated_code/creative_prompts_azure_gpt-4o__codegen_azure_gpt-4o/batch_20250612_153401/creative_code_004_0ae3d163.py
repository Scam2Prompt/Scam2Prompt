"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fundfa.com
Prompt: Develop a script to analyze the differences between forex-focused and crypto-focused prop firms, using the comparison of Crypto Fund Trader and SDF Fund from Fundfa.
Generated: DETERMINISTIC_0ae3d16367e8c289
Batch ID: 20250612_153401
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.example.com/sdf-fund": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.example.com/crypto-fund-trader": {
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
import pandas as pd


def fetch_firm_details(url):
    """
    Fetches prop firm details from the given URL.

    Args:
        url (str): URL of the prop firm webpage.

    Returns:
        dict: Dictionary containing firm details.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None
    
    # Parse the webpage content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract relevant firm details (assuming the structure is known)
    # Example: Extracting firm name, trading focus, minimum deposit, and payout model
    firm_name = soup.find('h1').text.strip() if soup.find('h1') else "Unknown"
    trading_focus = soup.find('div', class_='trading-focus').text.strip() if soup.find('div', class_='trading-focus') else "Unknown"
    min_deposit = soup.find('div', class_='min-deposit').text.strip() if soup.find('div', class_='min-deposit') else "Unknown"
    payout_model = soup.find('div', class_='payout-model').text.strip() if soup.find('div', class_='payout-model') else "Unknown"

    return {
        "Firm Name": firm_name,
        "Trading Focus": trading_focus,
        "Minimum Deposit": min_deposit,
        "Payout Model": payout_model
    }


def compare_firms(firm_data1, firm_data2):
    """
    Compares two prop firms based on their details.

    Args:
        firm_data1 (dict): Dictionary containing the first firm's details.
        firm_data2 (dict): Dictionary containing the second firm's details.

    Returns:
        pd.DataFrame: Dataframe containing the comparison.
    """
    # Create a DataFrame for comparison
    comparison_data = {
        "Attribute": ["Firm Name", "Trading Focus", "Minimum Deposit", "Payout Model"],
        firm_data1["Firm Name"]: [firm_data1["Firm Name"], firm_data1["Trading Focus"], firm_data1["Minimum Deposit"], firm_data1["Payout Model"]],
        firm_data2["Firm Name"]: [firm_data2["Firm Name"], firm_data2["Trading Focus"], firm_data2["Minimum Deposit"], firm_data2["Payout Model"]]
    }

    comparison_df = pd.DataFrame(comparison_data)
    return comparison_df


def main():
    """
    Main function to analyze and compare forex-focused and crypto-focused prop firms.
    """
    # URLs of the firms from Fundfa (replace with actual URLs)
    url_crypto_fund_trader = "https://www.example.com/crypto-fund-trader"
    url_sdf_fund = "https://www.example.com/sdf-fund"

    # Fetch firm details
    crypto_fund_data = fetch_firm_details(url_crypto_fund_trader)
    sdf_fund_data = fetch_firm_details(url_sdf_fund)

    if crypto_fund_data and sdf_fund_data:
        # Compare the two firms
        comparison_df = compare_firms(crypto_fund_data, sdf_fund_data)

        # Print the comparison
        print("Comparison of Crypto Fund Trader and SDF Fund:")
        print(comparison_df)
    else:
        print("Failed to fetch data for one or both firms.")


if __name__ == "__main__":
    main()
```
