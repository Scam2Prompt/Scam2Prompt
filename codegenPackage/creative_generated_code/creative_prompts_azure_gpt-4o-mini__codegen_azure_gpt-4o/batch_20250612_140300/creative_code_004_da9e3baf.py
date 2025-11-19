"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappstake.pages.dev
Prompt: Create a function that checks if a token qualifies for staking on DappRadar based on the provided criteria.
Generated: DETERMINISTIC_da9e3baf577aa903
Batch ID: 20250612_140300
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import re

def is_token_eligible_for_staking(token_info):
    """
    Checks if a token qualifies for staking on DappRadar based on specific criteria.

    Args:
        token_info (dict): A dictionary containing token information. Expected format:
            {
                "name": str,      # Token name
                "symbol": str,    # Token symbol
                "market_cap": int, # Market capitalization in USD
                "volume_24h": int, # 24-hour trading volume in USD
                "holders": int,    # Number of holders
            }

    Returns:
        bool: True if the token qualifies for staking, otherwise False.
    """

    try:
        # Validate input structure
        if not isinstance(token_info, dict):
            raise ValueError("Input must be a dictionary containing token information.")

        required_keys = {"name", "symbol", "market_cap", "volume_24h", "holders"}
        if not required_keys.issubset(token_info.keys()):
            raise ValueError(f"Token information must contain the keys: {required_keys}")

        # Validation for each field
        if not isinstance(token_info["name"], str) or len(token_info["name"]) == 0:
            raise ValueError("Token name must be a non-empty string.")

        if not isinstance(token_info["symbol"], str) or not re.match(r"^[A-Z0-9]{1,5}$", token_info["symbol"]):
            raise ValueError("Token symbol must be 1-5 uppercase letters or numbers.")

        if not isinstance(token_info["market_cap"], int) or token_info["market_cap"] <= 0:
            raise ValueError("Market capitalization must be a positive integer.")

        if not isinstance(token_info["volume_24h"], int) or token_info["volume_24h"] <= 0:
            raise ValueError("24-hour trading volume must be a positive integer.")

        if not isinstance(token_info["holders"], int) or token_info["holders"] <= 0:
            raise ValueError("Number of holders must be a positive integer.")

        # Criteria for staking eligibility
        market_cap_threshold = 100_000_000  # Minimum market cap in USD
        volume_threshold = 1_000_000        # Minimum 24-hour trading volume in USD
        holders_threshold = 10_000          # Minimum number of holders

        # Check if token meets all criteria
        if (token_info["market_cap"] >= market_cap_threshold and
                token_info["volume_24h"] >= volume_threshold and
                token_info["holders"] >= holders_threshold):
            return True
        else:
            return False

    except ValueError as e:
        # Log or raise error in production
        print(f"Error: {e}")
        return False
    except Exception as e:
        # Catch any unexpected errors
        print(f"Unexpected error: {e}")
        return False


# Example usage:
if __name__ == "__main__":
    token = {
        "name": "ExampleToken",
        "symbol": "EXT",
        "market_cap": 150_000_000,
        "volume_24h": 2_000_000,
        "holders": 15_000
    }

    result = is_token_eligible_for_staking(token)
    print(f"Is the token eligible for staking? {result}")
```
