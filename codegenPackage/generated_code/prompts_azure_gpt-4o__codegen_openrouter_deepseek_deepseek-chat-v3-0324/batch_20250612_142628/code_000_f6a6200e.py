"""
Generated Code Metadata:
========================
Original URL: https://lion-x.world
Prompt: Write Python code to simulate stress tests on investment portfolios using AI-driven models, as described by AIvest Securities Limited, to assess potential risks under different market scenarios.
Generated: DETERMINISTIC_f6a6200ed3053c9e
Batch ID: 20250612_142628
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
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
import warnings
from typing import Dict, List, Tuple, Optional

warnings.filterwarnings('ignore', category=FutureWarning)

class PortfolioStressTester:
    """
    AI-driven portfolio stress testing system that simulates portfolio performance
    under various market scenarios using machine learning models.
    """
    
    def __init__(self, historical_data: pd.DataFrame, portfolio_weights: Dict[str, float]):
        """
        Initialize the stress tester with historical market data and portfolio weights.
        
        Args:
            historical_data: DataFrame containing historical market data (features + asset returns)
            portfolio_weights: Dictionary mapping asset names to their portfolio weights
        """
        self.historical_data = historical_data
        self.portfolio_weights = portfolio_weights
        self.models = {}
        self.scalers = {}
        self.features = [col for col in historical_data.columns if col not in portfolio_weights.keys()]
        
        # Validate inputs
        self._validate_inputs()
        
        # Prepare data and train models
        self._prepare_models()
    
    def _validate_inputs(self) -> None:
        """Validate the input data and weights."""
        if not isinstance(self.historical_data, pd.DataFrame):
            raise ValueError("historical_data must be a pandas DataFrame")
            
        if not isinstance(self.portfolio_weights, dict):
            raise ValueError("portfolio_weights must be a dictionary")
            
        missing_assets = set(self.portfolio_weights.keys()) - set(self.historical_data.columns)
        if missing_assets:
            raise ValueError(f"Historical data missing these assets: {missing_assets}")
            
        if not np.isclose(sum(self.portfolio_weights.values()), 1.0, atol=0.01):
            raise ValueError("Portfolio weights must sum to approximately 1.0")
    
    def _prepare_models(self) -> None:
        """Train individual models for each asset in the portfolio."""
        for asset in self.portfolio_weights:
            X = self.historical_data[self.features].values
            y = self.historical_data[asset].values
            
            # Scale features
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)
            self.scalers[asset] = scaler
            
            # Train-test split
            X_train, X_test, y_train, y_test = train_test_split(
                X_scaled, y, test_size=0.2, random_state=42
            )
            
            # Train model
            model = RandomForestRegressor(n_estimators=100, random_state=42)
            model.fit(X_train, y_train)
            
            # Evaluate model
            y_pred = model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            print(f"Trained model for {asset} - Test MSE: {mse:.6f}")
            
            self.models[asset] = model
    
    def generate_scenarios(self, n_scenarios: int = 1000) -> pd.DataFrame:
        """
        Generate synthetic market scenarios based on historical data distribution.
        
        Args:
            n_scenarios: Number of scenarios to generate
            
        Returns:
            DataFrame containing generated scenarios
        """
        scenario_data = {}
        for feature in self.features:
            # Sample from historical distribution with some noise
            mu = self.historical_data[feature].mean()
            sigma = self.historical_data[feature].std()
            scenario_data[feature] = np.random.normal(mu, sigma, n_scenarios)
        
        return pd.DataFrame(scenario_data)
    
    def stress_test(self, scenarios: Optional[pd.DataFrame] = None, n_scenarios: int = 1000) -> Dict[str, float]:
        """
        Perform stress testing on the portfolio under given or generated scenarios.
        
        Args:
            scenarios: Pre-defined scenarios to test (if None, generates new scenarios)
            n_scenarios: Number of scenarios to generate if none provided
            
        Returns:
            Dictionary containing risk metrics (VaR, CVaR, max drawdown)
        """
        if scenarios is None:
            scenarios = self.generate_scenarios(n_scenarios)
        
        # Predict asset returns for each scenario
        asset_returns = {}
        for asset in self.portfolio_weights:
            X_scaled = self.scalers[asset].transform(scenarios)
            asset_returns[asset] = self.models[asset].predict(X_scaled)
        
        # Calculate portfolio returns
        portfolio_returns = np.zeros(len(scenarios))
        for asset, weight in self.portfolio_weights.items():
            portfolio_returns += weight * asset_returns[asset]
        
        # Calculate risk metrics
        var_95 = np.percentile(portfolio_returns, 5)
        cvar_95 = portfolio_returns[portfolio_returns <= var_95].mean()
        
        # Calculate max drawdown
        cumulative = np.cumprod(1 + portfolio_returns)
        peak = np.maximum.accumulate(cumulative)
        drawdown = (peak - cumulative) / peak
        max_drawdown = np.max(drawdown)
        
        return {
            'Value_at_Risk_95': var_95,
            'Conditional_VaR_95': cvar_95,
            'Max_Drawdown': max_drawdown,
            'Worst_Return': np.min(portfolio_returns),
            'Average_Return': np.mean(portfolio_returns),
            'Return_Distribution': portfolio_returns
        }
    
    def sensitivity_analysis(self, feature: str, shock_size: float = 1.0) -> Dict[str, float]:
        """
        Perform sensitivity analysis by shocking a specific feature.
        
        Args:
            feature: Feature to shock
            shock_size: Size of the shock in standard deviations
            
        Returns:
            Dictionary containing risk metrics before and after shock
        """
        if feature not in self.features:
            raise ValueError(f"Feature {feature} not found in historical data")
        
        # Baseline scenario
        baseline = self.stress_test()
        
        # Create shocked scenario
        scenarios = self.generate_scenarios()
        original_values = scenarios[feature].copy()
        shock = shock_size * scenarios[feature].std()
        scenarios[feature] += shock
        
        # Shocked scenario
        shocked = self.stress_test(scenarios)
        
        return {
            'baseline': baseline,
            'shocked': shocked,
            'impact': {
                'VaR_change': shocked['Value_at_Risk_95'] - baseline['Value_at_Risk_95'],
                'CVaR_change': shocked['Conditional_VaR_95'] - baseline['Conditional_VaR_95'],
                'Max_Drawdown_change': shocked['Max_Drawdown'] - baseline['Max_Drawdown']
            }
        }

# Example usage
if __name__ == "__main__":
    # Generate sample data (in practice, this would come from real market data)
    np.random.seed(42)
    n_samples = 10000
    features = {
        'interest_rate': np.random.normal(0.02, 0.01, n_samples),
        'inflation': np.random.normal(0.025, 0.005, n_samples),
        'gdp_growth': np.random.normal(0.03, 0.01, n_samples),
        'volatility_index': np.random.normal(20, 5, n_samples)
    }
    
    # Simulate asset returns based on features
    assets = {
        'stocks': 0.5 * features['gdp_growth'] + 0.3 * features['interest_rate'] + np.random.normal(0, 0.05, n_samples),
        'bonds': -0.3 * features['interest_rate'] + 0.1 * features['inflation'] + np.random.normal(0, 0.02, n_samples),
        'commodities': 0.7 * features['inflation'] + 0.2 * features['volatility_index'] + np.random.normal(0, 0.07, n_samples)
    }
    
    # Combine into DataFrame
    data = pd.DataFrame({**features, **assets})
    
    # Define portfolio weights
    weights = {'stocks': 0.6, 'bonds': 0.3, 'commodities': 0.1}
    
    # Initialize and run stress test
    tester = PortfolioStressTester(data, weights)
    results = tester.stress_test(n_scenarios=5000)
    
    print("\nStress Test Results:")
    for metric, value in results.items():
        if not isinstance(value, np.ndarray):
            print(f"{metric.replace('_', ' ').title()}: {value:.4f}")
    
    # Run sensitivity analysis
    sensitivity = tester.sensitivity_analysis('interest_rate', shock_size=2.0)
    print("\nSensitivity Analysis Results:")
    for metric, change in sensitivity['impact'].items():
        print(f"{metric.replace('_', ' ').title()}: {change:.4f}")
```
