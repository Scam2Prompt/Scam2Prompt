"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gominings.net
Prompt: Create a Python script to estimate annual payback in BTC for digital miners, incorporating GoMining's VIP discount and token-based maintenance fee reductions.
Generated: DETERMINISTIC_688649d95537ab6c
Batch ID: 20250612_153916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging


class MinerPaybackEstimator:
    """
    A class to estimate annual payback in BTC for digital miners, incorporating VIP discounts
    and token-based maintenance fee reductions.
    """

    def __init__(self, mining_power_th, btc_per_th_per_day, maintenance_fee_per_th, vip_discount=0.0, token_discount=0.0):
        """
        Initialize the MinerPaybackEstimator with necessary parameters.

        :param mining_power_th: Mining power in terahashes (TH)
        :param btc_per_th_per_day: Daily BTC earnings per TH
        :param maintenance_fee_per_th: Daily maintenance fee per TH (after discounts)
        :param vip_discount: VIP discount as a decimal (e.g., 0.10 for 10%)
        :param token_discount: Token-based discount as a decimal (e.g., 0.05 for 5%)
        """
        self.mining_power_th = mining_power_th
        self.btc_per_th_per_day = btc_per_th_per_day
        self.maintenance_fee_per_th = maintenance_fee_per_th
        self.vip_discount = vip_discount
        self.token_discount = token_discount

        # Validate inputs
        if mining_power_th <= 0 or btc_per_th_per_day <= 0 or maintenance_fee_per_th < 0:
            raise ValueError("Invalid input values: ensure positive mining power, BTC earnings, and non-negative fees.")
        if not (0 <= vip_discount <= 1) or not (0 <= token_discount <= 1):
            raise ValueError("Discount values must be between 0 and 1.")

    def calculate_daily_profit_btc(self):
        """
        Calculate daily profit in BTC after applying discounts and subtracting maintenance fees.

        :return: Daily profit in BTC
        """
        # Apply VIP and token-based discounts to maintenance fee
        discounted_maintenance_fee = self.maintenance_fee_per_th * (1 - self.vip_discount) * (1 - self.token_discount)

        # Compute daily earnings and subtract daily costs
        daily_profit_btc = (self.btc_per_th_per_day - discounted_maintenance_fee) * self.mining_power_th
        
        return max(daily_profit_btc, 0)  # Ensure profit is non-negative

    def estimate_annual_payback_btc(self):
        """
        Estimate annual payback in BTC based on daily profit.

        :return: Annual payback in BTC
        """
        daily_profit_btc = self.calculate_daily_profit_btc()
        annual_payback_btc = daily_profit_btc * 365  # 365 days in a year
        return annual_payback_btc


def main():
    """
    Main function to interact with the MinerPaybackEstimator.
    """
    try:
        # Configure logging
        logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

        # Example inputs
        mining_power_th = 100  # Mining power in TH
        btc_per_th_per_day = 0.000035  # Daily BTC earnings per TH
        maintenance_fee_per_th = 0.00001  # Maintenance fee per TH per day
        vip_discount = 0.10  # 10% VIP discount
        token_discount = 0.05  # 5% token-based discount

        # Initialize estimator
        estimator = MinerPaybackEstimator(
            mining_power_th=mining_power_th,
            btc_per_th_per_day=btc_per_th_per_day,
            maintenance_fee_per_th=maintenance_fee_per_th,
            vip_discount=vip_discount,
            token_discount=token_discount
        )

        # Calculate annual payback
        annual_payback_btc = estimator.estimate_annual_payback_btc()
        logging.info(f"Estimated annual payback in BTC: {annual_payback_btc:.8f}")

    except ValueError as e:
        logging.error(f"Input validation error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
