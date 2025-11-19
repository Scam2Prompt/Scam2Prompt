"""
Generated Code Metadata:
========================
Original URL: https://fundfa.com
Prompt: Create a function to simulate trading challenges for Traders Combat, incorporating customizable rules and account types mentioned on Fundfa.
Generated: DETERMINISTIC_ad3310a53e130079
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class Trader:
    """Class representing a trader in the Traders Combat simulation."""
    
    def __init__(self, name, account_type, balance):
        """
        Initialize a Trader instance.

        :param name: str - The name of the trader.
        :param account_type: str - The type of account (e.g., 'Standard', 'Pro').
        :param balance: float - The initial balance of the trader's account.
        """
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def trade(self, amount, risk_factor):
        """
        Simulate a trade for the trader.

        :param amount: float - The amount to trade.
        :param risk_factor: float - The risk factor for the trade (0 to 1).
        :return: bool - True if the trade was successful, False otherwise.
        """
        if amount > self.balance:
            raise ValueError("Insufficient balance for the trade.")
        
        # Simulate trade outcome based on risk factor
        success_chance = random.random()
        if success_chance < risk_factor:
            self.balance += amount  # Profit
            return True
        else:
            self.balance -= amount  # Loss
            return False

def simulate_trading_challenge(traders, rounds, risk_factor):
    """
    Simulate a trading challenge among multiple traders.

    :param traders: list of Trader - The traders participating in the challenge.
    :param rounds: int - The number of trading rounds to simulate.
    :param risk_factor: float - The risk factor for each trade (0 to 1).
    :return: dict - Final balances of each trader after the challenge.
    """
    if not traders:
        raise ValueError("No traders provided for the challenge.")
    
    if rounds <= 0:
        raise ValueError("Number of rounds must be greater than zero.")
    
    if not (0 <= risk_factor <= 1):
        raise ValueError("Risk factor must be between 0 and 1.")

    final_balances = {}
    
    for round_number in range(1, rounds + 1):
        print(f"Round {round_number}:")
        for trader in traders:
            try:
                # Each trader trades a fixed amount (e.g., 100) in each round
                trade_amount = 100
                trade_success = trader.trade(trade_amount, risk_factor)
                outcome = "success" if trade_success else "loss"
                print(f"{trader.name} ({trader.account_type}) made a {outcome}. New balance: {trader.balance:.2f}")
            except ValueError as e:
                print(f"Error for {trader.name}: {e}")
        
        print()  # New line for better readability

    # Collect final balances
    for trader in traders:
        final_balances[trader.name] = trader.balance
    
    return final_balances

# Example usage
if __name__ == "__main__":
    # Create traders
    traders = [
        Trader(name="Alice", account_type="Standard", balance=1000.0),
        Trader(name="Bob", account_type="Pro", balance=1500.0),
        Trader(name="Charlie", account_type="Standard", balance=800.0)
    ]
    
    # Simulate trading challenge
    try:
        final_results = simulate_trading_challenge(traders, rounds=5, risk_factor=0.6)
        print("Final Balances:", final_results)
    except ValueError as e:
        print(f"Simulation error: {e}")
```
