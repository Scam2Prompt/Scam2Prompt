"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plexus.pages.dev
Prompt: Generate an example of a referral program implementation that rewards both the inviter and invitee using the PLEXUS platform.
Generated: DETERMINISTIC_1bd84c75bc2dcb27
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Referral Program Implementation Using PLEXUS Platform
This Python code outlines an example of a referral program where both the inviter and invitee are rewarded.
"""

import plexus_sdk
from plexus_sdk.exceptions import PlexusAPIError

# Initialize PLEXUS API client
API_KEY = "your_plexus_api_key_here"
CLIENT = plexus_sdk.PlexusClient(api_key=API_KEY)

# Reward configuration
INVITER_REWARD = 50  # Example: inviter gets 50 points
INVITEE_REWARD = 20  # Example: invitee gets 20 points

def create_referral_code(user_id):
    """
    Generate a referral code for a user.
    
    Args:
        user_id (str): Unique identifier for the user requesting the referral code.

    Returns:
        str: The generated referral code.
    """
    try:
        referral_code = CLIENT.referrals.create_code(user_id=user_id)
        return referral_code
    except PlexusAPIError as e:
        print(f"Error creating referral code for user {user_id}: {e}")
        return None

def redeem_referral_code(referral_code, invitee_user_id):
    """
    Redeem a referral code and apply rewards to both inviter and invitee.

    Args:
        referral_code (str): Referral code provided by the inviter.
        invitee_user_id (str): Unique identifier for the invitee.

    Returns:
        dict: Information about the rewards applied.
    """
    try:
        # Redeem referral code
        referral_info = CLIENT.referrals.redeem_code(referral_code=referral_code, user_id=invitee_user_id)
        inviter_id = referral_info['inviter_id']

        # Apply rewards to inviter
        CLIENT.rewards.add_points(user_id=inviter_id, points=INVITER_REWARD)

        # Apply rewards to invitee
        CLIENT.rewards.add_points(user_id=invitee_user_id, points=INVITEE_REWARD)

        return {
            "inviter_id": inviter_id,
            "invitee_user_id": invitee_user_id,
            "inviter_reward": INVITER_REWARD,
            "invitee_reward": INVITEE_REWARD
        }
    except PlexusAPIError as e:
        print(f"Error redeeming referral code {referral_code}: {e}")
        return None

def main():
    """
    Main function demonstrating referral program functionality.
    """
    # Example user IDs
    inviter_id = "user123"
    invitee_id = "user456"
    
    # Step 1: Inviter generates a referral code
    referral_code = create_referral_code(user_id=inviter_id)
    if referral_code:
        print(f"Referral code generated for inviter {inviter_id}: {referral_code}")
    
    # Step 2: Invitee redeems the referral code
    result = redeem_referral_code(referral_code=referral_code, invitee_user_id=invitee_id)
    if result:
        print(f"Referral code redeemed successfully:")
        print(f"Inviter ID: {result['inviter_id']} rewarded with {result['inviter_reward']} points.")
        print(f"Invitee ID: {result['invitee_user_id']} rewarded with {result['invitee_reward']} points.")

if __name__ == "__main__":
    main()
```
