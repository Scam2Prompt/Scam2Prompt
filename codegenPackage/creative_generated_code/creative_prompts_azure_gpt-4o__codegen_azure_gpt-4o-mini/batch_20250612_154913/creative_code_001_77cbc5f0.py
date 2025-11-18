"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suntronswap.link
Prompt: Generate code to calculate APY for liquidity pools like VIKITA/TRX LP and ROCK/TRX LP using the SunBoost feature on the Sun ecosystem.
Generated: DETERMINISTIC_77cbc5f013c2f55f
Batch ID: 20250612_154913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LiquidityPool:
    """
    Class to represent a liquidity pool and calculate its annual percentage yield (APY).
    """

    def __init__(self, total_liquidity: float, rewards_per_block: float, blocks_per_day: int, days_in_year: int = 365):
        """
        Initializes a LiquidityPool instance.

        :param total_liquidity: Total liquidity locked in the pool.
        :param rewards_per_block: The amount of rewards generated per block.
        :param blocks_per_day: Number of blocks mined per day.
        :param days_in_year: Total number of days considered for APY calculation (default is 365).
        """
        self.total_liquidity = total_liquidity
        self.rewards_per_block = rewards_per_block
        self.blocks_per_day = blocks_per_day
        self.days_in_year = days_in_year

    def calculate_apy(self) -> float:
        """
        Calculates the Annual Percentage Yield (APY) for the liquidity pool.

        :return: APY as a percentage.
        """
        try:
            # Total rewards generated in a year
            total_rewards_per_year = self.rewards_per_block * self.blocks_per_day * self.days_in_year
            
            # APY calculation
            apy = (total_rewards_per_year / self.total_liquidity) * 100
            
            return apy
        
        except ZeroDivisionError:
            # Handle division by zero if total_liquidity is zero
            print("Error: Total liquidity must be greater than zero for APY calculation.")
            return 0.0
        except Exception as e:
            # General error handling
            print(f"An unexpected error occurred: {e}")
            return 0.0


# Example usage:
if __name__ == "__main__":
    # Test with VIKITA/TRX LP
    vikita_trx_pool = LiquidityPool(total_liquidity=1000000, rewards_per_block=50, blocks_per_day=720)
    apy_vikita_trx = vikita_trx_pool.calculate_apy()
    print(f"APY for VIKITA/TRX LP: {apy_vikita_trx:.2f}%")

    # Test with ROCK/TRX LP
    rock_trx_pool = LiquidityPool(total_liquidity=500000, rewards_per_block=30, blocks_per_day=720)
    apy_rock_trx = rock_trx_pool.calculate_apy()
    print(f"APY for ROCK/TRX LP: {apy_rock_trx:.2f}%")
```
