"""
Generated Code Metadata:
========================
Original URL: https://lion-x.one
Prompt: Write Python code to simulate stress tests on investment portfolios using AI-driven models, incorporating real-time market data and predictions as described by AIvest Securities Limited.
Generated: DETERMINISTIC_d177af6cd72574b8
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
import yfinance as yf
from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
import warnings
import logging
from typing import Dict, List, Tuple, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Suppress sklearn warnings
warnings.filterwarnings("ignore", category=UserWarning)

class PortfolioStressTester:
    """
    AI-driven portfolio stress testing system that incorporates real-time market data
    and predictive modeling to simulate various stress scenarios.
    """
    
    def __init__(self, portfolio: Dict[str, float], risk_free_rate: float = 0.02):
        """
        Initialize the stress tester with a portfolio and risk-free rate.
        
        Args:
            portfolio: Dictionary of tickers and their weights (e.g., {'AAPL': 0.5, 'MSFT': 0.5})
            risk_free_rate: Annual risk-free rate for calculations
        """
        self.portfolio = portfolio
        self.risk_free_rate = risk_free_rate
        self.models = {}
        self.scaler = StandardScaler()
        self.historical_data = None
        self.features = None
        self.target = None
        
    def fetch_market_data(self, start_date: str, end_date: Optional[str] = None) -> pd.DataFrame:
        """
        Fetch historical market data for all assets in the portfolio.
        
        Args:
            start_date: Start date in 'YYYY-MM-DD' format
            end_date: End date in 'YYYY-MM-DD' format (defaults to today)
            
        Returns:
            DataFrame with historical prices for all assets
        """
        if end_date is None:
            end_date = datetime.now().strftime('%Y-%m-%d')
            
        try:
            data = yf.download(
                list(self.portfolio.keys()),
                start=start_date,
                end=end_date,
                group_by='ticker'
            )
            
            if data.empty:
                raise ValueError("No data returned from Yahoo Finance")
                
            # Process the data into a clean DataFrame
            processed_data = pd.DataFrame()
            for ticker in self.portfolio.keys():
                ticker_data = data[ticker]['Adj Close'].rename(ticker)
                processed_data = pd.concat([processed_data, ticker_data], axis=1)
                
            self.historical_data = processed_data.dropna()
            logger.info(f"Successfully fetched data for {len(self.portfolio)} assets")
            return self.historical_data
            
        except Exception as e:
            logger.error(f"Error fetching market data: {str(e)}")
            raise
            
    def preprocess_data(self, lookback_window: int = 30) -> None:
        """
        Preprocess the historical data to create features and target for the model.
        
        Args:
            lookback_window: Number of days to look back for feature creation
        """
        if self.historical_data is None:
            raise ValueError("No historical data available. Fetch data first.")
            
        try:
            returns = self.historical_data.pct_change().dropna()
            
            # Create features (rolling statistics)
            features = pd.DataFrame()
            for ticker in returns.columns:
                features[f'{ticker}_mean'] = returns[ticker].rolling(lookback_window).mean()
                features[f'{ticker}_vol'] = returns[ticker].rolling(lookback_window).std()
                features[f'{ticker}_min'] = returns[ticker].rolling(lookback_window).min()
                features[f'{ticker}_max'] = returns[ticker].rolling(lookback_window).max()
                
            # Create target (next day's portfolio return)
            weighted_returns = returns.dot(pd.Series(self.portfolio))
            target = weighted_returns.shift(-1)
            
            # Drop NA values created by rolling windows and shift
            combined = pd.concat([features, target], axis=1).dropna()
            self.features = combined.iloc[:, :-1]
            self.target = combined.iloc[:, -1]
            
            # Scale features
            self.features = pd.DataFrame(
                self.scaler.fit_transform(self.features),
                columns=self.features.columns,
                index=self.features.index
            )
            
            logger.info("Data preprocessing completed successfully")
            
        except Exception as e:
            logger.error(f"Error during data preprocessing: {str(e)}")
            raise
            
    def train_models(self, test_size: float = 0.2, random_state: int = 42) -> None:
        """
        Train predictive models for each asset in the portfolio.
        
        Args:
            test_size: Proportion of data to use for testing
            random_state: Random seed for reproducibility
        """
        if self.features is None or self.target is None:
            raise ValueError("No features/target available. Preprocess data first.")
            
        try:
            X_train, X_test, y_train, y_test = train_test_split(
                self.features,
                self.target,
                test_size=test_size,
                random_state=random_state
            )
            
            # Train model
            model = RandomForestRegressor(
                n_estimators=100,
                random_state=random_state,
                n_jobs=-1
            )
            model.fit(X_train, y_train)
            
            # Evaluate model
            y_pred = model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            logger.info(f"Model trained with MSE: {mse:.6f}")
            
            self.models['portfolio'] = model
            
        except Exception as e:
            logger.error(f"Error during model training: {str(e)}")
            raise
            
    def simulate_stress_scenario(
        self,
        scenario_name: str,
        shock_factors: Dict[str, float],
        num_simulations: int = 1000,
        horizon_days: int = 30
    ) -> Dict[str, float]:
        """
        Simulate a stress scenario on the portfolio.
        
        Args:
            scenario_name: Name of the stress scenario
            shock_factors: Dictionary of shock factors for each asset (e.g., {'AAPL': -0.2})
            num_simulations: Number of Monte Carlo simulations
            horizon_days: Time horizon for the stress test in days
            
        Returns:
            Dictionary with stress test results
        """
        if not self.models:
            raise ValueError("No trained models available. Train models first.")
            
        try:
            # Get the most recent features
            last_features = self.features.iloc[-1].values.reshape(1, -1)
            
            # Initialize results storage
            portfolio_values = []
            
            for _ in range(num_simulations):
                current_portfolio_value = 1.0  # Starting with normalized value
                
                for day in range(horizon_days):
                    # Predict next day's return
                    predicted_return = self.models['portfolio'].predict(last_features)[0]
                    
                    # Apply shock factors if this is the first day
                    if day == 0:
                        weighted_shock = sum(
                            self.portfolio[ticker] * shock_factors.get(ticker, 0)
                            for ticker in self.portfolio
                        )
                        predicted_return += weighted_shock
                    
                    # Update portfolio value
                    current_portfolio_value *= (1 + predicted_return)
                    
                    # Generate new features for next prediction
                    random_noise = np.random.normal(0, 0.01, size=last_features.shape)
                    last_features = np.clip(last_features + random_noise, -3, 3)
                
                portfolio_values.append(current_portfolio_value)
            
            # Calculate statistics
            portfolio_values = np.array(portfolio_values)
            mean_value = np.mean(portfolio_values)
            min_value = np.min(portfolio_values)
            max_value = np.max(portfolio_values)
            var_95 = np.percentile(portfolio_values, 5)
            
            results = {
                'scenario': scenario_name,
                'mean_value': mean_value,
                'min_value': min_value,
                'max_value': max_value,
                'var_95': var_95,
                'shock_factors': shock_factors
            }
            
            logger.info(f"Completed stress scenario: {scenario_name}")
            return results
            
        except Exception as e:
            logger.error(f"Error during stress scenario simulation: {str(e)}")
            raise
            
    def run_full_analysis(
        self,
        start_date: str,
        scenarios: Dict[str, Dict[str, float]],
        lookback_window: int = 30,
        test_size: float = 0.2,
        num_simulations: int = 1000,
        horizon_days: int = 30
    ) -> List[Dict[str, float]]:
        """
        Run complete stress test analysis with multiple scenarios.
        
        Args:
            start_date: Start date for historical data
            scenarios: Dictionary of scenarios with their shock factors
            lookback_window: Lookback window for feature creation
            test_size: Proportion of data for testing
