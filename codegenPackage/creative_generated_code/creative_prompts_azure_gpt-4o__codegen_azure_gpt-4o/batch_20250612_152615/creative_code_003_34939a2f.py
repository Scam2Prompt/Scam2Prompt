"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stether.us
Prompt: Create a script to calculate JD.com’s warehouse network utilization based on the reported 32 million sqm GFA and 1,600+ warehouses.
Generated: DETERMINISTIC_34939a2fcdebaeb3
Batch ID: 20250612_152615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sys

def calculate_utilization(total_gfa, total_warehouses):
    """
    Calculate the average utilization of JD.com's warehouse network.
    
    Parameters:
    total_gfa (float): Total gross floor area in square meters across all warehouses.
    total_warehouses (int): Number of warehouses.
    
    Returns:
    float: Average utilization in square meters per warehouse.
    """
    try:
        # Validate inputs
        if total_gfa <= 0 or total_warehouses <= 0:
            raise ValueError("Both total_gfa and total_warehouses must be greater than zero.")
        
        # Calculate utilization
        utilization = total_gfa / total_warehouses
        return utilization
    
    except TypeError:
        raise TypeError("Inputs must be a float for total_gfa and an int for total_warehouses.")
    except Exception as e:
        raise Exception(f"An error occurred: {str(e)}")

def main():
    """
    Main function to calculate JD.com's warehouse network utilization.
    """
    try:
        # Inputs for GFA and number of warehouses
        total_gfa = 32_000_000  # Gross floor area in square meters
        total_warehouses = 1600  # Number of warehouses
        
        # Calculate utilization
        utilization = calculate_utilization(total_gfa, total_warehouses)
        
        # Print the result
        print(f"Warehouse Network Utilization: {utilization:.2f} sqm per warehouse")
    
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    # Execute the main function
    main()
```
