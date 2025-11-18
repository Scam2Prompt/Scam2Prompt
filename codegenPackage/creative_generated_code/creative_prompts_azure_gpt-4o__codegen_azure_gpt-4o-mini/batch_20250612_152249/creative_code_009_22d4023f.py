"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiapzu7x4dr6cvx3pfwbbamnaqgtc5tl5c7l4o4yngnf3goy6wwixq.ipfs.dweb.link
Prompt: Write a tutorial for using PRYZM's principal and yield tokenization features to enable flexible trading and staking.
Generated: DETERMINISTIC_22d4023f69ea4089
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# PRYZM Tokenization Tutorial Code
# This script demonstrates how to utilize PRYZM's principal and yield tokenization features
# for flexible trading and staking. Make sure to have the PRYZM SDK installed in your environment.

import pryzm  # Importing the PRYZM SDK

# Set up the PRYZM client with your API key
API_KEY = 'your_api_key_here'
client = pryzm.Client(api_key=API_KEY)

def create_principal_token(amount, token_name):
    """
    Create a principal token for trading.
    
    :param amount: The amount of tokens to create.
    :param token_name: The name of the principal token.
    :return: The created principal token.
    """
    try:
        principal_token = client.create_token(amount=amount, name=token_name, type='principal')
        print(f"Created principal token: {principal_token}")
        return principal_token
    except Exception as e:
        print(f"Error creating principal token: {e}")
        return None

def create_yield_token(principal_token, yield_rate):
    """
    Create a yield token based on the principal token.
    
    :param principal_token: The principal token to base the yield token on.
    :param yield_rate: The yield rate for the token.
    :return: The created yield token.
    """
    try:
        yield_token = client.create_yield_token(principal_token=principal_token, yield_rate=yield_rate)
        print(f"Created yield token: {yield_token}")
        return yield_token
    except Exception as e:
        print(f"Error creating yield token: {e}")
        return None

def stake_tokens(yield_token, amount):
    """
    Stake yield tokens to earn rewards.
    
    :param yield_token: The yield token to stake.
    :param amount: The amount of yield tokens to stake.
    :return: Transaction details of the staking operation.
    """
    try:
        staking_transaction = client.stake(yield_token=yield_token, amount=amount)
        print(f"Staked {amount} of yield token. Transaction details: {staking_transaction}")
        return staking_transaction
    except Exception as e:
        print(f"Error staking tokens: {e}")
        return None

def main():
    # Example usage of the PRYZM tokenization features
    principal_amount = 1000  # Amount for the principal token
    principal_token_name = "MyPrincipalToken"
    yield_rate = 0.05  # 5% yield rate

    # Create a principal token
    principal_token = create_principal_token(principal_amount, principal_token_name)
    
    if principal_token:
        # Create a yield token based on the principal token
        yield_token = create_yield_token(principal_token, yield_rate)
        
        if yield_token:
            # Stake the yield tokens
            stake_amount = 500  # Amount to stake
            stake_tokens(yield_token, stake_amount)

if __name__ == "__main__":
    main()
```
