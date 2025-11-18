"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capinvest.ltd
Prompt: Create a script to simulate risk minimization strategies described by CAPINVEST LTD, including diversification and balancing short-term and long-term investments.
Generated: DETERMINISTIC_c82b89114ca9bcf5
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class InvestmentPortfolio:
    def __init__(self):
        """Initializes an empty investment portfolio."""
        self.investments = []
        self.weights = []

    def add_investment(self, name, expected_return, risk, weight):
        """
        Adds an investment to the portfolio.

        Parameters:
            name (str): Name of the investment.
            expected_return (float): Expected return of the investment.
            risk (float): Risk associated with the investment (standard deviation).
            weight (float): Proportion of the total portfolio to allocate to this investment.
        """
        if weight < 0 or weight > 1:
            raise ValueError("Weight must be between 0 and 1.")
        if len(self.investments) > 0 and abs(sum(self.weights) + weight - 1) > 1e-6:
            raise ValueError("Total weights must sum to 1.")

        self.investments.append({
            'name': name,
            'expected_return': expected_return,
            'risk': risk
        })
        self.weights.append(weight)

    def portfolio_return(self):
        """Calculates the expected portfolio return."""
        return sum(w * inv['expected_return'] for w, inv in zip(self.weights, self.investments))

    def portfolio_risk(self):
        """Calculates the portfolio risk using variance-covariance approach."""
        covariance_matrix = np.zeros((len(self.investments), len(self.investments)))

        for i in range(len(self.investments)):
            for j in range(len(self.investments)):
                covariance_matrix[i, j] = self.investments[i]['risk'] * self.investments[j]['risk'] * random.uniform(0.5, 1.0)

        portfolio_variance = np.dot(self.weights, np.dot(covariance_matrix, self.weights))
        return np.sqrt(portfolio_variance)

    def optimal_allocation(self):
        """
        Suggests an optimal allocation of investments based on maximizing return while minimizing risk.
        This is a simple heuristic and should be replaced with a more sophisticated algorithm in production.
        """
        returns = np.array([inv['expected_return'] for inv in self.investments])
        risks = np.array([inv['risk'] for inv in self.investments])

        # Normalize weights based on risk
        self.weights = risks / risks.sum()
        return self.weights

def simulate_investments():
    """Simulates a set of investments and demonstrates the portfolio management."""
    # Create an investment portfolio instance
    portfolio = InvestmentPortfolio()

    # Sample investments
    investments_data = [
        ("Stock A", 0.10, 0.15, 0.4),
        ("Bond B", 0.05, 0.02, 0.2),
        ("Real Estate C", 0.07, 0.1, 0.3),
        ("Commodities D", 0.08, 0.12, 0.1)
    ]

    # Adding investments to the portfolio
    for name, expected_return, risk, weight in investments_data:
        try:
            portfolio.add_investment(name, expected_return, risk, weight)
        except ValueError as e:
            print(f"Error adding investment: {e}")

    print("Optimal Portfolio Return: {:.2f}%".format(portfolio.portfolio_return() * 100))
    print("Optimal Portfolio Risk: {:.2f}%".format(portfolio.portfolio_risk() * 100))

    # Calculate optimal allocation
    optimal_weights = portfolio.optimal_allocation()
    print("Optimal Weights: ", optimal_weights)

    # Plotting the investment distribution
    labels = [inv['name'] for inv in portfolio.investments]
    sizes = [w * 100 for w in optimal_weights]

    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is a circle.
    plt.title('Investment Portfolio Allocation')
    plt.show()

if __name__ == "__main__":
    simulate_investments()
```
