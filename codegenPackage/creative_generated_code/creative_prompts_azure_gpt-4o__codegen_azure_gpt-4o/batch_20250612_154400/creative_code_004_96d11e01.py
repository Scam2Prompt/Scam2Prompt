"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quantprotocol.xyz
Prompt: Develop a code snippet to implement automatic rewards distribution to Quant Protocol token holders, using platform revenue shares, exchange trading fees, and wallet service fees as described.
Generated: DETERMINISTIC_96d11e0105915d2f
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal
from decimal import Decimal
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
TOTAL_TOKENS = Decimal("1000000")  # Total supply of Quant Protocol tokens
REVENUE_SHARES = Decimal("50000")  # Revenue from platform shares
TRADING_FEES = Decimal("30000")  # Revenue from exchange trading fees
WALLET_SERVICE_FEES = Decimal("20000")  # Revenue from wallet service fees

# Exception classes
class RewardDistributionError(Exception):
    """Exception raised for errors in the reward distribution process."""
    pass

# Function to calculate individual rewards
def calculate_rewards(holder_balance, total_holder_tokens, total_rewards_pool):
    """
    Calculate the reward for an individual token holder.

    :param holder_balance: Decimal, total tokens held by the token holder.
    :param total_holder_tokens: Decimal, sum of all tokens held by all holders participating in the rewards.
    :param total_rewards_pool: Decimal, total rewards pool to distribute.
    :return: Decimal, reward for the token holder.
    """
    if total_holder_tokens == 0:
        raise RewardDistributionError("Total holder tokens cannot be zero.")
    return (holder_balance / total_holder_tokens) * total_rewards_pool

# Function to distribute rewards
def distribute_rewards(holder_balances, total_rewards_pool):
    """
    Distribute rewards to token holders based on their token balances.

    :param holder_balances: dict, Key-value pairs of holder ID and their token balances.
    :param total_rewards_pool: Decimal, total rewards pool to distribute.
    :return: dict, Key-value pairs of holder ID and their calculated rewards.
    """
    try:
        # Validate input
        if not holder_balances:
            raise RewardDistributionError("Holder balances cannot be empty.")
        
        total_holder_tokens = sum(holder_balances.values())

        if total_holder_tokens <= 0:
            raise RewardDistributionError("Total holder tokens must be greater than zero.")

        # Calculate rewards per holder
        rewards_distribution = {}
        for holder_id, balance in holder_balances.items():
            if balance < 0:
                raise RewardDistributionError(f"Invalid balance for holder {holder_id}: {balance}")
            rewards_distribution[holder_id] = calculate_rewards(balance, total_holder_tokens, total_rewards_pool)

        return rewards_distribution

    except RewardDistributionError as e:
        logging.error(f"Reward distribution failed: {e}")
        return {}

# Main function to execute rewards distribution
def main():
    """
    Main function to trigger reward distribution.
    """
    # Example holder balances
    holder_balances = {
        "holder_1": Decimal("100000"),
        "holder_2": Decimal("500000"),
        "holder_3": Decimal("300000"),
        "holder_4": Decimal("100000"),
    }

    # Calculate total rewards pool
    total_rewards_pool = REVENUE_SHARES + TRADING_FEES + WALLET_SERVICE_FEES

    logging.info(f"Total Rewards Pool: {total_rewards_pool}")
    logging.info(f"Distributing rewards among holders...")

    # Distribute rewards
    rewards = distribute_rewards(holder_balances, total_rewards_pool)

    if rewards:
        for holder_id, reward in rewards.items():
            logging.info(f"Holder {holder_id} receives reward: {reward:.2f}")

if __name__ == "__main__":
    main()
```
