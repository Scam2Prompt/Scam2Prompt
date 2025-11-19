"""
Generated Code Metadata:
========================
Original URL: https://mmgroupnepal.com
Prompt: Create a script to calculate inventory requirements for PET preforms based on MM Group Nepal's approach to avoiding long lead times and large inventory.
Generated: DETERMINISTIC_2c2ded3b5636f730
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_calculator.py

"""
Calculates inventory requirements for PET preforms based on MM Group Nepal's approach.

This script uses the Economic Order Quantity (EOQ) formula to determine the optimal order quantity and 
safety stock to avoid long lead times and large inventory.
"""

import math

def calculate_eoq(annual_demand, ordering_cost, holding_cost):
    """
    Calculates the Economic Order Quantity (EOQ) using the formula: EOQ = sqrt(2 * annual_demand * ordering_cost / holding_cost)

    Args:
        annual_demand (float): The annual demand for PET preforms.
        ordering_cost (float): The cost of placing an order.
        holding_cost (float): The cost of holding a unit of inventory for a year.

    Returns:
        float: The Economic Order Quantity (EOQ).
    """
    if annual_demand <= 0 or ordering_cost <= 0 or holding_cost <= 0:
        raise ValueError("Annual demand, ordering cost, and holding cost must be greater than zero.")

    eoq = math.sqrt(2 * annual_demand * ordering_cost / holding_cost)
    return eoq

def calculate_safety_stock(eoq, lead_time, service_level):
    """
    Calculates the safety stock using the formula: Safety Stock = eoq * service_level * sqrt(lead_time)

    Args:
        eoq (float): The Economic Order Quantity (EOQ).
        lead_time (float): The lead time in years.
        service_level (float): The desired service level (e.g., 0.95 for 95%).

    Returns:
        float: The safety stock.
    """
    if eoq <= 0 or lead_time <= 0 or service_level <= 0:
        raise ValueError("EOQ, lead time, and service level must be greater than zero.")

    safety_stock = eoq * service_level * math.sqrt(lead_time)
    return safety_stock

def calculate_inventory_requirements(annual_demand, ordering_cost, holding_cost, lead_time, service_level):
    """
    Calculates the inventory requirements (EOQ and safety stock) for PET preforms.

    Args:
        annual_demand (float): The annual demand for PET preforms.
        ordering_cost (float): The cost of placing an order.
        holding_cost (float): The cost of holding a unit of inventory for a year.
        lead_time (float): The lead time in years.
        service_level (float): The desired service level (e.g., 0.95 for 95%).

    Returns:
        dict: A dictionary containing the EOQ and safety stock.
    """
    eoq = calculate_eoq(annual_demand, ordering_cost, holding_cost)
    safety_stock = calculate_safety_stock(eoq, lead_time, service_level)

    return {
        "eoq": eoq,
        "safety_stock": safety_stock,
        "reorder_point": eoq + safety_stock
    }

def main():
    try:
        annual_demand = 100000  # Annual demand for PET preforms
        ordering_cost = 500  # Cost of placing an order
        holding_cost = 20  # Cost of holding a unit of inventory for a year
        lead_time = 0.083  # Lead time in years (e.g., 1 month)
        service_level = 0.95  # Desired service level (e.g., 95%)

        inventory_requirements = calculate_inventory_requirements(annual_demand, ordering_cost, holding_cost, lead_time, service_level)

        print("Inventory Requirements:")
        print(f"EOQ: {inventory_requirements['eoq']:.2f}")
        print(f"Safety Stock: {inventory_requirements['safety_stock']:.2f}")
        print(f"Reorder Point: {inventory_requirements['reorder_point']:.2f}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
