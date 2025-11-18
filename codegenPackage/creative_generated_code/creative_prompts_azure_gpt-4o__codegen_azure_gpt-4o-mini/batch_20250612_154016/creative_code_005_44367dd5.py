"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fun-virtuals-agent.pages.dev
Prompt: Develop a function to calculate trading fees and agent creation fees for a blockchain-based platform, using the fee structure described on the Fun Virtuals Agent webpage.
Generated: DETERMINISTIC_44367dd54a527a74
Batch ID: 20250612_154016
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TradingFeeCalculator:
    """
    A class to calculate trading fees and agent creation fees for a blockchain-based platform.
    The fee structure is based on the guidelines provided by the Fun Virtuals Agent webpage.
    """

    def __init__(self, base_fee, agent_creation_fee):
        """
        Initializes the TradingFeeCalculator with base and agent creation fees.

        Args:
            base_fee (float): The fixed fee for each transaction.
            agent_creation_fee (float): The fee for creating a new agent.
        """
        if base_fee < 0 or agent_creation_fee < 0:
            raise ValueError("Fees must be non-negative values.")
        
        self.base_fee = base_fee
        self.agent_creation_fee = agent_creation_fee

    def calculate_trading_fee(self, transaction_amount):
        """
        Calculates the trading fee based on the transaction amount.

        Args:
            transaction_amount (float): The amount of the transaction.

        Returns:
            float: The calculated trading fee.

        Raises:
            ValueError: If the transaction amount is negative.
        """
        if transaction_amount < 0:
            raise ValueError("Transaction amount must be a non-negative value.")

        # Assuming the trading fee is a percentage of the transaction amount plus base fee
        trading_fee_percentage = 0.01  # 1% fee
        trading_fee = (transaction_amount * trading_fee_percentage) + self.base_fee
        return trading_fee

    def calculate_agent_creation_fee(self):
        """
        Returns the fixed agent creation fee.

        Returns:
            float: The agent creation fee.
        """
        return self.agent_creation_fee


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the fee calculator with example fees
        calculator = TradingFeeCalculator(base_fee=2.0, agent_creation_fee=50.0)

        # Calculate trading fee for a transaction
        transaction_amount = 1000.0  # Example transaction amount
        trading_fee = calculator.calculate_trading_fee(transaction_amount)
        print(f"Trading Fee for transaction of {transaction_amount}: {trading_fee}")

        # Calculate agent creation fee
        agent_fee = calculator.calculate_agent_creation_fee()
        print(f"Agent Creation Fee: {agent_fee}")

    except ValueError as e:
        print(f"Error: {e}")
```
