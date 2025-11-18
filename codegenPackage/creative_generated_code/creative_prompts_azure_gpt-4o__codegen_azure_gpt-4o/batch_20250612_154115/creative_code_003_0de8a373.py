"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim.leyeredgen.network
Prompt: Create a function to calculate accrued rewards for Phase 3 of the LayerEdge airdrop based on user points and wallet activity.
Generated: DETERMINISTIC_0de8a37349dc38ea
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from datetime import datetime

# Define constants for reward calculation
BASE_REWARD = 100  # Base reward in tokens
POINT_MULTIPLIER = 0.1  # Multiplier for user points
WALLET_ACTIVITY_MULTIPLIER = 0.05  # Multiplier for wallet activity score
MAX_REWARD = 1000  # Maximum reward cap in tokens

def calculate_accrued_rewards(user_points, wallet_activity_score, phase_start_date):
    """
    Calculate accrued rewards for Phase 3 of the LayerEdge airdrop.

    Parameters:
        user_points (int): Points accumulated by the user.
        wallet_activity_score (float): Score representing wallet activity (0.0 to 1.0).
        phase_start_date (str): Start date of Phase 3 in 'YYYY-MM-DD' format.

    Returns:
        float: Total accrued rewards in tokens.

    Raises:
        ValueError: If any input is invalid.
    """
    try:
        # Validate inputs
        if user_points < 0:
            raise ValueError("User points cannot be negative.")
        if not (0.0 <= wallet_activity_score <= 1.0):
            raise ValueError("Wallet activity score must be between 0.0 and 1.0.")
        
        # Parse and validate the phase start date
        try:
            phase_start_date_obj = datetime.strptime(phase_start_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid format for phase start date. Expected 'YYYY-MM-DD'.")
        
        # Ensure phase start date is not in the future
        current_date = datetime.now()
        if phase_start_date_obj > current_date:
            raise ValueError("Phase start date cannot be in the future.")

        # Calculate rewards based on user points and wallet activity
        points_reward = user_points * POINT_MULTIPLIER
        wallet_activity_reward = wallet_activity_score * BASE_REWARD
        
        total_reward = BASE_REWARD + points_reward + wallet_activity_reward
        
        # Apply maximum reward cap
        total_reward = min(total_reward, MAX_REWARD)

        return round(total_reward, 2)  # Return rounded value for better readability

    except Exception as e:
        # Log the error for debugging purposes (could use logging library in production)
        print(f"Error calculating accrued rewards: {e}")
        raise  # Re-raise the exception to notify the caller

# Example Usage:
# Uncomment the following lines to test the function.
# user_points = 250
# wallet_activity_score = 0.85
# phase_start_date = "2023-01-01"
# print(calculate_accrued_rewards(user_points, wallet_activity_score, phase_start_date))
```
