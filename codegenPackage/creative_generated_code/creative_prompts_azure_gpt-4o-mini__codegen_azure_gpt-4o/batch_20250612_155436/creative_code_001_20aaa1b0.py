"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wwwmorpho.org
Prompt: Write a code snippet to calculate the APY for different vaults listed on Morpho, such as Spark DAI and MEV Capital USDC.
Generated: DETERMINISTIC_20aaa1b0f2a7b36d
Batch ID: 20250612_155436
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.morpho.com/vaults": {
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

def fetch_vault_data(api_url):
    """
    Fetch vault data from the Morpho API.
    
    Args:
        api_url (str): The URL of the API endpoint.
        
    Returns:
        list: A list of vaults with their respective details.
        
    Raises:
        Exception: If the API request fails or the response is invalid.
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch vault data: {e}")

def calculate_apy(vault_data):
    """
    Calculate the APY for the given vault data.
    
    Args:
        vault_data (dict): A dictionary containing details of a vault.
        
    Returns:
        float: The calculated APY for the vault.
    """
    try:
        # Ensure necessary keys exist
        if 'borrow_rate' not in vault_data or 'lend_rate' not in vault_data:
            raise ValueError("Vault data missing required fields: borrow_rate or lend_rate.")
        
        borrow_rate = float(vault_data['borrow_rate'])
        lend_rate = float(vault_data['lend_rate'])
        
        # Example formula for APY calculation (adjust according to Morpho's actual implementation)
        apy = lend_rate - borrow_rate
        
        # APY is often expressed as a percentage
        return apy * 100
    except ValueError as e:
        raise ValueError(f"Error calculating APY: {e}")

def main():
    """
    Main function to fetch vault data and calculate APYs.
    """
    # Morpho API endpoint (replace with the actual endpoint URL)
    api_url = "https://api.morpho.com/vaults"
    
    try:
        vaults = fetch_vault_data(api_url)
        
        if not isinstance(vaults, list):
            raise Exception("Unexpected response format. Expected a list of vaults.")
        
        print("Vault APYs:")
        for vault in vaults:
            name = vault.get('name', 'Unknown Vault')  # Default to 'Unknown Vault' if name is missing
            try:
                apy = calculate_apy(vault)
                print(f"{name}: {apy:.2f}% APY")
            except ValueError as e:
                print(f"{name}: Error calculating APY - {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
