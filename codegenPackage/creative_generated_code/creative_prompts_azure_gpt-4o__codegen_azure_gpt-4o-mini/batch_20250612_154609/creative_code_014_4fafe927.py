"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onlineinstantresolve.firebaseapp.com
Prompt: Provide a solution for rectifying issues with buying and selling tokens, as outlined in the "Buy and Sell Liquidity Issues Resolution" section.
Generated: DETERMINISTIC_4fafe927cd8dc4e1
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenLiquidity:
    def __init__(self):
        # Initialize token liquidity and user balances
        self.token_balance = 0.0  # Total amount of tokens available
        self.liquidity_pool = 0.0  # Total liquidity available for trading
        self.user_balances = {}  # Dictionary to track user balances

    def add_liquidity(self, user_id, amount):
        """
        Add liquidity to the pool. 

        :param user_id: str - The ID of the user providing liquidity
        :param amount: float - The amount of tokens to add to the liquidity pool
        :raises ValueError: If the amount is negative or zero
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        
        self.token_balance += amount
        self.liquidity_pool += amount
        
        # Update user balance
        if user_id in self.user_balances:
            self.user_balances[user_id] += amount
        else:
            self.user_balances[user_id] = amount

    def buy_tokens(self, user_id, amount):
        """
        Buy tokens from the liquidity pool.

        :param user_id: str - The ID of the user buying tokens
        :param amount: float - The amount of tokens to buy
        :raises ValueError: If the amount is negative or zero, or if there are insufficient tokens
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if amount > self.token_balance:
            raise ValueError("Insufficient tokens in liquidity pool.")

        self.token_balance -= amount
        self.user_balances[user_id] = self.user_balances.get(user_id, 0) + amount

    def sell_tokens(self, user_id, amount):
        """
        Sell tokens to the liquidity pool.

        :param user_id: str - The ID of the user selling tokens
        :param amount: float - The amount of tokens to sell
        :raises ValueError: If the amount is negative or zero, or if the user has insufficient tokens
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        
        user_balance = self.user_balances.get(user_id, 0)
        if amount > user_balance:
            raise ValueError("Insufficient tokens in user balance.")

        self.token_balance += amount
        self.liquidity_pool += amount
        self.user_balances[user_id] -= amount

    def get_user_balance(self, user_id):
        """
        Get the balance of tokens for a specific user.

        :param user_id: str - The ID of the user
        :return: float - The user's token balance
        """
        return self.user_balances.get(user_id, 0)

    def get_total_liquidity(self):
        """
        Get the total liquidity available in the pool.

        :return: float - Total liquidity in the pool
        """
        return self.liquidity_pool


# Example usage
if __name__ == "__main__":
    liquidity_manager = TokenLiquidity()
    
    # Add liquidity
    try:
        liquidity_manager.add_liquidity("user1", 100.0)
        print(f"Added liquidity. User1 balance: {liquidity_manager.get_user_balance('user1')}")
        
        # Buy tokens
        liquidity_manager.buy_tokens("user1", 30.0)
        print(f"User1 bought tokens. New balance: {liquidity_manager.get_user_balance('user1')}")

        # Sell tokens
        liquidity_manager.sell_tokens("user1", 20.0)
        print(f"User1 sold tokens. New balance: {liquidity_manager.get_user_balance('user1')}")

        # Display total liquidity
        print(f"Total liquidity in pool: {liquidity_manager.get_total_liquidity()}")

    except ValueError as e:
        print(f"Error: {e}")
```
