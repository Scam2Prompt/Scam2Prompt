"""
Generated Code Metadata:
========================
Original URL: https://www.staderlabs.fi
Prompt: Develop a program to simulate the initiation, tokenization, and unstaking phases of Stader Labs' liquid staking process for PoS networks.
Generated: DETERMINISTIC_36d98ccd27bfdacb
Batch ID: 20250612_153820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LiquidStaking:
    def __init__(self):
        """
        Initializes the LiquidStaking class with empty lists for staked tokens and unstaked tokens.
        """
        self.staked_tokens = []
        self.unstaked_tokens = []

    def initiate_staking(self, token_id, amount):
        """
        Initiates the staking process for a given token.

        :param token_id: Unique identifier for the token to be staked.
        :param amount: Amount of tokens to stake.
        :raises ValueError: If the amount is non-positive.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        self.staked_tokens.append({'token_id': token_id, 'amount': amount})
        print(f"Staked {amount} of token {token_id}.")

    def tokenize(self, token_id):
        """
        Tokenizes the staked token into a liquid token.

        :param token_id: Unique identifier for the token to be tokenized.
        :raises ValueError: If the token is not found in staked tokens.
        """
        for token in self.staked_tokens:
            if token['token_id'] == token_id:
                print(f"Tokenized {token['amount']} of token {token_id} into liquid token.")
                return
        
        raise ValueError(f"Token {token_id} not found in staked tokens.")

    def unstake(self, token_id, amount):
        """
        Unstakes a specified amount of a token.

        :param token_id: Unique identifier for the token to be unstaked.
        :param amount: Amount of tokens to unstake.
        :raises ValueError: If the amount is non-positive or exceeds staked amount.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        for token in self.staked_tokens:
            if token['token_id'] == token_id:
                if amount > token['amount']:
                    raise ValueError("Cannot unstake more than staked amount.")
                
                token['amount'] -= amount
                if token['amount'] == 0:
                    self.staked_tokens.remove(token)
                
                self.unstaked_tokens.append({'token_id': token_id, 'amount': amount})
                print(f"Unstaked {amount} of token {token_id}.")
                return
        
        raise ValueError(f"Token {token_id} not found in staked tokens.")

    def get_staked_tokens(self):
        """
        Returns a list of currently staked tokens.

        :return: List of staked tokens.
        """
        return self.staked_tokens

    def get_unstaked_tokens(self):
        """
        Returns a list of currently unstaked tokens.

        :return: List of unstaked tokens.
        """
        return self.unstaked_tokens


# Example usage
if __name__ == "__main__":
    try:
        staking = LiquidStaking()
        staking.initiate_staking("ETH", 10)
        staking.tokenize("ETH")
        staking.unstake("ETH", 5)
        print("Current staked tokens:", staking.get_staked_tokens())
        print("Current unstaked tokens:", staking.get_unstaked_tokens())
    except ValueError as e:
        print(f"Error: {e}")
```
