"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pytheth.com
Prompt: Explain how Pytheth's market data oracles can be used to prevent price manipulation in DeFi protocols.
Generated: DETERMINISTIC_9fdf0f3c01086c63
Batch ID: 20250612_155015
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://pyth.network/api/v1": {
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
"""
This script demonstrates how Pyth's market data oracles can be integrated into a DeFi protocol
to prevent price manipulation. It fetches trusted price data from Pyth and validates prices 
before allowing transactions, mitigating risks of price manipulation attacks.

Prerequisites:
- Install the `pyth-client` library for interacting with Pyth's oracle.
    pip install pyth-client
- Pyth network access and appropriate credentials for fetching signed data.
"""

from pyth_client import PythClient, PythError

# Define constants for the Pyth network configuration
PYTH_NETWORK_URL = "https://pyth.network/api/v1"  # Replace with correct Pyth network endpoint
ASSET_PRICE_ID = "0x1234abcd5678efgh9012ijkl3456mnop"  # Example asset price ID
PRICE_MAX_AGE_SECONDS = 60  # Maximum age of price data in seconds

def get_asset_price(client, asset_price_id):
    """
    Fetch the price of the asset from Pyth's oracle.
    
    Args:
        client (PythClient): Instance of PythClient for interacting with Pyth.
        asset_price_id (str): The ID of the asset whose price is being fetched.
        
    Returns:
        float: The trusted price of the asset.
        
    Raises:
        ValueError: If the price data is too old or invalid.
    """
    try:
        # Fetch price data from Pyth
        price_data = client.get_price(asset_price_id)
        
        # Check if price data is stale
        if price_data.age_seconds > PRICE_MAX_AGE_SECONDS:
            raise ValueError("Price data is too old to be trusted.")
        
        # Return the trusted price
        return price_data.price
        
    except PythError as e:
        # Handle errors specific to Pyth
        raise ValueError(f"Failed to fetch price data: {str(e)}")
    except Exception as e:
        # General error handling
        raise ValueError(f"An unexpected error occurred: {str(e)}")

def validate_transaction(price, user_price_input):
    """
    Validate a DeFi transaction based on trusted price data.
    
    Args:
        price (float): Trusted price fetched from Pyth.
        user_price_input (float): Price input provided by the user.
        
    Returns:
        bool: True if the transaction is valid, False otherwise.
    """
    # Define an allowable deviation percentage (e.g., 1%)
    ALLOWABLE_DEVIATION_PERCENT = 0.01
    
    # Calculate price deviation
    deviation = abs(price - user_price_input) / price
    
    # Transaction is valid only if deviation is within the acceptable range
    return deviation <= ALLOWABLE_DEVIATION_PERCENT

def main():
    """
    Main function to demonstrate price validation for a DeFi protocol using Pyth.
    """
    try:
        # Initialize Pyth client
        client = PythClient(PYTH_NETWORK_URL)
        
        # Fetch trusted price from Pyth oracle
        trusted_price = get_asset_price(client, ASSET_PRICE_ID)
        print(f"Trusted price fetched from Pyth: {trusted_price}")

        # Example: User-provided price for a DeFi transaction
        user_price_input = float(input("Enter the price provided by the user: "))
        
        # Validate the transaction
        if validate_transaction(trusted_price, user_price_input):
            print("Transaction is valid.")
        else:
            print("Transaction rejected due to price manipulation risk.")
            
    except ValueError as e:
        # Handle validation errors
        print(f"Error: {str(e)}")
    except Exception as e:
        # Handle unexpected errors
        print(f"Unexpected error occurred: {str(e)}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
