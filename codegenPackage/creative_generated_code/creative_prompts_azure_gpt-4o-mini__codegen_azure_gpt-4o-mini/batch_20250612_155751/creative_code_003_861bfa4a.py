"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xai560k.com
Prompt: Create a function that calculates the potential bonus for participating in the xAI560K presale based on different cryptocurrencies.
Generated: DETERMINISTIC_861bfa4a4f40d5ae
Batch ID: 20250612_155751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_bonus(participation_amount: float, crypto_type: str, bonus_percentage: float) -> float:
    """
    Calculate the potential bonus for participating in the xAI560K presale.

    Parameters:
    participation_amount (float): The amount of cryptocurrency the user participates with.
    crypto_type (str): The type of cryptocurrency being used. Valid options are 'ETH', 'BTC', 'USDT'.
    bonus_percentage (float): The percentage of bonus calculated on the participation amount.

    Returns:
    float: The calculated bonus amount.

    Raises:
    ValueError: If the participation amount is less than or equal to zero.
    ValueError: If the crypto_type is not one of the valid options.
    ValueError: If the bonus_percentage is not in the range of 0 to 100.
    """
    
    # Define valid cryptocurrency types
    valid_crypto_types = ['ETH', 'BTC', 'USDT']

    # Validate participation amount
    if participation_amount <= 0:
        raise ValueError("Participation amount must be greater than zero.")

    # Validate cryptocurrency type
    if crypto_type not in valid_crypto_types:
        raise ValueError(f"Invalid cryptocurrency type '{crypto_type}'. Valid options are: {', '.join(valid_crypto_types)}.")

    # Validate bonus percentage
    if not (0 <= bonus_percentage <= 100):
        raise ValueError("Bonus percentage must be between 0 and 100.")

    # Calculate and return the bonus amount
    bonus_amount = (participation_amount * (bonus_percentage / 100))
    return bonus_amount

# Example usage
if __name__ == "__main__":
    try:
        participation_amount = 1000.0  # Example participation amount in USD
        crypto_type = 'ETH'              # Example cryptocurrency type
        bonus_percentage = 10.0          # Example bonus percentage

        bonus = calculate_bonus(participation_amount, crypto_type, bonus_percentage)
        print(f"The potential bonus for participating with {crypto_type} is: ${bonus:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
```
