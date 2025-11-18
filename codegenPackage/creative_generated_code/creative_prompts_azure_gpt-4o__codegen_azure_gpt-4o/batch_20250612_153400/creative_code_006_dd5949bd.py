"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marketplace-dogcoin.pages.dev
Prompt: Write a function in Python that calculates the remaining presale cap in ETH based on the total deposits made to the DOG token presale smart contract.
Generated: DETERMINISTIC_dd5949bd13f4da1f
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary modules
from typing import List

def calculate_remaining_presale_cap(total_deposits: List[float], presale_cap: float) -> float:
    """
    Calculate the remaining presale cap for the DOG token presale.

    Parameters:
        total_deposits (List[float]): A list of deposit amounts (in ETH) made to the presale contract.
        presale_cap (float): The maximum presale cap (in ETH).

    Returns:
        float: The remaining presale cap (in ETH). Returns 0 if the cap is exceeded.
    """
    try:
        # Validate inputs
        if not isinstance(total_deposits, list) or not all(isinstance(d, (int, float)) for d in total_deposits):
            raise ValueError("total_deposits must be a list of numbers (int or float).")
        
        if not isinstance(presale_cap, (int, float)) or presale_cap <= 0:
            raise ValueError("presale_cap must be a positive number (int or float).")
        
        # Calculate the sum of deposits
        total_deposited_eth = sum(total_deposits)
        
        # Calculate remaining presale cap
        remaining_cap = presale_cap - total_deposited_eth
        
        # Ensure remaining cap is not negative
        return max(remaining_cap, 0)
    
    except ValueError as ve:
        raise ve  # Re-raise ValueError with the original message
    except Exception as e:
        # Catch all other unexpected errors
        raise RuntimeError(f"An unexpected error occurred: {str(e)}")

# Example usage:
if __name__ == "__main__":
    # Presale details
    deposits = [2.5, 3.0, 1.2]  # Example deposit amounts in ETH
    cap = 10.0  # Presale cap in ETH

    try:
        remaining_cap = calculate_remaining_presale_cap(deposits, cap)
        print(f"Remaining presale cap: {remaining_cap} ETH")
    except Exception as error:
        print(f"Error: {error}")
```
