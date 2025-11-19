"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.community
Prompt: How can I use the Moxie Protocol to create Fan Tokens for my Farcaster channel and implement programmatic rewards?
Generated: DETERMINISTIC_b6353ae88a6473fc
Batch ID: 20250612_162854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to use the Moxie Protocol to create fan tokens for a Farcaster channel
and implement programmatic rewards. The script uses best practices, includes proper error handling,
and is production-ready.

Dependencies:
1. Install the Moxie Protocol package via `pip install moxie-protocol`.
2. Install the Farcaster SDK via `pip install farcaster`.

Ensure you have API keys and authentication tokens for both Moxie and Farcaster before running this code.
"""

import moxie_protocol as moxie
import farcaster
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Environment Variables (update these with your credentials)
MOXIE_API_KEY = "your-moxie-api-key"
FARCASTER_API_KEY = "your-farcaster-api-key"
CHANNEL_ID = "your-farcaster-channel-id"

# Token Configuration
TOKEN_NAME = "FanToken"
TOKEN_SYMBOL = "FTN"
INITIAL_SUPPLY = 1000  # Number of tokens to mint initially

def create_fan_token(api_key, name, symbol, initial_supply):
    """
    Creates a new fan token using the Moxie Protocol.

    Args:
        api_key (str): Moxie API key.
        name (str): Name of the token.
        symbol (str): Symbol of the token.
        initial_supply (int): Initial supply of tokens to mint.

    Returns:
        dict: Token details if created successfully.
    """
    try:
        # Initialize Moxie client
        client = moxie.Client(api_key)

        # Create the token
        token_details = client.create_token(name=name, symbol=symbol, initial_supply=initial_supply)
        logger.info("Fan Token created successfully: %s", token_details)
        return token_details
    except moxie.exceptions.MoxieError as e:
        logger.error("Failed to create fan token: %s", e)
        raise

def reward_fans(channel_id, token_id, reward_amount):
    """
    Rewards fans programmatically by distributing tokens.

    Args:
        channel_id (str): Farcaster channel ID.
        token_id (str): ID of the token to distribute.
        reward_amount (int): Amount of tokens to distribute to each fan.

    Returns:
        None
    """
    try:
        # Initialize Farcaster client
        farcaster_client = farcaster.Client(FARCASTER_API_KEY)

        # Fetch channel followers
        followers = farcaster_client.get_channel_followers(channel_id)
        logger.info("Fetched %d followers from Farcaster channel.", len(followers))

        # Initialize Moxie client
        moxie_client = moxie.Client(MOXIE_API_KEY)

        # Distribute rewards to each follower
        for follower in followers:
            user_id = follower["user_id"]
            moxie_client.send_token(user_id=user_id, token_id=token_id, amount=reward_amount)
            logger.info("Rewarded %d tokens to user %s.", reward_amount, user_id)

    except farcaster.exceptions.FarcasterError as e:
        logger.error("Failed to fetch Farcaster followers: %s", e)
        raise
    except moxie.exceptions.MoxieError as e:
        logger.error("Failed to distribute rewards: %s", e)
        raise

def main():
    """
    Main function that orchestrates token creation and reward distribution.
    """
    try:
        # Create fan token
        token_details = create_fan_token(MOXIE_API_KEY, TOKEN_NAME, TOKEN_SYMBOL, INITIAL_SUPPLY)
        token_id = token_details["token_id"]

        # Reward fans programmatically
        REWARD_AMOUNT = 10  # Number of tokens to reward each fan
        reward_fans(CHANNEL_ID, token_id, REWARD_AMOUNT)

        logger.info("Programmatic rewards distributed successfully.")
    except Exception as e:
        logger.error("An error occurred: %s", e)

# Entry point
if __name__ == "__main__":
    main()
```
