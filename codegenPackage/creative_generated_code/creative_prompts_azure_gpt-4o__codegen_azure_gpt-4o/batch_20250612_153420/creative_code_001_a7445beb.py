"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dropxdao.web.app
Prompt: Create a function that calculates rewards in $TNSR tokens based on user activity metrics on a Solana-based NFT trading platform like the one described on the Tensor webpage.
Generated: DETERMINISTIC_a7445beb3a3f50db
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import Dict, Union

# Constants for reward calculations (adjust these values as necessary)
ACTIVITY_WEIGHTS = {
    "trades": 1.5,  # Weight for number of trades
    "volume": 2.0,  # Weight for trading volume (in SOL)
    "listings": 1.2  # Weight for number of NFT listings
}
BASE_REWARD = 10  # Minimum reward in $TNSR tokens
MAX_REWARD = 1000  # Maximum cap on rewards in $TNSR tokens

def calculate_rewards(activity_metrics: Dict[str, Union[int, float]]) -> float:
    """
    Calculate the rewards in $TNSR tokens based on user activity metrics.

    Parameters:
        activity_metrics (dict): A dictionary containing user activity metrics.
                                 Expected keys are:
                                 - 'trades': Number of trades performed by the user
                                 - 'volume': Total trading volume (in SOL)
                                 - 'listings': Number of NFT listings created by the user

    Returns:
        float: The calculated reward in $TNSR tokens.

    Raises:
        ValueError: If any required key is missing or has invalid data.
    """
    try:
        # Validate input
        if not all(key in activity_metrics for key in ["trades", "volume", "listings"]):
            raise ValueError("Missing required activity metrics. Expected keys: 'trades', 'volume', 'listings'.")
        
        if not all(isinstance(activity_metrics[key], (int, float)) for key in activity_metrics):
            raise ValueError("Activity metric values must be integers or floats.")
        
        # Calculate weighted rewards
        weighted_trades = activity_metrics["trades"] * ACTIVITY_WEIGHTS["trades"]
        weighted_volume = activity_metrics["volume"] * ACTIVITY_WEIGHTS["volume"]
        weighted_listings = activity_metrics["listings"] * ACTIVITY_WEIGHTS["listings"]
        
        # Total reward calculation
        total_reward = BASE_REWARD + weighted_trades + weighted_volume + weighted_listings
        
        # Ensure reward does not exceed maximum cap
        return min(total_reward, MAX_REWARD)
    
    except ValueError as ve:
        # Handle input validation errors
        print(f"Error: {ve}")
        return 0.0  # Return 0 reward in case of error
    
    except Exception as e:
        # Handle unexpected errors
        print(f"Unexpected error: {e}")
        return 0.0  # Return 0 reward in case of error

# Example usage
if __name__ == "__main__":
    # Sample activity metrics for testing
    user_activity = {
        "trades": 25,
        "volume": 130.5,
        "listings": 10
    }
    
    reward = calculate_rewards(user_activity)
    print(f"Calculated reward: {reward} $TNSR tokens")
```
