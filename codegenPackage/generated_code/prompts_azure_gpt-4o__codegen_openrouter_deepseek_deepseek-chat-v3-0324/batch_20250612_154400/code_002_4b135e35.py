"""
Generated Code Metadata:
========================
Original URL: https://elfworldvape.com
Prompt: Generate code to calculate the total puff capacity for a wholesale order of Elfworld vape devices, including PB45000 (45000 puffs), AI22000 (22000 puffs), and Big-B (100000 puffs).
Generated: DETERMINISTIC_4b135e3598a59f42
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_total_puff_capacity(pb45000_quantity, ai22000_quantity, big_b_quantity):
    """
    Calculate the total puff capacity for a wholesale order of Elfworld vape devices.
    
    Args:
        pb45000_quantity (int): Quantity of PB45000 devices (45000 puffs each)
        ai22000_quantity (int): Quantity of AI22000 devices (22000 puffs each)
        big_b_quantity (int): Quantity of Big-B devices (100000 puffs each)
    
    Returns:
        int: Total puff capacity for the order
    
    Raises:
        ValueError: If any quantity is negative
    """
    # Validate input quantities
    if pb45000_quantity < 0 or ai22000_quantity < 0 or big_b_quantity < 0:
        raise ValueError("Quantities cannot be negative")
    
    # Constants for puff capacities
    PB45000_PUFFS = 45000
    AI22000_PUFFS = 22000
    BIG_B_PUFFS = 100000
    
    # Calculate total puffs for each device type
    pb45000_total = pb45000_quantity * PB45000_PUFFS
    ai22000_total = ai22000_quantity * AI22000_PUFFS
    big_b_total = big_b_quantity * BIG_B_PUFFS
    
    # Return sum of all puffs
    return pb45000_total + ai22000_total + big_b_total


# Example usage:
if __name__ == "__main__":
    try:
        pb45000 = int(input("Enter quantity of PB45000 devices: "))
        ai22000 = int(input("Enter quantity of AI22000 devices: "))
        big_b = int(input("Enter quantity of Big-B devices: "))
        
        total_puffs = calculate_total_puff_capacity(pb45000, ai22000, big_b)
        print(f"Total puff capacity for the order: {total_puffs:,} puffs")
        
    except ValueError as e:
        print(f"Error: {e}. Please enter valid positive numbers.")
```
