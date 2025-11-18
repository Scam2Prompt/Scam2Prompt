"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertiv.dns.cz
Prompt: Create a Python function to simulate power load balancing using Vertiv's UPS systems in a multi-rack data center environment.
Generated: DETERMINISTIC_b8282cff2b2a9de4
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Set up logging for the application
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def power_load_balancing(rack_power_demands, ups_capacity):
    """
    Simulates power load balancing using Vertiv's UPS systems in a multi-rack data center environment.

    Args:
        rack_power_demands (list): A list of power demands (in kW) for each rack.
        ups_capacity (float): Maximum power capacity of the UPS system (in kW).

    Returns:
        dict: Dictionary containing load allocation details for each rack and remaining capacity of the UPS.
    """
    try:
        # Validate input types
        if not isinstance(rack_power_demands, list) or not all(isinstance(d, (int, float)) for d in rack_power_demands):
            raise ValueError("rack_power_demands must be a list of numeric values.")
        
        if not isinstance(ups_capacity, (int, float)) or ups_capacity <= 0:
            raise ValueError("ups_capacity must be a positive numeric value.")

        # Initialize load allocation result
        load_allocation = {}
        remaining_capacity = ups_capacity

        for i, demand in enumerate(rack_power_demands):
            rack_id = f"Rack_{i+1}"

            if remaining_capacity >= demand:
                # Fully satisfy the rack's demand
                load_allocation[rack_id] = demand
                remaining_capacity -= demand
            else:
                # Partially satisfy the rack's demand if UPS capacity is insufficient
                load_allocation[rack_id] = remaining_capacity
                remaining_capacity = 0
                logging.warning(
                    f"{rack_id}'s demand of {demand}kW could not be fully met. "
                    f"Allocated {load_allocation[rack_id]}kW."
                )
                break  # No more capacity left in the UPS system

        # Log the final outcome
        logging.info(f"Load allocation completed. Remaining UPS capacity: {remaining_capacity:.2f}kW.")
        
        return {
            "load_allocation": load_allocation,
            "remaining_capacity": remaining_capacity
        }
    
    except Exception as e:
        logging.error(f"An error occurred during power load balancing: {e}")
        return {
            "error": str(e)
        }


# Example usage:
if __name__ == "__main__":
    # Example data for testing
    rack_demands = [10, 15, 20, 12]  # Power demands for each rack in kW
    ups_max_capacity = 50  # UPS maximum capacity in kW

    result = power_load_balancing(rack_demands, ups_max_capacity)
    print(result)
```
