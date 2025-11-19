"""
Generated Code Metadata:
========================
Original URL: https://maximuslimited.com
Prompt: Create a program to model capital investment strategies for raising funds in new markets, referencing Maximus Limited’s consultancy services.
Generated: DETERMINISTIC_da83fb1726866080
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# capital_investment_strategy.py

class InvestmentStrategy:
    """
    Base class for capital investment strategies.
    """

    def __init__(self, investment_amount, market_growth_rate):
        """
        Initializes an investment strategy.

        Args:
            investment_amount (float): The initial investment amount.
            market_growth_rate (float): The expected market growth rate.
        """
        self.investment_amount = investment_amount
        self.market_growth_rate = market_growth_rate

    def calculate_returns(self):
        """
        Calculates the returns on investment.

        Returns:
            float: The returns on investment.
        """
        raise NotImplementedError("Subclass must implement abstract method")


class ConservativeInvestmentStrategy(InvestmentStrategy):
    """
    Conservative investment strategy with low risk.
    """

    def __init__(self, investment_amount, market_growth_rate, risk_factor=0.05):
        """
        Initializes a conservative investment strategy.

        Args:
            investment_amount (float): The initial investment amount.
            market_growth_rate (float): The expected market growth rate.
            risk_factor (float, optional): The risk factor. Defaults to 0.05.
        """
        super().__init__(investment_amount, market_growth_rate)
        self.risk_factor = risk_factor

    def calculate_returns(self):
        """
        Calculates the returns on investment for a conservative strategy.

        Returns:
            float: The returns on investment.
        """
        return self.investment_amount * (1 + self.market_growth_rate - self.risk_factor)


class AggressiveInvestmentStrategy(InvestmentStrategy):
    """
    Aggressive investment strategy with high risk.
    """

    def __init__(self, investment_amount, market_growth_rate, risk_factor=0.1):
        """
        Initializes an aggressive investment strategy.

        Args:
            investment_amount (float): The initial investment amount.
            market_growth_rate (float): The expected market growth rate.
            risk_factor (float, optional): The risk factor. Defaults to 0.1.
        """
        super().__init__(investment_amount, market_growth_rate)
        self.risk_factor = risk_factor

    def calculate_returns(self):
        """
        Calculates the returns on investment for an aggressive strategy.

        Returns:
            float: The returns on investment.
        """
        return self.investment_amount * (1 + self.market_growth_rate + self.risk_factor)


class MaximusLimitedConsultancy:
    """
    Maximus Limited consultancy services.
    """

    def __init__(self):
        """
        Initializes the consultancy services.
        """
        self.investment_strategies = {}

    def add_investment_strategy(self, strategy_name, investment_strategy):
        """
        Adds an investment strategy.

        Args:
            strategy_name (str): The name of the investment strategy.
            investment_strategy (InvestmentStrategy): The investment strategy.
        """
        self.investment_strategies[strategy_name] = investment_strategy

    def get_investment_strategy(self, strategy_name):
        """
        Gets an investment strategy.

        Args:
            strategy_name (str): The name of the investment strategy.

        Returns:
            InvestmentStrategy: The investment strategy.

        Raises:
            ValueError: If the strategy name is not found.
        """
        try:
            return self.investment_strategies[strategy_name]
        except KeyError:
            raise ValueError("Strategy name not found")


def main():
    # Create consultancy services
    consultancy = MaximusLimitedConsultancy()

    # Create investment strategies
    conservative_strategy = ConservativeInvestmentStrategy(100000, 0.05)
    aggressive_strategy = AggressiveInvestmentStrategy(100000, 0.05)

    # Add investment strategies to consultancy services
    consultancy.add_investment_strategy("conservative", conservative_strategy)
    consultancy.add_investment_strategy("aggressive", aggressive_strategy)

    # Get investment strategies
    strategy = consultancy.get_investment_strategy("conservative")
    print(f"Conservative strategy returns: {strategy.calculate_returns()}")

    strategy = consultancy.get_investment_strategy("aggressive")
    print(f"Aggressive strategy returns: {strategy.calculate_returns()}")

    # Test error handling
    try:
        consultancy.get_investment_strategy("non-existent")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
