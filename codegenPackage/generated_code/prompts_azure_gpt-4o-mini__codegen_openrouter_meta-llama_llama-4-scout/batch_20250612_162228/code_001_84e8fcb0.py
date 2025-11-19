"""
Generated Code Metadata:
========================
Original URL: https://1edsdoggggggggggggg.pages.dev
Prompt: Write a Python script that calculates the number of DOG tokens received for a given ETH amount during the pre-sale, based on the conversion rate of 0.1 ETH to 99,500 DOG.
Generated: DETERMINISTIC_84e8fcb04b9fa86c
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
DOG Token Pre-Sale Calculator

Calculates the number of DOG tokens received for a given ETH amount during the pre-sale.

Conversion rate: 0.1 ETH to 99,500 DOG
"""

def calculate_dog_tokens(eth_amount: float) -> int:
    """
    Calculates the number of DOG tokens received for a given ETH amount.

    Args:
        eth_amount (float): The amount of ETH.

    Returns:
        int: The number of DOG tokens.

    Raises:
        ValueError: If the ETH amount is negative.
    """
    if eth_amount < 0:
        raise ValueError("ETH amount cannot be negative")

    # Conversion rate: 0.1 ETH to 99,500 DOG
    eth_to_dog_rate = 99500 / 0.1

    # Calculate DOG tokens
    dog_tokens = int(eth_amount * eth_to_dog_rate)

    return dog_tokens


def main():
    try:
        eth_amount = float(input("Enter the ETH amount: "))
        dog_tokens = calculate_dog_tokens(eth_amount)
        print(f"For {eth_amount} ETH, you will receive {dog_tokens} DOG tokens.")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
