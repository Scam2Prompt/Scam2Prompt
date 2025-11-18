"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openmse.com
Prompt: Create Python code to simulate multi-stock and multi-fleet Operating Models using openMSE. Include an example of configuring fleet selectivity.
Generated: DETERMINISTIC_138c5ad06a95dfc7
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Simulate multi-stock and multi-fleet Operating Models using openMSE.

This script demonstrates how to set up multi-stock and multi-fleet operating models
and configure fleet selectivity using the openMSE library.

Note: Ensure you have installed openMSE (`pip install openmse`) to execute this code.
"""

import openmse as mse
import numpy as np

def multi_stock_multi_fleet_simulation():
    # Initialize OpenMSE operating model configuration
    try:
        # Define parameters for stocks
        num_stocks = 2
        stock_names = ["Stock_A", "Stock_B"]
        stock_biomass = [1000, 2000]  # Initial biomass for each stock
        stock_growth_rates = [0.05, 0.03]  # Growth rates (per year)
        stock_carrying_capacities = [5000, 7000]  # Carrying capacities

        # Define parameters for fleets
        num_fleets = 3
        fleet_names = ["Fleet_1", "Fleet_2", "Fleet_3"]
        fleet_effort = [0.1, 0.2, 0.3]  # Initial fishing effort for each fleet

        # Create stocks
        stocks = []
        for i in range(num_stocks):
            stock = mse.Stock(
                name=stock_names[i],
                biomass=stock_biomass[i],
                growth_rate=stock_growth_rates[i],
                carrying_capacity=stock_carrying_capacities[i]
            )
            stocks.append(stock)

        # Configure fleet selectivity for each stock and fleet
        fleets = []
        for i in range(num_fleets):
            # Fleet selectivity values (arbitrarily defined for example purposes)
            selectivity = np.random.uniform(0, 1, num_stocks).tolist()
            
            fleet = mse.Fleet(
                name=fleet_names[i],
                effort=fleet_effort[i],
                selectivity=selectivity  # Configure selectivity per stock
            )
            fleets.append(fleet)

        # Initialize the Operating Model
        operating_model = mse.OperatingModel(stocks=stocks, fleets=fleets)

        # Run the simulation
        years = 10  # Number of years to simulate
        results = operating_model.simulate(years=years)

        # Display the results
        print(f"Simulation complete! Results for {years} years:")
        for year in range(years):
            print(f"Year {year + 1}:")
            for stock in stocks:
                print(f"  {stock.name} biomass: {results[stock.name]['biomass'][year]}")
            for fleet in fleets:
                print(f"  {fleet.name} effort: {results[fleet.name]['effort'][year]}")

    except Exception as e:
        print(f"An error occurred during simulation: {str(e)}")
        raise

# Execute the simulation function
if __name__ == "__main__":
    multi_stock_multi_fleet_simulation()
```
