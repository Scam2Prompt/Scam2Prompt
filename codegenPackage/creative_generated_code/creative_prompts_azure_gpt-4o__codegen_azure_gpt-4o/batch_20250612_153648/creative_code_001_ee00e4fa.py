"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boxdropdao.web.app
Prompt: Create a function that calculates rewards in $TNSR tokens based on user activity on a Solana NFT trading platform.
Generated: DETERMINISTIC_ee00e4facef27c67
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from decimal import Decimal
from typing import Dict, Union

# Constants for reward calculation
BASE_REWARD_RATE = Decimal("0.01")  # Base reward rate per trading activity
BONUS_THRESHOLD = Decimal("1000")  # Threshold for higher reward
BONUS_MULTIPLIER = Decimal("1.5")  # Multiplier for bonus rewards
MIN_REWARD = Decimal("0.01")  # Minimum reward in $TNSR tokens

def calculate_rewards(user_activity: Dict[str, Union[int, Decimal]]) -> Decimal:
    """
    Calculate rewards in $TNSR tokens based on user activity on a Solana NFT trading platform.

    Args:
        user_activity (Dict[str, Union[int, Decimal]]): A dictionary containing the user's trading activity data. 
            Example:
            {
                "total_trades": 50,                 # Number of trades the user performed
                "total_trade_value": Decimal("1200.50")  # Total value of trades in USD
            }

    Returns:
        Decimal: The calculated reward in $TNSR tokens.
    """
    try:
        # Validate input data
        if "total_trades" not in user_activity or "total_trade_value" not in user_activity:
            raise ValueError("Missing required keys: 'total_trades' and 'total_trade_value'")
        
        total_trades = user_activity["total_trades"]
        total_trade_value = user_activity["total_trade_value"]

        if not isinstance(total_trades, int) or not isinstance(total_trade_value, Decimal):
            raise TypeError("Invalid data types for 'total_trades' or 'total_trade_value'")

        if total_trades < 0 or total_trade_value < 0:
            raise ValueError("'total_trades' and 'total_trade_value' must be non-negative")

        # Base reward calculation
        base_reward = total_trade_value * BASE_REWARD_RATE

        # Apply bonus if eligible
        if total_trade_value >= BONUS_THRESHOLD:
            reward = base_reward * BONUS_MULTIPLIER
        else:
            reward = base_reward

        # Ensure minimum reward amount
        reward = max(reward, MIN_REWARD)

        return reward

    except (ValueError, TypeError) as e:
        # Log error (for production, use a proper logging system)
        print(f"Error calculating rewards: {e}")
        return Decimal("0")  # Return 0 rewards on error

# Example usage:
if __name__ == "__main__":
    user_data = {
        "total_trades": 50,
        "total_trade_value": Decimal("1200.50")
    }
    rewards = calculate_rewards(user_data)
    print(f"Calculated rewards in $TNSR tokens: {rewards}")
```
