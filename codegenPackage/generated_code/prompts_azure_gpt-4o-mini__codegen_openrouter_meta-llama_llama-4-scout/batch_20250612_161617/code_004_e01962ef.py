"""
Generated Code Metadata:
========================
Original URL: https://infinite-v2.vercel.app
Prompt: Create a function that calculates risk factors for vaults in a DeFi trading environment, inspired by the metrics discussed on Infinite Trading's site.
Generated: DETERMINISTIC_e01962ef0ca9db2b
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_risk_factors(
    collateral_ratio: float, 
    liquidation_ratio: float, 
    volatility: float, 
    liquidity: float, 
    debt_to_equity: float
) -> dict:
    """
    Calculates risk factors for vaults in a DeFi trading environment.

    Args:
    - collateral_ratio (float): The ratio of collateral to debt.
    - liquidation_ratio (float): The ratio at which liquidation occurs.
    - volatility (float): The historical volatility of the collateral asset.
    - liquidity (float): The liquidity of the collateral asset.
    - debt_to_equity (float): The debt-to-equity ratio of the vault.

    Returns:
    - dict: A dictionary containing the calculated risk factors.
    """

    # Check for invalid input values
    if collateral_ratio < 0 or liquidation_ratio < 0 or volatility < 0 or liquidity < 0 or debt_to_equity < 0:
        raise ValueError("All input values must be non-negative.")

    # Calculate the collateralization risk factor
    collateralization_risk_factor = 1 - (collateral_ratio / liquidation_ratio)
    collateralization_risk_factor = max(collateralization_risk_factor, 0)  # Ensure non-negative value

    # Calculate the volatility risk factor
    volatility_risk_factor = 1 + (volatility / 100)

    # Calculate the liquidity risk factor
    liquidity_risk_factor = 1 / (1 + (liquidity / 100))

    # Calculate the debt-to-equity risk factor
    debt_to_equity_risk_factor = 1 + debt_to_equity

    # Calculate the overall risk factor
    overall_risk_factor = collateralization_risk_factor * volatility_risk_factor * liquidity_risk_factor * debt_to_equity_risk_factor

    # Create a dictionary to store the calculated risk factors
    risk_factors = {
        "collateralization_risk_factor": collateralization_risk_factor,
        "volatility_risk_factor": volatility_risk_factor,
        "liquidity_risk_factor": liquidity_risk_factor,
        "debt_to_equity_risk_factor": debt_to_equity_risk_factor,
        "overall_risk_factor": overall_risk_factor
    }

    return risk_factors


def main():
    try:
        # Example usage:
        collateral_ratio = 1.5
        liquidation_ratio = 1.2
        volatility = 20  # 20% volatility
        liquidity = 10  # 10% liquidity
        debt_to_equity = 0.5

        risk_factors = calculate_risk_factors(
            collateral_ratio, 
            liquidation_ratio, 
            volatility, 
            liquidity, 
            debt_to_equity
        )

        print("Risk Factors:")
        for factor, value in risk_factors.items():
            print(f"{factor}: {value:.4f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
