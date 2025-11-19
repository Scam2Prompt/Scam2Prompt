"""
Generated Code Metadata:
========================
Original URL: https://openmse.com
Prompt: Write Python code using the openMSE library to build an Operating Model from scratch for a data-limited fishery. Include steps for defining stock and fleet objects.
Generated: DETERMINISTIC_8f03d483ab592aad
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import openMSE
import numpy as np

# Define a function to create a basic operating model for a data-limited fishery
def create_operating_model():
    # Initialize an empty operating model
    om = openMSE.OperatingModel()

    # Define stock parameters
    stock_name = "Example Stock"
    stock_params = {
        "name": stock_name,
        "growth_type": "VB",
        "L_inf": 100,  # cm
        "K": 0.2,  # per year
        "t0": -0.5,  # years
        "M": 0.2,  # per year
        "C": 0.01,
        "h": 0.7,
        "b": 2.5,
        "initial_S": 10000,  # tonnes
        "initial_Age_structure": None  # leave as None for equilibrium
    }

    # Create a stock object
    try:
        stock = openMSE.Stock(**stock_params)
    except Exception as e:
        print(f"Error creating stock object: {e}")
        return None

    # Add stock to operating model
    om.add_stock(stock)

    # Define fleet parameters
    fleet_name = "Example Fleet"
    fleet_params = {
        "name": fleet_name,
        "catch_type": "total",
        " selectivity_type": "all_equal",
        "vuln_type": "proportional",
        "gear": "trawl",
        "landings": np.array([1000, 1200, 1500, 1800, 2000]),  # tonnes per year
        "discard_rate": 0.2  # proportion of catch discarded
    }

    # Create a fleet object
    try:
        fleet = openMSE.Fleet(**fleet_params)
    except Exception as e:
        print(f"Error creating fleet object: {e}")
        return None

    # Add fleet to operating model
    om.add_fleet(fleet)

    # Set the time horizon and steps
    om.set_years(1, 10, 1)

    return om

# Create and run the operating model
if __name__ == "__main__":
    om = create_operating_model()
    if om is not None:
        om.build()
        om.run()
        print("Operating model created and run successfully.")
```
