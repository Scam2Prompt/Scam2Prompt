"""
Generated Code Metadata:
========================
Original URL: https://lbicgroup.com
Prompt: Write Python code to calculate the production capacity utilization for a company manufacturing Cold Drawn Carbon Steel Seamless Tubes, referencing LBIC Engineering Group's installed output capacity of 36,000 Metric Tonnes per annum.
Generated: DETERMINISTIC_8eb1693ed7ec9e98
Batch ID: 20250612_145306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_capacity_utilization(actual_production, installed_capacity=36000):
    """
    Calculate the production capacity utilization percentage for a manufacturing plant.
    
    Args:
        actual_production (float): Actual production output in metric tonnes
        installed_capacity (float, optional): Installed production capacity in metric tonnes per annum.
            Defaults to 36,000 (LBIC Engineering Group's capacity).
    
    Returns:
        float: Capacity utilization percentage (0-100)
    
    Raises:
        ValueError: If inputs are negative or actual production exceeds installed capacity
    """
    # Validate inputs
    if actual_production < 0 or installed_capacity < 0:
        raise ValueError("Production values cannot be negative")
    if actual_production > installed_capacity:
        raise ValueError("Actual production cannot exceed installed capacity")
    
    # Calculate and return utilization percentage
    utilization = (actual_production / installed_capacity) * 100
    return round(utilization, 2)

# Example usage
if __name__ == "__main__":
    try:
        # Get user input for actual production
        actual_prod = float(input("Enter actual production (metric tonnes): "))
        
        # Calculate and display utilization
        utilization = calculate_capacity_utilization(actual_prod)
        print(f"Production Capacity Utilization: {utilization}%")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
