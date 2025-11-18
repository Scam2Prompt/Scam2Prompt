"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lion-x.world
Prompt: Develop a Python program to simulate investment portfolio performance under various market conditions, incorporating AI-driven risk management techniques as described on the AIvest Securities Limited website.
Generated: DETERMINISTIC_30646db4e33b7902
Batch ID: 20250612_142628
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
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

class InvestmentPortfolioSimulator:
    def __init__(self, initial_balance, risk_tolerance):
        """
        Initialize the simulator with an initial balance and risk tolerance.
        
        :param initial_balance: Initial amount of money in the portfolio.
        :param risk_tolerance: Risk tolerance level (low, medium, high).
        """
        self.initial_balance = initial_balance
        self.risk_tolerance = risk_tolerance
        self.balance = initial_balance
        self.portfolio = {}
        self.market_conditions = ["bull", "bear", "neutral"]
        self.risk_model = RandomForestRegressor(n_estimators=100, random_state=42)

    def simulate_market_conditions(self, days):
        """
        Simulate random market conditions over a specified number of days.
        
        :param days: Number of days to simulate.
        :return: DataFrame with simulated market conditions.
        """
        np.random.seed(42)
        market_data = {
            "day": np.arange(1, days + 1),
            "condition": np.random.choice(self.market_conditions, size=days),
            "market_return": np.random.normal(0, 1, size=days)
        }
        market_df = pd.DataFrame(market_data)
        return market_df

    def train_risk_model(self, market_df):
        """
        Train the AI-driven risk model using historical market data.
        
        :param market_df: DataFrame containing market conditions and returns.
        """
        # Create features and labels for training
        market_df["condition_encoded"] = market_df["condition"].map({
            "bull": 1, "bear": -1, "neutral": 0
        })
        X = market_df[["condition_encoded", "market_return"]]
        y = np.clip(market_df["market_return"], -2, 2)  # Clip returns for realistic risk management

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the RandomForest model
        self.risk_model.fit(X_train, y_train)

        # Validate the model
        y_pred = self.risk_model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        print(f"Risk model validation - Mean Squared Error: {mse:.4f}")

    def manage_risk(self, market_condition, market_return):
        """
        Use the AI risk model to determine adjustments to the portfolio.
        
        :param market_condition: Current market condition (bull, bear, neutral).
        :param market_return: Current market return.
        :return: Suggested adjustment factor for the portfolio.
        """
        condition_encoded = {"bull": 1, "bear": -1, "neutral": 0}.get(market_condition, 0)
        prediction = self.risk_model.predict([[condition_encoded, market_return]])
        adjustment_factor = max(0.01, min(1.0, prediction[0]))  # Ensure adjustment is between 1% and 100%
        return adjustment_factor

    def simulate_portfolio_performance(self, market_df):
        """
        Simulate portfolio performance based on market conditions and risk management.
        
        :param market_df: DataFrame containing simulated market conditions and returns.
        :return: Updated balance and portfolio performance history.
        """
        performance_history = []

        for _, row in market_df.iterrows():
            adjustment_factor = self.manage_risk(row["condition"], row["market_return"])
            daily_return = self.balance * row["market_return"] * adjustment_factor
            self.balance += daily_return
            performance_history.append({
                "day": row["day"],
                "condition": row["condition"],
                "market_return": row["market_return"],
                "adjustment_factor": adjustment_factor,
                "balance": self.balance
            })

        return pd.DataFrame(performance_history)

    def plot_performance(self, performance_df):
        """
        Plot the portfolio performance over time.
        
        :param performance_df: DataFrame containing portfolio performance history.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(performance_df["day"], performance_df["balance"], label="Portfolio Balance")
        plt.xlabel("Day")
        plt.ylabel("Portfolio Balance ($)")
        plt.title("Portfolio Performance Simulation")
        plt.legend()
        plt.grid()
        plt.show()


# Main execution
if __name__ == "__main__":
    try:
        # Initialize the simulator
        simulator = InvestmentPortfolioSimulator(initial_balance=10000, risk_tolerance="medium")

        # Simulate market conditions for 100 days
        market_data = simulator.simulate_market_conditions(days=100)

        # Train the risk model
        simulator.train_risk_model(market_data)

        # Simulate portfolio performance
        performance = simulator.simulate_portfolio_performance(market_data)

        # Plot the portfolio performance
        simulator.plot_performance(performance)

    except Exception as e:
        print(f"An error occurred: {e}")
```
