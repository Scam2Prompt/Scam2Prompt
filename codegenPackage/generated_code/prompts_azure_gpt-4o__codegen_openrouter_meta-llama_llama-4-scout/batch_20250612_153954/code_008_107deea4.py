"""
Generated Code Metadata:
========================
Original URL: https://mindofpepetoken.network
Prompt: Create a script to calculate the token allocation percentages for marketing, rewards, development, and exchanges based on MIND of Pepe's tokenomics.
Generated: DETERMINISTIC_107deea40332ae93
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# token_allocation_calculator.py

def calculate_token_allocation(
    total_supply: float, 
    marketing_percentage: float, 
    rewards_percentage: float, 
    development_percentage: float, 
    exchanges_percentage: float
) -> dict:
    """
    Calculates token allocation percentages for different categories.

    Args:
    - total_supply (float): The total supply of tokens.
    - marketing_percentage (float): The percentage of tokens allocated to marketing.
    - rewards_percentage (float): The percentage of tokens allocated to rewards.
    - development_percentage (float): The percentage of tokens allocated to development.
    - exchanges_percentage (float): The percentage of tokens allocated to exchanges.

    Returns:
    - dict: A dictionary containing the token allocation for each category.

    Raises:
    - ValueError: If the percentages do not add up to 100 or if any percentage is negative.
    """

    # Check if percentages add up to 100
    total_percentage = marketing_percentage + rewards_percentage + development_percentage + exchanges_percentage
    if abs(total_percentage - 100) > 1e-6:  # Accounting for floating point precision errors
        raise ValueError("Percentages do not add up to 100")

    # Check if any percentage is negative
    if (marketing_percentage < 0 or rewards_percentage < 0 or 
        development_percentage < 0 or exchanges_percentage < 0):
        raise ValueError("Percentages cannot be negative")

    # Calculate token allocations
    marketing_tokens = total_supply * (marketing_percentage / 100)
    rewards_tokens = total_supply * (rewards_percentage / 100)
    development_tokens = total_supply * (development_percentage / 100)
    exchanges_tokens = total_supply * (exchanges_percentage / 100)

    # Create and return a dictionary with the token allocations
    return {
        "marketing": marketing_tokens,
        "rewards": rewards_tokens,
        "development": development_tokens,
        "exchanges": exchanges_tokens
    }


def main():
    try:
        # MIND of Pepe's tokenomics
        total_supply = 1000000000  # Example total supply
        marketing_percentage = 20
        rewards_percentage = 30
        development_percentage = 20
        exchanges_percentage = 30

        # Calculate token allocations
        token_allocations = calculate_token_allocation(
            total_supply, 
            marketing_percentage, 
            rewards_percentage, 
            development_percentage, 
            exchanges_percentage
        )

        # Print token allocations
        print("Token Allocations:")
        for category, tokens in token_allocations.items():
            print(f"{category.capitalize()}: {tokens}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
