"""
Generated Code Metadata:
========================
Original URL: https://cloudminingglobal.com
Prompt: Create a Python program to simulate token sales, allowing users to purchase tokens at a discounted price and track rewards, inspired by Cloudminingglobal's token sale feature.
Generated: DETERMINISTIC_77572dc7c12e60f8
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# token_sale.py

class TokenSale:
    def __init__(self, token_price, discount_rate, reward_rate):
        """
        Initialize the token sale simulator.

        Args:
            token_price (float): The regular price of a token.
            discount_rate (float): The discount rate for purchasing tokens.
            reward_rate (float): The rate at which rewards are earned.
        """
        self.token_price = token_price
        self.discount_rate = discount_rate
        self.reward_rate = reward_rate
        self.users = {}
        self.tokens_sold = 0
        self.total_rewards = 0

    def register_user(self, user_id):
        """
        Register a new user.

        Args:
            user_id (str): The unique ID of the user.
        """
        if user_id not in self.users:
            self.users[user_id] = {"tokens": 0, "rewards": 0}
            print(f"User {user_id} registered successfully.")
        else:
            print(f"User {user_id} already exists.")

    def purchase_tokens(self, user_id, amount):
        """
        Purchase tokens at a discounted price.

        Args:
            user_id (str): The unique ID of the user.
            amount (int): The number of tokens to purchase.
        """
        if user_id in self.users:
            discounted_price = self.token_price * (1 - self.discount_rate)
            total_cost = discounted_price * amount
            self.users[user_id]["tokens"] += amount
            self.tokens_sold += amount
            self.users[user_id]["rewards"] += amount * self.reward_rate
            self.total_rewards += amount * self.reward_rate
            print(f"User {user_id} purchased {amount} tokens at a discounted price of ${discounted_price:.2f} each.")
            print(f"User {user_id} now holds {self.users[user_id]['tokens']} tokens and ${self.users[user_id]['rewards']:.2f} in rewards.")
        else:
            print(f"User {user_id} does not exist.")

    def claim_rewards(self, user_id):
        """
        Claim rewards for a user.

        Args:
            user_id (str): The unique ID of the user.
        """
        if user_id in self.users:
            rewards = self.users[user_id]["rewards"]
            self.users[user_id]["rewards"] = 0
            print(f"User {user_id} claimed ${rewards:.2f} in rewards.")
        else:
            print(f"User {user_id} does not exist.")

    def get_user_balance(self, user_id):
        """
        Get the token and reward balance for a user.

        Args:
            user_id (str): The unique ID of the user.

        Returns:
            dict: A dictionary containing the user's token and reward balance.
        """
        if user_id in self.users:
            return self.users[user_id]
        else:
            print(f"User {user_id} does not exist.")
            return None

    def get_token_sale_stats(self):
        """
        Get the token sale statistics.

        Returns:
            dict: A dictionary containing the token sale statistics.
        """
        return {
            "tokens_sold": self.tokens_sold,
            "total_rewards": self.total_rewards,
        }


def main():
    token_sale = TokenSale(token_price=100, discount_rate=0.1, reward_rate=0.05)

    while True:
        print("\nToken Sale Simulator")
        print("1. Register User")
        print("2. Purchase Tokens")
        print("3. Claim Rewards")
        print("4. Get User Balance")
        print("5. Get Token Sale Stats")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            user_id = input("Enter user ID: ")
            token_sale.register_user(user_id)
        elif choice == "2":
            user_id = input("Enter user ID: ")
            amount = int(input("Enter number of tokens to purchase: "))
            token_sale.purchase_tokens(user_id, amount)
        elif choice == "3":
            user_id = input("Enter user ID: ")
            token_sale.claim_rewards(user_id)
        elif choice == "4":
            user_id = input("Enter user ID: ")
            balance = token_sale.get_user_balance(user_id)
            if balance:
                print(f"Tokens: {balance['tokens']}, Rewards: ${balance['rewards']:.2f}")
        elif choice == "5":
            stats = token_sale.get_token_sale_stats()
            print(f"Tokens Sold: {stats['tokens_sold']}, Total Rewards: ${stats['total_rewards']:.2f}")
        elif choice == "6":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
