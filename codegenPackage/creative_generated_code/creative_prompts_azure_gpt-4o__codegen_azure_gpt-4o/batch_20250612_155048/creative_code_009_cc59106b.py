"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trumpchest.com
Prompt: Provide code examples for querying token allocation schedules for $TRUMP on the Solana blockchain, referencing the 3-year unlocking schedule mentioned on the site.
Generated: DETERMINISTIC_cc59106b4620d218
Batch ID: 20250612_155048
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mainnet-beta.solana.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
from solana.rpc.api import Client
from solana.rpc.types import MemcmpOpts, TokenAccountOpts
from datetime import datetime, timedelta

# Constants
RPC_ENDPOINT = "https://api.mainnet-beta.solana.com"  # Solana mainnet RPC
TOKEN_MINT = "$TRUMP_TOKEN_MINT_ADDRESS_HERE"  # Replace with the actual token mint address
UNLOCK_START_DATE = datetime(2023, 1, 1)  # Replace with the start date of the unlocking schedule
UNLOCK_PERIOD_YEARS = 3

# Helper function to calculate unlocked tokens based on the schedule
def calculate_unlocked_tokens(total_tokens: int, start_date: datetime, current_date: datetime, duration_years: int) -> int:
    """
    Calculates the number of unlocked tokens based on a linear unlocking schedule.

    Args:
        total_tokens (int): Total token allocation.
        start_date (datetime): The start date of unlocking.
        current_date (datetime): The current date for calculation.
        duration_years (int): Total duration of unlocking (in years).

    Returns:
        int: Number of unlocked tokens.
    """
    end_date = start_date + timedelta(days=duration_years * 365)
    if current_date < start_date:
        return 0  # No tokens unlocked before the start date
    elif current_date >= end_date:
        return total_tokens  # All tokens unlocked after the end date

    # Linear unlocking over the duration
    elapsed_time = (current_date - start_date).total_seconds()
    total_time = (end_date - start_date).total_seconds()
    unlock_ratio = elapsed_time / total_time
    unlocked_tokens = int(total_tokens * unlock_ratio)
    return unlocked_tokens

# Function to query token allocation schedules
def query_token_allocation_schedule(mint_address: str):
    """
    Queries the token allocation schedules for the given mint address.

    Args:
        mint_address (str): The mint address of the token.

    Returns:
        dict: A dictionary containing allocation data and unlocking schedule.
    """
    try:
        client = Client(RPC_ENDPOINT)

        # Fetch token account balances for the mint address
        opts = TokenAccountOpts(mint=mint_address)
        response = client.get_token_accounts_by_mint(mint_address, opts)

        if response["result"]["value"] == []:
            return {"error": "No token accounts found for the specified mint address."}

        allocation_data = {}
        current_date = datetime.now()

        # Iterate through token accounts and calculate allocation schedule
        for account in response["result"]["value"]:
            account_pubkey = account["pubkey"]
            account_info = client.get_account_info(account_pubkey)

            if "data" in account_info["result"]:
                data = account_info["result"]["data"]
                total_tokens = int(data)  # Replace with actual logic to parse token data

                # Calculate unlocked tokens based on the schedule
                unlocked_tokens = calculate_unlocked_tokens(
                    total_tokens, UNLOCK_START_DATE, current_date, UNLOCK_PERIOD_YEARS
                )

                allocation_data[account_pubkey] = {
                    "total_tokens": total_tokens,
                    "unlocked_tokens": unlocked_tokens,
                    "remaining_tokens": total_tokens - unlocked_tokens,
                }

        return allocation_data
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    # Example usage
    mint_address = TOKEN_MINT  # Replace with your token's mint address
    allocation_schedule = query_token_allocation_schedule(mint_address)

    if "error" in allocation_schedule:
        print(f"Error: {allocation_schedule['error']}")
    else:
        for account, data in allocation_schedule.items():
            print(f"Account: {account}")
            print(f"Total Tokens: {data['total_tokens']}")
            print(f"Unlocked Tokens: {data['unlocked_tokens']}")
            print(f"Remaining Tokens: {data['remaining_tokens']}")
            print("---------------------------------------------")
```
