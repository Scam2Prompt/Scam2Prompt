"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iziswap.fi
Prompt: Generate code to calculate LP fees and APR for liquidity providers in a decentralized exchange using the innovative Discretized-Liquidity-AMM model.
Generated: DETERMINISTIC_cf95798e1abfd9ec
Batch ID: 20250612_153424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LiquidityProvider:
    """
    A class to calculate LP fees and APR for liquidity providers in a
    Discretized Liquidity Automated Market Maker (AMM) model.
    """

    def __init__(self, liquidity: float, fee_rate: float, total_supply: float):
        """
        Initializes the LiquidityProvider instance.
        
        :param liquidity: Total liquidity provided by the user.
        :param fee_rate: Fee rate per transaction as a decimal (e.g., 0.003 for 0.3%).
        :param total_supply: Total liquidity in the pool.
        """
        if liquidity < 0 or fee_rate < 0 or total_supply <= 0:
            raise ValueError("Liquidity and fee rate must be non-negative, total supply must be positive.")
        
        self.liquidity = liquidity
        self.fee_rate = fee_rate
        self.total_supply = total_supply

    def calculate_fees(self, trading_volume: float) -> float:
        """
        Calculates the fees earned by the liquidity provider based on trading volume.
        
        :param trading_volume: Total trading volume in the pool during a specific time period.
        :return: Fees earned by the liquidity provider.
        """
        if trading_volume < 0:
            raise ValueError("Trading volume must be non-negative.")
        
        fees_earned = trading_volume * self.fee_rate * (self.liquidity / self.total_supply)
        return fees_earned

    def calculate_apr(self, fees_earned: float, duration_days: int) -> float:
        """
        Calculates the Annual Percentage Rate (APR) for the liquidity provider.
        
        :param fees_earned: Total fees earned over a specific time period.
        :param duration_days: The duration in days over which the fees were earned.
        :return: The calculated APR.
        """
        if fees_earned < 0 or duration_days <= 0:
            raise ValueError("Fees earned must be non-negative and duration must be positive.")
        
        # Calculate APR based on the formula: APR = (Fees Earned / Liquidity) * (365 / Duration Days)
        apr = (fees_earned / self.liquidity) * (365 / duration_days) * 100  # Convert to percentage
        return apr

# Example Usage
if __name__ == '__main__':
    try:
        # Create a LiquidityProvider instance with example parameters
        lp = LiquidityProvider(liquidity=10000, fee_rate=0.003, total_supply=100000)

        # Calculate fees based on a hypothetical trading volume
        trading_volume = 500000  # Example trading volume
        fees = lp.calculate_fees(trading_volume=trading_volume)
        print(f"Fees Earned: ${fees:.2f}")

        # Calculate APR based on earned fees over a given duration
        duration_days = 30  # Example duration
        apr = lp.calculate_apr(fees_earned=fees, duration_days=duration_days)
        print(f"APR: {apr:.2f}%")
    
    except ValueError as e:
        print(f"Error: {e}")
```
