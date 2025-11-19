"""
Generated Code Metadata:
========================
Original URL: https://lion-x.name
Prompt: Write Python code to simulate stress tests on investment portfolios using AI-driven models, as described by AIvest Securities Limited's risk management services. Include market scenario simulations.
Generated: DETERMINISTIC_30dc8c1a791035e1
Batch ID: 20250612_142638
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from scipy.stats import norm
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import warnings
warnings.filterwarnings('ignore')

class PortfolioStressTester:
    """
    AI-driven portfolio stress testing system that simulates various market scenarios.
    """
    
    def __init__(self, portfolio_data, market_data):
        """
        Initialize the stress tester with portfolio and market data.
        
        Args:
            portfolio_data (pd.DataFrame): Portfolio holdings with columns ['asset', 'quantity', 'price']
            market_data (pd.DataFrame): Historical market data with columns ['date', 'asset', 'return']
        """
        self.portfolio = portfolio_data
        self.market_data = market_data
        self.models = {}
        self.scenarios = {
            'recession': -0.25,
            'bull_market': 0.20,
            'volatility_spike': 0.35,
            'normal': 0.05
        }
        
    def preprocess_data(self):
        """
        Prepare data for modeling by pivoting market returns and cleaning.
        """
        try:
            # Pivot market data to wide format (assets as columns)
            returns = self.market_data.pivot(index='date', columns='asset', values='return')
            returns = returns.dropna(axis=1)
            return returns
        except Exception as e:
            raise ValueError(f"Data preprocessing failed: {str(e)}")
    
    def train_models(self):
        """
        Train AI models (Random Forest) to predict asset returns based on other assets.
        """
        try:
            returns = self.preprocess_data()
            assets = returns.columns
            
            for asset in assets:
                # Prepare features (other assets) and target (current asset)
                X = returns.drop(columns=[asset])
                y = returns[asset]
                
                # Split data
                X_train, X_test, y_train, y_test = train_test_split(
                    X, y, test_size=0.2, random_state=42
                )
                
                # Train model
                model = RandomForestRegressor(n_estimators=100, random_state=42)
                model.fit(X_train, y_train)
                
                # Store model
                self.models[asset] = model
                
                # Evaluate
                preds = model.predict(X_test)
                mse = mean_squared_error(y_test, preds)
                print(f"Trained model for {asset} with MSE: {mse:.6f}")
                
        except Exception as e:
            raise RuntimeError(f"Model training failed: {str(e)}")
    
    def simulate_scenario(self, scenario_name, num_simulations=1000):
        """
        Simulate portfolio performance under a given market scenario.
        
        Args:
            scenario_name (str): Name of scenario (must be in self.scenarios)
            num_simulations (int): Number of Monte Carlo simulations
            
        Returns:
            dict: Simulation results with portfolio values and risk metrics
        """
        if scenario_name not in self.scenarios:
            raise ValueError(f"Unknown scenario: {scenario_name}")
            
        try:
            # Get base return for scenario
            base_return = self.scenarios[scenario_name]
            
            # Prepare portfolio
            portfolio_value = (self.portfolio['quantity'] * self.portfolio['price']).sum()
            asset_weights = self.portfolio.set_index('asset')['price'] / portfolio_value
            
            # Simulate returns
            simulated_returns = []
            for _ in range(num_simulations):
                asset_returns = {}
                
                # Generate correlated returns using trained models
                for asset in self.models:
                    if asset in asset_weights.index:
                        # Get predicted return based on other assets
                        other_assets = [a for a in self.models if a != asset]
                        random_returns = np.random.normal(base_return, 0.1, len(other_assets))
                        input_data = pd.DataFrame([random_returns], columns=other_assets)
                        pred_return = self.models[asset].predict(input_data)[0]
                        asset_returns[asset] = pred_return
                
                # Calculate portfolio return
                port_return = sum(
                    asset_weights[asset] * asset_returns.get(asset, base_return)
                    for asset in asset_weights.index
                )
                simulated_returns.append(port_return)
            
            # Calculate risk metrics
            simulated_returns = np.array(simulated_returns)
            mean_return = simulated_returns.mean()
            std_dev = simulated_returns.std()
            var_95 = np.percentile(simulated_returns, 5)
            cvar_95 = simulated_returns[simulated_returns <= var_95].mean()
            
            return {
                'scenario': scenario_name,
                'initial_value': portfolio_value,
                'mean_return': mean_return,
                'std_dev': std_dev,
                'var_95': var_95,
                'cvar_95': cvar_95,
                'simulated_returns': simulated_returns
            }
            
        except Exception as e:
            raise RuntimeError(f"Scenario simulation failed: {str(e)}")
    
    def run_all_scenarios(self, num_simulations=1000):
        """
        Run all defined scenarios and return comprehensive results.
        
        Args:
            num_simulations (int): Number of Monte Carlo simulations per scenario
            
        Returns:
            pd.DataFrame: Results for all scenarios
        """
        results = []
        for scenario in self.scenarios:
            try:
                scenario_result = self.simulate_scenario(scenario, num_simulations)
                results.append(scenario_result)
            except Exception as e:
                print(f"Failed to run scenario {scenario}: {str(e)}")
                continue
                
        return pd.DataFrame(results)

# Example usage
if __name__ == "__main__":
    # Sample portfolio data
    portfolio_data = pd.DataFrame({
        'asset': ['AAPL', 'MSFT', 'GOOGL', 'AMZN'],
        'quantity': [100, 50, 30, 20],
        'price': [150, 300, 2500, 3500]
    })
    
    # Generate synthetic market data
    dates = pd.date_range(start='2020-01-01', end='2023-01-01', freq='D')
    assets = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']
    market_data = []
    
    for date in dates:
        for asset in assets:
            # Generate correlated returns
            base = np.random.normal(0.0005, 0.02)
            if asset == 'AAPL':
                ret = base + np.random.normal(0.0002, 0.01)
            elif asset == 'MSFT':
                ret = base * 0.8 + np.random.normal(0.0003, 0.015)
            elif asset == 'GOOGL':
                ret = base * 1.2 + np.random.normal(0.0001, 0.025)
            else:
                ret = base * 1.5 + np.random.normal(0.0004, 0.03)
                
            market_data.append({'date': date, 'asset': asset, 'return': ret})
    
    market_data = pd.DataFrame(market_data)
    
    # Initialize and run stress tests
    tester = PortfolioStressTester(portfolio_data, market_data)
    tester.train_models()
    results = tester.run_all_scenarios()
    
    # Display results
    print("\nStress Test Results:")
    print(results[['scenario', 'initial_value', 'mean_return', 'std_dev', 'var_95', 'cvar_95']])
```
