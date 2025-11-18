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
# Function to calculate and display the total minting fees in BTC
def calculate_minting_fees(provider_fee_percentage, network_fee_btc, minting_amount_btc):
    """
    Calculate the total minting fees in BTC, including provider fees and network fees.
    
    Args:
        provider_fee_percentage (float): The percentage fee charged by the provider (e.g., 2.5 for 2.5%).
        network_fee_btc (float): The fixed network fee in BTC.
        minting_amount_btc (float): The amount of BTC being minted.

    Returns:
        float: The total minting fees in BTC.
    """

    try:
        # Validate inputs
        if provider_fee_percentage < 0 or network_fee_btc < 0 or minting_amount_btc <= 0:
            raise ValueError("Invalid input values: fees and minting amount must be positive numbers.")

        # Calculate provider fee (percentage of the minting amount)
        provider_fee_btc = (provider_fee_percentage / 100) * minting_amount_btc
        
        # Calculate total fees
        total_fees_btc = provider_fee_btc + network_fee_btc
        
        # Display the calculated fees
        print(f"Provider Fee (BTC): {provider_fee_btc:.8f}")
        print(f"Network Fee (BTC): {network_fee_btc:.8f}")
        print(f"Total Minting Fees (BTC): {total_fees_btc:.8f}")
        
        return total_fees_btc

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    # Example parameters
    provider_fee_percentage = 2.5  # Provider charges 2.5% fee
    network_fee_btc = 0.0001      # Network fee is 0.0001 BTC
    minting_amount_btc = 0.05     # User is minting 0.05 BTC
    
    # Calculate and display the minting fees
    calculate_minting_fees(provider_fee_percentage, network_fee_btc, minting_amount_btc)
```
