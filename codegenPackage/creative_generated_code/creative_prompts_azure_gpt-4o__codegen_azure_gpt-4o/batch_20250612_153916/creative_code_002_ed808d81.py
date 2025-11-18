"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbinu.app
Prompt: Generate code to calculate the percentage of Arbinu tokens that have been burned and staked, given the total supply and relevant tokenomics data.
Generated: DETERMINISTIC_ed808d8193ab7887
Batch ID: 20250612_153916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary library
from typing import Dict

def calculate_token_distribution(total_supply: float, token_data: Dict[str, float]) -> Dict[str, float]:
    """
    Calculate the percentage of Arbinu tokens that have been burned and staked.

    Parameters:
    total_supply (float): Total supply of Arbinu tokens.
    token_data (Dict[str, float]): A dictionary containing tokenomics data with keys:
                                   - 'burned': The amount of burned tokens.
                                   - 'staked': The amount of staked tokens.

    Returns:
    Dict[str, float]: A dictionary containing the percentage of burned and staked tokens.
                      Keys: 'burned_percentage', 'staked_percentage'
    """
    # Validate input
    if total_supply <= 0:
        raise ValueError("Total supply must be greater than 0.")
    if 'burned' not in token_data or 'staked' not in token_data:
        raise KeyError("Token data must include 'burned' and 'staked' keys.")
    if not isinstance(token_data['burned'], (int, float)) or not isinstance(token_data['staked'], (int, float)):
        raise TypeError("'burned' and 'staked' values must be numeric.")
    if token_data['burned'] < 0 or token_data['staked'] < 0:
        raise ValueError("'burned' and 'staked' values must not be negative.")

    # Calculate percentages
    burned_percentage = (token_data['burned'] / total_supply) * 100
    staked_percentage = (token_data['staked'] / total_supply) * 100

    # Return the results
    return {
        "burned_percentage": round(burned_percentage, 2),
        "staked_percentage": round(staked_percentage, 2)
    }

# Example usage
if __name__ == "__main__":
    try:
        # Example total supply and tokenomics data
        total_supply = 1000000  # Total supply of Arbinu tokens
        token_data = {
            "burned": 250000,   # Amount of burned tokens
            "staked": 300000    # Amount of staked tokens
        }

        # Calculate percentages
        percentages = calculate_token_distribution(total_supply, token_data)
        print("Percentage of burned tokens:", percentages["burned_percentage"], "%")
        print("Percentage of staked tokens:", percentages["staked_percentage"], "%")
    except Exception as e:
        print(f"Error: {e}")
```
