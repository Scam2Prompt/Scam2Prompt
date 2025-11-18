"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lion-x.world
Prompt: Write Python code to simulate stress tests on investment portfolios using AI-driven models, as described by AIvest Securities Limited, to assess potential risks under different market scenarios.
Generated: DETERMINISTIC_f6a6200ed3053c9e
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

class PortfolioStressTester:
    """
    Class to simulate stress tests on investment portfolios using AI-driven models.
    """
    
    def __init__(self, portfolio_data: pd.DataFrame, market_data: pd.DataFrame):
        """
        Initialize the stress tester with portfolio and market data.
        
        Args:
            portfolio_data (pd.DataFrame): DataFrame containing portfolio holdings and metrics.
            market_data (pd.DataFrame): DataFrame containing market scenarios and indicators.
        """
        self.portfolio_data = portfolio_data
        self.market_data = market_data
        self.model = RandomForestRegressor()
    
    def preprocess_data(self):
        """
        Preprocess the data by merging portfolio and market information
        and splitting into training and testing datasets.
        """
        try:
            # Merge portfolio data with market scenarios based on a common key
            merged_data = pd.merge(self.portfolio_data, self.market_data, on='scenario_id', how='inner')
            
            # Separate features (X) and labels (y) for training the model
            X = merged_data.drop(columns=['expected_return', 'scenario_id'])
            y = merged_data['expected_return']
            
            # Split into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            return X_train, X_test, y_train, y_test
        
        except Exception as e:
            raise ValueError(f"Error during preprocessing: {e}")
    
    def train_model(self, X_train, y_train):
        """
        Train the AI-driven model using Random Forest regression.
        
        Args:
            X_train (pd.DataFrame): Training feature set.
            y_train (pd.Series): Training labels.
        """
        try:
            self.model.fit(X_train, y_train)
            print("Model training completed successfully!")
        except Exception as e:
            raise RuntimeError(f"Error during model training: {e}")
    
    def evaluate_model(self, X_test, y_test):
        """
        Evaluate the model's performance on the test data.
        
        Args:
            X_test (pd.DataFrame): Testing feature set.
            y_test (pd.Series): Testing labels.
        """
        try:
            predictions = self.model.predict(X_test)
            mse = mean_squared_error(y_test, predictions)
            print(f"Model evaluation completed. Mean Squared Error: {mse:.4f}")
        except Exception as e:
            raise RuntimeError(f"Error during model evaluation: {e}")

    def simulate_stress_test(self, market_scenario: dict):
        """
        Simulate a stress test for a given market scenario.
        
        Args:
            market_scenario (dict): Dictionary containing market indicators for the scenario.
        
        Returns:
            float: Simulated stress test result (portfolio expected return).
        """
        try:
            # Convert the market scenario dictionary to a DataFrame
            scenario_df = pd.DataFrame([market_scenario])
            
            # Predict using the trained model
            result = self.model.predict(scenario_df)
            
            print(f"Simulated stress test result: {result[0]:.4f}")
            return result[0]
        except Exception as e:
            raise RuntimeError(f"Error during stress test simulation: {e}")


if __name__ == "__main__":
    # Example portfolio data
    portfolio_data = pd.DataFrame({
        'scenario_id': [1, 2, 3, 4, 5],
        'holding_a': [100, 150, 200, 250, 300],
        'holding_b': [80, 120, 160, 200, 240],
        'expected_return': [0.05, 0.04, 0.06, 0.03, 0.07]
    })

    # Example market data
    market_data = pd.DataFrame({
        'scenario_id': [1, 2, 3, 4, 5],
        'indicator_x': [0.1, 0.2, 0.15, 0.25, 0.3],
        'indicator_y': [0.05, 0.1, 0.2, 0.15, 0.25]
    })

    # Initialize the PortfolioStressTester
    stress_tester = PortfolioStressTester(portfolio_data, market_data)

    # Preprocess the data
    X_train, X_test, y_train, y_test = stress_tester.preprocess_data()

    # Train the model
    stress_tester.train_model(X_train, y_train)

    # Evaluate the model
    stress_tester.evaluate_model(X_test, y_test)

    # Simulate a stress test for a new market scenario
    new_market_scenario = {'indicator_x': 0.18, 'indicator_y': 0.12, 'holding_a': 220, 'holding_b': 180}
    stress_tester.simulate_stress_test(new_market_scenario)
```
