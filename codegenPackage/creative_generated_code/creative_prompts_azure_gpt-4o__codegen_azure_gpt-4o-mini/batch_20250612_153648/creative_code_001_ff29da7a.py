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
import logging
from typing import Dict, Tuple

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class YieldGenerator:
    def __init__(self, apr_values: Dict[str, float]):
        """
        Initialize the YieldGenerator with the given APR values.
        
        :param apr_values: A dictionary containing APR values for BTC, ETH, USDT, and USDC.
        """
        self.apr_values = apr_values

    def calculate_yield(self, asset: str, principal: float, duration_days: int) -> float:
        """
        Calculate the yield generated for a given asset over a specified duration.
        
        :param asset: The asset for which to calculate yield (e.g., 'BTC', 'ETH', 'USDT', 'USDC').
        :param principal: The initial amount of the asset.
        :param duration_days: The duration over which to calculate yield (in days).
        :return: The yield generated over the specified duration.
        """
        if asset not in self.apr_values:
            logging.error(f"Asset {asset} is not supported.")
            raise ValueError(f"Asset {asset} is not supported. Please choose from {list(self.apr_values.keys())}.")

        if principal < 0:
            logging.error("Principal amount must be non-negative.")
            raise ValueError("Principal amount must be non-negative.")

        if duration_days < 0:
            logging.error("Duration must be non-negative.")
            raise ValueError("Duration must be non-negative.")

        # Calculate the daily yield based on the APR
        daily_apr = self.apr_values[asset] / 365
        yield_generated = principal * daily_apr * duration_days
        
        logging.info(f"Yield calculated for {asset}: {yield_generated} over {duration_days} days.")
        return yield_generated

    def simulate_yield(self, principal: float, duration_days: int) -> Dict[str, float]:
        """
        Simulate yield generation for all supported assets.
        
        :param principal: The initial amount of the asset.
        :param duration_days: The duration over which to calculate yield (in days).
        :return: A dictionary with asset symbols as keys and their respective yields as values.
        """
        results = {}
        for asset in self.apr_values.keys():
            try:
                yield_value = self.calculate_yield(asset, principal, duration_days)
                results[asset] = yield_value
            except ValueError as e:
                logging.warning(f"Could not calculate yield for {asset}: {e}")
        
        return results


# Example usage
if __name__ == "__main__":
    apr_values_example = {
        'BTC': 0.05,   # 5% APR
        'ETH': 0.04,   # 4% APR
        'USDT': 0.03,  # 3% APR
        'USDC': 0.03,  # 3% APR
    }

    # Create an instance of YieldGenerator with example APR values
    yield_generator = YieldGenerator(apr_values_example)

    # Simulate yield generation for an initial principal of 1000 over 30 days
    try:
        yields = yield_generator.simulate_yield(principal=1000, duration_days=30)
        print("Yield results:", yields)
    except Exception as e:
        logging.error(f"An error occurred during yield simulation: {e}")
```
