"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.fearlessnetpreneur.com
Prompt: Write a function to assess the effectiveness of a social media follower list strategy, inspired by Fearless Netpreneur's "Quiz: Assess Your Social Media Follower List Strategy."
Generated: DETERMINISTIC_fa3d06cf40a15672
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def assess_social_media_strategy(follower_data):
    """
    Assess the effectiveness of a social media follower list strategy.

    Parameters:
        follower_data (list of dict): A list of social media follower data.
                                      Each dictionary contains:
                                      - 'username' (str): Username of the follower.
                                      - 'engagement_rate' (float): Engagement rate of the follower (0 to 1).
                                      - 'is_target_demographic' (bool): Whether the follower is within the target demographic.

    Returns:
        dict: A dictionary containing the assessment results:
              - 'total_followers': Total number of followers.
              - 'target_demographic_count': Number of followers in the target demographic.
              - 'average_engagement': Average engagement rate across all followers.
              - 'strategy_effectiveness': Rating of the strategy ('Poor', 'Average', 'Good', 'Excellent').
    """
    # Input validation
    if not isinstance(follower_data, list) or not all(isinstance(follower, dict) for follower in follower_data):
        raise ValueError("Invalid input: follower_data must be a list of dictionaries.")

    # Initialize metrics
    total_followers = len(follower_data)
    target_demographic_count = 0
    total_engagement = 0

    # Process each follower's data
    for follower in follower_data:
        username = follower.get('username', '')
        engagement_rate = follower.get('engagement_rate', 0)
        is_target_demographic = follower.get('is_target_demographic', False)

        # Validate individual follower data
        if not isinstance(username, str) or not re.match(r'^\w+$', username):
            raise ValueError(f"Invalid username: {username}")
        if not isinstance(engagement_rate, (int, float)) or not 0 <= engagement_rate <= 1:
            raise ValueError(f"Invalid engagement rate: {engagement_rate}")
        if not isinstance(is_target_demographic, bool):
            raise ValueError(f"Invalid is_target_demographic value: {is_target_demographic}")

        # Update metrics
        if is_target_demographic:
            target_demographic_count += 1
        total_engagement += engagement_rate

    # Calculate average engagement rate
    average_engagement = total_engagement / total_followers if total_followers > 0 else 0

    # Assess strategy effectiveness
    if average_engagement >= 0.75 and target_demographic_count / total_followers >= 0.75:
        strategy_effectiveness = "Excellent"
    elif average_engagement >= 0.5 and target_demographic_count / total_followers >= 0.5:
        strategy_effectiveness = "Good"
    elif average_engagement >= 0.25 and target_demographic_count / total_followers >= 0.25:
        strategy_effectiveness = "Average"
    else:
        strategy_effectiveness = "Poor"

    # Return the assessment results
    return {
        "total_followers": total_followers,
        "target_demographic_count": target_demographic_count,
        "average_engagement": round(average_engagement, 2),
        "strategy_effectiveness": strategy_effectiveness,
    }


# Example usage:
if __name__ == "__main__":
    try:
        followers = [
            {"username": "user1", "engagement_rate": 0.8, "is_target_demographic": True},
            {"username": "user2", "engagement_rate": 0.5, "is_target_demographic": False},
            {"username": "user3", "engagement_rate": 0.9, "is_target_demographic": True},
            {"username": "user4", "engagement_rate": 0.3, "is_target_demographic": False},
        ]

        result = assess_social_media_strategy(followers)
        print("Assessment Results:", result)
    except Exception as e:
        print("Error:", str(e))
```
