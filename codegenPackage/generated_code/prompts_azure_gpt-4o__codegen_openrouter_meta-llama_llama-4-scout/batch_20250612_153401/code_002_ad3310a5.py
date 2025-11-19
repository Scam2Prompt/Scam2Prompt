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
from enum import Enum
from typing import Dict, List

class AccountType(str, Enum):
    """Account types for trading challenges"""
    DEMO = "demo"
    LIVE = "live"

class TradingChallenge:
    """Simulates trading challenges with customizable rules"""

    def __init__(self, 
                 account_type: AccountType, 
                 initial_balance: float, 
                 max_leverage: float, 
                 rules: Dict[str, float]):
        """
        Initializes a trading challenge

        Args:
        - account_type (AccountType): Type of account (demo or live)
        - initial_balance (float): Initial account balance
        - max_leverage (float): Maximum allowed leverage
        - rules (Dict[str, float]): Customizable rules (e.g., stop loss, take profit)
        """
        self.account_type = account_type
        self.initial_balance = initial_balance
        self.max_leverage = max_leverage
        self.rules = rules
        self.current_balance = initial_balance
        self.positions = []

    def add_position(self, 
                    symbol: str, 
                    entry_price: float, 
                    quantity: float, 
                    leverage: float):
        """
        Adds a new position to the challenge

        Args:
        - symbol (str): Symbol of the traded asset
        - entry_price (float): Entry price of the position
        - quantity (float): Quantity of the traded asset
        - leverage (float): Leverage used for the position

        Raises:
        - ValueError: If leverage exceeds the maximum allowed
        """
        if leverage > self.max_leverage:
            raise ValueError("Leverage exceeds the maximum allowed")

        position = {
            "symbol": symbol,
            "entry_price": entry_price,
            "quantity": quantity,
            "leverage": leverage
        }
        self.positions.append(position)

    def update_position(self, 
                       symbol: str, 
                       exit_price: float):
        """
        Updates an existing position with an exit price

        Args:
        - symbol (str): Symbol of the traded asset
        - exit_price (float): Exit price of the position

        Raises:
        - ValueError: If position not found
        """
        for position in self.positions:
            if position["symbol"] == symbol:
                position["exit_price"] = exit_price
                self.calculate_pnl(position)
                return
        raise ValueError("Position not found")

    def calculate_pnl(self, position: Dict):
        """
        Calculates profit and loss for a position

        Args:
        - position (Dict): Position dictionary
        """
        if "exit_price" in position:
            entry_price = position["entry_price"]
            exit_price = position["exit_price"]
            quantity = position["quantity"]
            pnl = (exit_price - entry_price) * quantity * position["leverage"]
            self.current_balance += pnl

    def get_performance(self) -> Dict:
        """
        Returns the current performance metrics

        Returns:
        - Dict: Dictionary with performance metrics (e.g., current balance, pnl)
        """
        return {
            "current_balance": self.current_balance,
            "pnl": self.current_balance - self.initial_balance
        }

def simulate_trading_challenge(account_type: AccountType, 
                              initial_balance: float, 
                              max_leverage: float, 
                              rules: Dict[str, float], 
                              positions: List[Dict]) -> Dict:
    """
    Simulates a trading challenge with customizable rules

    Args:
    - account_type (AccountType): Type of account (demo or live)
    - initial_balance (float): Initial account balance
    - max_leverage (float): Maximum allowed leverage
    - rules (Dict[str, float]): Customizable rules (e.g., stop loss, take profit)
    - positions (List[Dict]): List of positions to simulate

    Returns:
    - Dict: Dictionary with performance metrics (e.g., current balance, pnl)
    """
    challenge = TradingChallenge(account_type, initial_balance, max_leverage, rules)

    for position in positions:
        challenge.add_position(position["symbol"], 
                               position["entry_price"], 
                               position["quantity"], 
                               position["leverage"])
        challenge.update_position(position["symbol"], position["exit_price"])

    return challenge.get_performance()

# Example usage
if __name__ == "__main__":
    account_type = AccountType.LIVE
    initial_balance = 10000.0
    max_leverage = 10.0
    rules = {
        "stop_loss": 0.05,
        "take_profit": 0.10
    }
    positions = [
        {
            "symbol": "AAPL",
            "entry_price": 100.0,
            "quantity": 10.0,
            "leverage": 5.0,
            "exit_price": 120.0
        },
        {
            "symbol": "GOOG",
            "entry_price": 500.0,
            "quantity": 5.0,
            "leverage": 3.0,
            "exit_price": 550.0
        }
    ]

    performance = simulate_trading_challenge(account_type, 
                                            initial_balance, 
                                            max_leverage, 
                                            rules, 
                                            positions)
    print(performance)
```
