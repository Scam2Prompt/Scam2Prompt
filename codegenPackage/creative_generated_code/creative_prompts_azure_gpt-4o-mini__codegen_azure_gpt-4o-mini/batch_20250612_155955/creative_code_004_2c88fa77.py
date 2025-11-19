"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerswiss.com
Prompt: Create a function that calculates the total earnings based on the number of upgrades and coins collected in a game.
Generated: DETERMINISTIC_2c88fa77a805fc7f
Batch ID: 20250612_155955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_total_earnings(upgrades: int, coins_collected: int) -> float:
    """
    Calculate the total earnings based on the number of upgrades and coins collected.

    Parameters:
    upgrades (int): The number of upgrades purchased in the game.
    coins_collected (int): The total number of coins collected during gameplay.

    Returns:
    float: The total earnings calculated as:
           (base_coin_value * coins_collected) + (upgrade_value * upgrades)

    Raises:
    ValueError: If upgrades or coins_collected is negative.
    """
    
    # Define constants for coin and upgrade values
    BASE_COIN_VALUE = 0.1  # Value of each coin
    UPGRADE_VALUE = 5.0    # Value of each upgrade

    # Validate inputs
    if upgrades < 0:
        raise ValueError("The number of upgrades cannot be negative.")
    if coins_collected < 0:
        raise ValueError("The number of coins collected cannot be negative.")

    # Calculate total earnings
    total_earnings = (BASE_COIN_VALUE * coins_collected) + (UPGRADE_VALUE * upgrades)
    
    return total_earnings

# Example usage
if __name__ == "__main__":
    try:
        # Replace these values with actual game data
        upgrades = 3
        coins_collected = 150
        earnings = calculate_total_earnings(upgrades, coins_collected)
        print(f"Total earnings: ${earnings:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
