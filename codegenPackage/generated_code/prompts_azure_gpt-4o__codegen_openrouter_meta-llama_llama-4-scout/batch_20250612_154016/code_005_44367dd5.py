"""
Generated Code Metadata:
========================
Original URL: https://fun-virtuals-agent.pages.dev
Prompt: Develop a function to calculate trading fees and agent creation fees for a blockchain-based platform, using the fee structure described on the Fun Virtuals Agent webpage.
Generated: DETERMINISTIC_44367dd54a527a74
Batch ID: 20250612_154016
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fee_calculator.py

from enum import Enum
from typing import Dict

class FeeType(Enum):
    """Enum for fee types."""
    TRADING = 1
    AGENT_CREATION = 2

class FeeCalculator:
    """Calculates trading fees and agent creation fees."""

    def __init__(self, fee_structure: Dict[FeeType, float]):
        """
        Initializes the FeeCalculator with a fee structure.

        Args:
        - fee_structure (Dict[FeeType, float]): A dictionary containing fee types and their corresponding rates.
        """
        self.fee_structure = fee_structure

    def calculate_trading_fee(self, trade_amount: float) -> float:
        """
        Calculates the trading fee based on the trade amount.

        Args:
        - trade_amount (float): The amount of the trade.

        Returns:
        - float: The trading fee.

        Raises:
        - ValueError: If the trade amount is negative.
        """
        if trade_amount < 0:
            raise ValueError("Trade amount cannot be negative.")

        trading_fee_rate = self.fee_structure.get(FeeType.TRADING, 0)
        return trade_amount * trading_fee_rate

    def calculate_agent_creation_fee(self, agent_type: str, agent_value: float) -> float:
        """
        Calculates the agent creation fee based on the agent type and value.

        Args:
        - agent_type (str): The type of the agent.
        - agent_value (float): The value of the agent.

        Returns:
        - float: The agent creation fee.

        Raises:
        - ValueError: If the agent value is negative.
        """
        if agent_value < 0:
            raise ValueError("Agent value cannot be negative.")

        agent_creation_fee_rate = self.fee_structure.get(FeeType.AGENT_CREATION, 0)
        return agent_value * agent_creation_fee_rate

def main():
    # Example usage:
    fee_structure = {
        FeeType.TRADING: 0.001,  # 0.1%
        FeeType.AGENT_CREATION: 0.05  # 5%
    }

    calculator = FeeCalculator(fee_structure)

    trade_amount = 1000.0
    trading_fee = calculator.calculate_trading_fee(trade_amount)
    print(f"Trading fee for ${trade_amount:.2f}: ${trading_fee:.2f}")

    agent_type = "Basic"
    agent_value = 100.0
    agent_creation_fee = calculator.calculate_agent_creation_fee(agent_type, agent_value)
    print(f"Agent creation fee for {agent_type} agent worth ${agent_value:.2f}: ${agent_creation_fee:.2f}")

if __name__ == "__main__":
    main()
```
