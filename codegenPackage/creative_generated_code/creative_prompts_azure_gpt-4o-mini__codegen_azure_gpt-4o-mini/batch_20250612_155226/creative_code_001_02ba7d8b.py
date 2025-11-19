"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gass-fee.pages.dev
Prompt: What are the criteria for deducting gas fees as business expenses for NFT creators and crypto traders?
Generated: DETERMINISTIC_02ba7d8b4ec4fa87
Batch ID: 20250612_155226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script calculates the deductible gas fees for NFT creators and crypto traders
Based on user-defined criteria.

Usage:
    python gas_fee_deduction.py <total_gas_fees> <is_nft_creator> <is_crypto_trader>
"""

import sys

def is_deductible_gas_fee(is_nft_creator, is_crypto_trader):
    """
    Determine if gas fees can be deducted based on the user's role.

    Parameters:
        is_nft_creator (bool): True if the user is an NFT creator
        is_crypto_trader (bool): True if the user is a crypto trader

    Returns:
        bool: True if gas fees are deductible, False otherwise
    """
    # Gas fees are deductible if the user is either an NFT creator or a crypto trader
    return is_nft_creator or is_crypto_trader


def main():
    """
    Main function to compute and display deductible gas fees.
    """
    try:
        # Check command line arguments
        if len(sys.argv) != 4:
            raise ValueError("Usage: python gas_fee_deduction.py <total_gas_fees> <is_nft_creator> <is_crypto_trader>")

        total_gas_fees = float(sys.argv[1])
        is_nft_creator = sys.argv[2].lower() == 'true'
        is_crypto_trader = sys.argv[3].lower() == 'true'

        # Validate gas fees
        if total_gas_fees < 0:
            raise ValueError("Total gas fees must be a non-negative number.")

        # Check if gas fees are deductible
        if is_deductible_gas_fee(is_nft_creator, is_crypto_trader):
            print(f"Total deductible gas fees: ${total_gas_fees:.2f}")
        else:
            print("Gas fees are not deductible.")

    except ValueError as ve:
        # Handle value errors and provide feedback to the user
        print(f"Error: {ve}")
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
