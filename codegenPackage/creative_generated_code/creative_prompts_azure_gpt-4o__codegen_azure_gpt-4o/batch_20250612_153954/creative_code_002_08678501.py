"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trollercat-claim.pages.dev
Prompt: Create a function to calculate the total $TCAT tokens received based on the current presale price and input cryptocurrency amount, supporting multiple networks like ERC-20, BSC, and Solana.
Generated: DETERMINISTIC_08678501bbda934c
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import Literal

# Define supported networks
SUPPORTED_NETWORKS = ["ERC-20", "BSC", "Solana"]

# Presale prices (in terms of cryptocurrency per $TCAT token)
PRESALE_PRICES = {
    "ERC-20": 0.01,  # Example: 1 TCAT = 0.01 ETH
    "BSC": 0.0002,   # Example: 1 TCAT = 0.0002 BNB
    "Solana": 0.0001 # Example: 1 TCAT = 0.0001 SOL
}

def calculate_tcat_tokens(network: Literal["ERC-20", "BSC", "Solana"], crypto_amount: float) -> float:
    """
    Calculate the total $TCAT tokens received during the presale based on the network and cryptocurrency amount.
    
    Args:
        network (str): The blockchain network used (e.g., 'ERC-20', 'BSC', 'Solana').
        crypto_amount (float): The amount of cryptocurrency being exchanged for $TCAT tokens.
    
    Returns:
        float: The total number of $TCAT tokens received.
    
    Raises:
        ValueError: If an unsupported network is provided or if crypto_amount is negative.
    """
    # Validate network input
    if network not in SUPPORTED_NETWORKS:
        raise ValueError(f"Unsupported network '{network}'. Supported networks are: {', '.join(SUPPORTED_NETWORKS)}")

    # Validate crypto_amount input
    if crypto_amount < 0:
        raise ValueError("Cryptocurrency amount must be non-negative.")

    # Get the presale price for the specified network
    presale_price = PRESALE_PRICES[network]

    # Calculate the number of $TCAT tokens received
    tcat_tokens = crypto_amount / presale_price

    return tcat_tokens

# Example usage:
# Uncomment the lines below to test the function in a real environment.
# try:
#     network = "ERC-20"
#     crypto_amount = 0.1  # Example input
#     tcat_tokens = calculate_tcat_tokens(network, crypto_amount)
#     print(f"You will receive {tcat_tokens} $TCAT tokens on the {network} network.")
# except ValueError as e:
#     print(f"Error: {e}")
```
