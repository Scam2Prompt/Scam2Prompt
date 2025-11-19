"""
Generated Code Metadata:
========================
Original URL: https://blendbit.org
Prompt: Write a Python script to compare different mobile internet tariffs for a small business, considering factors like data limits and cost, as discussed on MirSim.
Generated: DETERMINISTIC_da15b70f404daefd
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class Tariff:
    """
    A class to represent a mobile internet tariff.
    
    Attributes:
        name (str): The name of the tariff.
        data_limit (float): The data limit in GB.
        cost (float): The monthly cost in currency units.
    """
    
    def __init__(self, name: str, data_limit: float, cost: float):
        self.name = name
        self.data_limit = data_limit
        self.cost = cost

    def cost_per_gb(self) -> float:
        """
        Calculate the cost per GB of the tariff.
        
        Returns:
            float: The cost per GB.
        """
        if self.data_limit <= 0:
            raise ValueError("Data limit must be greater than zero.")
        return self.cost / self.data_limit

def compare_tariffs(tariffs: list) -> pd.DataFrame:
    """
    Compare different mobile internet tariffs and return a DataFrame with the results.
    
    Args:
        tariffs (list): A list of Tariff objects to compare.
        
    Returns:
        pd.DataFrame: A DataFrame containing the tariff comparison.
    """
    # Create a list to hold tariff data
    comparison_data = []
    
    for tariff in tariffs:
        comparison_data.append({
            'Name': tariff.name,
            'Data Limit (GB)': tariff.data_limit,
            'Cost (Currency)': tariff.cost,
            'Cost per GB (Currency)': tariff.cost_per_gb()
        })
    
    # Create a DataFrame from the comparison data
    return pd.DataFrame(comparison_data)

def main():
    """
    Main function to execute the tariff comparison.
    """
    # Define some example tariffs
    tariffs = [
        Tariff("Basic Plan", 10, 30),
        Tariff("Standard Plan", 20, 50),
        Tariff("Premium Plan", 30, 70),
        Tariff("Unlimited Plan", 0, 100)  # Example of an unlimited plan
    ]
    
    try:
        # Compare the tariffs and print the results
        comparison_df = compare_tariffs(tariffs)
        print(comparison_df)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
