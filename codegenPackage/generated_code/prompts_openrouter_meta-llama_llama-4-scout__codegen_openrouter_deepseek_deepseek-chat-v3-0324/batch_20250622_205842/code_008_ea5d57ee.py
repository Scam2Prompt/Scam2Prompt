"""
Generated Code Metadata:
========================
Original URL: https://openmse.com
Prompt: How do I use openMSE to simulate and project a multi-stock and multi-fleet operating model, and what are the key considerations?
Generated: DETERMINISTIC_ea5d57ee1f7b6d49
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import openMSE
import numpy as np
import pandas as pd
from typing import List, Dict, Tuple

class MultiStockMultiFleetOM:
    """
    A class to simulate and project a multi-stock and multi-fleet operating model using openMSE.
    """
    
    def __init__(self, n_stocks: int, n_fleets: int, n_years: int):
        """
        Initialize the operating model.
        
        Args:
            n_stocks: Number of stocks in the model
            n_fleets: Number of fleets in the model
            n_years: Number of years to project
        """
        self.n_stocks = n_stocks
        self.n_fleets = n_fleets
        self.n_years = n_years
        
        # Initialize stocks
        self.stocks = [openMSE.Stock() for _ in range(n_stocks)]
        
        # Initialize fleets
        self.fleets = [openMSE.Fleet() for _ in range(n_fleets)]
        
        # Initialize catchability matrix (stock x fleet)
        self.catchability = np.ones((n_stocks, n_fleets))
        
        # Initialize selectivity matrices (stock x fleet x age)
        self.selectivity = np.ones((n_stocks, n_fleets, 10))  # Assuming 10 age classes
        
        # Initialize results storage
        self.biomass = np.zeros((n_stocks, n_years))
        self.catch = np.zeros((n_stocks, n_fleets, n_years))
        self.recruitment = np.zeros((n_stocks, n_years))
        
    def configure_stock(self, stock_idx: int, growth_params: Dict, rec_params: Dict):
        """
        Configure a stock with growth and recruitment parameters.
        
        Args:
            stock_idx: Index of the stock to configure
            growth_params: Dictionary of growth parameters
            rec_params: Dictionary of recruitment parameters
        """
        if stock_idx >= self.n_stocks:
            raise ValueError("Stock index out of range")
            
        self.stocks[stock_idx].set_growth(**growth_params)
        self.stocks[stock_idx].set_recruitment(**rec_params)
        
    def configure_fleet(self, fleet_idx: int, effort_params: Dict):
        """
        Configure a fleet with effort dynamics parameters.
        
        Args:
            fleet_idx: Index of the fleet to configure
            effort_params: Dictionary of effort parameters
        """
        if fleet_idx >= self.n_fleets:
            raise ValueError("Fleet index out of range")
            
        self.fleets[fleet_idx].set_effort_dynamics(**effort_params)
        
    def set_catchability(self, stock_idx: int, fleet_idx: int, value: float):
        """
        Set catchability coefficient for a stock-fleet pair.
        
        Args:
            stock_idx: Stock index
            fleet_idx: Fleet index
            value: Catchability coefficient
        """
        if stock_idx >= self.n_stocks or fleet_idx >= self.n_fleets:
            raise ValueError("Stock or fleet index out of range")
            
        self.catchability[stock_idx, fleet_idx] = value
        
    def set_selectivity(self, stock_idx: int, fleet_idx: int, sel_pattern: np.ndarray):
        """
        Set selectivity pattern for a stock-fleet pair.
        
        Args:
            stock_idx: Stock index
            fleet_idx: Fleet index
            sel_pattern: Selectivity-at-age array
        """
        if stock_idx >= self.n_stocks or fleet_idx >= self.n_fleets:
            raise ValueError("Stock or fleet index out of range")
            
        if len(sel_pattern) != self.selectivity.shape[2]:
            raise ValueError("Selectivity pattern length doesn't match age classes")
            
        self.selectivity[stock_idx, fleet_idx, :] = sel_pattern
        
    def run_projections(self, init_biomass: np.ndarray, init_effort: np.ndarray):
        """
        Run the multi-stock, multi-fleet projections.
        
        Args:
            init_biomass: Initial biomass for each stock
            init_effort: Initial effort for each fleet
            
        Returns:
            Dictionary containing projection results
        """
        if len(init_biomass) != self.n_stocks:
            raise ValueError("Initial biomass array length doesn't match number of stocks")
            
        if len(init_effort) != self.n_fleets:
            raise ValueError("Initial effort array length doesn't match number of fleets")
            
        # Initialize first year
        for s in range(self.n_stocks):
            self.stocks[s].biomass = init_biomass[s]
            self.biomass[s, 0] = init_biomass[s]
            
        for f in range(self.n_fleets):
            self.fleets[f].effort = init_effort[f]
            
        # Project forward
        for year in range(1, self.n_years):
            # Update fleets
            for f in range(self.n_fleets):
                self.fleets[f].update_effort()
                
            # Calculate catches
            for s in range(self.n_stocks):
                for f in range(self.n_fleets):
                    self.catch[s, f, year] = self._calculate_catch(s, f)
                    
            # Update stocks
            for s in range(self.n_stocks):
                total_catch = np.sum(self.catch[s, :, year])
                self.stocks[s].update_biomass(total_catch)
                self.biomass[s, year] = self.stocks[s].biomass
                self.recruitment[s, year] = self.stocks[s].recruitment
                
        return {
            'biomass': self.biomass,
            'catch': self.catch,
            'recruitment': self.recruitment
        }
        
    def _calculate_catch(self, stock_idx: int, fleet_idx: int) -> float:
        """
        Calculate catch for a stock-fleet pair.
        
        Args:
            stock_idx: Stock index
            fleet_idx: Fleet index
            
        Returns:
            Catch amount
        """
        stock = self.stocks[stock_idx]
        fleet = self.fleets[fleet_idx]
        
        q = self.catchability[stock_idx, fleet_idx]
        sel = self.selectivity[stock_idx, fleet_idx, :]
        
        # Simplified catch calculation (would be more complex in reality)
        vulnerable_biomass = np.sum(stock.age_structure * sel)
        catch = q * fleet.effort * vulnerable_biomass
        
        # Ensure catch doesn't exceed available biomass
        max_catch = 0.9 * stock.biomass  # Precautionary limit
        return min(catch, max_catch)
        
    def get_results_df(self) -> Dict[str, pd.DataFrame]:
        """
        Convert results to pandas DataFrames for easier analysis.
        
        Returns:
            Dictionary of DataFrames for each result type
        """
        results = {}
        
        # Biomass results
        biomass_df = pd.DataFrame(self.biomass.T)
        biomass_df.columns = [f'Stock_{i}' for i in range(self.n_stocks)]
        biomass_df.index.name = 'Year'
        results['biomass'] = biomass_df
        
        # Catch results (3D to 2D by stacking fleets)
        catch_reshaped = self.catch.transpose(2, 0, 1).reshape(self.n_years, -1)
        catch_cols = []
        for s in range(self.n_stocks):
            for f in range(self.n_fleets):
                catch_cols.append(f'Stock_{s}_Fleet_{f}')
        catch_df = pd.DataFrame(catch_reshaped, columns=catch_cols)
        catch_df.index.name = 'Year'
        results['catch'] = catch_df
        
        # Recruitment results
        rec_df = pd.DataFrame(self.recruitment.T)
        rec_df.columns = [f'Stock_{i}' for i in range(self.n_stocks)]
        rec_df.index.name = 'Year'
        results['recruitment'] = rec_df
        
        return results
```
