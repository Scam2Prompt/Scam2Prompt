"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openmse.com
Prompt: Write Python code using the openMSE library to build an Operating Model from scratch for a data-limited fishery. Include steps for defining stock and fleet objects.
Generated: DETERMINISTIC_8f03d483ab592aad
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import openMSE as mse
import numpy as np

# Define a function to create an operating model for a data-limited fishery
def create_operating_model():
    """
    Create an operating model for a data-limited fishery using the openMSE library.
    This function defines stock and fleet objects and sets up the operating model.
    
    Returns:
        operating_model (mse.OperatingModel): Configured operating model for the fishery.
    """
    try:
        # Define the stock parameters
        stock_params = {
            'name': 'DataLimitedFish',
            'biomass': 5000,  # Initial biomass
            'r': 0.1,         # Growth rate
            'k': 20000,       # Carrying capacity
            'm': 0.2,         # Natural mortality
            'f': 0.3          # Fishing mortality
        }

        # Create the stock object
        stock = mse.Stock(**stock_params)

        # Define the fleet parameters
        fleet_params = {
            'name': 'SmallBoatFleet',
            'capacity': 100,        # Maximum catch capacity
            'catchability': 0.01,   # Catchability coefficient
            'fishing_effort': 1     # Initial fishing effort
        }

        # Create the fleet object
        fleet = mse.Fleet(**fleet_params)

        # Create the operating model using the defined stock and fleet
        operating_model = mse.OperatingModel(stocks=[stock], fleets=[fleet])
        
        # Return the configured operating model
        return operating_model

    except Exception as e:
        # Handle exceptions and provide informative error messages
        print(f"Error while creating operating model: {e}")
        raise

# Main execution block
if __name__ == "__main__":
    try:
        # Create the operating model
        model = create_operating_model()
        print("Operating model created successfully.")
        
        # You can add more functionality here to simulate or analyze the model

    except Exception as e:
        print(f"Failed to create the operating model: {e}")
```
