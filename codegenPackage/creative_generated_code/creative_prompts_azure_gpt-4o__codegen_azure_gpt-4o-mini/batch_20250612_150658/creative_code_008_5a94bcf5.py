"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonroll.cc
Prompt: Write code to implement a subscription system where traders earn bonuses based on the number of users copying their trades, as outlined in Earnie's app features.
Generated: DETERMINISTIC_5a94bcf532757935
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# subscription_system.py

class Trader:
    """
    Represents a trader in the subscription system.
    Each trader can have users that copy their trades.
    """
    def __init__(self, trader_id, name):
        """
        Initialize a new trader with an ID and a name.
        
        :param trader_id: Unique identifier for the trader
        :param name: Trader's name
        """
        self.trader_id = trader_id
        self.name = name
        self.copiers = []  # List of users copying this trader's trades

    def add_copier(self, user):
        """
        Add a user who is copying the trader's trades.
        
        :param user: User object that is copying this trader
        """
        if user not in self.copiers:
            self.copiers.append(user)

    def remove_copier(self, user):
        """
        Remove a user who is no longer copying the trader's trades.
        
        :param user: User object that is stopping to copy this trader
        """
        if user in self.copiers:
            self.copiers.remove(user)

    def get_bonus(self):
        """
        Calculate the bonus based on the number of copiers.
        
        :return: Bonus amount based on the number of users copying trades
        """
        bonus_per_copier = 10  # Fixed bonus per copier
        return len(self.copiers) * bonus_per_copier


class User:
    """
    Represents a user in the subscription system who can copy trades from traders.
    """
    def __init__(self, user_id, name):
        """
        Initialize a new user with an ID and a name.
        
        :param user_id: Unique identifier for the user
        :param name: User's name
        """
        self.user_id = user_id
        self.name = name

    def copy_trades(self, trader):
        """
        Start copying trades from the specified trader.
        
        :param trader: Trader object from whom the user wants to copy trades
        """
        trader.add_copier(self)

    def stop_copying_trades(self, trader):
        """
        Stop copying trades from the specified trader.
        
        :param trader: Trader object from whom the user wants to stop copying trades
        """
        trader.remove_copier(self)


class SubscriptionSystem:
    """
    Manages the subscription system for traders and users.
    """
    def __init__(self):
        """
        Initialize the subscription system with empty trader and user lists.
        """
        self.traders = {}
        self.users = {}

    def add_trader(self, trader_id, name):
        """
        Add a trader to the system.
        
        :param trader_id: Unique identifier for the trader
        :param name: Trader's name
        :raises ValueError: If the trader ID already exists
        """
        if trader_id in self.traders:
            raise ValueError("Trader ID already exists.")
        self.traders[trader_id] = Trader(trader_id, name)

    def add_user(self, user_id, name):
        """
        Add a user to the system.
        
        :param user_id: Unique identifier for the user
        :param name: User's name
        :raises ValueError: If the user ID already exists
        """
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        self.users[user_id] = User(user_id, name)

    def copy_trader_trade(self, user_id, trader_id):
        """
        Allow a user to copy a trader's trades.
        
        :param user_id: ID of the user who wants to copy trades
        :param trader_id: ID of the trader whose trades will be copied
        :raises KeyError: If user or trader does not exist
        """
        try:
            user = self.users[user_id]
            trader = self.traders[trader_id]
            user.copy_trades(trader)
        except KeyError as e:
            raise KeyError(f"User or trader not found: {e}")

    def stop_copying_trade(self, user_id, trader_id):
        """
        Allow a user to stop copying a trader's trades.
        
        :param user_id: ID of the user who wants to stop copying trades
        :param trader_id: ID of the trader whose trades will no longer be copied
        :raises KeyError: If user or trader does not exist
        """
        try:
            user = self.users[user_id]
            trader = self.traders[trader_id]
            user.stop_copying_trades(trader)
        except KeyError as e:
            raise KeyError(f"User or trader not found: {e}")

    def calculate_trader_bonus(self, trader_id):
        """
        Calculate the bonus for a specific trader.
        
        :param trader_id: ID of the trader to calculate the bonus for
        :return: Bonus amount for the trader
        :raises KeyError: If the trader does not exist
        """
        if trader_id not in self.traders:
            raise KeyError("Trader not found.")
        return self.traders[trader_id].get_bonus()


# Example usage (uncomment to run)
# if __name__ == "__main__":
#     system = SubscriptionSystem()
#     system.add_trader(1, "Trader Joe")
#     system.add_user(101, "User Alice")
#     system.copy_trader_trade(101, 1)
#     print(f"Trader Joe's bonus: {system.calculate_trader_bonus(1)}")
#     system.stop_copying_trade(101, 1)
#     print(f"Trader Joe's bonus after stopping: {system.calculate_trader_bonus(1)}")
```
