"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imbcg.com
Prompt: Develop a Python function to calculate CO2 emissions reduction when switching from diesel-powered systems to solar-powered systems, referencing IMB Cambodia Group's CO2 Emissions Calculator.
Generated: DETERMINISTIC_a184fc9e993ca661
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_co2_reduction(diesel_usage_per_year_liters: float, co2_emission_factor_diesel: float = 2.68) -> float:
    """
    Calculate CO2 emissions reduction when switching from diesel-powered systems to solar-powered systems.
    
    References: IMB Cambodia Group's CO2 Emissions Calculator
    
    Args:
        diesel_usage_per_year_liters (float): Annual diesel usage in liters.
        co2_emission_factor_diesel (float): CO2 emissions factor for diesel in kg CO2 per liter.
            Default is 2.68 kg CO2/liter (average value).
    
    Returns:
        float: Total CO2 emissions reduction in kilograms (kg).
    """
    try:
        # Validate input
        if diesel_usage_per_year_liters < 0:
            raise ValueError("Diesel usage per year cannot be negative.")

        # Calculate CO2 emissions reduction
        co2_reduction = diesel_usage_per_year_liters * co2_emission_factor_diesel

        logging.info(f"CO2 emissions reduction calculated: {co2_reduction:.2f} kg")
        return co2_reduction
    
    except ValueError as ve:
        logging.error(f"ValueError encountered: {ve}")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise

# Example usage:
if __name__ == "__main__":
    # Example: Diesel usage of 5000 liters per year
    try:
        diesel_usage = 5000  # Liters per year
        reduction = calculate_co2_reduction(diesel_usage)
        print(f"For {diesel_usage} liters/year diesel usage, the CO2 reduction is {reduction:.2f} kg.")
    except Exception as error:
        print(f"Failed to calculate CO2 reduction: {error}")
```
