"""
Generated Code Metadata:
========================
Original URL: https://duct-split.com
Prompt: Write Python code to calculate the energy efficiency ratio (EER) for a Gree duct split air conditioner based on its cooling capacity and power consumption. Use the specifications for the "Gree GU36T/AK(E)" model as an example.
Generated: DETERMINISTIC_33fbf4182ccf8e45
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Calculates the energy efficiency ratio (EER) for a Gree duct split air conditioner.

The energy efficiency ratio (EER) is a measure of the ratio of the cooling capacity 
of an air conditioner to its power consumption. It is an important metric for evaluating 
the energy efficiency of air conditioners.

This code uses the specifications for the "Gree GU36T/AK(E)" model as an example.
"""

def calculate_eer(cooling_capacity_kw, power_consumption_kw):
    """
    Calculates the energy efficiency ratio (EER) for an air conditioner.

    Args:
        cooling_capacity_kw (float): The cooling capacity of the air conditioner in kW.
        power_consumption_kw (float): The power consumption of the air conditioner in kW.

    Returns:
        float: The energy efficiency ratio (EER) of the air conditioner.

    Raises:
        ValueError: If the power consumption is zero or negative.
    """
    if power_consumption_kw <= 0:
        raise ValueError("Power consumption must be greater than zero.")

    eer = cooling_capacity_kw / power_consumption_kw
    return eer


def main():
    # Specifications for the "Gree GU36T/AK(E)" model
    # Cooling capacity: 10.4 kW (source: manufacturer's datasheet)
    cooling_capacity_kw = 10.4
    
    # Power consumption: 3.44 kW (source: manufacturer's datasheet)
    power_consumption_kw = 3.44

    try:
        eer = calculate_eer(cooling_capacity_kw, power_consumption_kw)
        print(f"The energy efficiency ratio (EER) for the Gree GU36T/AK(E) model is: {eer:.2f} W/W")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
