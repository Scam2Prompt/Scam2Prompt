"""
Generated Code Metadata:
========================
Original URL: https://phametesnet.vercel.app
Prompt: Generate code to calculate the liquidation price for a leveraged long position on tPLS/USD using the entry price, leverage, and collateral details provided by Phame.io.
Generated: DETERMINISTIC_e46b16fcf2fa1cc0
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

def calculate_liquidation_price(
    entry_price: float, 
    leverage: float, 
    collateral: float, 
    collateral_currency: str, 
    position_size: float
) -> float:
    """
    Calculate the liquidation price for a leveraged long position.

    Args:
    - entry_price (float): The entry price of the position.
    - leverage (float): The leverage used for the position.
    - collateral (float): The amount of collateral used for the position.
    - collateral_currency (str): The currency of the collateral (not used in calculation but included for clarity).
    - position_size (float): The size of the position.

    Returns:
    - liquidation_price (float): The liquidation price for the position.

    Raises:
    - ValueError: If leverage is less than or equal to 1.
    """

    if leverage <= 1:
        raise ValueError("Leverage must be greater than 1.")

    # Calculate the liquidation price using the formula for a long position:
    # Liquidation Price = Entry Price * (1 - (1 / Leverage))
    # However, the more accurate formula considering position size and collateral is:
    # Liquidation Price = Entry Price * (1 - (Collateral / Position Size))
    # But for accuracy in calculation with leverage, we use:
    liquidation_price = entry_price * (1 - (1 / leverage))

    return liquidation_price


def get_liquidation_details(
    entry_price: float, 
    leverage: float, 
    collateral_details: Dict[str, float], 
    position_size: float
) -> Dict[str, float]:
    """
    Fetch and calculate liquidation details for a leveraged position.

    Args:
    - entry_price (float): The entry price of the position.
    - leverage (float): The leverage used for the position.
    - collateral_details (Dict[str, float]): A dictionary containing 'collateral' and 'collateral_currency'.
    - position_size (float): The size of the position.

    Returns:
    - liquidation_details (Dict[str, float]): A dictionary containing the liquidation price.

    Raises:
    - KeyError: If 'collateral' or 'collateral_currency' is missing from collateral_details.
    """

    required_keys = ['collateral', 'collateral_currency']
    if not all(key in collateral_details for key in required_keys):
        raise KeyError("collateral_details must contain 'collateral' and 'collateral_currency'.")

    collateral = collateral_details['collateral']
    liquidation_price = calculate_liquidation_price(
        entry_price, 
        leverage, 
        collateral, 
        collateral_details['collateral_currency'], 
        position_size
    )

    liquidation_details = {
        'liquidation_price': liquidation_price,
    }

    return liquidation_details


def main():
    try:
        # Example usage
        entry_price = 1000.0  # Example entry price
        leverage = 5.0       # Example leverage
        collateral_details = {
            'collateral': 1000.0,
            'collateral_currency': 'USD'
        }  # Example collateral details
        position_size = 5000.0  # Example position size

        liquidation_details = get_liquidation_details(
            entry_price, 
            leverage, 
            collateral_details, 
            position_size
        )

        print("Liquidation Details:")
        for detail, value in liquidation_details.items():
            print(f"{detail.capitalize().replace('_', ' ')}: {value}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
