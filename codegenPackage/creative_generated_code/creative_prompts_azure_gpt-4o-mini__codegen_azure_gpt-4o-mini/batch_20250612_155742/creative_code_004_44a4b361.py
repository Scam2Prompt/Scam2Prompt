"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fun-virtuals-agent.pages.dev
Prompt: How do I implement the trading fee structure when creating an agent on Fun Virtuals?
Generated: DETERMINISTIC_44a4b361d0b9ebf6
Batch ID: 20250612_155742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TradingAgent:
    """
    A class to represent a trading agent on Fun Virtuals.

    Attributes:
        name (str): The name of the trading agent.
        balance (float): The balance of the agent, initialized to zero.
        trading_fee_percentage (float): The trading fee percentage applied to each transaction.
    """
    
    def __init__(self, name: str, trading_fee_percentage: float):
        """
        Initializes a new TradingAgent instance.

        Args:
            name (str): The name of the trading agent.
            trading_fee_percentage (float): The percentage fee to charge on trades.

        Raises:
            ValueError: If trading_fee_percentage is negative or greater than 100.
        """
        if trading_fee_percentage < 0 or trading_fee_percentage > 100:
            raise ValueError("Trading fee percentage must be between 0 and 100.")
        
        self.name = name
        self.balance = 0.0
        self.trading_fee_percentage = trading_fee_percentage

    def add_balance(self, amount: float):
        """
        Adds an amount to the agent's balance.

        Args:
            amount (float): The amount to add to the balance.

        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount to add must be non-negative.")
        self.balance += amount

    def trade(self, trade_amount: float):
        """
        Executes a trade operation, deducting the trading fee from the agent's balance.

        Args:
            trade_amount (float): The amount to trade.

        Raises:
            ValueError: If trade_amount is negative or exceeds available balance.
        """
        if trade_amount < 0:
            raise ValueError("Trade amount must be non-negative.")
        if trade_amount > self.balance:
            raise ValueError("Insufficient balance for this trade.")
        
        # Calculate trading fee
        trading_fee = (self.trading_fee_percentage / 100) * trade_amount
        total_deduction = trade_amount + trading_fee
        
        # Deduct from balance
        self.balance -= total_deduction
        return trading_fee, total_deduction

    def get_balance(self) -> float:
        """
        Returns the current balance of the trading agent.

        Returns:
            float: The current balance.
        """
        return self.balance

    def __str__(self):
        """
        Returns a string representation of the TradingAgent.

        Returns:
            str: Informal string representation of the TradingAgent.
        """
        return f"TradingAgent(name={self.name}, balance={self.balance:.2f}, trading_fee_percentage={self.trading_fee_percentage})"

# Example usage
if __name__ == "__main__":
    try:
        # Create a trading agent with a 2% trading fee
        agent = TradingAgent("Agent007", 2.0)
        agent.add_balance(1000.0)  # Add balance to agent
        print(agent)  # Display agent details

        # Perform a trade
        fee, total_deduction = agent.trade(100.0)
        print(f"Trade executed! Trading fee: {fee:.2f}, Total deducted: {total_deduction:.2f}")

        # Check the new balance
        print(f"New balance: {agent.get_balance():.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
