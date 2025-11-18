"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wwwmorpho.org
Prompt: Write a program to query Morpho's API and display the details of all vaults curated by `MEV Capital`, including APY and deposit amounts.
Generated: DETERMINISTIC_12ff68aa43646849
Batch ID: 20250612_145444
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.morpho.com/v1": {
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

# Constants for the API
BASE_URL = "https://api.morpho.com/v1"  # Replace with the actual Morpho API base URL
VAULTS_ENDPOINT = "/vaults"
CURATOR_NAME = "MEV Capital"  # The specific curator to filter by

def fetch_vaults():
    """
    Fetch the list of vaults from the Morpho API.

    Returns:
        list: A list of vaults if the API call is successful, otherwise None.
    """
    try:
        # Make a GET request to fetch all vaults
        response = requests.get(BASE_URL + VAULTS_ENDPOINT)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching vault data: {e}")
        return None

def filter_vaults_by_curator(vaults, curator_name):
    """
    Filter the vaults curated by a specific entity.

    Args:
        vaults (list): A list of vaults.
        curator_name (str): The name of the curator to filter by.

    Returns:
        list: A list of vaults curated by the specified entity.
    """
    return [vault for vault in vaults if vault.get("curator") == curator_name]

def display_vault_details(vaults):
    """
    Display details of the vaults in a readable format.

    Args:
        vaults (list): A list of vaults to display.
    """
    if not vaults:
        print("No vaults found for the specified curator.")
        return

    print(f"Vaults curated by {CURATOR_NAME}:\n")
    for vault in vaults:
        name = vault.get("name", "Unknown")
        apy = vault.get("apy", "N/A")
        deposit = vault.get("deposit_amount", "N/A")
        print(f"Name: {name}")
        print(f"APY: {apy}%")
        print(f"Deposit Amount: {deposit}")
        print("-" * 40)

def main():
    """
    Main function to fetch, filter, and display vault details.
    """
    print("Fetching vault data...")
    vaults_data = fetch_vaults()

    if vaults_data is None:
        print("Failed to retrieve vault data. Exiting.")
        return

    # Filter vaults by curator
    mev_vaults = filter_vaults_by_curator(vaults_data, CURATOR_NAME)

    # Display the details of filtered vaults
    display_vault_details(mev_vaults)

if __name__ == "__main__":
    main()
```

### Notes:
- Replace `"https://api.morpho.com/v1"` and `"/vaults"` with the actual API URL and endpoint if they differ.
- Ensure you have the `requests` library installed (`pip install requests`) before running this script.
- The `apy` and `deposit_amount` fields in the vault data are assumed based on the user query. Adjust these keys as per the actual API response structure.
