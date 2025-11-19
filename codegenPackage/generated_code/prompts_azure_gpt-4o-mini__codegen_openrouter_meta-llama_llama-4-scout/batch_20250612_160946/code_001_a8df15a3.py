"""
Generated Code Metadata:
========================
Original URL: https://openmse.com
Prompt: What are the steps to condition an operating model with data in openMSE, and how does it differ for data-moderate conditions?
Generated: DETERMINISTIC_a8df15a363e00028
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide the code, but I need to clarify that I'll be using Python as the programming language. Here's the code:

```python
import pandas as pd
from openMSE.model.osm import OperatingModel
from openMSE.model.estimation import Estimation
from openMSE.model.scenarios import Scenario
from openMSE.model.biology import Biology
from openMSE.model.fisheries import Fishery

def condition_osm_with_data(osm: OperatingModel, 
                           data: pd.DataFrame, 
                           data_moderate: bool = False) -> OperatingModel:
    """
    Conditions an operating model with data.

    Args:
    - osm (OperatingModel): The operating model to condition.
    - data (pd.DataFrame): The data to condition with.
    - data_moderate (bool): Whether to use data-moderate conditions. Defaults to False.

    Returns:
    - OperatingModel: The conditioned operating model.
    """

    # Check if data is provided
    if data is None:
        raise ValueError("Data is required to condition the operating model")

    # Set up estimation object
    estimation = Estimation(osm, data)

    # Condition operating model with data
    if data_moderate:
        # Use data-moderate conditions
        estimation.configure_data_moderate()
    else:
        # Use default conditions
        pass  # default conditions already set up in estimation

    # Run estimation to condition operating model
    try:
        estimation.run_estimation()
    except Exception as e:
        print(f"Error running estimation: {str(e)}")

    # Update operating model with estimated parameters
    osm.update_parameters(estimation.get_estimated_parameters())

    return osm

def main():
    # Example usage:
    # Create an operating model
    osm = OperatingModel()

    # Create a scenario
    scenario = Scenario()

    # Create biology object
    biology = Biology()

    # Create fishery object
    fishery = Fishery()

    # Configure operating model
    osm.configure_osm(scenario, biology, fishery)

    # Sample data
    data = pd.DataFrame({
        'year': [2010, 2011, 2012],
        'catch': [100, 120, 110],
        'survey biomass': [1000, 900, 1100]
    })

    # Condition operating model with data
    conditioned_osm = condition_osm_with_data(osm, data)

    # Condition operating model with data-moderate conditions
    conditioned_osm_moderate = condition_osm_with_data(osm, data, data_moderate=True)

if __name__ == "__main__":
    main()
```
