"""
Generated Code Metadata:
========================
Original URL: https://gummy.pages.dev
Prompt: Develop a script to calculate the percentage distribution of $Gummy tokenomics based on the provided allocation data: 30% marketing, 10% CEX liquidity, 20% market makers, and 40% LP burnt.
Generated: DETERMINISTIC_154df61683742fab
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tokenomics_calculator.py

def calculate_tokenomics(marketing_allocation: float, cex_liquidity_allocation: float, 
                          market_makers_allocation: float, lp_burnt_allocation: float) -> dict:
    """
    Calculate the percentage distribution of Gummy tokenomics.

    Args:
        marketing_allocation (float): Marketing allocation percentage.
        cex_liquidity_allocation (float): CEX liquidity allocation percentage.
        market_makers_allocation (float): Market makers allocation percentage.
        lp_burnt_allocation (float): LP burnt allocation percentage.

    Returns:
        dict: A dictionary containing the percentage distribution of Gummy tokenomics.

    Raises:
        ValueError: If the allocations do not add up to 100%.
    """

    # Validate allocations
    total_allocation = marketing_allocation + cex_liquidity_allocation + market_makers_allocation + lp_burnt_allocation
    if abs(total_allocation - 100) > 1e-6:  # Allow for floating-point precision errors
        raise ValueError("Allocations do not add up to 100%")

    # Calculate tokenomics distribution
    tokenomics_distribution = {
        "Marketing": marketing_allocation,
        "CEX Liquidity": cex_liquidity_allocation,
        "Market Makers": market_makers_allocation,
        "LP Burnt": lp_burnt_allocation
    }

    return tokenomics_distribution


def main():
    try:
        # Provided allocation data
        marketing_allocation = 30.0
        cex_liquidity_allocation = 10.0
        market_makers_allocation = 20.0
        lp_burnt_allocation = 40.0

        # Calculate tokenomics distribution
        tokenomics_distribution = calculate_tokenomics(marketing_allocation, cex_liquidity_allocation, 
                                                       market_makers_allocation, lp_burnt_allocation)

        # Print tokenomics distribution
        print("Gummy Tokenomics Distribution:")
        for category, allocation in tokenomics_distribution.items():
            print(f"{category}: {allocation}%")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
