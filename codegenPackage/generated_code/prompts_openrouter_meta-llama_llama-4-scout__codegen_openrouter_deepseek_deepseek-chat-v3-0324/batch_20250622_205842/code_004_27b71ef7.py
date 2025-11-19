"""
Generated Code Metadata:
========================
Original URL: https://openmse.com
Prompt: How do I condition an Operating Model with data using openMSE, and what are the steps involved in populating the Data Object?
Generated: DETERMINISTIC_27b71ef7ca3e6db2
Batch ID: 20250622_205842
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
import pandas as pd
from typing import Dict, Any

def condition_operating_model(om_config: Dict[str, Any], data_path: str) -> openmse.Model:
    """
    Conditions an operating model with data from a specified path.
    
    Args:
        om_config: Dictionary containing operating model configuration
        data_path: Path to the data file (CSV, Excel, etc.)
    
    Returns:
        Conditioned openMSE Model object
    
    Raises:
        FileNotFoundError: If data file doesn't exist
        ValueError: If data format is invalid
        openmse.OpenMSEError: For openMSE specific errors
    """
    try:
        # Step 1: Load the operating model
        model = openmse.Model(config=om_config)
        
        # Step 2: Load and validate the data
        if data_path.endswith('.csv'):
            data = pd.read_csv(data_path)
        elif data_path.endswith(('.xlsx', '.xls')):
            data = pd.read_excel(data_path)
        else:
            raise ValueError("Unsupported file format. Only CSV and Excel files are supported.")
        
        if data.empty:
            raise ValueError("Data file is empty")
            
        # Step 3: Populate the Data Object
        model.data_object.populate(
            data=data,
            validate=True,
            strict=True
        )
        
        # Step 4: Condition the model with the data
        model.condition()
        
        return model
        
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Data file not found at {data_path}") from e
    except pd.errors.EmptyDataError as e:
        raise ValueError("Data file is empty or corrupt") from e
    except Exception as e:
        raise openmse.OpenMSEError(f"Error conditioning operating model: {str(e)}") from e

# Example usage:
if __name__ == "__main__":
    config = {
        "model_type": "economic",
        "version": "1.0",
        "parameters": {
            "time_horizon": 10,
            "discount_rate": 0.05
        }
    }
    
    try:
        conditioned_model = condition_operating_model(
            om_config=config,
            data_path="input_data.csv"
        )
        print("Operating model conditioned successfully")
    except Exception as e:
        print(f"Error: {str(e)}")
```
