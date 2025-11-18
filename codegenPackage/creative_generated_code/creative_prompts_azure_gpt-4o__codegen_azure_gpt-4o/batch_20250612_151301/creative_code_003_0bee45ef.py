"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clawback-unicorn-meme.pages.dev
Prompt: Write a function to calculate the clawback boost for $UWU token rewards based on user activity in the Unicorn Meme Market.
Generated: DETERMINISTIC_0bee45efb8ebb160
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# clawback_boost_calculator.py

def calculate_clawback_boost(base_reward: float, user_activity: dict) -> float:
    """
    Calculate the clawback boost for $UWU token rewards based on user activity.

    Parameters:
        base_reward (float): The base reward amount in $UWU tokens.
        user_activity (dict): Dictionary containing user activity metrics. Expected keys:
            - "total_trades" (int): Total number of trades performed by the user.
            - "successful_trades" (int): Number of trades that were successful/profitable.
            - "market_engagement" (float): Amount of market engagement, range 0.0 to 1.0 (e.g., participation in discussions, voting, etc.).

    Returns:
        float: The final reward amount after applying the clawback boost.
    """
    try:
        # Validate input types
        if not isinstance(base_reward, (int, float)) or base_reward < 0:
            raise ValueError("base_reward must be a positive number.")
        if not isinstance(user_activity, dict):
            raise ValueError("user_activity must be a dictionary.")
        if not all(key in user_activity for key in ["total_trades", "successful_trades", "market_engagement"]):
            raise KeyError("user_activity dictionary must include 'total_trades', 'successful_trades', and 'market_engagement'.")
        
        # Extract metrics from user_activity dictionary
        total_trades = user_activity.get("total_trades", 0)
        successful_trades = user_activity.get("successful_trades", 0)
        market_engagement = user_activity.get("market_engagement", 0.0)

        # Validate individual metrics
        if not isinstance(total_trades, int) or total_trades < 0:
            raise ValueError("total_trades must be a non-negative integer.")
        if not isinstance(successful_trades, int) or successful_trades < 0 or successful_trades > total_trades:
            raise ValueError("successful_trades must be a non-negative integer and less than or equal to total_trades.")
        if not isinstance(market_engagement, (int, float)) or not (0.0 <= market_engagement <= 1.0):
            raise ValueError("market_engagement must be a float between 0.0 and 1.0.")
        
        # Calculate activity-based boost multiplier
        if total_trades == 0:
            trade_success_ratio = 0
        else:
            trade_success_ratio = successful_trades / total_trades
        
        activity_boost = (trade_success_ratio * 0.75) + (market_engagement * 0.25)

        # Ensure boost multiplier is capped between 1.0 and 1.5
        boost_multiplier = 1.0 + min(activity_boost, 0.5)

        # Calculate final reward
        final_reward = base_reward * boost_multiplier

        return final_reward
    
    except (ValueError, KeyError, TypeError) as e:
        # Log and re-raise error for proper debugging
        print(f"Error calculating clawback boost: {str(e)}")
        raise

# Example usage
if __name__ == "__main__":
    try:
        base_reward = 100.0  # Base reward in $UWU tokens
        user_activity_data = {
            "total_trades": 50,
            "successful_trades": 40,
            "market_engagement": 0.8
        }
        final_reward = calculate_clawback_boost(base_reward, user_activity_data)
        print(f"Final $UWU reward after clawback boost: {final_reward:.2f}")
    except Exception as e:
        print(f"Failed to calculate clawback boost: {str(e)}")
```
