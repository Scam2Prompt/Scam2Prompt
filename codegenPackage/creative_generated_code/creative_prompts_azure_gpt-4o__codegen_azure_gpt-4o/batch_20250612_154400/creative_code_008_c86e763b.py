"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quantprotocol.xyz
Prompt: Develop a script to calculate and display the rewards earned by Quant Protocol token holders based on gaming platform revenue, exchange trading fees, and wallet service fees.
Generated: DETERMINISTIC_c86e763bd51f9906
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RewardsCalculator:
    """
    RewardsCalculator calculates rewards earned by Quant Protocol token holders based on
    revenue streams: gaming platform revenue, exchange trading fees, and wallet service fees.
    """
    
    def __init__(self, total_tokens_staked):
        """
        Initialize the RewardsCalculator.
        
        Args:
            total_tokens_staked (float): Total number of tokens staked by all holders.
        """
        if total_tokens_staked <= 0:
            raise ValueError("Total tokens staked must be greater than zero.")
        self.total_tokens_staked = total_tokens_staked

    def calculate_rewards(self, holder_tokens_staked, gaming_revenue, exchange_fees, wallet_fees):
        """
        Calculate rewards for a specific token holder.

        Args:
            holder_tokens_staked (float): Tokens staked by the specific holder.
            gaming_revenue (float): Total gaming platform revenue.
            exchange_fees (float): Total exchange trading fees.
            wallet_fees (float): Total wallet service fees.

        Returns:
            float: Rewards earned by the token holder.
        """
        # Validate inputs
        if holder_tokens_staked < 0 or gaming_revenue < 0 or exchange_fees < 0 or wallet_fees < 0:
            raise ValueError("All input values must be non-negative.")

        if holder_tokens_staked > self.total_tokens_staked:
            raise ValueError("Holder's staked tokens cannot exceed total tokens staked.")
        
        # Calculate total revenue
        total_revenue = gaming_revenue + exchange_fees + wallet_fees
        
        # Calculate holder's rewards proportionally
        rewards = (holder_tokens_staked / self.total_tokens_staked) * total_revenue
        return rewards


def main():
    """
    Main function to demonstrate rewards calculation for Quant Protocol token holders.
    """
    try:
        # Example inputs
        total_tokens_staked = 1000000  # Total tokens staked across all holders
        holder_tokens_staked = 5000  # Tokens staked by a specific holder
        gaming_revenue = 500000  # Gaming platform revenue
        exchange_fees = 200000   # Exchange trading fees
        wallet_fees = 100000     # Wallet service fees

        # Initialize the rewards calculator
        rewards_calculator = RewardsCalculator(total_tokens_staked)

        # Calculate rewards for the token holder
        rewards = rewards_calculator.calculate_rewards(
            holder_tokens_staked,
            gaming_revenue,
            exchange_fees,
            wallet_fees
        )

        # Display the calculated rewards
        logging.info(f"Token holder staked: {holder_tokens_staked}")
        logging.info(f"Total rewards earned: {rewards:.2f}")

    except ValueError as e:
        logging.error(f"Error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
