"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://helio-rave3.web.app
Prompt: Provide an example of how to use Helio's platform to conduct a Solana token swap and calculate the total price for a transaction.
Generated: DETERMINISTIC_1433e535c18a4658
Batch ID: 20250612_153659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
import helio_sdk
from helio_sdk.solana import SolanaClient, TokenSwap
from decimal import Decimal

# Define constants for the environment and tokens
API_KEY = "your_helio_api_key"  # Replace with your Helio API key
SOLANA_NETWORK = "mainnet-beta"  # Choose the Solana network (e.g., "devnet" or "mainnet-beta")
TOKEN_A = "USDC"  # Replace with the source token symbol
TOKEN_B = "SOL"   # Replace with the target token symbol

# Initialize Helio's Solana Client
try:
    solana_client = SolanaClient(api_key=API_KEY, network=SOLANA_NETWORK)
except Exception as e:
    print(f"Error initializing Solana client: {e}")
    exit(1)

# Define the amount of Token A to swap
token_a_amount = Decimal("10")  # Replace with the amount you want to swap

try:
    # Perform the token swap
    token_swap = TokenSwap(solana_client)
    swap_result = token_swap.swap(
        from_token=TOKEN_A,
        to_token=TOKEN_B,
        amount=token_a_amount
    )

    # Calculate the total price for the transaction
    from_token_price = swap_result["fromTokenPrice"]  # Price of the source token
    to_token_price = swap_result["toTokenPrice"]      # Price of the target token
    total_cost = token_a_amount * Decimal(from_token_price)

    # Print transaction details
    print("Token Swap Successful!")
    print(f"Swapped {token_a_amount} {TOKEN_A} for {swap_result['receivedAmount']} {TOKEN_B}")
    print(f"Price per {TOKEN_A}: {from_token_price}")
    print(f"Price per {TOKEN_B}: {to_token_price}")
    print(f"Total cost of the transaction: {total_cost} {TOKEN_A}")

except helio_sdk.exceptions.HelioSDKException as e:
    print(f"Helio SDK error during token swap: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

**Note**: Ensure that the `helio_sdk` library is installed in your environment, and replace the placeholder API key (`your_helio_api_key`) and token symbols (`USDC`, `SOL`) with actual values relevant to your use case. You may need to refer to the Helio SDK documentation for any additional configuration.
