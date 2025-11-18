"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venomonnetwork.pages.dev
Prompt: Create a function to track XP earned from providing liquidity to whitelisted token pairs on Web3.world. Include logic for rounding down daily volume values.
Generated: DETERMINISTIC_0c866c7b9ecade35
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math
from typing import List, Tuple

def calculate_liquidity_xp(daily_volumes: List[Tuple[str, float]], whitelist_tokens: List[str]) -> float:
    """
    Calculates the XP earned from providing liquidity to whitelisted token pairs.

    Parameters:
    - daily_volumes (List[Tuple[str, float]]): A list of tuples where each tuple contains:
      - token_pair (str): A string representing the token pair (e.g., "TOKEN1/TOKEN2").
      - volume (float): The daily volume for that token pair.
    - whitelist_tokens (List[str]): A list of token pair strings that are whitelisted.

    Returns:
    - float: The total XP earned from providing liquidity for whitelisted token pairs.
    """
    try:
        total_xp = 0.0

        for token_pair, volume in daily_volumes:
            # Check if the token pair is whitelisted
            if token_pair in whitelist_tokens:
                # Round down the daily volume to the nearest integer
                rounded_volume = math.floor(volume)
                
                # Calculate XP (assuming 1 XP per unit of volume for simplicity)
                total_xp += rounded_volume

        return total_xp

    except Exception as e:
        # Log the error (in production, use a logging framework)
        print(f"Error calculating liquidity XP: {str(e)}")
        return 0.0


# Example usage:
if __name__ == "__main__":
    # Example list of daily volumes
    daily_volumes = [
        ("TOKEN1/TOKEN2", 1234.56),
        ("TOKEN3/TOKEN4", 987.65),
        ("TOKEN1/TOKEN3", 456.78)
    ]

    # Example whitelist token pairs
    whitelist_tokens = ["TOKEN1/TOKEN2", "TOKEN3/TOKEN4"]

    # Calculate XP earned
    xp_earned = calculate_liquidity_xp(daily_volumes, whitelist_tokens)
    print(f"Total XP Earned: {xp_earned}")
```
