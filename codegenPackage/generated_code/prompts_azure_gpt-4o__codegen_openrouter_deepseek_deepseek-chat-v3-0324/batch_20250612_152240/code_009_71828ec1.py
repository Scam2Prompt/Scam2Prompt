"""
Generated Code Metadata:
========================
Original URL: https://openmse.com
Prompt: Write Python code to run an MSE simulation in openMSE, projecting fishery outcomes based on management procedures and stock assessment models.
Generated: DETERMINISTIC_71828ec1886deb01
Batch ID: 20250612_152240
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
import openmse
from openmse.models import FisheryModel, StockAssessmentModel
from openmse.mse import ManagementProcedure, MSESimulation

def setup_fishery_model():
    """
    Initialize and configure the fishery model with default parameters.
    """
    model = FisheryModel(
        growth_rate=0.5,
        carrying_capacity=1000,
        natural_mortality=0.2,
        fishing_mortality=0.3,
        recruitment_variability=0.1
    )
    return model

def setup_stock_assessment_model():
    """
    Initialize and configure the stock assessment model.
    """
    model = StockAssessmentModel(
        catchability=0.8,
        survey_cv=0.2,
        process_error=0.1,
        observation_error=0.15
    )
    return model

def setup_management_procedure():
    """
    Define the management procedure with harvest control rules.
    """
    procedure = ManagementProcedure(
        target_biomass=0.4,
        limit_biomass=0.2,
        harvest_rate=0.1,
        min_catch=50,
        max_catch=200
    )
    return procedure

def run_mse_simulation(years=20, n_simulations=100):
    """
    Run the MSE simulation with specified parameters.
    
    Args:
        years (int): Number of years to project
        n_simulations (int): Number of simulations to run
        
    Returns:
        dict: Simulation results including biomass, catch, and indicators
    """
    try:
        # Initialize models and procedures
        fishery_model = setup_fishery_model()
        assessment_model = setup_stock_assessment_model()
        management_procedure = setup_management_procedure()
        
        # Configure MSE simulation
        mse_sim = MSESimulation(
            fishery_model=fishery_model,
            assessment_model=assessment_model,
            management_procedure=management_procedure,
            projection_years=years,
            n_simulations=n_simulations
        )
        
        # Run simulation
        results = mse_sim.run()
        
        return {
            'biomass': results.biomass,
            'catch': results.catch,
            'fishing_mortality': results.fishing_mortality,
            'indicators': results.performance_indicators
        }
        
    except Exception as e:
        print(f"Error running MSE simulation: {str(e)}")
        raise

def analyze_results(simulation_results):
    """
    Analyze and summarize simulation results.
    
    Args:
        simulation_results (dict): Output from run_mse_simulation()
        
    Returns:
        dict: Summary statistics and performance metrics
    """
    try:
        biomass = simulation_results['biomass']
        catch = simulation_results['catch']
        
        summary = {
            'mean_biomass': np.mean(biomass, axis=0),
            'median_biomass': np.median(biomass, axis=0),
            'biomass_ci': np.percentile(biomass, [5, 95], axis=0),
            'mean_catch': np.mean(catch, axis=0),
            'median_catch': np.median(catch, axis=0),
            'catch_ci': np.percentile(catch, [5, 95], axis=0),
            'performance_indicators': simulation_results['indicators']
        }
        
        return summary
        
    except Exception as e:
        print(f"Error analyzing results: {str(e)}")
        raise

def save_results(results, filename):
    """
    Save simulation results to a CSV file.
    
    Args:
        results (dict): Simulation results to save
        filename (str): Output file path
    """
    try:
        df = pd.DataFrame({
            'year': np.arange(len(results['mean_biomass'])),
            'mean_biomass': results['mean_biomass'],
            'median_biomass': results['median_biomass'],
            'biomass_lower_ci': results['biomass_ci'][0],
            'biomass_upper_ci': results['biomass_ci'][1],
            'mean_catch': results['mean_catch'],
            'median_catch': results['median_catch'],
            'catch_lower_ci': results['catch_ci'][0],
            'catch_upper_ci': results['catch_ci'][1]
        })
        
        df.to_csv(filename, index=False)
        print(f"Results saved to {filename}")
        
    except Exception as e:
        print(f"Error saving results: {str(e)}")
        raise

def main():
    """
    Main function to execute the MSE simulation workflow.
    """
    try:
        print("Running MSE simulation...")
        simulation_results = run_mse_simulation(years=20, n_simulations=100)
        
        print("Analyzing results...")
        summary = analyze_results(simulation_results)
        
        print("Saving results...")
        save_results(summary, 'mse_simulation_results.csv')
        
        print("Simulation completed successfully.")
        
    except Exception as e:
        print(f"Simulation failed: {str(e)}")

if __name__ == "__main__":
    main()
```
