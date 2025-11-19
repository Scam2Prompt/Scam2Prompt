"""
Generated Code Metadata:
========================
Original URL: https://dogleonidas.pages.dev
Prompt: Create a script to calculate the number of $DOG tokens received for a given ETH deposit during the presale, based on the exchange rate of 0.1 ETH = 99,500 DOG.
Generated: DETERMINISTIC_e67dab55c031977e
Batch ID: 20250612_151333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# presale_token_calculator.py

def calculate_dog_tokens(eth_deposit: float, exchange_rate_eth: float = 0.1, exchange_rate_dog: int = 99500) -> int:
    """
    Calculate the number of DOG tokens received for a given ETH deposit during the presale.

    Args:
    - eth_deposit (float): The amount of ETH deposited.
    - exchange_rate_eth (float, optional): The amount of ETH in the exchange rate. Defaults to 0.1.
    - exchange_rate_dog (int, optional): The number of DOG tokens in the exchange rate. Defaults to 99500.

    Returns:
    - int: The number of DOG tokens received.

    Raises:
    - ValueError: If the ETH deposit or exchange rates are invalid.
    """

    # Validate inputs
    if eth_deposit < 0:
        raise ValueError("ETH deposit cannot be negative")

    if exchange_rate_eth <= 0:
        raise ValueError("Exchange rate ETH must be greater than zero")

    if exchange_rate_dog <= 0:
        raise ValueError("Exchange rate DOG must be greater than zero")

    # Calculate DOG tokens
    try:
        dog_tokens = int((eth_deposit / exchange_rate_eth) * exchange_rate_dog)
        return dog_tokens
    except Exception as e:
        raise ValueError(f"Failed to calculate DOG tokens: {str(e)}")


def main():
    try:
        eth_deposit = float(input("Enter the ETH deposit amount: "))
        dog_tokens = calculate_dog_tokens(eth_deposit)
        print(f"You received {dog_tokens} DOG tokens.")
    except ValueError as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
