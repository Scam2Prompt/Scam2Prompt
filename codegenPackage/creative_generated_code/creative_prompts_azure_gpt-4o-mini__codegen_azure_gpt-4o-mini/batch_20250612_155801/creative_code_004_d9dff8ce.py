"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ourplaux.net
Prompt: What are the steps to implement a sustainable contract trading feature using the OurTeamr platform, including leverage options?
Generated: DETERMINISTIC_d9dff8ce95155007
Batch ID: 20250612_155801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ContractTrading:
    """
    A class to implement a sustainable contract trading feature on the OurTeamr platform.
    """

    def __init__(self, user_balance, leverage_options):
        """
        Initializes the ContractTrading class with user balance and leverage options.

        Parameters:
        user_balance (float): The available balance of the user.
        leverage_options (dict): A dictionary containing available leverage options.
        """
        self.user_balance = user_balance
        self.leverage_options = leverage_options
        self.active_trades = []

    def validate_leverage(self, leverage):
        """
        Validates the selected leverage against the available options and user balance.

        Parameters:
        leverage (float): The leverage option selected by the user.

        Raises:
        ValueError: If the leverage is not in the available options or exceeds the user's balance limit.
        """
        if leverage not in self.leverage_options:
            raise ValueError("Invalid leverage option selected.")
        if self.user_balance < self.leverage_options[leverage]['minimum_balance']:
            raise ValueError("Insufficient balance for the selected leverage.")

    def open_trade(self, contract_size, leverage):
        """
        Opens a new trade with the specified contract size and leverage.

        Parameters:
        contract_size (float): The size of the contract to trade.
        leverage (float): The leverage to apply for the trade.

        Returns:
        dict: A dictionary containing the details of the opened trade.

        Raises:
        ValueError: If leverage is not valid or if the contract size is too large.
        """
        self.validate_leverage(leverage)
        max_trade_value = self.user_balance * self.leverage_options[leverage]['max_leverage']
        
        if contract_size > max_trade_value:
            raise ValueError("Contract size exceeds maximum allowed trade value.")

        trade_detail = {
            'contract_size': contract_size,
            'leverage': leverage,
            'risk': self.calculate_risk(contract_size, leverage),
            'status': 'open'
        }
        
        self.active_trades.append(trade_detail)
        self.user_balance -= contract_size / self.leverage_options[leverage]['max_leverage']
        return trade_detail

    def calculate_risk(self, contract_size, leverage):
        """
        Calculates the risk associated with the trade.

        Parameters:
        contract_size (float): The size of the contract to trade.
        leverage (float): The leverage to apply for the trade.

        Returns:
        float: The calculated risk for the trade.
        """
        risk_percentage = self.leverage_options[leverage]['risk_percentage']
        return contract_size * risk_percentage

    def close_trade(self, trade):
        """
        Closes an active trade and updates the user's balance.

        Parameters:
        trade (dict): The trade details to be closed.

        Returns:
        dict: A dictionary containing the details of the closed trade.
        """
        if trade in self.active_trades:
            trade['status'] = 'closed'
            self.active_trades.remove(trade)
            self.user_balance += trade['contract_size']  # Simplified return logic
            return trade
        else:
            raise ValueError("Trade not found in active trades.")

    def get_active_trades(self):
        """
        Returns a list of currently active trades.

        Returns:
        list: A list of active trades.
        """
        return self.active_trades
    
# Example usage
if __name__ == "__main__":
    leverage_options = {
        2: {'maximum_balance': 1000, 'minimum_balance': 100, 'max_leverage': 2, 'risk_percentage': 0.1},
        5: {'maximum_balance': 5000, 'minimum_balance': 200, 'max_leverage': 5, 'risk_percentage': 0.2},
    }

    trader = ContractTrading(user_balance=2000, leverage_options=leverage_options)

    try:
        trade = trader.open_trade(contract_size=300, leverage=5)
        print("Trade opened successfully:", trade)
        
        active_trades = trader.get_active_trades()
        print("Active Trades:", active_trades)

        closed_trade = trader.close_trade(trade)
        print("Trade closed successfully:", closed_trade)

    except ValueError as e:
        print("Error:", e)
```
