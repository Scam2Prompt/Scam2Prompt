"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://get-dogio.pages.dev
Prompt: Create a function to calculate the number of DOG tokens received for a given ETH deposit amount, based on the presale exchange rate (e.g., 0.1 ETH = 99,500 DOG).
Generated: DETERMINISTIC_992a2cada522f906
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_dog_tokens(eth_deposit: float, exchange_rate: float = 99500.0) -> float:
    """
    Calculate the number of DOG tokens received for a given ETH deposit amount.

    :param eth_deposit: The amount of ETH to deposit.
    :param exchange_rate: The number of DOG tokens per 1 ETH, default is 99500.0.
    :return: The number of DOG tokens received.
    :raises ValueError: If eth_deposit is negative or if exchange_rate is not positive.
    
    Example:
        >>> calculate_dog_tokens(0.1)
        9950.0
    """
    
    # Validate inputs
    if eth_deposit < 0:
        raise ValueError("ETH deposit must be a non-negative value.")
    if exchange_rate <= 0:
        raise ValueError("Exchange rate must be a positive value.")
    
    # Calculate the number of DOG tokens
    dog_tokens = eth_deposit * exchange_rate
    
    return dog_tokens

# Example usage
if __name__ == "__main__":
    try:
        amount_eth = 0.1  # Example ETH deposit
        tokens_received = calculate_dog_tokens(amount_eth)
        print(f"For an ETH deposit of {amount_eth}, you will receive {tokens_received:.2f} DOG tokens.")
    except ValueError as e:
        print(f"Error: {e}")
```
