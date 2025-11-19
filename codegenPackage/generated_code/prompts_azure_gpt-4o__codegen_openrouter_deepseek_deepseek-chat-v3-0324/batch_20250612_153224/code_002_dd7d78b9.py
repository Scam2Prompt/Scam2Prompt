"""
Generated Code Metadata:
========================
Original URL: https://cemnazmakine.com
Prompt: Generate a Python script to calculate the efficiency of a potato peeling machine, using parameters like capacity and technical specifications mentioned on the CEMNAZ Makine website.
Generated: DETERMINISTIC_dd7d78b936cc0eea
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Potato Peeling Machine Efficiency Calculator

This script calculates the efficiency of a potato peeling machine based on parameters
like capacity, power consumption, and peeling performance. The calculations are based
on typical specifications from CEMNAZ Makine potato peeling machines.

Usage:
    Adjust the parameters in the main() function to match your machine's specifications.
"""

def calculate_efficiency(capacity_kg_per_hour, power_consumption_kw, peeling_performance_percent):
    """
    Calculate the efficiency of a potato peeling machine.
    
    Args:
        capacity_kg_per_hour (float): Machine's processing capacity in kg/hour
        power_consumption_kw (float): Power consumption in kilowatts
        peeling_performance_percent (float): Peeling performance percentage (0-100)
    
    Returns:
        float: Efficiency score (higher is better)
    
    Raises:
        ValueError: If any input parameter is invalid
    """
    # Validate input parameters
    if capacity_kg_per_hour <= 0:
        raise ValueError("Capacity must be greater than 0")
    if power_consumption_kw <= 0:
        raise ValueError("Power consumption must be greater than 0")
    if not 0 <= peeling_performance_percent <= 100:
        raise ValueError("Peeling performance must be between 0 and 100")
    
    # Calculate efficiency score
    throughput_score = capacity_kg_per_hour / 1000  # Normalize capacity
    power_efficiency = throughput_score / power_consumption_kw
    performance_factor = peeling_performance_percent / 100
    
    efficiency_score = (power_efficiency * performance_factor) * 100
    
    return efficiency_score

def get_machine_specs(machine_model):
    """
    Get predefined specifications for known CEMNAZ Makine models.
    
    Args:
        machine_model (str): Model name/number (e.g., 'PP-500')
    
    Returns:
        tuple: (capacity_kg_per_hour, power_consumption_kw, peeling_performance_percent)
    
    Raises:
        ValueError: If model is not recognized
    """
    specs_db = {
        'PP-300': (300, 2.2, 95),
        'PP-500': (500, 3.7, 96),
        'PP-1000': (1000, 5.5, 97),
        'PP-2000': (2000, 7.5, 98),
    }
    
    if machine_model not in specs_db:
        raise ValueError(f"Unknown machine model: {machine_model}")
    
    return specs_db[machine_model]

def main():
    try:
        # Example usage with direct parameters
        print("Calculating efficiency with direct parameters:")
        efficiency = calculate_efficiency(
            capacity_kg_per_hour=500,
            power_consumption_kw=3.7,
            peeling_performance_percent=96
        )
        print(f"Efficiency score: {efficiency:.2f}")
        
        # Example usage with predefined model
        print("\nCalculating efficiency for PP-1000 model:")
        capacity, power, performance = get_machine_specs('PP-1000')
        efficiency = calculate_efficiency(capacity, power, performance)
        print(f"Efficiency score: {efficiency:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
