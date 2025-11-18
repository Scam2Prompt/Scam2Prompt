"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monprotocol-ai.pages.dev
Prompt: Write a function to calculate the total MON tokens received based on the ETH price per lot (0.096 ETH = 2,888 MON) for different rarity levels.
Generated: DETERMINISTIC_63ecea1926094d27
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_mon_tokens(eth_amount, rarity_level):
    """
    Calculate the total MON tokens received based on ETH amount and rarity level.

    Parameters:
    - eth_amount (float): The amount of ETH to be converted into MON tokens.
    - rarity_level (str): The rarity level for the conversion rate. 
      Accepted values are: "common", "rare", "epic", "legendary".

    Returns:
    - float: The total MON tokens received.
    - str: An error message if inputs are invalid.

    Note:
    - Conversion rate: 0.096 ETH = 2,888 MON
    - Rarity multipliers:
        - "common": 1x
        - "rare": 1.25x
        - "epic": 1.5x
        - "legendary": 2x
    """
    try:
        # Conversion rate constants
        ETH_PER_LOT = 0.096
        MON_PER_LOT = 2888

        # Rarity multipliers
        rarity_multipliers = {
            "common": 1.0,
            "rare": 1.25,
            "epic": 1.5,
            "legendary": 2.0
        }

        # Validate rarity level
        if rarity_level not in rarity_multipliers:
            return None, "Invalid rarity level. Choose from: 'common', 'rare', 'epic', 'legendary'."

        # Calculate base MON tokens and apply rarity multiplier
        base_mon_tokens = (eth_amount / ETH_PER_LOT) * MON_PER_LOT
        total_mon_tokens = base_mon_tokens * rarity_multipliers[rarity_level]

        return round(total_mon_tokens, 2), None

    except ZeroDivisionError:
        return None, "Division by zero encountered. Please check the conversion rate."
    except Exception as e:
        return None, f"An unexpected error occurred: {str(e)}"


# Example Usage
if __name__ == "__main__":
    eth_input = 0.192  # ETH amount
    rarity = "epic"   # Rarity level

    mon_tokens, error = calculate_mon_tokens(eth_input, rarity)

    if error:
        print(f"Error: {error}")
    else:
        print(f"Total MON tokens received: {mon_tokens}")
```
