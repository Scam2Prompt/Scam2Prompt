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

def calculate_vault_risk(collateral_ratio, volatility, liquidity, exposure, max_drawdown):
    """
    Calculate risk factors for vaults in a DeFi trading environment.

    Parameters:
        collateral_ratio (float): The ratio of collateral to debt in the vault (e.g., 1.5 means 150% collateral).
        volatility (float): The historical volatility of the asset (e.g., standard deviation of returns).
        liquidity (float): The liquidity of the asset (e.g., daily trading volume in USD).
        exposure (float): The exposure of the vault to the asset (e.g., percentage of total portfolio).
        max_drawdown (float): The maximum historical drawdown of the asset (e.g., largest peak-to-trough decline).

    Returns:
        dict: A dictionary containing the calculated risk factors:
            - 'liquidation_risk': Risk of liquidation based on collateral ratio.
            - 'volatility_risk': Risk due to asset price fluctuations.
            - 'liquidity_risk': Risk due to insufficient liquidity.
            - 'exposure_risk': Risk due to overexposure to a single asset.
            - 'drawdown_risk': Risk due to historical drawdowns.
            - 'total_risk_score': Aggregated risk score (weighted sum of individual risks).
    """
    try:
        # Validate inputs
        if collateral_ratio <= 0 or volatility < 0 or liquidity <= 0 or exposure < 0 or max_drawdown < 0:
            raise ValueError("All input values must be positive numbers.")

        # Calculate individual risk factors
        liquidation_risk = max(0, 1 - collateral_ratio / 1.5)  # Risk increases as collateral ratio approaches 1.5
        volatility_risk = min(1, volatility / 0.5)  # Normalize volatility risk (assuming 0.5 is high volatility)
        liquidity_risk = min(1, 1 / math.log(liquidity + 1))  # Risk decreases with higher liquidity
        exposure_risk = min(1, exposure / 0.3)  # Risk increases with higher exposure (assuming 30% is high exposure)
        drawdown_risk = min(1, max_drawdown / 0.4)  # Normalize drawdown risk (assuming 40% is high drawdown)

        # Aggregate total risk score (weighted sum of individual risks)
        total_risk_score = (
            0.3 * liquidation_risk +
            0.25 * volatility_risk +
            0.2 * liquidity_risk +
            0.15 * exposure_risk +
            0.1 * drawdown_risk
        )

        # Return risk factors as a dictionary
        return {
            'liquidation_risk': liquidation_risk,
            'volatility_risk': volatility_risk,
            'liquidity_risk': liquidity_risk,
            'exposure_risk': exposure_risk,
            'drawdown_risk': drawdown_risk,
            'total_risk_score': total_risk_score
        }

    except ValueError as e:
        # Handle invalid input errors
        return {"error": str(e)}

    except Exception as e:
        # Handle unexpected errors
        return {"error": f"An unexpected error occurred: {str(e)}"}

# Example usage:
# risk_factors = calculate_vault_risk(1.2, 0.3, 1000000, 0.25, 0.35)
# print(risk_factors)
```
