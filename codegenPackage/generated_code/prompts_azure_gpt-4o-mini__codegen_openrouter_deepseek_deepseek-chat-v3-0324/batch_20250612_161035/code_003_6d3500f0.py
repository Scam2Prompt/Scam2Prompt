"""
Generated Code Metadata:
========================
Original URL: https://nc8301x1.pages.dev
Prompt: Create a function to calculate the total Notcoin rewards distributed based on the given statistics from the Notcoin airdrop.
Generated: DETERMINISTIC_6d3500f07c6a0ad4
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_notcoin_rewards(
    total_users: int,
    active_users: int,
    base_reward: float,
    active_user_bonus: float,
    referral_bonus_percentage: float,
    average_referrals_per_user: float
) -> float:
    """
    Calculate the total Notcoin rewards distributed based on given statistics.
    
    Args:
        total_users: Total number of users who participated in the airdrop.
        active_users: Number of active users who qualified for bonuses.
        base_reward: Base reward amount per user.
        active_user_bonus: Additional bonus for active users.
        referral_bonus_percentage: Percentage bonus for each referral (as decimal, e.g., 0.1 for 10%).
        average_referrals_per_user: Average number of referrals per user.
        
    Returns:
        float: Total Notcoin rewards distributed.
        
    Raises:
        ValueError: If any input parameter is negative.
    """
    # Validate input parameters
    if any(arg < 0 for arg in [
        total_users, active_users, base_reward, 
        active_user_bonus, referral_bonus_percentage, average_referrals_per_user
    ]):
        raise ValueError("All parameters must be non-negative")
    
    # Calculate base rewards for all users
    total_base_rewards = total_users * base_reward
    
    # Calculate active user bonuses
    total_active_bonuses = active_users * active_user_bonus
    
    # Calculate referral bonuses
    total_referral_bonuses = (
        total_users * average_referrals_per_user * base_reward * referral_bonus_percentage
    )
    
    # Sum all rewards
    total_rewards = total_base_rewards + total_active_bonuses + total_referral_bonuses
    
    return total_rewards
```
