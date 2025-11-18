"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nansenportfolio.app
Prompt: Create a script to model private equity investment strategies, focusing on optimal timing, pricing, and risk aversion as detailed by Grade World Investment Limited.
Generated: DETERMINISTIC_faebbab42886d40d
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
from scipy.optimize import minimize


class PrivateEquityModel:
    """
    A class to model private equity investment strategies focusing on optimal timing,
    pricing, and risk aversion.

    Attributes:
        risk_tolerance (float): The investor's risk tolerance (0 to 1).
        initial_capital (float): The initial amount of capital available for investment.
    """

    def __init__(self, risk_tolerance: float, initial_capital: float):
        """
        Initialize the private equity investment model.

        Args:
            risk_tolerance (float): Risk tolerance level between 0 and 1.
            initial_capital (float): Initial capital in dollars.
        """
        self.risk_tolerance = risk_tolerance
        self.initial_capital = initial_capital

    def simulate_market_conditions(self, num_periods: int = 50) -> pd.DataFrame:
        """
        Simulates market conditions for a given number of periods.

        Args:
            num_periods (int): Number of periods to simulate (default is 50).

        Returns:
            pd.DataFrame: Simulated market conditions with columns for 'period', 'price', and 'risk'.
        """
        np.random.seed(42)  # For reproducible results

        # Randomly simulate price and risk conditions
        price = np.random.uniform(50, 500, num_periods)
        risk = np.random.uniform(0.1, 1.0, num_periods)

        # Create a DataFrame to hold simulated data
        market_conditions = pd.DataFrame({
            'period': range(1, num_periods + 1),
            'price': price,
            'risk': risk
        })

        return market_conditions

    def objective_function(self, decision_variables: np.ndarray, market_conditions: pd.DataFrame) -> float:
        """
        Objective function for optimization. Minimizes the weighted cost of investment,
        factoring in price, risk, and investor's risk tolerance.

        Args:
            decision_variables (np.ndarray): Decision variables (investment proportions per period).
            market_conditions (pd.DataFrame): Simulated market conditions.

        Returns:
            float: The total cost of investment.
        """
        # Extract price and risk data
        prices = market_conditions['price'].values
        risks = market_conditions['risk'].values

        # Calculate weighted cost (price + risk penalty based on risk tolerance)
        weighted_cost = np.sum(decision_variables * (prices + risks * (1 - self.risk_tolerance)))

        return weighted_cost

    def optimize_investment(self, market_conditions: pd.DataFrame) -> np.ndarray:
        """
        Optimizes the investment strategy based on market conditions.

        Args:
            market_conditions (pd.DataFrame): Simulated market conditions.

        Returns:
            np.ndarray: Optimal investment proportions per period.
        """
        num_periods = len(market_conditions)

        # Initial guess for decision variables (equal investment in each period)
        initial_guess = np.ones(num_periods) / num_periods

        # Bounds for decision variables (investment proportions must be between 0 and 1)
        bounds = [(0, 1) for _ in range(num_periods)]

        # Constraint: Total proportion of investment should equal 1
        constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}

        # Perform optimization
        result = minimize(
            fun=self.objective_function,
            x0=initial_guess,
            args=(market_conditions,),
            bounds=bounds,
            constraints=constraints,
            method='SLSQP'
        )

        # Check for optimization success
        if not result.success:
            raise ValueError("Optimization failed: " + result.message)

        return result.x

    def simulate_strategy(self, num_periods: int = 50) -> pd.DataFrame:
        """
        Simulate the private equity investment strategy and generate results.

        Args:
            num_periods (int): Number of periods to simulate (default is 50).

        Returns:
            pd.DataFrame: Final DataFrame containing periods, prices, risks,
                          and optimal investment proportions.
        """
        # Simulate market conditions
        market_conditions = self.simulate_market_conditions(num_periods)

        # Compute optimal investment proportions
        optimal_investment = self.optimize_investment(market_conditions)

        # Add optimal investment proportions to the market conditions DataFrame
        market_conditions['optimal_investment'] = optimal_investment

        return market_conditions


if __name__ == "__main__":
    # Define parameters for the model
    risk_tolerance = 0.7  # Investor's risk tolerance (0.7 indicates moderate risk tolerance)
    initial_capital = 1_000_000  # Initial capital in dollars

    # Initialize model
    model = PrivateEquityModel(risk_tolerance, initial_capital)

    # Generate strategy for a simulated market
    num_periods = 50  # Number of periods to simulate
    strategy_results = model.simulate_strategy(num_periods)

    # Print results
    print(strategy_results)
```
