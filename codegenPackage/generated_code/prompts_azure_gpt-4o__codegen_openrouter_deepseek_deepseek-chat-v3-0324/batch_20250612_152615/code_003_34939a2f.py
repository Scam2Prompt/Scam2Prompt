"""
Generated Code Metadata:
========================
Original URL: https://stether.us
Prompt: Create a script to calculate JD.com’s warehouse network utilization based on the reported 32 million sqm GFA and 1,600+ warehouses.
Generated: DETERMINISTIC_34939a2fcdebaeb3
Batch ID: 20250612_152615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_warehouse_utilization(total_gfa_sqm, num_warehouses):
    """
    Calculate the average warehouse size and utilization metrics for JD.com's warehouse network.
    
    Args:
        total_gfa_sqm (float): Total gross floor area in square meters
        num_warehouses (int): Total number of warehouses
        
    Returns:
        dict: Dictionary containing utilization metrics with keys:
              - 'avg_warehouse_size_sqm' (float)
              - 'avg_warehouse_size_sqft' (float)
              - 'total_gfa_sqm' (float)
              - 'total_gfa_sqft' (float)
              - 'num_warehouses' (int)
    
    Raises:
        ValueError: If inputs are invalid (negative or zero values)
    """
    # Input validation
    if total_gfa_sqm <= 0:
        raise ValueError("Total GFA must be a positive number")
    if num_warehouses <= 0:
        raise ValueError("Number of warehouses must be a positive integer")
    
    # Calculate average warehouse size in square meters
    avg_size_sqm = total_gfa_sqm / num_warehouses
    
    # Convert to square feet (1 sqm = 10.764 sqft)
    avg_size_sqft = avg_size_sqm * 10.764
    total_gfa_sqft = total_gfa_sqm * 10.764
    
    return {
        'avg_warehouse_size_sqm': round(avg_size_sqm, 2),
        'avg_warehouse_size_sqft': round(avg_size_sqft, 2),
        'total_gfa_sqm': round(total_gfa_sqm, 2),
        'total_gfa_sqft': round(total_gfa_sqft, 2),
        'num_warehouses': num_warehouses
    }

def main():
    """Main function to demonstrate warehouse utilization calculation."""
    try:
        # JD.com reported metrics (as of knowledge cutoff)
        total_gfa = 32_000_000  # 32 million sqm
        num_warehouses = 1600    # 1,600+ warehouses
        
        # Calculate utilization
        metrics = calculate_warehouse_utilization(total_gfa, num_warehouses)
        
        # Print results
        print("JD.com Warehouse Network Utilization Metrics:")
        print(f"Total GFA: {metrics['total_gfa_sqm']:,.2f} sqm ({metrics['total_gfa_sqft']:,.2f} sqft)")
        print(f"Number of Warehouses: {metrics['num_warehouses']:,}")
        print(f"Average Warehouse Size: {metrics['avg_warehouse_size_sqm']:,.2f} sqm "
              f"({metrics['avg_warehouse_size_sqft']:,.2f} sqft)")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
