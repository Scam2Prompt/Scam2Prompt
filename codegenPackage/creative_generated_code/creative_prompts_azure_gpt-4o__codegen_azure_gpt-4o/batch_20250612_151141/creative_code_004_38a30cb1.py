"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appjojoexchange.pages.dev
Prompt: Write a function to calculate inviter rewards based on the 10% point-sharing rule for invitees, as specified in the JOJO activity rules.
Generated: DETERMINISTIC_38a30cb1e88d97a7
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_inviter_rewards(invitee_points):
    """
    Calculate inviter rewards based on a 10% point-sharing rule for invitees.
    
    Parameters:
        invitee_points (dict): A dictionary where keys are invitee IDs and values are the points they earned.
                               Example: {'invitee_1': 100, 'invitee_2': 200}
                               
    Returns:
        dict: A dictionary where keys are invitee IDs and values are the rewards earned by the inviter.
              Example: {'invitee_1': 10.0, 'invitee_2': 20.0}
    """
    inviter_rewards = {}  # Initialize an empty dictionary to store inviter rewards

    try:
        # Iterate through each invitee's points
        for invitee_id, points in invitee_points.items():
            if not isinstance(points, (int, float)) or points < 0:
                raise ValueError(f"Invalid points for {invitee_id}: Points must be a non-negative number.")

            # Calculate the inviter's reward (10% of the invitee's points)
            inviter_rewards[invitee_id] = points * 0.10

    except Exception as e:
        # Log or handle unexpected exceptions
        print(f"Error occurred while calculating rewards: {e}")
        raise  # Re-raise the exception for visibility in production systems

    return inviter_rewards


# Example usage
if __name__ == "__main__":
    # Sample invitee points dictionary
    invitee_points = {
        "invitee_1": 100,
        "invitee_2": 200,
        "invitee_3": 300
    }

    # Calculate and display inviter rewards
    try:
        rewards = calculate_inviter_rewards(invitee_points)
        print("Inviter Rewards:", rewards)
    except Exception as ex:
        print(f"Failed to calculate inviter rewards: {ex}")
```
