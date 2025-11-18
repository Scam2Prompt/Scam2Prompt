"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supermining.website
Prompt: Create a program that simulates Bitcoin cloud mining using SuperMining's described packages, including affiliate bonuses and earning rates.
Generated: DETERMINISTIC_20b55bde2beb055a
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random


class SuperMining:
    """
    SuperMining Cloud Mining Simulator
    Offers packages for simulating Bitcoin mining earnings and affiliate bonuses.
    """

    def __init__(self):
        # Mining packages with daily earning rates in BTC
        self.packages = {
            "Basic": {"rate": 0.0001, "price": 50},
            "Standard": {"rate": 0.0005, "price": 200},
            "Premium": {"rate": 0.001, "price": 500},
        }
        self.users = {}  # Stores user information
        self.affiliate_bonus_rate = 0.05  # 5% affiliate bonus

    def register_user(self, username):
        """
        Registers a new user with an empty account.
        """
        if username in self.users:
            raise ValueError("Username already exists")
        self.users[username] = {
            "balance": 0.0,
            "package": None,
            "affiliate_bonus": 0.0,
        }
        print(f"User '{username}' registered successfully.")

    def purchase_package(self, username, package_name):
        """
        Allows a user to purchase a mining package.
        """
        if username not in self.users:
            raise ValueError("User not found")
        if package_name not in self.packages:
            raise ValueError("Invalid package name")

        package_info = self.packages[package_name]
        self.users[username]["package"] = package_name
        print(
            f"User '{username}' purchased the '{package_name}' package for ${package_info['price']}."
        )

    def simulate_earnings(self, username, days=1):
        """
        Simulates Bitcoin mining earnings for the specified number of days.
        """
        if username not in self.users:
            raise ValueError("User not found")
        user = self.users[username]
        if not user["package"]:
            raise ValueError("No mining package purchased")

        daily_rate = self.packages[user["package"]]["rate"]
        earnings = daily_rate * days
        user["balance"] += earnings
        print(f"User '{username}' earned {earnings:.8f} BTC in {days} day(s).")

    def add_affiliate_bonus(self, referrer_username, referred_username):
        """
        Adds affiliate bonuses to the referrer when a referred user purchases a package.
        """
        if referrer_username not in self.users or referred_username not in self.users:
            raise ValueError("Invalid usernames")
        referred_user = self.users[referred_username]
        referrer_user = self.users[referrer_username]

        if not referred_user["package"]:
            raise ValueError("Referred user has not purchased a package")

        package_price = self.packages[referred_user["package"]]["price"]
        bonus = package_price * self.affiliate_bonus_rate
        referrer_user["affiliate_bonus"] += bonus
        print(
            f"Referrer '{referrer_username}' earned an affiliate bonus of ${bonus:.2f}."
        )

    def check_balance(self, username):
        """
        Displays the user's Bitcoin balance.
        """
        if username not in self.users:
            raise ValueError("User not found")
        user = self.users[username]
        print(
            f"User '{username}' - Balance: {user['balance']:.8f} BTC, Affiliate Bonus: ${user['affiliate_bonus']:.2f}"
        )


# Example usage
if __name__ == "__main__":
    try:
        cloud_mining = SuperMining()

        # Register users
        cloud_mining.register_user("alice")
        cloud_mining.register_user("bob")

        # Purchase packages
        cloud_mining.purchase_package("alice", "Premium")
        cloud_mining.purchase_package("bob", "Standard")

        # Simulate earnings
        cloud_mining.simulate_earnings("alice", days=7)
        cloud_mining.simulate_earnings("bob", days=7)

        # Add affiliate bonus
        cloud_mining.add_affiliate_bonus("alice", "bob")

        # Check balances
        cloud_mining.check_balance("alice")
        cloud_mining.check_balance("bob")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
