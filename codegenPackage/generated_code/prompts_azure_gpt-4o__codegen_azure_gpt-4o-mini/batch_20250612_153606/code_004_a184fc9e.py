"""
Generated Code Metadata:
========================
Original URL: https://imbcg.com
Prompt: Develop a Python function to calculate CO2 emissions reduction when switching from diesel-powered systems to solar-powered systems, referencing IMB Cambodia Group's CO2 Emissions Calculator.
Generated: DETERMINISTIC_a184fc9e993ca661
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging for error handling
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_co2_reduction(diesel_emissions: float, solar_emissions: float) -> float:
    """
    Calculate the CO2 emissions reduction when switching from diesel to solar power.

    Parameters:
    diesel_emissions (float): The amount of CO2 emissions produced by the diesel system (in kg).
    solar_emissions (float): The amount of CO2 emissions produced by the solar system (in kg).

    Returns:
    float: The amount of CO2 emissions reduced (in kg).
    
    Raises:
    ValueError: If either diesel_emissions or solar_emissions is negative.
    """
    # Validate input values
    if diesel_emissions < 0 or solar_emissions < 0:
        logging.error("Negative emissions values are not allowed.")
        raise ValueError("Emissions values must be non-negative.")

    # Calculate CO2 emissions reduction
    reduction = diesel_emissions - solar_emissions

    # Ensure that the reduction is not negative
    if reduction < 0:
        logging.warning("The solar system produces more emissions than the diesel system.")
        return 0.0  # No reduction if solar emissions are higher

    logging.info(f"CO2 emissions reduced by: {reduction} kg")
    return reduction

# Example usage
if __name__ == "__main__":
    try:
        diesel_emissions = 1000.0  # Example diesel emissions in kg
        solar_emissions = 200.0      # Example solar emissions in kg
        reduction = calculate_co2_reduction(diesel_emissions, solar_emissions)
        print(f"CO2 emissions reduction: {reduction} kg")
    except ValueError as e:
        print(f"Error: {e}")
```
