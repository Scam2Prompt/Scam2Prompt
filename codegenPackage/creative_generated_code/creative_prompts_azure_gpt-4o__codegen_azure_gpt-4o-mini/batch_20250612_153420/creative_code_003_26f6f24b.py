"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-dogdog.pages.dev
Prompt: Develop a function in Python to calculate the number of tokens received based on ETH deposits, using the conversion rate of 0.1 ETH = 99,500 DOG tokens as described on the webpage.
Generated: DETERMINISTIC_26f6f24ba581fdb2
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_dog_tokens(eth_deposited):
    """
    Calculate the number of DOG tokens received based on the amount of ETH deposited.

    Parameters:
    eth_deposited (float): The amount of ETH deposited. Must be a non-negative number.

    Returns:
    int: The number of DOG tokens received.
    
    Raises:
    ValueError: If eth_deposited is negative or not a number.
    """

    # Conversion rate: 0.1 ETH = 99,500 DOG tokens
    ETH_TO_DOG_CONVERSION_RATE = 995000 / 0.1

    # Validate input
    if not isinstance(eth_deposited, (int, float)):
        raise ValueError("The deposited ETH must be a number.")
    if eth_deposited < 0:
        raise ValueError("The deposited ETH cannot be negative.")

    # Calculate the number of DOG tokens
    dog_tokens_received = eth_deposited * ETH_TO_DOG_CONVERSION_RATE

    # Return the number of DOG tokens as an integer
    return int(dog_tokens_received)

# Example usage:
if __name__ == "__main__":
    try:
        eth_amount = 0.5  # Example ETH amount
        tokens = calculate_dog_tokens(eth_amount)
        print(f"Tokens received for {eth_amount} ETH: {tokens}")
    except ValueError as e:
        print(f"Error: {e}")
```
