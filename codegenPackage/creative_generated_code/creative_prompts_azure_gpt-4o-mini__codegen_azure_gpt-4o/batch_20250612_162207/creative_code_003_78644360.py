"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asd-col.pages.dev
Prompt: Create a function that calculates the number of $DOG tokens received for a given ETH amount during the presale.
Generated: DETERMINISTIC_786443608142c4b5
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_dog_tokens(eth_amount, eth_to_dog_rate):
    """
    Calculate the number of $DOG tokens received for a given ETH amount during the presale.

    Parameters:
        eth_amount (float): The amount of ETH being used to purchase $DOG tokens.
        eth_to_dog_rate (float): The conversion rate (number of $DOG tokens per 1 ETH).

    Returns:
        float: The number of $DOG tokens received.

    Raises:
        ValueError: If eth_amount or eth_to_dog_rate is less than or equal to zero.
    """
    try:
        # Validate the inputs
        if eth_amount <= 0:
            raise ValueError("ETH amount must be greater than zero.")
        if eth_to_dog_rate <= 0:
            raise ValueError("ETH to DOG rate must be greater than zero.")

        # Calculate the number of $DOG tokens
        dog_tokens = eth_amount * eth_to_dog_rate
        return dog_tokens

    except ValueError as e:
        # Handle invalid input errors gracefully
        print(f"Error: {e}")
        return None


# Example Usage
if __name__ == "__main__":
    eth_amount = 2.5  # Example ETH amount
    eth_to_dog_rate = 1000  # Example exchange rate: 1000 DOG tokens per ETH

    dog_tokens = calculate_dog_tokens(eth_amount, eth_to_dog_rate)

    if dog_tokens is not None:
        print(f"For {eth_amount} ETH, you will receive {dog_tokens} $DOG tokens.")
```
