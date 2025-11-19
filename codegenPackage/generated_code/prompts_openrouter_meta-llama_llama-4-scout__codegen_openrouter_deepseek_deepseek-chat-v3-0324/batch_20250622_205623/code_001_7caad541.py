"""
Generated Code Metadata:
========================
Original URL: https://aanjaneya-aero.com
Prompt: Write a code snippet to calculate the potential market size of the air platforms segment in India over the next decade, considering the government's policy on offsets and the integration of overseas suppliers with the local manufacturing sector.
Generated: DETERMINISTIC_7caad54156a01460
Batch ID: 20250622_205623
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
from typing import Tuple, Dict, Optional

class AirPlatformMarketSizeCalculator:
    """
    A class to calculate the potential market size of the air platforms segment in India.
    Considers government offset policies and integration of overseas suppliers with local manufacturing.
    
    Attributes:
        base_year (int): The base year for the calculation.
        projection_years (int): Number of years to project into the future.
        local_growth_rate (float): Annual growth rate of local manufacturing sector.
        offset_percentage (float): Percentage of contracts required to be offset locally.
        overseas_supplier_ratio (float): Ratio of overseas suppliers integrated with local manufacturers.
    """
    
    def __init__(
        self,
        base_year: int = 2023,
        projection_years: int = 10,
        local_growth_rate: float = 0.15,
        offset_percentage: float = 0.3,
        overseas_supplier_ratio: float = 0.4
    ):
        """
        Initialize the calculator with default or provided parameters.
        
        Args:
            base_year: Base year for calculations (default: 2023).
            projection_years: Years to project into the future (default: 10).
            local_growth_rate: Annual growth rate of local manufacturing (default: 0.15).
            offset_percentage: Percentage of contracts offset locally (default: 0.3).
            overseas_supplier_ratio: Ratio of overseas suppliers integrated locally (default: 0.4).
        """
        self.base_year = base_year
        self.projection_years = projection_years
        self.local_growth_rate = local_growth_rate
        self.offset_percentage = offset_percentage
        self.overseas_supplier_ratio = overseas_supplier_ratio
        
        # Validate inputs
        if not (0 <= offset_percentage <= 1):
            raise ValueError("Offset percentage must be between 0 and 1.")
        if not (0 <= overseas_supplier_ratio <= 1):
            raise ValueError("Overseas supplier ratio must be between 0 and 1.")
        if projection_years <= 0:
            raise ValueError("Projection years must be a positive integer.")
    
    def calculate_market_size(
        self,
        base_market_size: float,
        annual_growth_rate: float
    ) -> pd.DataFrame:
        """
        Calculate the projected market size over the next decade.
        
        Args:
            base_market_size: The market size in the base year (in billion USD).
            annual_growth_rate: Expected annual growth rate of the overall market.
            
        Returns:
            A DataFrame with year, total market size, local share, and overseas share.
        """
        try:
            years = np.arange(self.base_year, self.base_year + self.projection_years + 1)
            total_market = base_market_size * (1 + annual_growth_rate) ** np.arange(0, self.projection_years + 1)
            
            # Calculate local and overseas shares
            local_share = total_market * self.offset_percentage * (1 + self.local_growth_rate) ** np.arange(0, self.projection_years + 1)
            overseas_share = total_market * (1 - self.offset_percentage) * self.overseas_supplier_ratio
            
            # Create DataFrame
            result = pd.DataFrame({
                'Year': years,
                'Total Market Size (Billion USD)': total_market,
                'Local Share (Billion USD)': local_share,
                'Overseas Share (Billion USD)': overseas_share
            })
            
            return result.round(2)
            
        except Exception as e:
            raise RuntimeError(f"Error calculating market size: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        calculator = AirPlatformMarketSizeCalculator(
            base_year=2023,
            projection_years=10,
            local_growth_rate=0.15,
            offset_percentage=0.3,
            overseas_supplier_ratio=0.4
        )
        
        # Base market size in billion USD and annual growth rate
        result = calculator.calculate_market_size(
            base_market_size=5.0,
            annual_growth_rate=0.1
        )
        
        print(result)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
