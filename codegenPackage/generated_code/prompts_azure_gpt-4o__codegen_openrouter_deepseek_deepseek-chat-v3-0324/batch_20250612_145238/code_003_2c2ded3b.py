"""
Generated Code Metadata:
========================
Original URL: https://mmgroupnepal.com
Prompt: Create a script to calculate inventory requirements for PET preforms based on MM Group Nepal's approach to avoiding long lead times and large inventory.
Generated: DETERMINISTIC_2c2ded3b5636f730
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from datetime import datetime, timedelta
import numpy as np
from typing import Dict, List, Tuple, Optional

class PETPreformInventoryCalculator:
    """
    Calculates optimal PET preform inventory levels based on historical demand,
    lead times, and service level targets to minimize stockouts while avoiding
    excessive inventory.
    """
    
    def __init__(self, safety_stock_factor: float = 1.65):
        """
        Initialize the calculator with default safety stock factor (Z-score for 95% service level).
        
        Args:
            safety_stock_factor: Z-score corresponding to desired service level
        """
        self.safety_stock_factor = safety_stock_factor
        
    def calculate_inventory_requirements(
        self,
        historical_demand: pd.Series,
        lead_time_days: int,
        review_period_days: int = 7,
        current_inventory: int = 0,
        min_order_quantity: int = 1
    ) -> Dict[str, float]:
        """
        Calculate optimal inventory parameters for PET preforms.
        
        Args:
            historical_demand: Pandas Series with datetime index and demand quantities
            lead_time_days: Supplier lead time in days
            review_period_days: How often inventory is reviewed (days)
            current_inventory: Current on-hand inventory
            min_order_quantity: Minimum order quantity constraint
            
        Returns:
            Dictionary containing calculated inventory parameters
        """
        try:
            # Validate inputs
            if not isinstance(historical_demand, pd.Series):
                raise ValueError("historical_demand must be a pandas Series")
            if lead_time_days <= 0:
                raise ValueError("lead_time_days must be positive")
            if review_period_days <= 0:
                raise ValueError("review_period_days must be positive")
            if min_order_quantity <= 0:
                raise ValueError("min_order_quantity must be positive")
                
            # Calculate demand statistics
            daily_demand_mean = historical_demand.mean()
            daily_demand_std = historical_demand.std()
            
            # Calculate lead time demand
            lead_time_demand_mean = daily_demand_mean * lead_time_days
            lead_time_demand_std = daily_demand_std * np.sqrt(lead_time_days)
            
            # Calculate review period demand
            review_period_demand_mean = daily_demand_mean * review_period_days
            review_period_demand_std = daily_demand_std * np.sqrt(review_period_days)
            
            # Calculate safety stock
            safety_stock = self.safety_stock_factor * np.sqrt(
                lead_time_days + review_period_days
            ) * daily_demand_std
            
            # Calculate reorder point
            reorder_point = (daily_demand_mean * (lead_time_days + review_period_days)) + safety_stock
            
            # Calculate order quantity (EOQ-like approximation)
            order_quantity = max(
                min_order_quantity,
                np.sqrt(2 * daily_demand_mean * lead_time_days)
            )
            
            # Calculate suggested order
            suggested_order = max(
                0,
                (reorder_point - current_inventory + daily_demand_mean * lead_time_days)
            )
            suggested_order = max(min_order_quantity, suggested_order)
            
            return {
                "daily_demand_mean": daily_demand_mean,
                "daily_demand_std": daily_demand_std,
                "lead_time_demand_mean": lead_time_demand_mean,
                "lead_time_demand_std": lead_time_demand_std,
                "safety_stock": safety_stock,
                "reorder_point": reorder_point,
                "order_quantity": order_quantity,
                "suggested_order": suggested_order,
                "current_inventory": current_inventory,
                "days_of_inventory": current_inventory / daily_demand_mean if daily_demand_mean > 0 else float('inf')
            }
            
        except Exception as e:
            raise RuntimeError(f"Error calculating inventory requirements: {str(e)}")

def load_historical_data(file_path: str) -> pd.Series:
    """
    Load historical demand data from CSV file.
    
    Args:
        file_path: Path to CSV file with columns 'date' and 'demand'
        
    Returns:
        Pandas Series with datetime index and demand values
    """
    try:
        df = pd.read_csv(file_path, parse_dates=['date'])
        df.set_index('date', inplace=True)
        return df['demand']
    except Exception as e:
        raise RuntimeError(f"Error loading historical data: {str(e)}")

def generate_sample_data(days: int = 365) -> pd.Series:
    """
    Generate sample demand data for testing.
    
    Args:
        days: Number of days of data to generate
        
    Returns:
        Pandas Series with datetime index and random demand values
    """
    dates = pd.date_range(end=datetime.today(), periods=days)
    base_demand = 1000
    noise = np.random.normal(0, 150, days)
    demand = np.maximum(base_demand + noise, 0).astype(int)
    return pd.Series(demand, index=dates)

def main():
    try:
        # Example usage
        calculator = PETPreformInventoryCalculator()
        
        # Option 1: Load from file
        # historical_demand = load_historical_data('demand_history.csv')
        
        # Option 2: Generate sample data
        historical_demand = generate_sample_data()
        
        # Calculate inventory requirements
        results = calculator.calculate_inventory_requirements(
            historical_demand=historical_demand,
            lead_time_days=14,
            review_period_days=7,
            current_inventory=5000,
            min_order_quantity=1000
        )
        
        # Print results
        print("PET Preform Inventory Requirements:")
        for key, value in results.items():
            print(f"{key.replace('_', ' ').title()}: {value:,.2f}")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
