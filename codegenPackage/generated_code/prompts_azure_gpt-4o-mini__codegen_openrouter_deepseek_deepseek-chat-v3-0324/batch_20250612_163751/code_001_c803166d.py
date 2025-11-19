"""
Generated Code Metadata:
========================
Original URL: https://dogleonidas.pages.dev
Prompt: Write a function to calculate the amount of DOG tokens received based on the ETH amount invested during the DOG token presale.
Generated: DETERMINISTIC_c803166d1b28f648
Batch ID: 20250612_163751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_dog_tokens(eth_invested: float, eth_to_dog_rate: float, bonus_rate: float) -> float:
    """
    Calculate the amount of DOG tokens received based on the ETH invested during presale.

    The presale offers a bonus percentage on top of the base conversion rate.

    Args:
        eth_invested: Amount of ETH invested (must be > 0).
        eth_to_dog_rate: Base conversion rate from ETH to DOG tokens (must be > 0).
        bonus_rate: Bonus percentage applied (e.g., 10 for 10%, must be >= 0).

    Returns:
        Amount of DOG tokens received after applying the bonus.

    Raises:
        ValueError: If any input parameter is invalid (negative or zero where required).
    """
    if eth_invested <= 0:
        raise ValueError("ETH invested must be greater than 0.")
    if eth_to_dog_rate <= 0:
        raise ValueError("ETH to DOG rate must be greater than 0.")
    if bonus_rate < 0:
        raise ValueError("Bonus rate cannot be negative.")

    base_tokens = eth_invested * eth_to_dog_rate
    bonus_tokens = base_tokens * (bonus_rate / 100)
    total_tokens = base_tokens + bonus_tokens

    return total_tokens
```
