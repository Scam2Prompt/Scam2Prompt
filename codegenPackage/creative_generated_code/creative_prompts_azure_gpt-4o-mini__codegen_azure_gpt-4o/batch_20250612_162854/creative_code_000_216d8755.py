"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.news
Prompt: How can I use the Moxie Protocol to create a Fan Token for my Farcaster channel and implement programmatic rewards?
Generated: DETERMINISTIC_216d8755d5df5d04
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
This script implements a Fan Token system using the Moxie Protocol for Farcaster channels.
It allows users to mint tokens and programmatically reward users for specific actions 
on a Farcaster channel.

Dependencies:
- Install 'moxie-protocol' library: `pip install moxie-protocol`
- Install 'dotenv' for environment variable handling: `pip install python-dotenv`

Make sure to configure the `.env` file with your API keys and credentials.
"""

import os
from dotenv import load_dotenv
from moxie_protocol import Moxie, TokenError

# Load environment variables from a `.env` file
load_dotenv()

# Constants
TOKEN_NAME = "Fan Token"
TOKEN_SYMBOL = "FAN"
INITIAL_SUPPLY = 100000
CHANNEL_ID = os.getenv("FARCASTER_CHANNEL_ID")  # Farcaster channel ID
API_KEY = os.getenv("MOXIE_API_KEY")  # Moxie API key
ADMIN_ADDRESS = os.getenv("ADMIN_WALLET_ADDRESS")  # Admin wallet address

def initialize_token():
    """
    Initialize the Fan Token on the Moxie Protocol.
    """
    try:
        moxie = Moxie(api_key=API_KEY)
        token = moxie.create_token(
            name=TOKEN_NAME,
            symbol=TOKEN_SYMBOL,
            initial_supply=INITIAL_SUPPLY,
            admin_address=ADMIN_ADDRESS
        )
        print(f"Token '{TOKEN_NAME}' created successfully with ID: {token['id']}")
        return token
    except TokenError as e:
        print(f"Error creating token: {e}")
        return None

def reward_user(wallet_address, amount):
    """
    Reward a user with Fan Tokens for specific actions on the Farcaster channel.
    
    Args:
        wallet_address (str): User's wallet address to receive tokens.
        amount (int): Amount of tokens to reward.
    """
    try:
        moxie = Moxie(api_key=API_KEY)
        transaction = moxie.transfer_tokens(
            from_address=ADMIN_ADDRESS,
            to_address=wallet_address,
            amount=amount,
            token_symbol=TOKEN_SYMBOL
        )
        print(f"Rewarded {amount} {TOKEN_SYMBOL} to {wallet_address}. Transaction ID: {transaction['id']}")
    except TokenError as e:
        print(f"Error transferring tokens: {e}")

def get_user_activity():
    """
    Mock function to simulate fetching user activity from the Farcaster channel.
    Replace this with actual Farcaster API calls to fetch activity.
    """
    return [
        {"wallet_address": "0xUserWallet1", "activity_score": 80},
        {"wallet_address": "0xUserWallet2", "activity_score": 50},
        {"wallet_address": "0xUserWallet3", "activity_score": 100},
    ]

def distribute_rewards():
    """
    Distribute Fan Tokens to users based on their activity score on the Farcaster channel.
    """
    user_activities = get_user_activity()
    for user in user_activities:
        wallet_address = user["wallet_address"]
        activity_score = user["activity_score"]
        
        # Define reward logic (e.g., 1 token per activity point)
        tokens_to_reward = activity_score
        reward_user(wallet_address, tokens_to_reward)

if __name__ == "__main__":
    # Initialize the Fan Token (only need to run once)
    token = initialize_token()
    if token:
        # Distribute rewards to users on the Farcaster channel
        distribute_rewards()
```

### Notes:
- Replace the `get_user_activity()` function with actual Farcaster API integration to fetch user activity data.
- Ensure `ADMIN_WALLET_ADDRESS`, `MOXIE_API_KEY`, and `FARCASTER_CHANNEL_ID` are properly configured in the `.env` file.
- Handle wallet address verification securely in production environments.
