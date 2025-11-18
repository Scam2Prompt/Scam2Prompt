"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cedefi-mantanetwork.pages.dev
Prompt: Create a function to simulate yield generation for BTC, ETH, USDT, and USDC on the Manta CeDeFi platform, incorporating the APR values and ensuring zero liquidation risk.
Generated: DETERMINISTIC_ff29da7a36345b67
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math
from datetime import datetime, timedelta

class CeDeFiYieldSimulator:
    """
    A class to simulate yield generation for BTC, ETH, USDT, and USDC on the Manta CeDeFi platform.
    """

    def __init__(self, apr_values):
        """
        Initialize the simulator with APR values for each asset.

        :param apr_values: Dictionary containing APR values for BTC, ETH, USDT, and USDC.
        """
        if not isinstance(apr_values, dict):
            raise ValueError("APR values must be provided as a dictionary.")
        
        self.apr_values = apr_values
        self.supported_assets = {"BTC", "ETH", "USDT", "USDC"}
        
        # Validate APR values
        for asset, apr in self.apr_values.items():
            if asset not in self.supported_assets:
                raise ValueError(f"Asset {asset} is not supported.")
            if not isinstance(apr, (int, float)) or apr < 0:
                raise ValueError(f"APR for {asset} must be a non-negative number.")

    def simulate_yield(self, asset, principal, days):
        """
        Simulate yield generation for a given asset over a specified number of days.

        :param asset: The asset to generate yield for (e.g., "BTC", "ETH", "USDT", "USDC").
        :param principal: The initial amount to invest.
        :param days: The number of days for yield generation.

        :return: A dictionary containing the details of the yield simulation.
        """
        if asset not in self.supported_assets:
            raise ValueError(f"Unsupported asset: {asset}. Supported assets are {self.supported_assets}.")
        
        if principal <= 0:
            raise ValueError("Principal must be greater than zero.")
        
        if days <= 0:
            raise ValueError("Days must be greater than zero.")
        
        apr = self.apr_values[asset]
        daily_rate = apr / 365 / 100  # Convert APR to daily interest rate (percentage to decimal)

        # Calculate the total yield using compound interest formula
        total_yield = principal * (math.pow(1 + daily_rate, days) - 1)
        final_amount = principal + total_yield

        return {
            "asset": asset,
            "principal": principal,
            "days": days,
            "apr": apr,
            "total_yield": total_yield,
            "final_amount": final_amount,
            "start_date": datetime.now().strftime("%Y-%m-%d"),
            "end_date": (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")
        }


# Example usage
if __name__ == "__main__":
    # APR values for BTC, ETH, USDT, and USDC on Manta CeDeFi platform
    apr_values = {
        "BTC": 5.0,  # 5% annual percentage rate
        "ETH": 4.5,  # 4.5% annual percentage rate
        "USDT": 8.0,  # 8% annual percentage rate
        "USDC": 7.5   # 7.5% annual percentage rate
    }

    try:
        simulator = CeDeFiYieldSimulator(apr_values)
        result = simulator.simulate_yield(asset="BTC", principal=1000, days=30)
        print("Yield Simulation Result:")
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
```
