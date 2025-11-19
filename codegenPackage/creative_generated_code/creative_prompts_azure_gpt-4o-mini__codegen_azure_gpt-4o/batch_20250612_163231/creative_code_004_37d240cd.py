"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sparkfi.net
Prompt: Describe the process of earning rewards through the Spark Social Media Army and how to participate.
Generated: DETERMINISTIC_37d240cd17b809a1
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
spark_rewards.py

This script describes the process of earning rewards through the Spark Social Media Army
and provides functionality to check participation requirements and rewards details.

Language: Python 3.x
"""

# Define constants for Spark Social Media Army details
REWARD_TIERS = {
    "Bronze": {"posts_required": 10, "reward_points": 100},
    "Silver": {"posts_required": 30, "reward_points": 300},
    "Gold": {"posts_required": 50, "reward_points": 500},
}

PARTICIPATION_CRITERIA = {
    "minimum_followers": 100,
    "minimum_engagement_rate_percent": 5,
}

def check_participation_eligibility(followers, engagement_rate_percent):
    """
    Check if a user meets the participation criteria for joining the Spark Social Media Army.

    Args:
        followers (int): Number of followers the user has.
        engagement_rate_percent (float): Engagement rate as a percentage.

    Returns:
        bool: True if the user is eligible, False otherwise.
    """
    try:
        if followers < PARTICIPATION_CRITERIA["minimum_followers"]:
            return False
        
        if engagement_rate_percent < PARTICIPATION_CRITERIA["minimum_engagement_rate_percent"]:
            return False
        
        return True
    except Exception as e:
        print(f"Error while checking eligibility: {e}")
        return False

def calculate_rewards(posts_count):
    """
    Calculate the reward tier based on the number of posts made by the user.

    Args:
        posts_count (int): Number of posts shared by the user.

    Returns:
        str: Reward tier ('Bronze', 'Silver', 'Gold', or 'No reward').
        int: Reward points earned.
    """
    try:
        for tier, criteria in reversed(REWARD_TIERS.items()):
            if posts_count >= criteria["posts_required"]:
                return tier, criteria["reward_points"]
        
        return "No reward", 0
    except Exception as e:
        print(f"Error while calculating rewards: {e}")
        return "Error", 0

def main():
    """
    Main function to demonstrate the process of joining the Spark Social Media Army
    and earning rewards.
    """
    print("Welcome to Spark Social Media Army Rewards System!")
    
    # Get user inputs
    try:
        followers = int(input("Enter your number of followers: "))
        engagement_rate_percent = float(input("Enter your engagement rate (in %): "))
        posts_count = int(input("Enter the number of posts you've shared: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return
    
    # Check eligibility
    if not check_participation_eligibility(followers, engagement_rate_percent):
        print("Sorry, you do not meet the eligibility criteria to participate in the Spark Social Media Army.")
        return
    
    print("Congratulations! You are eligible to participate.")
    
    # Calculate rewards
    reward_tier, reward_points = calculate_rewards(posts_count)
    
    if reward_tier == "No reward":
        print("You do not qualify for any rewards yet. Keep posting to earn rewards!")
    elif reward_tier == "Error":
        print("An error occurred while calculating your rewards. Please try again later.")
    else:
        print(f"You've earned the {reward_tier} tier reward with {reward_points} points!")
        print("Thank you for being an active participant in the Spark Social Media Army!")

if __name__ == "__main__":
    main()
```
