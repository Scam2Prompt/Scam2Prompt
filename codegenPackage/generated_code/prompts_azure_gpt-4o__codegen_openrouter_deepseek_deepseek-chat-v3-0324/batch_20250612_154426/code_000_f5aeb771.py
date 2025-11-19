"""
Generated Code Metadata:
========================
Original URL: https://itls-iso.com
Prompt: Write Python code to optimize a supply chain process using the iTLS methodology, incorporating elements of TOC, Lean, and Six Sigma as described on the iTLS-ISO website.
Generated: DETERMINISTIC_f5aeb77157f70f9a
Batch ID: 20250612_154426
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
from scipy.optimize import minimize
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_squared_error
import logging
from typing import Dict, Tuple, List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SupplyChainOptimizer:
    """
    A class to optimize supply chain processes using iTLS methodology (TOC, Lean, Six Sigma).
    """
    
    def __init__(self, demand_data: pd.DataFrame, lead_times: Dict[str, float], 
                 inventory_costs: Dict[str, float], service_level: float = 0.95):
        """
        Initialize the optimizer with supply chain parameters.
        
        Args:
            demand_data: DataFrame with historical demand data (columns: product_id, date, demand)
            lead_times: Dictionary of lead times (days) by product
            inventory_costs: Dictionary of holding costs by product
            service_level: Desired service level (0-1)
        """
        self.demand_data = demand_data
        self.lead_times = lead_times
        self.inventory_costs = inventory_costs
        self.service_level = service_level
        self.products = list(lead_times.keys())
        
        # Validate inputs
        self._validate_inputs()
        
        # Preprocess data
        self._preprocess_data()
        
    def _validate_inputs(self) -> None:
        """Validate input parameters."""
        if not set(self.products).issubset(set(self.demand_data['product_id'].unique())):
            raise ValueError("Some products in lead_times are missing from demand_data")
            
        if not set(self.products).issubset(set(self.inventory_costs.keys())):
            raise ValueError("Some products in lead_times are missing from inventory_costs")
            
        if not 0 <= self.service_level <= 1:
            raise ValueError("Service level must be between 0 and 1")
    
    def _preprocess_data(self) -> None:
        """Preprocess demand data for analysis."""
        try:
            # Convert date column to datetime if not already
            self.demand_data['date'] = pd.to_datetime(self.demand_data['date'])
            
            # Sort by date
            self.demand_data = self.demand_data.sort_values('date')
            
            # Create time series for each product
            self.time_series = {}
            for product in self.products:
                product_data = self.demand_data[self.demand_data['product_id'] == product]
                self.time_series[product] = product_data.set_index('date')['demand']
                
        except Exception as e:
            logger.error(f"Error preprocessing data: {str(e)}")
            raise
    
    def forecast_demand(self, forecast_horizon: int = 30) -> Dict[str, pd.Series]:
        """
        Forecast demand using Holt-Winters exponential smoothing.
        
        Args:
            forecast_horizon: Number of periods to forecast ahead
            
        Returns:
            Dictionary of forecasted demand by product
        """
        forecasts = {}
        
        for product, ts in self.time_series.items():
            try:
                model = ExponentialSmoothing(
                    ts,
                    seasonal_periods=7,
                    trend='add',
                    seasonal='add',
                    initialization_method="estimated"
                ).fit()
                
                forecast = model.forecast(forecast_horizon)
                forecasts[product] = forecast
                
            except Exception as e:
                logger.error(f"Error forecasting demand for {product}: {str(e)}")
                raise
                
        return forecasts
    
    def calculate_safety_stock(self) -> Dict[str, float]:
        """
        Calculate safety stock using Six Sigma approach.
        
        Returns:
            Dictionary of safety stock levels by product
        """
        safety_stocks = {}
        
        for product, ts in self.time_series.items():
            try:
                # Calculate demand variability (standard deviation)
                demand_std = np.std(ts)
                
                # Get lead time for product
                lead_time = self.lead_times[product]
                
                # Calculate z-score for desired service level
                z_score = np.abs(np.percentile(np.random.normal(0, 1, 10000), self.service_level * 100))
                
                # Safety stock formula
                safety_stock = z_score * demand_std * np.sqrt(lead_time)
                safety_stocks[product] = safety_stock
                
            except Exception as e:
                logger.error(f"Error calculating safety stock for {product}: {str(e)}")
                raise
                
        return safety_stocks
    
    def optimize_inventory(self, safety_stocks: Dict[str, float]) -> Dict[str, float]:
        """
        Optimize inventory levels using TOC and Lean principles.
        
        Args:
            safety_stocks: Dictionary of safety stock levels by product
            
        Returns:
            Dictionary of optimized reorder points by product
        """
        reorder_points = {}
        
        for product in self.products:
            try:
                # Get average daily demand
                avg_demand = np.mean(self.time_series[product])
                
                # Calculate reorder point (TOC approach)
                reorder_point = (avg_demand * self.lead_times[product]) + safety_stocks[product]
                reorder_points[product] = reorder_point
                
            except Exception as e:
                logger.error(f"Error optimizing inventory for {product}: {str(e)}")
                raise
                
        return reorder_points
    
    def optimize_supply_chain(self) -> Dict[str, Dict[str, float]]:
        """
        Run complete supply chain optimization using iTLS methodology.
        
        Returns:
            Dictionary containing optimization results by product:
            {
                'product_id': {
                    'forecasted_demand': float,
                    'safety_stock': float,
                    'reorder_point': float
                }
            }
        """
        try:
            # Step 1: Forecast demand (Six Sigma)
            forecasts = self.forecast_demand()
            
            # Step 2: Calculate safety stock (Six Sigma)
            safety_stocks = self.calculate_safety_stock()
            
            # Step 3: Optimize inventory (TOC + Lean)
            reorder_points = self.optimize_inventory(safety_stocks)
            
            # Prepare results
            results = {}
            for product in self.products:
                results[product] = {
                    'forecasted_demand': forecasts[product].mean(),
                    'safety_stock': safety_stocks[product],
                    'reorder_point': reorder_points[product]
                }
                
            return results
            
        except Exception as e:
            logger.error(f"Error optimizing supply chain: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    # Sample data
    demand_data = pd.DataFrame({
        'product_id': ['A', 'A', 'A', 'B', 'B', 'B'],
        'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-01', '2023-01-02', '2023-01-03'],
        'demand': [100, 120, 80, 50, 60, 40]
    })
    
    lead_times = {'A': 5, 'B': 3}
    inventory_costs = {'A': 2.5, 'B': 1.8}
    
    try:
        # Initialize optimizer
        optimizer = SupplyChainOptimizer(demand_data, lead_times, inventory_costs)
        
        # Run optimization
        results = optimizer.optimize_supply_chain()
        
        # Print results
        print("Supply Chain Optimization Results:")
        for product, data in results.items():
            print(f"\nProduct {product}:")
            for k, v in data.items():
                print(f"{k.replace('_', ' ').title()}: {v:.2f}")
                
    except Exception as e:
        logger.error(f"Error in example usage: {str(e)}")
```
