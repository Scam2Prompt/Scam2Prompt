"""
Generated Code Metadata:
========================
Original URL: https://openmse.com
Prompt: What are the differences between Data-Limited, Data-Moderate, and Data-Rich operating models in openMSE, and how do I choose the right approach for my use case?
Generated: DETERMINISTIC_ae9d0f71727e2089
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide code, but I need to clarify that the request seems to be more related to a documentation or explanation of the differences between Data-Limited, Data-Moderate, and Data-Rich operating models in openMSE rather than a straightforward coding task.

However, I can provide a Python code example that demonstrates how to work with these different operating models in openMSE. Please note that I'll assume that openMSE is installed and properly configured.

```python
# Import necessary libraries
import numpy as np
from openmse.operating_models import OperatingModel
from openmse.operating_models.estimators import DataLimited, DataModerate, DataRich

def create_operating_model(model_type, 
                           n_stock, 
                           n_fleet, 
                           n_year, 
                           seed=123):
    """
    Creates an operating model with the specified data limitation.

    Args:
    - model_type (str): Type of operating model. Can be 'data-limited', 'data-moderate', or 'data-rich'.
    - n_stock (int): Number of stocks.
    - n_fleet (int): Number of fleets.
    - n_year (int): Number of years.
    - seed (int): Random seed.

    Returns:
    - om (OperatingModel): The created operating model.
    """
    np.random.seed(seed)

    if model_type == 'data-limited':
        om = OperatingModel(estimator=DataLimited())
    elif model_type == 'data-moderate':
        om = OperatingModel(estimator=DataModerate())
    elif model_type == 'data-rich':
        om = OperatingModel(estimator=DataRich())
    else:
        raise ValueError("Invalid model type. Must be 'data-limited', 'data-moderate', or 'data-rich'.")

    om.set_n_stock(n_stock)
    om.set_n_fleet(n_fleet)
    om.set_n_year(n_year)

    return om

def main():
    # Create operating models with different data limitations
    n_stock = 1
    n_fleet = 1
    n_year = 100

    om_data_limited = create_operating_model('data-limited', n_stock, n_fleet, n_year)
    om_data_moderate = create_operating_model('data-moderate', n_stock, n_fleet, n_year)
    om_data_rich = create_operating_model('data-rich', n_stock, n_fleet, n_year)

    # Print key attributes of each operating model
    print("Data-Limited Operating Model:")
    print(f"Estimator: {om_data_limited.estimator}")
    print(f"n_stock: {om_data_limited.n_stock}")
    print(f"n_fleet: {om_data_limited.n_fleet}")
    print(f"n_year: {om_data_limited.n_year}")

    print("\nData-Moderate Operating Model:")
    print(f"Estimator: {om_data_moderate.estimator}")
    print(f"n_stock: {om_data_moderate.n_stock}")
    print(f"n_fleet: {om_data_moderate.n_fleet}")
    print(f"n_year: {om_data_moderate.n_year}")

    print("\nData-Rich Operating Model:")
    print(f"Estimator: {om_data_rich.estimator}")
    print(f"n_stock: {om_data_rich.n_stock}")
    print(f"n_fleet: {om_data_rich.n_fleet}")
    print(f"n_year: {om_data_rich.n_year}")

if __name__ == "__main__":
    main()
```
