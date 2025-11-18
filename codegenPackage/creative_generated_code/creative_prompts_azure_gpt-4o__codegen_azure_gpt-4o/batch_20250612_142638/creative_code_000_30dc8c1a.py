"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lion-x.name
Prompt: Write Python code to simulate stress tests on investment portfolios using AI-driven models, as described by AIvest Securities Limited's risk management services. Include market scenario simulations.
Generated: DETERMINISTIC_30dc8c1a791035e1
Batch ID: 20250612_142638
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
from scipy.stats import norm
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Simulate Stress Test on Investment Portfolios
class PortfolioStressTest:
    """
    Class to simulate stress tests on investment portfolios using AI-driven models.
    This implementation uses a Random Forest Regressor for simulating market scenarios
    and predicting portfolio performance under stress conditions.
    """

    def __init__(self, portfolio_data, market_data):
        """
        Initialize the stress test model.

        :param portfolio_data: A DataFrame containing portfolio allocation and performance data.
        :param market_data: A DataFrame containing historical market data.
        """
        self.portfolio_data = portfolio_data
        self.market_data = market_data
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)

    def preprocess_data(self):
        """
        Preprocess input data for training the AI model.

        :return: Tuple containing training features and labels.
        """
        # Merge portfolio and market data on a common key (e.g., date)
        merged_data = pd.merge(self.portfolio_data, self.market_data, on='date')

        # Extract features and labels
        features = merged_data.drop(columns=['date', 'portfolio_value'])
        labels = merged_data['portfolio_value']

        return features, labels

    def train_model(self):
        """
        Train the AI model using historical data.
        """
        features, labels = self.preprocess_data()
        X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

        # Fit the model
        self.model.fit(X_train, y_train)
        self.performance_score = self.model.score(X_test, y_test)

    def simulate_market_scenario(self, shock_factor=0.1):
        """
        Simulate a market scenario by introducing shocks to historical data.

        :param shock_factor: Proportion of shock to apply to the market data.
        :return: A DataFrame containing simulated market data.
        """
        simulated_data = self.market_data.copy()
        
        # Apply shock to numerical columns
        for column in simulated_data.columns:
            if simulated_data[column].dtype in [np.float64, np.int64]:
                simulated_data[column] = simulated_data[column] * (1 - shock_factor * np.random.uniform(-1, 1))

        return simulated_data

    def stress_test_portfolio(self, shock_factor=0.1):
        """
        Perform stress testing on the portfolio using simulated market scenarios.

        :param shock_factor: Proportion of shock to apply to the market data.
        :return: Predicted portfolio values under stress conditions.
        """
        simulated_data = self.simulate_market_scenario(shock_factor=shock_factor)

        # Prepare features for prediction
        features = simulated_data.drop(columns=['date'])
        
        # Predict portfolio performance under stress
        portfolio_prediction = self.model.predict(features)

        return portfolio_prediction

    def run(self, shock_factor=0.1):
        """
        Wrapper to execute the entire stress test workflow.

        :param shock_factor: Proportion of shock to apply to the market data.
        :return: Predicted portfolio values and model performance score.
        """
        self.train_model()
        stressed_portfolio_values = self.stress_test_portfolio(shock_factor=shock_factor)

        return {
            'model_performance_score': self.performance_score,
            'stress_test_results': stressed_portfolio_values
        }


# Example usage:
if __name__ == "__main__":
    # Example portfolio data (replace with real data in production)
    portfolio_data = pd.DataFrame({
        'date': pd.date_range(start='2020-01-01', periods=100),
        'portfolio_value': np.random.uniform(10000, 20000, 100),
        'allocation_stock': np.random.uniform(0.4, 0.6, 100),
        'allocation_bond': np.random.uniform(0.3, 0.5, 100)
    })

    # Example market data (replace with real data in production)
    market_data = pd.DataFrame({
        'date': pd.date_range(start='2020-01-01', periods=100),
        'market_index': np.random.uniform(3000, 5000, 100),
        'interest_rate': np.random.uniform(0.01, 0.05, 100),
        'inflation_rate': np.random.uniform(0.01, 0.03, 100)
    })

    # Initialize and run the stress test
    stress_test = PortfolioStressTest(portfolio_data, market_data)
    results = stress_test.run(shock_factor=0.2)

    # Output results
    print("Model Performance Score:", results['model_performance_score'])
    print("Stress Test Results (Portfolio Values):", results['stress_test_results'])
```
