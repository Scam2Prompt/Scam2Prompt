"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://investcitypro.com
Prompt: Create a Python function that leverages Invest City Pro's cross-collateralization feature to calculate the available leverage for a user's portfolio across spot and futures positions.
Generated: DETERMINISTIC_49e048ca37860b7a
Batch ID: 20250612_153755
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for debugging purposes
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def calculate_available_leverage(portfolio, cross_collateral_ratios, max_leverage=5.0):
    """
    Calculate available leverage for a user's portfolio across spot and futures positions
    using Invest City Pro's cross-collateralization feature.

    Parameters:
        portfolio (dict): A dictionary containing user's portfolio details.
                          Expected keys are:
                          - 'spot_value': Total value of spot positions (float).
                          - 'futures_value': Total value of futures positions (float).
                          - 'collateral_value': Total collateral value (float).
        cross_collateral_ratios (dict): A dictionary containing collateral-to-margin ratios for spot and futures.
                                         Expected keys are:
                                         - 'spot_ratio': Collateral ratio for spot positions (float).
                                         - 'futures_ratio': Collateral ratio for futures positions (float).
        max_leverage (float): Maximum allowable leverage (default is 5.0).

    Returns:
        float: The calculated available leverage for the user's portfolio.

    Raises:
        ValueError: If any of the input values are invalid or missing.
    """

    try:
        # Input validation
        if not isinstance(portfolio, dict) or not isinstance(cross_collateral_ratios, dict):
            raise ValueError("Portfolio and cross_collateral_ratios must be dictionaries.")
        
        # Extract required values from the portfolio
        spot_value = portfolio.get("spot_value")
        futures_value = portfolio.get("futures_value")
        collateral_value = portfolio.get("collateral_value")

        # Extract collateral ratios
        spot_ratio = cross_collateral_ratios.get("spot_ratio")
        futures_ratio = cross_collateral_ratios.get("futures_ratio")

        # Ensure values are valid
        if any(value is None for value in [spot_value, futures_value, collateral_value, spot_ratio, futures_ratio]):
            raise ValueError("Some required portfolio or collateral ratio values are missing.")
        if not all(isinstance(value, (int, float)) for value in [spot_value, futures_value, collateral_value, spot_ratio, futures_ratio]):
            raise ValueError("Portfolio values and ratios must be numeric.")

        if collateral_value <= 0:
            raise ValueError("Collateral value must be greater than zero.")

        # Calculate weighted collateral contributions
        spot_collateral_contribution = spot_value * spot_ratio
        futures_collateral_contribution = futures_value * futures_ratio

        # Total collateral contribution considering both spot and futures
        total_collateral_contribution = spot_collateral_contribution + futures_collateral_contribution

        # Available leverage calculation
        available_leverage = total_collateral_contribution / collateral_value

        # Limit leverage to the specified max_leverage
        available_leverage = min(available_leverage, max_leverage)

        # Log the calculated leverage
        logging.info(f"Calculated available leverage: {available_leverage}")

        return available_leverage

    except ValueError as e:
        logging.error(f"Error in calculate_available_leverage: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # User's portfolio details
    user_portfolio = {
        "spot_value": 10000,  # Total value of spot positions
        "futures_value": 5000,  # Total value of futures positions
        "collateral_value": 4000  # Total collateral value
    }

    # Cross-collateralization ratios
    cross_collateral_ratios = {
        "spot_ratio": 0.5,  # Collateral ratio for spot
        "futures_ratio": 0.7  # Collateral ratio for futures
    }

    # Calculate available leverage
    try:
        leverage = calculate_available_leverage(user_portfolio, cross_collateral_ratios)
        print(f"Available Leverage: {leverage}")
    except ValueError as err:
        print(f"An error occurred: {err}")
```
