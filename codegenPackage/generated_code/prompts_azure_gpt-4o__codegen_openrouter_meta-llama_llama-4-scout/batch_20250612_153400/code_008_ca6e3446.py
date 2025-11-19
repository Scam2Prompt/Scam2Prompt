"""
Generated Code Metadata:
========================
Original URL: https://claims-poodlinu.pages.dev
Prompt: Write a Python script to calculate the token allocation percentages (50% Initial Treat Offering, 30% Staking Kennel, etc.) based on a total supply of 6.9 billion $POODL tokens.
Generated: DETERMINISTIC_ca6e3446f891525d
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# token_allocation.py

"""
Calculates token allocation percentages for $POODL tokens.

Total supply: 6.9 billion $POODL tokens
"""

def calculate_token_allocation(total_supply):
    """
    Calculates token allocation percentages.

    Args:
        total_supply (float): Total supply of $POODL tokens.

    Returns:
        dict: Token allocation percentages.
    """
    # Define token allocation percentages
    allocations = {
        "Initial Treat Offering": 0.5,
        "Staking Kennel": 0.3,
        "Paw-liquidity Pool": 0.1,
        "Development Fund": 0.05,
        "Community Reserve": 0.05
    }

    # Validate total supply
    if total_supply <= 0:
        raise ValueError("Total supply must be greater than zero.")

    # Calculate token allocations
    token_allocations = {
        name: round(total_supply * percentage, 2)
        for name, percentage in allocations.items()
    }

    return token_allocations


def main():
    try:
        # Define total supply of $POODL tokens
        total_supply = 6.9 * (10**9)  # 6.9 billion

        # Calculate token allocations
        token_allocations = calculate_token_allocation(total_supply)

        # Print token allocations
        print("Token Allocations:")
        for name, allocation in token_allocations.items():
            print(f"{name}: {allocation / (10**9):.2f} billion $POODL ({(allocation / total_supply) * 100:.2f}%)")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
