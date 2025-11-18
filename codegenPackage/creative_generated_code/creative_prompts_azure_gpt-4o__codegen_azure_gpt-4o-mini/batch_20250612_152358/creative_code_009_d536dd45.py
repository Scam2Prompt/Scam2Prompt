"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mintgenesis.pages.dev
Prompt: Create a function to calculate and display the total minting fees in BTC, including provider fees and network fees, based on user-selected parameters.
Generated: DETERMINISTIC_d536dd4523a2a09b
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Set up logging for error reporting
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_minting_fees(base_fee: float, provider_fee_percentage: float, network_fee: float) -> float:
    """
    Calculate the total minting fees in BTC.
    
    Args:
        base_fee (float): The base minting fee in BTC.
        provider_fee_percentage (float): The percentage of the provider fee as a decimal (e.g., 0.05 for 5%).
        network_fee (float): The network fee in BTC.
        
    Returns:
        float: The total minting fees calculated.
    
    Raises:
        ValueError: If any of the input values are negative.
    """
    # Validate inputs
    if base_fee < 0 or provider_fee_percentage < 0 or network_fee < 0:
        logging.error("Negative input value provided.")
        raise ValueError("Base fee, provider fee percentage, and network fee must be non-negative.")
    
    # Calculate provider fee
    provider_fee = base_fee * provider_fee_percentage
    
    # Calculate total minting fees
    total_fees = base_fee + provider_fee + network_fee
    
    return total_fees

def display_minting_fees(base_fee: float, provider_fee_percentage: float, network_fee: float) -> None:
    """
    Display the total minting fees in BTC.
    
    Args:
        base_fee (float): The base minting fee in BTC.
        provider_fee_percentage (float): The percentage of the provider fee as a decimal.
        network_fee (float): The network fee in BTC.
    """
    try:
        total_fees = calculate_minting_fees(base_fee, provider_fee_percentage, network_fee)
        print(f"Total minting fees: {total_fees:.8f} BTC")
    except ValueError as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    # User-selected parameters
    base_fee = 0.001  # Base minting fee in BTC
    provider_fee_percentage = 0.05  # 5% provider fee
    network_fee = 0.0001  # Network fee in BTC

    # Display the calculated minting fees
    display_minting_fees(base_fee, provider_fee_percentage, network_fee)
```
