"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tinnyman.io
Prompt: What are the key features of Tinyman v2 that enhance the trading experience for users on the Algorand blockchain?
Generated: DETERMINISTIC_1c631733351b5a41
Batch ID: 20250612_161039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TinymanV2:
    """
    This class represents the Tinyman V2 decentralized exchange on the Algorand blockchain.
    It provides key features that enhance the trading experience for users.
    """

    def __init__(self):
        """
        Initializes the Tinyman V2 instance with default attributes.
        """
        self.pools = []
        self.user_balances = {}
        self.transaction_history = []

    def add_pool(self, token_a, token_b, reserve_a, reserve_b):
        """
        Adds a liquidity pool to the exchange.

        :param token_a: The first token in the pool
        :param token_b: The second token in the pool
        :param reserve_a: The amount of token A in the pool
        :param reserve_b: The amount of token B in the pool
        :raises ValueError: If reserves are not positive
        """
        if reserve_a <= 0 or reserve_b <= 0:
            raise ValueError("Reserves must be positive numbers.")
        pool = {
            'token_a': token_a,
            'token_b': token_b,
            'reserve_a': reserve_a,
            'reserve_b': reserve_b
        }
        self.pools.append(pool)

    def trade(self, token_in, token_out, amount_in):
        """
        Executes a trade from one token to another.

        :param token_in: The token being traded in
        :param token_out: The token being traded out
        :param amount_in: The amount of token in to trade
        :raises ValueError: If the trading pair does not exist
        :raises Exception: If insufficient liquidity for trade
        """
        pool = self.find_pool(token_in, token_out)
        # Simplified trade logic for illustration
        if amount_in <= 0:
            raise ValueError("Amount must be positive.")
        
        # Logic to check liquidity and execute trade
        if pool:
            reserve_in = pool['reserve_a'] if pool['token_a'] == token_in else pool['reserve_b']
            reserve_out = pool['reserve_b'] if pool['token_a'] == token_in else pool['reserve_a']
            
            # Assuming simple constant product formula for liquidity check
            if amount_in > reserve_in:
                raise Exception("Insufficient liquidity for trade.")

            amount_out = self.calculate_amount_out(amount_in, reserve_in, reserve_out)
            self.update_reserves(pool, amount_in, amount_out)
            self.record_transaction(token_in, token_out, amount_in, amount_out)
            return amount_out
        else:
            raise ValueError("Trading pair not found.")

    def find_pool(self, token_a, token_b):
        """
        Finds a liquidity pool for the given token pair.

        :param token_a: The first token
        :param token_b: The second token
        :return: The liquidity pool if found, else None
        """
        for pool in self.pools:
            if (pool['token_a'] == token_a and pool['token_b'] == token_b) or \
               (pool['token_a'] == token_b and pool['token_b'] == token_a):
                return pool
        return None

    def calculate_amount_out(self, amount_in, reserve_in, reserve_out):
        """
        Calculates the output amount based on the input amount and reserves.

        :param amount_in: The input amount
        :param reserve_in: The reserve of the input token
        :param reserve_out: The reserve of the output token
        :return: The calculated output amount
        """
        # Simplified output amount calculation based on constant product formula
        return (amount_in * reserve_out) // (reserve_in + amount_in)

    def update_reserves(self, pool, amount_in, amount_out):
        """
        Updates the reserves of the liquidity pool after a trade.

        :param pool: The liquidity pool to update
        :param amount_in: The amount of token in
        :param amount_out: The amount of token out
        """
        if pool['token_a'] in self.user_balances:
            self.user_balances[pool['token_a']] += amount_in
        else:
            self.user_balances[pool['token_a']] = amount_in

        if pool['token_b'] in self.user_balances:
            self.user_balances[pool['token_b']] -= amount_out
        else:
            self.user_balances[pool['token_b']] = -amount_out

        pool['reserve_a'] += amount_in
        pool['reserve_b'] -= amount_out

    def record_transaction(self, token_in, token_out, amount_in, amount_out):
        """
        Records the transaction in the transaction history.

        :param token_in: The token being traded in
        :param token_out: The token being traded out
        :param amount_in: The amount of token in
        :param amount_out: The amount of token out
        """
        transaction = {
            'token_in': token_in,
            'token_out': token_out,
            'amount_in': amount_in,
            'amount_out': amount_out
        }
        self.transaction_history.append(transaction)

    def get_user_balance(self, token):
        """
        Returns the user's balance for a specific token.

        :param token: The token to check the balance for
        :return: The balance of the user for the given token
        """
        return self.user_balances.get(token, 0)

    def get_transaction_history(self):
        """
        Retrieves the transaction history of the user.

        :return: A list of transactions
        """
        return self.transaction_history


# Example usage:
if __name__ == "__main__":
    try:
        tinyman = TinymanV2()
        tinyman.add_pool('ALGO', 'USDC', 1000, 500)
        print(tinyman.trade('ALGO', 'USDC', 100))
        print(tinyman.get_user_balance('ALGO'))
        print(tinyman.get_user_balance('USDC'))
        print(tinyman.get_transaction_history())
    except Exception as e:
        print(f"An error occurred: {e}")
```
