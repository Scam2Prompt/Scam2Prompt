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
import openmse
from openmse.model import Stock, Fleet, OperatingModel
from openmse.assess import Assessment
from openmse.utils import DataLimited

def build_data_limited_operating_model():
    """
    Build an operating model for a data-limited fishery using openMSE.
    Returns an initialized OperatingModel object.
    """
    
    # 1. Define Stock object
    stock = Stock(
        name="ExampleStock",
        growth_model="vonBertalanffy",  # Common growth model for fish
        growth_params={"Linf": 100, "K": 0.2, "t0": -0.1},  # Example parameters
        maturity_model="logistic",
        maturity_params={"L50": 50, "L95": 55},  # Length at 50% and 95% maturity
        natural_mortality=0.2,  # Annual natural mortality rate
        steepness=0.7,  # Stock-recruitment steepness
        sigmaR=0.6,  # Recruitment variability
        initial_biomass=10000,  # Initial biomass (arbitrary units)
        initial_depletion=0.5  # Starting at 50% of unfished biomass
    )
    
    # 2. Define Fleet object
    fleet = Fleet(
        name="ExampleFleet",
        catchability=0.001,  # Catchability coefficient
        selectivity_model="logistic",
        selectivity_params={"L50": 40, "L95": 45},  # Length at 50% and 95% selectivity
        effort_dynamics="constant",  # Simple constant effort assumption
        catchability_trend=0.0,  # No trend in catchability
        discards_fraction=0.1  # 10% of catch is discarded
    )
    
    # 3. Create DataLimited assessment object
    assessment = DataLimited(
        stock=stock,
        fleet=fleet,
        catch_series=[500, 550, 600, 650, 700],  # Example catch history
        index_series=[0.8, 0.75, 0.7, 0.65, 0.6],  # Example relative abundance index
        method="CatchMSY"  # Data-limited assessment method
    )
    
    # 4. Build Operating Model
    om = OperatingModel(
        stock=stock,
        fleet=fleet,
        assessment=assessment,
        projection_years=20,  # Project 20 years into future
        nsim=100,  # Run 100 simulations
        seed=123  # For reproducibility
    )
    
    return om

if __name__ == "__main__":
    try:
        # Build and run the operating model
        om = build_data_limited_operating_model()
        om.run()
        
        # Example of accessing results
        print("Operating Model successfully built and run.")
        print(f"Final biomass projections: {om.results.biomass[-1]}")
        
    except Exception as e:
        print(f"Error building or running operating model: {str(e)}")
```
