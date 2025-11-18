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
import matplotlib.pyplot as plt
from scipy.optimize import minimize

class PrivateEquityInvestmentModel:
    def __init__(self, investment_data, risk_aversion_coefficient):
        """
        Initializes the PrivateEquityInvestmentModel with investment data and risk aversion coefficient.
        
        :param investment_data: DataFrame containing historical investment data with 'price', 'timing', 'risk' columns
        :param risk_aversion_coefficient: float representing the investor's risk aversion
        """
        self.investment_data = investment_data
        self.risk_aversion_coefficient = risk_aversion_coefficient

    def calculate_return(self, weights):
        """
        Calculate the expected return based on asset weights.
        
        :param weights: list of weights assigned to each investment
        :return: expected return of the portfolio
        """
        return np.dot(weights, self.investment_data['price'].values)

    def calculate_risk(self, weights):
        """
        Calculate the portfolio risk based on asset weights.
        
        :param weights: list of weights assigned to each investment
        :return: risk of the portfolio
        """
        return np.dot(weights, self.investment_data['risk'].values)

    def objective_function(self, weights):
        """
        Objective function to minimize, balancing return and risk.
        
        :param weights: list of weights assigned to each investment
        :return: negative of the utility function
        """
        expected_return = self.calculate_return(weights)
        portfolio_risk = self.calculate_risk(weights)
        return - (expected_return - self.risk_aversion_coefficient * portfolio_risk)

    def optimize_investment_strategy(self):
        """
        Optimize the investment strategy by finding the best weight distribution.

        :return: optimized weights
        """
        num_investments = len(self.investment_data)
        initial_weights = np.array([1.0 / num_investments] * num_investments)
        bounds = tuple((0, 1) for _ in range(num_investments))
        constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}

        # Minimize the objective function
        result = minimize(self.objective_function, initial_weights, bounds=bounds, constraints=constraints)

        if result.success:
            return result.x
        else:
            raise ValueError("Optimization failed: " + result.message)

    def plot_investment_strategy(self, optimized_weights):
        """
        Plot the optimized investment strategy.

        :param optimized_weights: list of optimized weights assigned to each investment
        """
        plt.figure(figsize=(10, 6))
        investments = self.investment_data.index
        plt.bar(investments, optimized_weights, color='blue', alpha=0.7)
        plt.title('Optimized Investment Strategy')
        plt.xlabel('Investments')
        plt.ylabel('Weights')
        plt.xticks(investments)
        plt.grid(axis='y')
        plt.show()

if __name__ == "__main__":
    # Example investment data
    investment_data = pd.DataFrame({
        'price': [100, 200, 150, 300],
        'timing': [1, 2, 3, 4],  # Placeholder, not used in calculations
        'risk': [0.1, 0.2, 0.15, 0.3]
    })

    risk_aversion_coefficient = 0.5

    # Instantiate the model
    model = PrivateEquityInvestmentModel(investment_data, risk_aversion_coefficient)

    try:
        # Optimize the investment strategy
        optimized_weights = model.optimize_investment_strategy()

        # Plot the optimized investment strategy
        model.plot_investment_strategy(optimized_weights)

    except Exception as e:
        print(f"An error occurred: {e}")
```
