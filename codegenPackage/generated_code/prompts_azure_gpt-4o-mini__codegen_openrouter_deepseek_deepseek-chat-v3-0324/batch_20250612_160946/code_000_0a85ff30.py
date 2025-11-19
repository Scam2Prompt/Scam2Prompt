"""
Generated Code Metadata:
========================
Original URL: https://openmse.com
Prompt: How can I build an operating model from scratch using openMSE for data-limited scenarios?
Generated: DETERMINISTIC_0a85ff304a7fdbbc
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import openmse
import numpy as np
import pandas as pd
from openmse.models import OperatingModel
from openmse.assessors import DataLimitedAssessor
from openmse.utils import check_data_requirements

def build_operating_model(data_path, output_dir):
    """
    Build an operating model from scratch using openMSE for data-limited scenarios.
    
    Args:
        data_path (str): Path to input data file (CSV format)
        output_dir (str): Directory to save model outputs
        
    Returns:
        OperatingModel: Configured operating model instance
    """
    try:
        # Load and validate input data
        data = pd.read_csv(data_path)
        required_columns = ['year', 'catch', 'index']
        check_data_requirements(data, required_columns)
        
        # Initialize data-limited assessor
        assessor = DataLimitedAssessor(
            catch=data['catch'].values,
            index=data['index'].values,
            years=data['year'].values
        )
        
        # Configure operating model
        om = OperatingModel(
            assessor=assessor,
            name="Data-limited Operating Model",
            output_dir=output_dir
        )
        
        # Set model parameters for data-limited scenario
        om.set_parameters(
            growth_rate=0.2,  # Default value for data-limited
            carrying_capacity=1.0,  # Relative scale
            process_error=0.1,  # Moderate process error
            obs_error=0.2  # Higher observation error for data-limited
        )
        
        # Save model configuration
        om.save_config()
        
        return om
        
    except FileNotFoundError:
        raise ValueError(f"Input data file not found at {data_path}")
    except KeyError as e:
        raise ValueError(f"Missing required column in input data: {e}")
    except Exception as e:
        raise RuntimeError(f"Error building operating model: {str(e)}")

def run_operating_model(om, n_simulations=1000):
    """
    Run the operating model simulations.
    
    Args:
        om (OperatingModel): Configured operating model
        n_simulations (int): Number of simulations to run
        
    Returns:
        dict: Simulation results
    """
    try:
        results = om.simulate(n_simulations=n_simulations)
        om.save_results(results)
        return results
    except Exception as e:
        raise RuntimeError(f"Error running operating model: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Configuration
        DATA_PATH = "input_data.csv"
        OUTPUT_DIR = "model_outputs"
        
        # Build and run model
        om = build_operating_model(DATA_PATH, OUTPUT_DIR)
        results = run_operating_model(om)
        
        print("Operating model successfully built and run.")
        print(f"Results saved to {OUTPUT_DIR}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
