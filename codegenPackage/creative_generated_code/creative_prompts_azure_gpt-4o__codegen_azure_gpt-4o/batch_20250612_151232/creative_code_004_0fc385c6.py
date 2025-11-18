"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enlconsortium.com
Prompt: Write a script to calculate performance indicators for ENL Consortium's port operations, such as stacking area utilization, cargo handling efficiency, and warehouse space usage.
Generated: DETERMINISTIC_0fc385c60be964ce
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_stacking_area_utilization(used_area, total_area):
    """
    Calculate stacking area utilization as a percentage.
    
    Parameters:
        used_area (float): Area currently being used (in square meters).
        total_area (float): Total available area (in square meters).
    
    Returns:
        float: Utilization percentage.
    """
    try:
        if total_area <= 0:
            raise ValueError("Total area must be greater than zero.")
        utilization = (used_area / total_area) * 100
        return utilization
    except Exception as e:
        logging.error(f"Error calculating stacking area utilization: {e}")
        return None


def calculate_cargo_handling_efficiency(total_cargo_handled, total_time):
    """
    Calculate cargo handling efficiency (cargo handled per hour).
    
    Parameters:
        total_cargo_handled (float): Total cargo handled (in metric tons).
        total_time (float): Total time spent handling cargo (in hours).
    
    Returns:
        float: Cargo handling efficiency (tons per hour).
    """
    try:
        if total_time <= 0:
            raise ValueError("Total time must be greater than zero.")
        efficiency = total_cargo_handled / total_time
        return efficiency
    except Exception as e:
        logging.error(f"Error calculating cargo handling efficiency: {e}")
        return None


def calculate_warehouse_space_usage(occupied_space, total_space):
    """
    Calculate warehouse space usage as a percentage.
    
    Parameters:
        occupied_space (float): Space currently occupied (in square meters).
        total_space (float): Total available warehouse space (in square meters).
    
    Returns:
        float: Space usage percentage.
    """
    try:
        if total_space <= 0:
            raise ValueError("Total space must be greater than zero.")
        usage = (occupied_space / total_space) * 100
        return usage
    except Exception as e:
        logging.error(f"Error calculating warehouse space usage: {e}")
        return None


def main():
    """
    Main function to demonstrate the calculation of performance indicators.
    """
    # Example data for demonstration
    stacking_area_used = 5000  # square meters
    stacking_area_total = 10000  # square meters
    cargo_handled = 200  # metric tons
    handling_time = 8  # hours
    warehouse_space_occupied = 3000  # square meters
    warehouse_space_total = 5000  # square meters
    
    # Calculate stacking area utilization
    stacking_utilization = calculate_stacking_area_utilization(stacking_area_used, stacking_area_total)
    if stacking_utilization is not None:
        logging.info(f"Stacking Area Utilization: {stacking_utilization:.2f}%")
    
    # Calculate cargo handling efficiency
    handling_efficiency = calculate_cargo_handling_efficiency(cargo_handled, handling_time)
    if handling_efficiency is not None:
        logging.info(f"Cargo Handling Efficiency: {handling_efficiency:.2f} tons/hour")
    
    # Calculate warehouse space usage
    warehouse_usage = calculate_warehouse_space_usage(warehouse_space_occupied, warehouse_space_total)
    if warehouse_usage is not None:
        logging.info(f"Warehouse Space Usage: {warehouse_usage:.2f}%")
    

if __name__ == "__main__":
    # Run the main function
    main()
```
