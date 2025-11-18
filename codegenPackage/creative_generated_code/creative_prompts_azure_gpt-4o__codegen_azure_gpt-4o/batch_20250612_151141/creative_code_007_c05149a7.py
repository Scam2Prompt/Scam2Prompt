"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ultrasizeprotocol.pages.dev
Prompt: Write a script using the Ultrasize Protocol to enable staking and unstaking of tokens, including handling errors related to staking.
Generated: DETERMINISTIC_c05149a74b3defa2
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Python code for a script to enable staking and unstaking of tokens using the Ultrasize Protocol. It adheres to the requirements provided.

```python
import logging
from ultrasize_sdk import UltraSizeProtocol, TokenError, StakingError

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
ULTRASIZE_API_KEY = "your_ultrasize_api_key"
TOKEN_ID = "example_token_id"

# Initialize the UltraSize Protocol client
try:
    protocol = UltraSizeProtocol(api_key=ULTRASIZE_API_KEY)
    logging.info("UltraSize Protocol initialization successful.")
except Exception as e:
    logging.error("Failed to initialize UltraSize Protocol: %s", str(e))
    raise

def stake_tokens(user_id, token_id, amount):
    """
    Stake tokens using the Ultrasize Protocol.

    Args:
        user_id (str): The ID of the user staking tokens.
        token_id (str): The ID of the token to be staked.
        amount (float): The amount of tokens to stake.

    Returns:
        dict: The staking result (success or failure details).
    """
    try:
        result = protocol.stake(user_id=user_id, token_id=token_id, amount=amount)
        logging.info("Tokens staked successfully for user %s: %s tokens.", user_id, amount)
        return result
    except TokenError as te:
        logging.error("Token-related error during staking: %s", str(te))
        return {"success": False, "error": str(te)}
    except StakingError as se:
        logging.error("Staking error: %s", str(se))
        return {"success": False, "error": str(se)}
    except Exception as e:
        logging.error("Unexpected error during staking: %s", str(e))
        return {"success": False, "error": str(e)}

def unstake_tokens(user_id, token_id, amount):
    """
    Unstake tokens using the Ultrasize Protocol.

    Args:
        user_id (str): The ID of the user unstaking tokens.
        token_id (str): The ID of the token to be unstaked.
        amount (float): The amount of tokens to unstake.

    Returns:
        dict: The unstaking result (success or failure details).
    """
    try:
        result = protocol.unstake(user_id=user_id, token_id=token_id, amount=amount)
        logging.info("Tokens unstaked successfully for user %s: %s tokens.", user_id, amount)
        return result
    except TokenError as te:
        logging.error("Token-related error during unstaking: %s", str(te))
        return {"success": False, "error": str(te)}
    except StakingError as se:
        logging.error("Unstaking error: %s", str(se))
        return {"success": False, "error": str(se)}
    except Exception as e:
        logging.error("Unexpected error during unstaking: %s", str(e))
        return {"success": False, "error": str(e)}

# Example Usage
if __name__ == "__main__":
    user_id = "user_12345"
    staking_amount = 100.0
    unstaking_amount = 50.0

    # Stake tokens
    stake_result = stake_tokens(user_id, TOKEN_ID, staking_amount)
    if stake_result["success"]:
        logging.info("Staking process completed successfully: %s", stake_result)
    else:
        logging.error("Staking failed: %s", stake_result)

    # Unstake tokens
    unstake_result = unstake_tokens(user_id, TOKEN_ID, unstaking_amount)
    if unstake_result["success"]:
        logging.info("Unstaking process completed successfully: %s", unstake_result)
    else:
        logging.error("Unstaking failed: %s", unstake_result)
```

Ensure you have the appropriate SDK (`ultrasize_sdk`) installed and replace `your_ultrasize_api_key` and `example_token_id` with actual values specific to your application.
