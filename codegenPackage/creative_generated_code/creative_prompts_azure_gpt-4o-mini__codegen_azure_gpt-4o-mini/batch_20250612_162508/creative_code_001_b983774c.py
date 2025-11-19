"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mercurial-v2-git-fix-slow-routing-wowcats.vercel.app
Prompt: How can I create a multi-token pool using the Meteora Pools library? Provide an example.
Generated: DETERMINISTIC_b983774c388fa637
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import the necessary libraries from Meteora Pools
from meteora_pools import MultiTokenPool, Token

# Function to create a multi-token pool
def create_multi_token_pool():
    try:
        # Define the tokens to be added to the pool
        token_a = Token(name="TokenA", symbol="TKNA", initial_supply=1000000)
        token_b = Token(name="TokenB", symbol="TKNB", initial_supply=500000)

        # Create the multi-token pool with the defined tokens
        multi_token_pool = MultiTokenPool(tokens=[token_a, token_b], pool_name="MyMultiTokenPool")

        # Check if the pool was created successfully
        if multi_token_pool.is_initialized():
            print(f"Multi-token pool '{multi_token_pool.pool_name}' created successfully with tokens:")
            for token in multi_token_pool.tokens:
                print(f"- {token.name} ({token.symbol}): {token.initial_supply} supply")
        else:
            print("Failed to create the multi-token pool.")

    except Exception as e:
        # Handle any exceptions that occur during pool creation
        print(f"An error occurred while creating the multi-token pool: {e}")

# Run the function to create the multi-token pool
if __name__ == "__main__":
    create_multi_token_pool()
```
