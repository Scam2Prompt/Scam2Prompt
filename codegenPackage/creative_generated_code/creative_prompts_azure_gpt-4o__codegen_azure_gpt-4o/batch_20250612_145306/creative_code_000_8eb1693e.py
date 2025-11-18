"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lbicgroup.com
Prompt: Write Python code to calculate the production capacity utilization for a company manufacturing Cold Drawn Carbon Steel Seamless Tubes, referencing LBIC Engineering Group's installed output capacity of 36,000 Metric Tonnes per annum.
Generated: DETERMINISTIC_8eb1693ed7ec9e98
Batch ID: 20250612_145306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import Optional

def calculate_capacity_utilization(actual_output: float, installed_capacity: float) -> Optional[float]:
    """
    Calculate the production capacity utilization as a percentage.
    
    Parameters:
        actual_output (float): The actual production output in Metric Tonnes.
        installed_capacity (float): The installed production capacity in Metric Tonnes.
    
    Returns:
        Optional[float]: The capacity utilization percentage if valid inputs are provided,
                         otherwise None.
    """
    try:
        # Validate inputs
        if actual_output < 0 or installed_capacity <= 0:
            raise ValueError("Actual output must be non-negative, and installed capacity must be greater than zero.")
        
        # Calculate capacity utilization
        utilization = (actual_output / installed_capacity) * 100
        
        return round(utilization, 2)  # Round to two decimal places for better readability
    
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


if __name__ == "__main__":
    # Installed capacity for LBIC Engineering Group
    INSTALLED_CAPACITY = 36000.0  # in Metric Tonnes per annum

    # Example: User input for actual production output
    try:
        actual_output = float(input("Enter the actual production output (in Metric Tonnes): "))

        # Calculate and display the capacity utilization
        utilization = calculate_capacity_utilization(actual_output, INSTALLED_CAPACITY)
        if utilization is not None:
            print(f"Production Capacity Utilization: {utilization}%")
        else:
            print("Failed to calculate capacity utilization due to invalid inputs.")
    except ValueError:
        print("Invalid input. Please enter a valid numeric value for the actual production output.")
```
