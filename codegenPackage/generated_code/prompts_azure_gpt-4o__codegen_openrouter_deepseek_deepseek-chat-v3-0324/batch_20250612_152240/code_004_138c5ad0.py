"""
Generated Code Metadata:
========================
Original URL: https://openmse.com
Prompt: Create Python code to simulate multi-stock and multi-fleet Operating Models using openMSE. Include an example of configuring fleet selectivity.
Generated: DETERMINISTIC_138c5ad06a95dfc7
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import openmse
import numpy as np
from typing import List, Dict, Optional

class OperatingModel:
    """
    A class to simulate multi-stock and multi-fleet operating models using openMSE.
    """
    
    def __init__(self, stocks: List[str], fleets: List[str], years: int):
        """
        Initialize the operating model with stocks, fleets, and simulation years.
        
        Args:
            stocks: List of stock names
            fleets: List of fleet names
            years: Number of simulation years
        """
        self.stocks = stocks
        self.fleets = fleets
        self.years = years
        self.model = openmse.OperatingModel(len(stocks), len(fleets), years)
        
        # Initialize data structures
        self.stock_params = {stock: {} for stock in stocks}
        self.fleet_params = {fleet: {} for fleet in fleets}
        self.selectivity = np.zeros((len(fleets), len(stocks)))
        
    def configure_stock(self, stock_name: str, growth_params: Dict, init_biomass: float):
        """
        Configure stock parameters.
        
        Args:
            stock_name: Name of the stock to configure
            growth_params: Dictionary of growth parameters (e.g., {'r': 0.3, 'K': 1000})
            init_biomass: Initial biomass for the stock
        """
        if stock_name not in self.stocks:
            raise ValueError(f"Stock {stock_name} not found in model")
            
        stock_idx = self.stocks.index(stock_name)
        self.model.set_growth_params(stock_idx, **growth_params)
        self.model.set_init_biomass(stock_idx, init_biomass)
        self.stock_params[stock_name] = {
            'growth_params': growth_params,
            'init_biomass': init_biomass
        }
        
    def configure_fleet(self, fleet_name: str, catchability: float, effort: float):
        """
        Configure fleet parameters.
        
        Args:
            fleet_name: Name of the fleet to configure
            catchability: Catchability coefficient
            effort: Fishing effort
        """
        if fleet_name not in self.fleets:
            raise ValueError(f"Fleet {fleet_name} not found in model")
            
        fleet_idx = self.fleets.index(fleet_name)
        self.model.set_catchability(fleet_idx, catchability)
        self.model.set_effort(fleet_idx, effort)
        self.fleet_params[fleet_name] = {
            'catchability': catchability,
            'effort': effort
        }
        
    def set_selectivity(self, fleet_name: str, stock_name: str, value: float):
        """
        Set selectivity of a fleet for a particular stock.
        
        Args:
            fleet_name: Name of the fleet
            stock_name: Name of the stock
            value: Selectivity value (0-1)
        """
        if fleet_name not in self.fleets:
            raise ValueError(f"Fleet {fleet_name} not found in model")
        if stock_name not in self.stocks:
            raise ValueError(f"Stock {stock_name} not found in model")
            
        fleet_idx = self.fleets.index(fleet_name)
        stock_idx = self.stocks.index(stock_name)
        
        if not 0 <= value <= 1:
            raise ValueError("Selectivity must be between 0 and 1")
            
        self.selectivity[fleet_idx, stock_idx] = value
        self.model.set_selectivity(fleet_idx, stock_idx, value)
        
    def run_simulation(self) -> Dict[str, np.ndarray]:
        """
        Run the operating model simulation.
        
        Returns:
            Dictionary with biomass and catch time series for each stock
        """
        results = self.model.run()
        
        output = {}
        for i, stock in enumerate(self.stocks):
            output[f"{stock}_biomass"] = results.biomass[:, i]
            output[f"{stock}_catch"] = results.catch[:, i]
            
        return output

# Example usage
if __name__ == "__main__":
    # Create an operating model with 2 stocks and 3 fleets for 10 years
    om = OperatingModel(
        stocks=["Cod", "Haddock"],
        fleets=["Trawl", "Gillnet", "Longline"],
        years=10
    )
    
    # Configure stocks
    om.configure_stock("Cod", {"r": 0.3, "K": 1000}, init_biomass=800)
    om.configure_stock("Haddock", {"r": 0.4, "K": 1500}, init_biomass=1200)
    
    # Configure fleets
    om.configure_fleet("Trawl", catchability=0.7, effort=50)
    om.configure_fleet("Gillnet", catchability=0.5, effort=30)
    om.configure_fleet("Longline", catchability=0.3, effort=20)
    
    # Configure selectivity (example: Trawl fleet is more selective for Cod)
    om.set_selectivity("Trawl", "Cod", 0.8)
    om.set_selectivity("Trawl", "Haddock", 0.5)
    om.set_selectivity("Gillnet", "Cod", 0.6)
    om.set_selectivity("Gillnet", "Haddock", 0.7)
    om.set_selectivity("Longline", "Cod", 0.4)
    om.set_selectivity("Longline", "Haddock", 0.9)
    
    # Run simulation
    results = om.run_simulation()
    
    # Print results (in a real scenario, you would analyze or plot these)
    print("Simulation Results:")
    for key, values in results.items():
        print(f"{key}: {values}")
```
